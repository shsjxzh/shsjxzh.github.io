#!/usr/bin/bash

# clear out old files
rm _awards/*.md
rm _posters/*.md
rm _service/*.md
rm _publications/*.md
rm _talks/*.md

# regenerate from TSV's
python markdown_generator/awards.py
python markdown_generator/posters.py
python markdown_generator/publications.py
python markdown_genrrator/service.py
python markdown_generator/talks.py
