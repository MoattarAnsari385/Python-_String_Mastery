name = "moattar"
number = "123"

# Length of the string
print(len(name))  

# Check if the string ends with "tar"
print(name.endswith("tar"))  

# Check if the string starts with "Moatt"
print(name.startswith("Moatt"))  

# Capitalize the first letter
print(name.capitalize())  

# Convert string to uppercase
print(name.upper())  

# Convert string to lowercase
print(name.lower())  

# Remove leading and trailing whitespace
print("  hello".strip())  

# Replace "moattar" with "fatima"
print(name.replace("moattar", "fatima"))  

# Find the index of the first occurrence of "o"
print(name.find("o"))  

# Split the string into a list of words (default separator is space)
print(name.split())  

# Check if all characters in the string are alphabetic
print(name.isalpha())  

# Check if all characters in the string are digits
print(number.isdigit())  

# Convert the first character of each word to uppercase
print("hello world".title())  

# Count occurrences of the character "l"
print("hello".count("l"))  

# Join a list of words into a single string with spaces
words = ['Python', 'is', 'fun']
sentence = " ".join(words)
print(sentence)  
