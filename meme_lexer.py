import json
import sys

class Scanner:
    def __init__(self, source_code):
        # Initialize the scanner with the source code input
        self.source_code = source_code
        # List to store the tokens extracted from the source code
        self.tokens = []
        # Current state of the scanner; starting at "Start"
        self.current_state = "Start"
        # Set of keywords recognized by the scanner
        self.keywords = {"create", "meme", "background", "load", "size", "border", "style", "text", 
                         "placement", "overlay", "count", "save", "images"}
        # Set of operators recognized by the scanner; currently only "x"
        self.operators = {"x"}
        # Set of delimiters used to separate tokens, such as space and newline
        self.delimiters = {" ", "\n"}
    
    def scan(self):
        # Index used to traverse the source code
        index = 0
        # Loop through the source code character by character
        while index < len(self.source_code):
            char = self.source_code[index]
            
            # Check current state of the scanner
            if self.current_state == "Start":
                if char.isalpha():  # If the character is alphabetic, start of a keyword or identifier
                    start_index = index
                    # Continue scanning while the characters are alphabetic, numeric, or underscores
                    while index < len(self.source_code) and (self.source_code[index].isalpha() or self.source_code[index].isdigit() or self.source_code[index] == '_'):
                        index += 1
                    # Extract the token value
                    value = self.source_code[start_index:index]
                    
                    # Check if the value is an operator (e.g., 'x')
                    if value in self.operators:
                        self.tokens.append(("OP", value))
                    else:
                        # Check if it's a keyword or an identifier (ID)
                        token_type = "KEYWORD" if value in self.keywords else "ID"
                        self.tokens.append((token_type, value))
                    
                    # After processing, go back to the Start state
                    self.current_state = "Start"
                elif char.isdigit():  # If the character is a digit, start of a number
                    start_index = index
                    # Continue scanning while characters are digits
                    while index < len(self.source_code) and self.source_code[index].isdigit():
                        index += 1
                    # Extract the number token
                    value = self.source_code[start_index:index]
                    self.tokens.append(("INT", value))
                    self.current_state = "Start"
                elif char == '"':  # If the character is a double quote, start of a string literal
                    start_index = index + 1
                    index += 1
                    # Continue scanning until the closing double quote is found
                    while index < len(self.source_code) and self.source_code[index] != '"':
                        index += 1
                    # Extract the string literal
                    value = self.source_code[start_index:index]
                    index += 1  # Skip the closing double quote
                    self.tokens.append(("STRING", value))
                    self.current_state = "Start"
                elif char in self.operators:  # If the character is an operator (like 'x')
                    self.tokens.append(("OP", char))
                    index += 1
                    self.current_state = "Start"
                elif char in self.delimiters:  # If the character is a delimiter (e.g., space or newline)
                    index += 1  # Simply skip the delimiter and move on
                    self.current_state = "Start"
                else:  # If an unexpected character is encountered, report a lexical error
                    self.current_state = "Error"
                    print(f"Lexical Error: Unexpected character '{char}'")
                    break
        # Return the list of tokens after scanning is complete
        return self.tokens

sample_input1 = """
create meme
    background blue
    load pictures dogs cats grass
    size 1024 x 1024
    border solid
        color
    style collage
    text "we all love animals"
        placement middle
        overlay yes
    text "of course"
        placement bottom
        overlay no
    count 50
save images
"""

# Function to run the scanner on a sample input and print the tokens
def run_sample(input_text, sample_number):
    print(f"\nSample {sample_number} Input:")
    print(input_text)
    # Create a scanner object with the input text
    scanner = Scanner(input_text)
    # Run the scanner to tokenize the input
    tokens = scanner.scan()
    # Print the tokens for the sample
    print(f"\nSample {sample_number} Tokens:")
    for token in tokens:
        print(token)

# Run all sample inputs through the scanner and print tokens
run_sample(sample_input1, 1)