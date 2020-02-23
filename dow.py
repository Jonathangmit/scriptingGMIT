import datetime
L={1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}
dayno = datetime.datetime.today().weekday()
print("todays day is", L[dayno])
if dayno<4:
    print ("dont drink")
else:
    print ("go on have a drink")