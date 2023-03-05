import os

# Set the path to the file containing the words
file_path = "ac.txt"  # Replace with the path to your file

# Read the words from the file and store them in a list
with open(file_path, "r") as f:
    words = [line.strip() for line in f.readlines()]

# Create a folder for each word
for word in words:
    folder_path = os.path.join(os.getcwd(), word)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

