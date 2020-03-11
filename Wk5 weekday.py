#Jonathan Harper Days of week using the date time function
import datetime
L={0:'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
#here I worked for a long time with Monday set at 1 causing all days to slip by 1. Corrected 11/03/20
dayno = datetime.datetime.today().weekday()
print("todays day is", L[dayno])
if dayno<4:
    print ("dont drink")
#I like a drink on a Friday,Saturday or Sunday
else:
    print ("go on have a drink")