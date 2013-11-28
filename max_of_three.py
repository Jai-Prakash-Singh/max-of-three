#/usr/bin/env python 


def max_of_two(no1, no2):
    if no1 > no2:
        return no1
    else:
        return no2


def max_of_three(num1, num2, num3):
    result1 = max_of_two(num1, num2)
    result2 = max_of_two(num3, result1)
    print "%d is bigger among %d, %d and %d"%(result2, num1, num2, num3)


if __name__=="__main__":
    try:
        num1 = int(raw_input("Enter the first number: "))
	num2 = int(raw_input("Enter the second number: "))
	num3 = int(raw_input("Enter the third number: "))
	max_of_three(num1, num2, num3)
    except:
        print " wrong input"  
