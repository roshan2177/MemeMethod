# #!/bin/bash

# # Check if the input file is provided as an argument
# if [ $# -ne 1 ]; then
#     echo "Usage: $0 <input_file>"
#     exit 1
# fi

# # Input file to be processed
# INPUT_FILE=$1

# # Check if the file exists
# if [ ! -f "$INPUT_FILE" ]; then
#     echo "Error: File '$INPUT_FILE' not found."
#     exit 1
# fi

# # Run the lexer Python script with the input file
# # with the lexer script is named 'meme_lexer.py'
# # and the input file is passed as a command-line argument
# python3 meme_lexer.py "$INPUT_FILE"

# # Check if the lexer execution was successful
# if [ $? -eq 0 ]; then
#     echo "Lexical analysis completed successfully."
# else
#     echo "Error occurred during lexical analysis."
#     exit 1
# fi
"""
#!/bin/bash

# Run the lexer Python script with standard input
# Redirect input to the Python script
python3 meme_lexer.py

# Check if the lexer execution was successful
if [ $? -eq 0 ]; then
    echo "Lexical analysis completed successfully."
else
    echo "Error occurred during lexical analysis."
    exit 1
fi
"""
#!/bin/bash

# Check if the source file is provided as an argument
if [ "$#" -ne 1 ]; then
    echo "Usage: ./scanner.sh <source_file>"
    exit 1
fi

# Run the lexer Python script with the provided source file
python3 meme_lexer.py "$1"

# Check if the lexer execution was successful
if [ $? -eq 0 ]; then
    echo "Lexical analysis completed successfully."
else
    echo "Error occurred during lexical analysis."
    exit 1
fi

