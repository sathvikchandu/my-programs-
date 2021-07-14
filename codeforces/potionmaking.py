def ratioFunction(num1, num2):
    num1 = input('Enter the first number: ')
    num1 = int(num1) # Now we are good
    num2 = input('Enter the second number: ')
    num2 = int(num2) # Good, good
    ratio12 = int(num1/num2)
    print('The ratio of', num1, 'and', num2,'is', ratio12 + '.')

ratioFunction(10, 20)