import re

# Token types
TOKEN_TYPES = {
    'KEYWORD': ['create', 'background', 'text', 'save', 'pictures', 'resize', 'if'],
    'OPERATOR': ['==', '!=', '+', '-', '*', '/'],
    'LITERAL': r'[0-9]+',  # Integer literals
    'STRING': r'"[^"]*"',  # Strings inside double quotes
    'IDENTIFIER': r'[a-zA-Z_][a-zA-Z_0-9]*',  # Variables, keywords, and meme element names
    'COMMENT': r'//.*',  # Single-line comments
    'COMMA': r',',  # Comma handling
    'WHITESPACE': r'[ \t\n]+',  # Whitespace characters
}

class Lexer:
    def __init__(self, code):
        self.code = code
        self.position = 0
        self.tokens = []

    def tokenize(self):
        while self.position < len(self.code):
            matched = False
            for token_type, pattern in TOKEN_TYPES.items():
                if token_type == 'KEYWORD':
                    matched = self.match_keyword()
                elif token_type == 'OPERATOR':
                    matched = self.match_operator()
                else:
                    regex = re.compile(pattern)
                    match = regex.match(self.code, self.position)
                    if match:
                        value = match.group(0)
                        if token_type != 'WHITESPACE':  # Ignore whitespace tokens
                            self.tokens.append((token_type, value))
                        self.position = match.end(0)
                        matched = True
                        break
            if not matched:
                raise SyntaxError(f"Unrecognized token at position {self.position}: {self.code[self.position]}")
        return self.tokens

    def match_keyword(self):
        for keyword in TOKEN_TYPES['KEYWORD']:
            if self.code[self.position:].startswith(keyword) and not re.match(r'[a-zA-Z_0-9]', self.code[self.position + len(keyword):]):
                self.tokens.append(('KEYWORD', keyword))
                self.position += len(keyword)
                return True
        return False

    def match_operator(self):
        for operator in TOKEN_TYPES['OPERATOR']:
            if self.code[self.position:].startswith(operator):
                self.tokens.append(('OPERATOR', operator))
                self.position += len(operator)
                return True
        return False

# Example function to test lexer
def run_lexer(file_name):
    with open(file_name, 'r') as file:
        code = file.read()
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    for token in tokens:
        print(f"<{token[0]}, {token[1]}>")

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python meme_lexer.py <input_file>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    run_lexer(file_name)
