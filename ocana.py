# Ocana - main program
import sys

# Get the file name from the command line
filename = sys.argv[1]

# Open the file and read all its text
with open(filename) as f:
    source = f.read()

# Show the text on screen
print(source)
