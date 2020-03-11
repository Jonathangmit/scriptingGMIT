# The song you want to name is 'Eezer Goode'
from collections import Counter
fileName= input("Please name your song: ")
with open (fileName+"."+"txt" , 'r') as f:
    contents = f.read()
    count = Counter(contents)
print ("I count " +(str(count['e']))+" e's in that song. Thats a lot of e's")
answer = input ("would you like to see the lyrics? y/n:")
if answer is "y":
    print (contents)
else:
    print ("naughty naughty, very naughty")
