#!/bin/bash

# Check if the input file is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <input_file>"
    exit 1
fi

# Input file to be processed
INPUT_FILE=$1

# Check if the file exists
if [ ! -f "$INPUT_FILE" ]; then
    echo "Error: File '$INPUT_FILE' not found."
    exit 1
fi

# Use awk to split the file by each "#Sample" comment line
awk -v prefix="sample_part" '
/^#Sample/ {
    # Close previous part file and increment part counter
    if (out) close(out)
    out = sprintf("%s%d.txt", prefix, ++count)
}
{
    # Write each line to the current part file
    if (out) print > out
}
' "$INPUT_FILE"

# Loop through each generated sample_part file and run the lexer and parser on it
for PART in sample_part*.txt; do
    echo "Running Lexer followed by Parser on $PART..."
    # Run the lexer (meme_lexer.py)
    if [ $? -eq 0 ]; then
        python3 meme_lexer_parser_generation.py "$PART"
    else
        echo "Error occurred during lexical analysis for $PART. Skipping syntax analysis."
        exit 1
    fi

    rm "$PART"
done
