class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string.")
        self._name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    def articles(self):
        return [a for a in Article.all if a.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(article.magazine.category for article in self.articles()))


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        else:
            raise Exception("Name must be a string 2-16 characters long.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        else:
            raise Exception("Category must be a non-empty string.")

    def articles(self):
        return [a for a in Article.all if a.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = [a.author for a in self.articles()]
        return list({a for a in authors if authors.count(a) > 2}) or None

    @classmethod
    def top_publisher(cls):
        magazines = cls.all
        top = max(magazines, key=lambda m: len(m.articles()), default=None)
        return top if top.articles() else None


class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author  
        self.magazine = magazine
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise Exception("Title must be a string 5-50 characters long.")
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise Exception("author must be an instance of Author")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            raise Exception("magazine must be an instance of Magazine")
