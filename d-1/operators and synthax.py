#operators are the special symbols in any programming language to carry out
#arithmetic and logical operations

a = 1
b = 2
c = a + b
# here '=' is an assignment operator  '+' is an arithmetic operator

#Arithmetic  Operators
#Addition (+)
#Subbtraction (-)
#Multiplication (*)
#division (/)
#Floor Division (//) => Floor division receives the decimal value and only
#provides  the integer towards floor.

print( 3//2) # It gives 1
print (-3//2) # it gives -2

#Exponential (**)
print(3**2) # it gives 9

#Modulus (%) => Gives remainder of a division
print (3 % 2) # Gives 1
print (4 % 2) # Gives 0




###### Comparision / Relational Operators ######
# ==,<, >,!=,>= , <= are the relational operators

print ( 4==5) # False
print ( 6 !=3) # True


#logical operators
#and , or , not are the logical operations and their operators are "and", "or"
#and "not" respectively. THE Results in logical operatons are either True or False



#Identity operators
#Identity operators check whether they are same or not .'is' and
#'is not' are used for the identity check.
a=1
b=1
print(a is b) # True
print(id(a))
print(id(B)) #For the same object , id () gives equal value


#Membership Operators
#It is used to check  membership of an object in a sequencen. 'in' and 'not in' are
#used for membership check
print (2 in [1,2,3])  # True
print (3 not in [1,2,4]  # False


#Assignment Operator
#The result of any operation can be assigned to a variable using assignment
#operator."=" is a basic assignment operator .
name = "jon"  # here = is an assignment operator

#+=,-=,*=,/= are also some of the assignment operators
a= 1
a = a + 1 # This line can also be written as a +=1
print(a) #2
a +=1 #3
print (a)


#Precedence and Associativity
#Precedence of the operators is the rule  that determines  which operator should be
#executed first
#If multiple operators is an operation  have the same precedence then  then associativity
#determines he operation sequence

#Normally associativity is from left -right except for the case of (**).
#For exponent (**), it is from right - left

print(2**3**2) # 512


