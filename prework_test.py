#Question 1 Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(user_name):
    """Print a username"""
    user_name=input('Enter USERNAME: ')
    print("hello_"+user_name)

  
hello_name(input)

#Question 2 Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for num in range(100):
        if(num % 2 != 0):
            print(num)
    return

first_odds()

#Question 3 Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    a_list = [100, 64, 395, 407, 8, 145, 15, 4, 890]
    max_num = max(a_list)
    print(max_num)

max_num_in_list(max)

#Question 4 Write a function to return if the given year is a leap year
def is_leap_year(a_year):
    a_year=int(input('Enter year: '))
    if (a_year % 400 == 0) and (a_year % 100==0):
        print(True)
        return True
    elif (a_year % 4 ==0 ) and (a_year % 100 != 0):
        print(True)
        return True
    else:
        print(False)
        return False
    
is_leap_year(input)

#Question 5
def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
    
a_list = [2, 3, 5, 6, 7,]
print(is_consecutive(a_list))