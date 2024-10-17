class Scanner:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.current_state = "Start"
        self.keywords = {"create", "meme", "background", "load", "size", "border", "style", "text", 
                         "placement", "overlay", "count", "save", "images"}
        self.operators = {"x"}
        self.delimiters = {" ", "\n"}
    
    def scan(self):
        index = 0
        while index < len(self.source_code):
            char = self.source_code[index]
            
            if self.current_state == "Start":
                if char.isalpha():  # Start of keyword or identifier
                    self.current_state = "Keyword/Identifier"
                    start_index = index
                    while index < len(self.source_code) and (self.source_code[index].isalpha() or self.source_code[index].isdigit() or self.source_code[index] == '_'):
                        index += 1
                    value = self.source_code[start_index:index]
                    token_type = "KEYWORD" if value in self.keywords else "ID"
                    self.tokens.append((token_type, value))
                    self.current_state = "Start"
                elif char.isdigit():  # Start of number
                    self.current_state = "Number"
                    start_index = index
                    while index < len(self.source_code) and self.source_code[index].isdigit():
                        index += 1
                    value = self.source_code[start_index:index]
                    self.tokens.append(("INT", value))
                    self.current_state = "Start"
                elif char == '"':  # Start of string literal
                    self.current_state = "String"
                    start_index = index + 1
                    index += 1
                    while index < len(self.source_code) and self.source_code[index] != '"':
                        index += 1
                    value = self.source_code[start_index:index]
                    index += 1  # To skip closing quote
                    self.tokens.append(("STRING", value))
                    self.current_state = "Start"
                elif char in self.operators:  # Operator
                    self.tokens.append(("OP", char))
                    index += 1
                    self.current_state = "Start"
                elif char in self.delimiters:  # Delimiter
                    index += 1  # Simply skip delimiters
                    self.current_state = "Start"
                else:  # Lexical error
                    self.current_state = "Error"
                    print(f"Lexical Error: Unexpected character '{char}'")
                    break
        return self.tokens

# Example usage:
source_code = """
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

scanner = Scanner(source_code)
tokens = scanner.scan()

for token in tokens:
    print(token)
