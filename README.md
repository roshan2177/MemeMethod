# MemeMethod
Teammates:
Name: Zakiy Manigo UNI: ztm2106
Name: Roshan Prakash UNI: rp3187

Output of sample input from first draft of code:
('KEYWORD', 'create')
('KEYWORD', 'meme')
('KEYWORD', 'background')
('ID', 'blue')
('KEYWORD', 'load')
('ID', 'pictures')
('ID', 'dogs')
('ID', 'cats')
('ID', 'grass')
('KEYWORD', 'size')
('INT', '1024')
('ID', 'x')
('INT', '1024')
('KEYWORD', 'border')
('ID', 'solid')
('ID', 'color')
('KEYWORD', 'style')
('ID', 'collage')
('KEYWORD', 'text')
('STRING', 'we all love animals')
('KEYWORD', 'placement')
('ID', 'middle')
('KEYWORD', 'overlay')
('ID', 'yes')
('KEYWORD', 'text')
('STRING', 'of course')
('KEYWORD', 'placement')
('ID', 'bottom')
('KEYWORD', 'overlay')
('ID', 'no')
('KEYWORD', 'count')
('INT', '50')
('KEYWORD', 'save')
('KEYWORD', 'images')

-- x should be an OP not an ID

Output of sample input from the second draft of code:
('KEYWORD', 'create')
('KEYWORD', 'meme')
('KEYWORD', 'background')
('ID', 'blue')
('KEYWORD', 'load')
('ID', 'pictures')
('ID', 'dogs')
('ID', 'cats')
('ID', 'grass')
('KEYWORD', 'size')
('INT', '1024')
('OP', 'x')
('INT', '1024')
('KEYWORD', 'border')
('ID', 'solid')
('ID', 'color')
('KEYWORD', 'style')
('ID', 'collage')
('KEYWORD', 'text')
('STRING', 'we all love animals')
('KEYWORD', 'placement')
('ID', 'middle')
('KEYWORD', 'overlay')
('ID', 'yes')
('KEYWORD', 'text')
('STRING', 'of course')
('KEYWORD', 'placement')
('ID', 'bottom')
('KEYWORD', 'overlay')
('ID', 'no')
('KEYWORD', 'count')
('INT', '50')
('KEYWORD', 'save')
('KEYWORD', 'images')

-- code seems correct. we are getting 5 different token types that are parsed correctly.

Token Types seen:
KEYWORD: Represents keywords in the language like create, meme, background, load, etc.

ID: Represents identifiers, which include words like blue, dogs, solid, etc.

INT: Represents integer literals like 1024, 50.

STRING: Represents string literals like "we all love animals", "of course".

OP: Represents operators, in this case, just x.




How to Running Everything:

make program an executable: chmod +x run_meme_lexer.sh

this is how to run the lexer with shell script:
./run_meme_lexer.sh


The meme_lexer.py has all 5 sample_input cases with one showing have errors are handled. When running the executable, the output ie tokenization is printed for each sample_input case

The Sample_meme_code.txt just hold the sample_inputs that as used in the meme_lexer.py.

The scanner.sh is an old shell script that we used for testing but is not used for the final run.


How our scanner works: 

This project contains a simple Python-based lexical scanner for a meme generation language. The Scanner class reads and tokenizes the source code, identifying keywords, operators, integers, and string literals from a provided meme creation script. The scanner processes commands such as create meme, load pictures, size, text, and save images to facilitate meme customization, including text placement, image loading, and overlay options.

Features:
Keywords: Recognizes commands like create, meme, background, load, size, text, save, etc.
Operators: Identifies operators such as x for dimensions.
Delimiters: Handles spaces and newlines for separating tokens.
Error Handling: Catches unexpected characters as lexical errors.
Example Inputs:
Several sample meme generation scripts are provided, including parameters for background color, image loading, text placement, and more. The Scanner class converts these scripts into tokens for further processing.
