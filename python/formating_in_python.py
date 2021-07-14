print('{} {}'.format(1,2))
#padding example
print('{:>10}'.format('hellopal'))
#align left example
print('{:10}'.format('heelo'))
#aligning at the center
print('{:^10}'.format('heelo'))
#printing a substring
print('{:.4}'.format('heelo'))
# if you want to print special characeters after entering a strring
print('{:_<10}'.format('heelo'))
#numbers can be represented in a certain width 
print('{: 4d}'.format(34))
#we want our output to have at least 6 characters with 2 after the decimal point.
print('{:06.2f}'.format(3.14161819233))
#if you want to print values with precision
print('{:04d}'.format(34))
#represent siged number
print('{:+d}'.format(9)) #positive number
print('{: d}'.format(-12)) #negative number

#New style formatting is also able to control the position of the sign symbol relative to the padding.
print('{:=5d}'.format((- 23)))

#Both formatting styles support named placeholders.
data = {'first': 'Hodor', 'last': 'Hodor!'}
print('{first} {last}'.format(**data))
            # the above one can also be written as
print('{first} {last}'.format(first='Hodor', last='Hodor!'))

#New style formatting allows even greater flexibility in accessing nested data structures.

person={'first': 'john','last':'james'}
print('{p[first]} {p[last]}'.format(p=person))

#As well as accessing attributes on objects via getattr():
class mywi(object):
    type='graph'
print('{m.type}'.format(m=mywi))