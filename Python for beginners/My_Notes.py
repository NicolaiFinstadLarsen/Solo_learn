print("Hei \nnå er jeg på ny linje og \n\tnå er jeg i en tab")
#husk å bruke små bokstaver

print()#dette lager bare en linje i terminalen

print("""Hei!
Nå kan jeg
skrive 
på mange 
linjer pga 3 stk 'hermetegn'""")

print() #dette lager bare en linje i terminalen

#man kan gange opp en string for å printe den x antall ganger.
print("en string" * 2)
print(4 * "2")

print() #dette lager bare en linje i terminalen 

nums = [1,2,3,4]
print(4 not in nums)
print(not 5 in nums)
print(4 in nums)
if 2 in nums:
    print("Its true and stuff")
    
print()

str = "testing for loops"
count = 0

for x in str:
   if(x == 't'):
    count += 1

print(count)

print()

nums2 = list(range(5))
print(nums2)
print(nums2[4])

print()

nums3 = list(range(1,10,2)) #siste argument gir steps 
nums4 = list(range(10,1,-1)) #liste teller nedover
print(nums3)
print(nums4)

print()

for i in range(5):
    print("yo" * 2) #printer "yo" 5 ganger og yo x 2 per linje
    
print()

# =============================================================================
# List slices
# Kan finne frem til en del av listen
# =============================================================================

liste = [1,2,3,4,5,6,7,8,9,0,10]
print(liste[2:5]) #for å gjøre dette bruker man : 
print(liste[5:7])
print(liste[1:]) #her slicer man til slutten av listen
print(liste[:10]) #her slicer man fra begynnelsen av listen

tup = ("a","b","c") #kan også slice tuples
print(tup[:2])

print(liste[1:8:2]) #kan også legge in steps argument
print(liste[::3])
print()
print(liste[::-1]) #negative steps kan brukes til å snu en liste
print(liste[1:5-2]) #fjerner de to siste tallene i listen man slicer 
print(liste[5:1:-1]) # snur liste og teller ned i -1 steps

print()

letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters.index('r'))
print(letters.index('p'))


words = ["Python", "fun"]
words.insert(1, "is")
print(words) 

print()

# string formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2} {3}". format(nums[0], nums[1], nums[2], nums[0])
print(msg)

#med .format kan man plassere indexer fra strings eller lister

print("{0}{1}{0}".format("abra","cad")) # som placeholders


test = "Magikeren sier {a}{b}{a}".format(a="abra",b="cad")
print(test)

print()

print(", ".join(["spam", "eggs", "ham"])) #joiner en liste med første arg som - 
#separator
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", ")) #splitter en string til en liste med 
#separator etter split 
#prints "['spam', 'eggs', 'ham']"

print()

def max(x, y):
    if x >=y:
        return x
    else:
        return y
    """
    forklare litt greier av koden her.
    og her kanskje
    """    
print(max(4, 7))
z = max(8, 5)
print(z)