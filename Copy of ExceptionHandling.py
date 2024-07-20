# -------------- Exception Handling --------------

# An exception in Python is an incident that happens while
# executing a program. When a Python program meets an error, it
# stops the execution of the rest of the program. When a Python
# code comes across a condition it can't handle, it raises
# an exception.

# In Python, we catch exceptions and handle them using try and
# except code blocks. The try clause contains the code that
# can raise an exception, while the except clause contains the
# code lines that handle the exception.

# ----------------------------------------------------

# any number divisible by zero raise a zero division error
# and the error can be handled by raising an exception

##a = 3
##b = 0
##print(a/b)
##try:
##    print(a/b)
##
##except:
##    print("Exception Handled")

##print("End of program")

# ---------------------------------------------------------

##num1 = int(input("Enter a number: "))
##num2 = int(input("Enter another number: "))
##
##try:
##    print(num1/num2)
##
##except Exception as e:
##    print("This operation is incorrect :", e)


# -------------------------------------------------------
# opening and closing of a program

##num1 = input("enter 1st num: ")
##num2 = input("enter 2nd num: ")

##try:
##    print("Start of a program")
##    print(int(num1)/int(num2))

##except Exception as e:
##    print("This is invalid :", e)

##finally:
##    print("End of Program")


##print("Program Terminated")

# ----------------------------------------------------------

##def weight(var):
##    try:
##        return int(var)
##    except Exception as ex:
##        print("It raises an error :",ex.args)
##
##print(weight('ten pounds'))


# ---------------- Custom Exception ----------------

##class NameTooLong(Exception):
##    pass
##
##name = input("enter a name : ")
##
##try:
##    if(len(name)>15):
##        raise NameTooLong("Name Too Long")
##
##except NameTooLong as e:
##    print(e)


    
