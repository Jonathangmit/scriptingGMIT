#setting and colllecting inputs
h = float(input("enter height in centimetres:"))
w = float (input("enter weight in Kilograms:"))
#performing calculation
bmi = w / ((h/100)**2)
#rounding my calculation to 2 decimal places
dp = (round (bmi,2))
#delivering my output to screen
print ("your BMI is", dp)
if bmi<18: print("skinny mini")
if bmi>18 and bmi<25: print("nearly chunky")
if bmi>25: print ("chunky monkey")