#----------------- ITERABLES ---------------------#
# an iterable is basically an object that any user can iterate over
#in python iterables include all sequence types
#such as list tuple and string
##and some of them non sequence
##types like dict,fileobjects and object of classes
#we can not access individual elements directly
#indexing methon wont work for sets and dict are unordered

alist=[2,4,6,8,10]
##print(alist)

##cities=['Bhopal','Mumbai','Dehli','Jaipur']
##print(cities)

##list1=[1,2,3,"hello"]
##for i in list1:  #in list1 is iterables
##    print(i)

##for i in (1,2.3,4.5,6):
##    print(i)
##
##for i in 'hello':
##    print(i)

##f=['apple','mango','banana','cherry']
##i=0
##while i<len(f):
##    print(f[i])
##    i=i+1

##f={'apple','mango','banana','cherry'}
##i=0
##while i<len(f):
##    print(f[i])
##    i=i+1

#--------ITERATORS----------------
# An iterator is an object that helps a user in iterating over another object
#an iterator is generated when we pass an iterable to iter()method
# It gives one value at a time
 #by the help of iter() it converts an iterable into an iterator
# every  iterator is also an iterable,but not every iterable is an iterator in python



x=iter(alist) #it returns an iterator object
##print(x)

 
#FOR accessing values from an iterator we use __next__()
## and __next__() we use for  iterating
## it returns the next item available for iteration

##print(x.__next__())

##here next is same as __next__()

##print(next(x))
##print(next(x))
##print(next(x))
##print(next(x))
##print(next(x))
##print(next(x))  #it will raise a stop iteration error

# or instead of that we use for loop to access it
##print(next(x))  iterator prints a value only once

##for i in x:
##    print(i)
##for i in {1,2,3,'g'}:
##    print(i)

    #loop will start from second value

s='python'
s=iter(s)
##print(s)  #<str_iterator object at 0x000001901E8CEB00> that output

##print(next(s))
##print(next(s))
##print(next(s))
##print(next(s))
##print(next(s))
##print(next(s))
##print(next(s))  #this will shows error StopIteration
##there is no further elements available

##cities=['Bhopal','Mumbai','Dehli','Jaipur']
##c=iter(cities)
##print(next(c))
##print(next(c))
##print(next(c))
##print(next(c))
##print(next(c))



