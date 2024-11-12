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

# Loop through each generated sample_part file and run the lexer on it
for PART in sample_part*.txt; do
    echo "Processing $PART..."
    # Run the lexer Python script on the current part
    python3 meme_lexer.py "$PART"

    # Check if the lexer execution was successful
    if [ $? -eq 0 ]; then
        echo "Lexical analysis for $PART completed successfully."
    else
        echo "Error occurred during lexical analysis for $PART."
        exit 1
    fi

    # Clean up by removing the temporary split file
    rm "$PART"
done
