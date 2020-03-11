from collections import Counter

with open ('scribble.txt' , 'r') as f:
    contents = f.read()
    count = Counter(contents)
    print ("I count " +(str(count['e']))+" e's in it")

    

    
