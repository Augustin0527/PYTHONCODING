import math
 
AB = float(input('Enter length of AB: '))
BC = float(input('Enter length of BC: '))
AC = float(input('Enter length of AC: '))
 
angleNeeded = input('Angle Needed [A, B or C]: ').upper()
 
sumOfSquares = {'A':AB*AB + AC*AC, 'B':BC*BC + AB*AB, 'C': AC*AC + BC*BC}
sqOfOppSide = {'A':BC*BC, 'B':AC*AC, 'C':AB*AB}
denominator = {'A': 2*AB*AC, 'B': 2*BC*AB, 'C': 2*AC*BC}
            
fraction = (sumOfSquares[angleNeeded] - sqOfOppSide[angleNeeded])/denominator[angleNeeded]
 
angle = math.degrees(math.acos(fraction))
 
print('Angle %s = %.1f degrees' %(angleNeeded, angle))
