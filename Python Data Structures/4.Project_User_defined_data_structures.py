# =============================================================================
# Balanced Parentheses
# 
# 
# Parentheses are balanced, if all opening parentheses have their corresponding
# closing parentheses.
# 
# Given an expression as input,
# we need to find out whether the parentheses are balanced or not.
# For example, "(x+y)*(z-2*(6))" is balanced,
# while "7-(3(2*9))4) (1" is not balanced.
# 
# The problem can be solved using a stack.
# Push each opening parenthesis to the stack and pop the last inserted
# opening parenthesis whenever a closing parenthesis is encountered.
# If the closing bracket does not correspond to the opening bracket,
# then stop and say that the brackets are not balanced.
# Also, after checking all the parentheses,
# we need to check the stack to be empty -- if it's not empty,
# then the parentheses are not balanced.
# 
# Implement the balanced() function to return True if the parentheses
# in the given expression are balanced, and False if not.
# 
# Sample Input:
# (a( ) eee) )
# 
# Sample Output:
# False
# You can use a simple list for a stack. Use list.insert(0, item)
# to push on the stack, and list.pop(0) to pop the top item.
# You can access the top element of the stack using list[0].
# =============================================================================


def balanced(expression):
    #your code goes here
    
    stacks = []
    for i in expression:
        if i == "(":
            stacks.insert(0, "(")
            tot = 1
            #print("(", stacks)
        if i == ")":
            try:
                stacks.pop(0)
                tot = 1
                #print(")", stacks)
            except:
                tot = 0
                print(False)
                break


    if tot != 0:
        if stacks == []:
            print(True)
        else:
            print(False)
            
#balanced(input()) #for bruk ved innlevering til SoloLearn            
balanced(" () () ( ") #test cases for bruk under konstruksjon
balanced(" () () () ") #test cases for bruk under konstruksjon
balanced(" ))))()()()") #test cases for bruk under konstruksjon
balanced(" ((((()()()") #test cases for bruk under konstruksjon