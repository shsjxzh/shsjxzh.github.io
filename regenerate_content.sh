#!/bin/bash

# clear out old files
rm _awards/*.md
rm _posters/*.md
rm _service/*.md
rm _publications/*.md
rm _talks/*.md
rm _reviewing/*.md

# regenerate from TSV's
cd markdown_generator
python awards.py
python posters.py
python publications.py
python service.py
python talks.py
python reviewing.py
#python markdown_generator/awards.py ./markdown_generator/awards.tsv
#python markdown_generator/posters.py ./markdown_generator/posters.tsv
#python markdown_generator/publications.py ./markdown_generator/publications.tsv
#python markdown_genrrator/service.py ./markdown_generator/service.tsv
#python markdown_generator/talks.py ./markdown_generator/talks.tsv
