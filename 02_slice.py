# Positive Slicing
name = "Moattar"
short_name = name[0:3] # start from index 0 all the way till 3 (excluding 3) 
print(short_name)

character1 = name[1]
print(character1)

# Negative Slicing
myName = "Aroob"
print(myName[-4 : -1]) 
print(myName[1 : 4]) 

# Advance Slicing
print(myName[: 4]) # is same as print(myName[0 : 4])
print(myName[1 :]) # is same as print(myName[1 : 5])

# Slicing With Skip Value

num = "0123456789"
print(num[1 : 7 : 4])  # It will start from index 1, go till index 7 (excluding 7), and then print the numbers from index 1 to 7, picking every 4th index number after the first one. The output will be: 15

word = "amazing"
word[1 : 6 : 2] # start from index 1 and go till index 6 (excluding 6) with a step of 2.

