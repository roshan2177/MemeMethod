import json
import sys



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














class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

class ASTNode:
    def __init__(self, node_type, token=None, children=None):
        self.node_type = node_type
        self.token = token  # Store the actual token tuple
        self.children = children if children is not None else []
    
    def to_string(self, level=0):
        """Recursive string representation with custom indentation for specific nodes."""
        # Determine token type (e.g., ID, INT), but do not show the actual token value.
        token_type = self.token[0] if self.token else ""
        token_value = self.token[1] if self.token else "None"
        # Custom indentation rules
        if level == 0:
            # No indentation for the root node `Program`
            ret = f"{self.node_type}\n"
        elif self.node_type in ["CreateCommand", "SaveCommand"]:
            # Single tab for `CreateCommand` and `SaveCommand`
            ret = "\t" + f"{self.node_type} {token_type}\n"
        elif self.node_type in ["LoadPictures", "Size", "Border", "Text"]:
            # Single tab for `CreateCommand` and `SaveCommand`
            ret = "\t\t" + f"{self.node_type} {token_type}\n"        
        else:
            # Double tabs for all other nodes
            ret = "\t\t" * level + f"{self.node_type} {token_type} ({token_value})\n"
        
        # Recursively call `to_string` on each child with increased level for further indentation
        for child in self.children:
            if isinstance(child, ASTNode):
                ret += child.to_string(level + 1)
            else:
                ret += "\t" * (level + 1) + str(child) + "\n"
                
        return ret

    def __repr__(self):
        return self.to_string()



class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0
        self.ast = None

    def parse(self):
        # Ensure the program starts with "create meme" and ends with "save images"
        self.match("KEYWORD", "create")
        self.match("KEYWORD", "meme")
        create_node = ASTNode("CreateCommand")

        # Parse the body of the program
        children = [create_node]
        while not self.check("KEYWORD", "save"):
            children.append(self.parse_section())
        
        # Match the ending keywords and create the SaveCommand node
        self.match("KEYWORD", "save")
        self.match("KEYWORD", "images")
        save_node = ASTNode("SaveCommand")
        children.append(save_node)

        # Return the root node of the AST
        return ASTNode("Program", children=children)

    def parse_section(self):
        """Parses each section based on the KEYWORD encountered."""
        if self.check("KEYWORD", "background"):
            self.match("KEYWORD", "background")
            color = self.consume("ID")
            return ASTNode("Background", token=color)
        
        elif self.check("KEYWORD", "load"):
            self.match("KEYWORD", "load")
            self.match("ID", "pictures")
            images = []
            while self.check("ID"):
                images.append(ASTNode("Image", token=self.consume("ID")))
            return ASTNode("LoadPictures", children=images)
        
        elif self.check("KEYWORD", "size"):
            self.match("KEYWORD", "size")
            width = self.consume("INT")
            operation = self.consume("OP")
            height = self.consume("INT")
            return ASTNode("Size", children=[ASTNode("Width", token=width), ASTNode("Operation", token=operation), ASTNode("Height", token=height)])
        
        elif self.check("KEYWORD", "border"):
            self.match("KEYWORD", "border")
            border_type = self.consume("ID")
            color = None
            if self.check("ID", "color"):
                color = self.consume("ID")
            return ASTNode("Border", children=[ASTNode("BorderType", token=border_type), ASTNode("BorderColor", token=color)])
        
        elif self.check("KEYWORD", "style"):
            self.match("KEYWORD", "style")
            style_value = self.consume("ID")
            return ASTNode("Style", token=style_value)
        
        elif self.check("KEYWORD", "text"):
            self.match("KEYWORD", "text")
            text_content = self.consume("STRING")
            properties = [ASTNode("TextContent", token=text_content)]
            if self.check("KEYWORD", "placement"):
                self.match("KEYWORD", "placement")
                placement = self.consume("ID")
                properties.append(ASTNode("Placement", token=placement))
            if self.check("KEYWORD", "overlay"):
                self.match("KEYWORD", "overlay")
                overlay = self.consume("ID")
                properties.append(ASTNode("Overlay", token=overlay))
            return ASTNode("Text", children=properties)
        
        elif self.check("KEYWORD", "count"):
            self.match("KEYWORD", "count")
            count_value = self.consume("INT")
            return ASTNode("Count", token=count_value)
        
        else:
            raise SyntaxError(f"Unexpected token: {self.peek()}")

    def match(self, token_type, token_value=None):
        """Advance if the next token matches the type and optional value."""
        if self.check(token_type, token_value):
            return self.advance()
        raise SyntaxError(f"Expected {token_type} {token_value or ''} but found {self.peek()}")

    def consume(self, token_type, token_value=None):
        """Consume a token of the specified type and optional value."""
        if self.check(token_type, token_value):
            return self.advance()
        raise SyntaxError(f"Expected token {token_type} {token_value or ''}, got {self.peek()}")

    def check(self, token_type, token_value=None):
        """Check the next token type and optional value."""
        if self.is_at_end():
            return False
        current_token = self.peek()
        if current_token[0] != token_type:
            return False
        if token_value is not None and current_token[1] != token_value:
            return False
        return True

    def advance(self):
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def is_at_end(self):
        return self.current >= len(self.tokens) or self.peek()[0] == "EOF"

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]




scanner = Scanner(sample_input1)
# Run the scanner to tokenize the input
tokens = scanner.scan()
print(tokens)

parser = Parser(tokens)
ast = parser.parse()
print("Abstract Syntax Tree:")
print(ast)
