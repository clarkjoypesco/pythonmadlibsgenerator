# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
    # your code here
    if day == 'Saturday' or day == 'Sunday':
        return True
    return False
    
print weekend('Monday')
#>>> False

print weekend('Saturday')
#>>> True

print weekend('July')
#>>> False


# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints
# out a countdown from that number to 1,
# followed by Blastoff!
# The procedure should not return anything.
# For this question, you just need to call 
# the procedure using the line
# countdown(3)
# instead of print countdown(3).

def countdown(n):
     while n > 0:
        print n
        n -=1
     print 'Blastoff!'


countdown(3)
#>>> 3
#>>> 2
#>>> 1
#>>> Blastoff!



# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):   
    if bigger(a,b) < biggest(a,b,c):
        return bigger(a,b)
    return c



print(median(1,2,3))
#>>> 2

print(median(9,3,6))
#>>> 6

print(median(7,8,7))
#>>> 7

print(median(11,33,22))
#>>> 22

print(median(4,5,6))
#>>> 5

print(median(8,7,7))
#>>> 7