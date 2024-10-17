
TOKEN_TYPES = {
    'KEYWORD': ['create', 'background', 'text', 'save', 'pictures', 'resize', 'if'],
    'OPERATOR': ['==', '!=', '+', '-', '*', '/'],
    'LITERAL': r'[0-9]+',  # Integer literals
    'STRING': r'"[^"]*"',  # Strings inside double quotes
    'IDENTIFIER': r'[a-zA-Z_][a-zA-Z_0-9]*',  # Variables, keywords, and meme element names
    'COMMENT': r'//.*',  # Single-line comments
    'WHITESPACE': r'[ \t\n]+',  # Whitespaces
}
