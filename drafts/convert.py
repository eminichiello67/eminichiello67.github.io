import re

# This little python script converts $...$ in
# a markdown file to \(...\) so that it renders in Jekyll serve.

input = input()

with open(input, "r") as f:
    text = f.read()

# Replace $$ ... $$ with \( ... \)
text = re.sub(r"\$(.+?)\$", r"\\(\1\\)", text, flags=re.DOTALL)

with open(input, "w") as f:
    f.write(text)
