# =============================================================================
# Letter Frequency
# 
# 
# You are making a program to analyze text.
# Take the text as the first input and a letter as the second input, and output the frequency of that letter in the text as a whole percentage.
# 
# Sample Input:
# hello
# l
# 
# Sample Output:
# 40
# 
# The letter l appears 2 times in the text hello, which has 5 letters. So, the frequency would be (2/5)*100 = 40.
# Division result is a float. Use the int() function to convert the result to an integer.
# =============================================================================


string = input()
char = input()

counter = string.count(char)

part = counter / len(string)

total = int(part *100)

print(total)

#litt cleaner

counter = ((string.count(char))/ len(string)) *100
print(int(counter))