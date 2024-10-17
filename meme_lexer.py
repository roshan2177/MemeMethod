# class Scanner:
#     def __init__(self, source_code):
#         self.source_code = source_code
#         self.tokens = []
#         self.current_state = "Start"
#         self.keywords = {"create", "meme", "background", "load", "size", "border", "style", "text", 
#                          "placement", "overlay", "count", "save", "images"}
#         self.operators = {"x"}  # Add x as an operator
#         self.delimiters = {" ", "\n"}
    
#     def scan(self):
#         index = 0
#         while index < len(self.source_code):
#             char = self.source_code[index]
            
#             if self.current_state == "Start":
#                 if char.isalpha():  # Start of keyword or identifier
#                     start_index = index
#                     while index < len(self.source_code) and (self.source_code[index].isalpha() or self.source_code[index].isdigit() or self.source_code[index] == '_'):
#                         index += 1
#                     value = self.source_code[start_index:index]
                    
#                     # Check if it's an operator like 'x'
#                     if value in self.operators:
#                         self.tokens.append(("OP", value))
#                     else:
#                         token_type = "KEYWORD" if value in self.keywords else "ID"
#                         self.tokens.append((token_type, value))
                    
#                     self.current_state = "Start"
#                 elif char.isdigit():  # Start of number
#                     start_index = index
#                     while index < len(self.source_code) and self.source_code[index].isdigit():
#                         index += 1
#                     value = self.source_code[start_index:index]
#                     self.tokens.append(("INT", value))
#                     self.current_state = "Start"
#                 elif char == '"':  # Start of string literal
#                     start_index = index + 1
#                     index += 1
#                     while index < len(self.source_code) and self.source_code[index] != '"':
#                         index += 1
#                     value = self.source_code[start_index:index]
#                     index += 1  # To skip closing quote
#                     self.tokens.append(("STRING", value))
#                     self.current_state = "Start"
#                 elif char in self.operators:  # Operator
#                     self.tokens.append(("OP", char))
#                     index += 1
#                     self.current_state = "Start"
#                 elif char in self.delimiters:  # Delimiter
#                     index += 1  # Simply skip delimiters
#                     self.current_state = "Start"
#                 else:  # Lexical error
#                     self.current_state = "Error"
#                     print(f"Lexical Error: Unexpected character '{char}'")
#                     break
#         return self.tokens

# # Example usage:
# sample_input1 = """
# create meme
#     background blue
#     load pictures dogs cats grass
#     size 1024 x 1024
#     border solid
#         color
#     style collage
#     text "we all love animals"
#         placement middle
#         overlay yes
#     text "of course"
#         placement bottom
#         overlay no
#     count 50
# save images
# """

# sample_input2 = """
# create meme
#     background black
#     load pictures stars moon
#     size 1920 x 1080
#     border dashed
#         color
#     style panorama
#     text "night sky beauty"
#         placement center
#         overlay no
#     count 5
# save images
# """

# # sample_input3 = """
# # create meme
# #     background white
# #     load pictures car bike road
# #     size 640 x 480
# #     border none
# #     style grid
# #     text "on the go"
# #         placement top-right
# #         overlay yes
# #     text "fast life"
# #         placement bottom-right
# #         overlay no
# #     count 20
# # save images
# # """

# # sample_input4 = """
# # create meme
# #     background green
# #     load pictures tree river mountain
# #     size 1024 x 768
# #     border solid
# #         color
# #     style landscape
# #     text "nature's beauty"
# #         placement bottom
# #         overlay yes
# #     count 15
# # save images
# # """

# # sample_input5 = """
# # create meme
# #     background green
# #     load pictures cat dog tree
# #     size 1024 / 768
# #     border dashed
# #     style grid
# # save images
# # """
# print("Sample 1")
# scanner = Scanner(sample_input1)
# tokens = scanner.scan()
# print("\n")

# print("Sample 2")
# scanner = Scanner(sample_input2)
# tokens = scanner.scan()
# print("\n")

# # print("Sample 3")
# # scanner = Scanner(sample_input3)
# # tokens = scanner.scan()
# # print("\n")

# # print("Sample 4")
# # scanner = Scanner(sample_input4)
# # tokens = scanner.scan()
# # print("\n")

# # print("Sample 5")
# # scanner = Scanner(sample_input5)
# # tokens = scanner.scan()
# # print("\n")

# for token in tokens:
#     print(token)

class Scanner:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.current_state = "Start"
        self.keywords = {"create", "meme", "background", "load", "size", "border", "style", "text", 
                         "placement", "overlay", "count", "save", "images"}
        self.operators = {"x"}  # Add x as an operator
        self.delimiters = {" ", "\n"}
    
    def scan(self):
        index = 0
        while index < len(self.source_code):
            char = self.source_code[index]
            
            if self.current_state == "Start":
                if char.isalpha():  # Start of keyword or identifier
                    start_index = index
                    while index < len(self.source_code) and (self.source_code[index].isalpha() or self.source_code[index].isdigit() or self.source_code[index] == '_'):
                        index += 1
                    value = self.source_code[start_index:index]
                    
                    # Check if it's an operator like 'x'
                    if value in self.operators:
                        self.tokens.append(("OP", value))
                    else:
                        token_type = "KEYWORD" if value in self.keywords else "ID"
                        self.tokens.append((token_type, value))
                    
                    self.current_state = "Start"
                elif char.isdigit():  # Start of number
                    start_index = index
                    while index < len(self.source_code) and self.source_code[index].isdigit():
                        index += 1
                    value = self.source_code[start_index:index]
                    self.tokens.append(("INT", value))
                    self.current_state = "Start"
                elif char == '"':  # Start of string literal
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

# Example inputs:
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

sample_input2 = """
create meme
    background black
    load pictures stars moon
    size 1920 x 1080
    border dashed
        color
    style panorama
    text "night sky beauty"
        placement center
        overlay no
    count 5
save images
"""

sample_input3 = """
create meme
    background white
    load pictures car bike road
    size 640 x 480
    border none
    style grid
    text "on the go"
        placement top-right
        overlay yes
    text "fast life"
        placement bottom-right
        overlay no
    count 20
save images
"""

sample_input4 = """
create meme
    background green
    load pictures tree river mountain
    size 1024 x 768
    border solid
        color
    style landscape
    text "nature's beauty"
        placement bottom
        overlay yes
    count 15
save images
"""

sample_input5 = """
create meme
    background green
    load pictures cat dog tree
    size 1024 / 768
    border dashed
    style grid
save images
"""

# Function to run and print tokens for a sample input
def run_sample(input_text, sample_number):
    print(f"\nSample {sample_number} Input:")
    print(input_text)
    scanner = Scanner(input_text)
    tokens = scanner.scan()
    print(f"\nSample {sample_number} Tokens:")
    for token in tokens:
        print(token)

# Run all sample inputs
run_sample(sample_input1, 1)
run_sample(sample_input2, 2)
run_sample(sample_input3, 3)
run_sample(sample_input4, 4)
run_sample(sample_input5, 5)