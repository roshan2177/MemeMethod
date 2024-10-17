#!/bin/bash

# Run the lexer Python script with standard input.
# This will execute the meme_lexer.py script using Python 3.
# You may provide input through standard input (e.g., by piping a file).
python3 meme_lexer.py

# Check if the lexer execution was successful.
# The special variable $? holds the exit status of the last command executed.
# If the exit status is 0, the script will print a success message.
if [ $? -eq 0 ]; then
    echo "Lexical analysis completed successfully."
else
    # If the exit status is not 0, print an error message and exit with status 1 (failure).
    echo "Error occurred during lexical analysis."
    exit 1
fi
