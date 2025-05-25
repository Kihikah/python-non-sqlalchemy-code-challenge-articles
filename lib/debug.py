#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Create Authors
    author1 = Author("Kariuki Kihikah")
    author2 = Author("Ada Lovelace")
    author3 = Author("George Orwell")

    # Create Magazines
    magazine1 = Magazine("Nature", "Science")
    magazine2 = Magazine("TechToday", "Technology")
    magazine3 = Magazine("Literary Digest", "Literature")

    # Add Articles using Author's add_article method
    article1 = author1.add_article(magazine1, "The Wonders of Quantum Physics")
    article2 = author1.add_article(magazine2, "The Future of Code")
    article3 = author1.add_article(magazine1, "Black Holes and You")
    article4 = author2.add_article(magazine1, "AI and Ethics")
    article5 = author2.add_article(magazine2, "Building the First Computer")
    article6 = author3.add_article(magazine3, "1984 Revisited")

    # Test some method outputs
    print(f"{author1.name}'s articles: {[a.title for a in author1.articles()]}")
    print(f"{author1.name}'s magazines: {[m.name for m in author1.magazines()]}")
    print(f"{author1.name}'s topic areas: {author1.topic_areas()}")

    print(f"{magazine1.name}'s article titles: {magazine1.article_titles()}")
    print(f"{magazine1.name}'s contributors: {[a.name for a in magazine1.contributors()]}")
    print(f"{magazine1.name}'s contributing authors: {[a.name for a in magazine1.contributing_authors()]}")

    print(f"Top publisher: {Magazine.top_publisher().name}")

    # Don't remove this line, it's for debugging!
    ipdb.set_trace()