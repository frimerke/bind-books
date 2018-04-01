#
# bind-books.py
# a script to initialize a book/document into a collection.
# loosely based on the node.js generate package script.
#

import argparse
import xml.etree.cElementTree as ET

parser = argparse.ArgumentParser(description='Script to initialize a book/document into a collection.')

# Take arguments - primarily a file to work off of.

parser.add_argument('file', metavar='f', help='a file to enter into the catalog.')

args = parser.parse_args()
to_archive = args.file

# Pose questions.

title = input("Title: ")
alternativetitle = input("Alternative titles?:").split(";")
author = input("Author: ")
year = input("Year: ")
language = input("Language: ")
tags = input("Tags: ").split(";")

# Generate XML

text_root = ET.Element("text")

author_el = ET.SubElement(text_root, "author")
author_name_el = ET.SubElement(author_el, "name").text = author

metadata_el = ET.SubElement(text_root, "metadata")
canonicaltitle_el = ET.SubElement(metadata_el, "canonicaltitle").text = title
if alternativetitle[0] != "":
    for tit in alternativetitle:
        ET.SubElement(metadata_el, "alternativetitle").text = tit
publisheddate_el = ET.SubElement(metadata_el, "publisheddate").text = year
publishedlang_el = ET.SubElement(metadata_el, "publishedlang").text = language
metatags_el = ET.SubElement(metadata_el, "metatags")
if tags[0] != ":"
    for t in tags:
        ET.SubElement(metatags_el, "tag").text = t

files_el = ET.SubElement(text_root, "files")

# DEBUG: print xml.

tree = ET.ElementTree(text_root)
print(ET.tostring(text_root))
print(alternativetitle)

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
