import os.path

# user input
filename = input("Provide a filename including its file extension.\n e.g 'python_notes.txt'\n> ")

# splits the filename in two parts
# (filename, extension)
filename_splitted = os.path.splitext(filename)

# saves the extension in a variable
extension = filename_splitted[1]

# removes extension from the original filename
clean_filename = filename.removesuffix(extension)
print(f"  {clean_filename}")

# I know this could be more straightforward by just printing the first part of the 
# filename_splitted variable, but I wanted to do this step by step for further
# reference on how this works, and to meet the exercise's requirement of using 
# removesuffix()

# https://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python
# https://docs.python.org/3/library/os.path.html
