filename = input("Enter local filename: ")

with open(filename) as f:
    text=f.read()
#print(text)

def char_looker(text, char):
    count = 0 
    for z in text:
        if z == char:
            count += 1 
    return count

print(char_looker(text, "n"))

#finner prosenten av hver bokstav i teksten
for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * char_looker(text, char) / len(text)
  #linjen under tar lager altså "char - perc%" som man kan printe ut eller lagre i variabel.
  total = ("{0} - {1}%".format(char, round(perc, 2)))
  print(total)
