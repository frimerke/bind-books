#
# bind-books.py
# a script to initialize a book/document into a collection.
# loosely based on the node.js generate package script.
#

import argparse

parser = argparse.ArgumentParser(description='Script to initialize a book/document into a collection.')

# Take arguments - primarily a file to work off of.

parser.add_argument('file', metavar='f', help='a file to enter into the catalog.')

args = parser.parse_args()
to_archive = args.file

# Pose questions.

title = input("Title: ")
author = input("Author: ")
year = input("Year: ")

# Generate XML
# validate against dtd

# Create folders & XML file.
#
# /Library/<year-author-title>/
#   ./src/<original-file>.pdf
#   <year-author-title>.XML
#

# Move source file to src dir above.

# Hook into database?

# Exit gracefully.
