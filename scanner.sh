#!/bin/bash

# This shell script runs the lexical analyzer
if [ "$#" -ne 1 ]; then
  echo "Usage: ./scanner.sh <source_file>"
  exit 1
fi

python3 meme_lexer.py "$1"
