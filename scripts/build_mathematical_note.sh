#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
mkdir -p tmp/pdfs/mathematical-note output/pdf
for pass in 1 2; do
  pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error \
    -output-directory=tmp/pdfs/mathematical-note \
    papers/anaghs-law-mathematical-note.tex
done
cp tmp/pdfs/mathematical-note/anaghs-law-mathematical-note.pdf \
  output/pdf/anaghs-law-mathematical-note.pdf
