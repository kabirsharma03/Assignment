#To count the number of occurences of each word or character in the string entered by the user.
a=str(input("Enter anything of your choice: "))
b=str(input("Enter the word whose number of occurences is to be checked: "))
x=a.count(b)
print(x)

#output
Enter anything of your choice: I like apple and i also like mango
Enter the word whose number of occurences is to be checked: like
2  





 #To write a python script to print next date of input date.

 month=int(input("Month- "))
 day=int(input("Day- "))
 year=int(input("Year- "))

# C1: 1<=month<=12
# C2: 1<=day<=31
# C3: 1800<=year<=2025
 if (month,day,year%4)==(2,28,0):
    print("Next Date is: "+str(day+1)+"/"+str(month)+"/"+str(year))

 elif (month,day)==(2,28):
    print("Next Date is: 1/3"+"/"+str(year))
 elif (month,day)==(12,31):
    print("Next Date is: 1/1"+"/"+str(year+1))

 elif (month,day)==(4,30):
  
    print("Next Date is: 1"+"/"+str(month+1)+"/"+str(year))
 elif (month,day)==(6,30):
    print("Next Date is: 1 "+"/"+str(month+1)+"/"+str(year))
 elif (month,day)==(9,30):
    print("Next Date is: 1"+"/"+str(month+1)+"/"+str(year))
 elif  (month,day)==(11,30):
    print("Next Date is: 1 "+"/"+str(month+1)+"/"+str(year))   
    
 else:

    print("Next Date is: "+str(day+1)+"/"+str(month)+"/"+str(year))   
    
#output    
Month- 2
Day- 28
Year- 2004
Next Date is: 29/2/2004
    
    
    





#To create a list of tuples with first element as the number and second element as the square of number.
a=int(input("Enter first number: "))    
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
list1=[a,b,c]
print([(a,a*a),(b,b*b),(c,c*c)])

#output
Enter first number: 3
Enter second number: 9
Enter third number: 10
[(3,9),(9,81),(10,100)]





#program to prompt the user for a grade between 4 and 10.
x=int(input("Enter your grade point: "))
if(x==4):
    print("Your grade is 'D' and Poor Performance")
if(x==5):
    print("Your grade is 'C' and Below Average Performance")    
if(x==6):
    print("Your grade is 'C+' and Average Performance")    
if(x==7):
    print("Your grade is 'B' and Good Performance")    
if(x==8):
    print("Your grade is 'B+' and Very Good performance")    
if(x==9):
    print("Your grade is 'A' and Excellent Performance")    
if(x==10):
    print("Your grade is 'A+' and Outstanding Performance")    
else:
    print("Error")   
    
#output
Enter your grade point: 10
Your grade is 'A+' and Outstanding Performance

    




x="ABCDEFGHIJK"
a=x.replace("JK","")
b=a.replace("HI","")
c=b.replace("FG","")
d=c.replace("DE","")
e=d.replace("BC","")
print(x)
print(a)
print(b)
print(c)
print(d)
print(e)

#output
ABCDEFGHIJK
ABCDEFGHI
ABCDEFG
ABCDE
ABC
A




#Question No.8
set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}
#A.) Part
x=set1-set2
y=set2-set1
newset=set.union(x,y)
print(newset)

#output
{1,3,5,6,8}

#B.) Part
x=set1-set3
y=set3-set1
z=set.union(x,y)
a=z-set2
b=set2-z
newset=set.union(a,b)
print(newset)

#output
{3,6,8,9,13,17}


#C.) Part
x=set1-set2
y=set1-x
z=set1-set3
a=z-set3
b=x-a
newset=set.union(b,y)
print(newset)

#output
{1,2,4,5}


#D.) Part
x={1,2,3,4,5,6,7,8,9}
newset=x-set1
print(newset)

#output
{6,8,9,13,17}


#E.) Part
x=set.union(set1,set2,set3)
y={1,2,3,4,5,6,7,8,9}
newset=y-x
print(newset)

#output
{7}





# Question No.6
 
 a=str(input("Enter Your Name: "))
 b=int(input("Enter Your SID: "))
 dict={a:b}
 print(dict)
  
 #output
Enter Your Name: Kabir 
Enter Your SID: 21104092
{Kabir:21104092}














#Fibonacci Sequence upto 12 numbers
 def fibonacci(n):
    a=0
    b=1
    if(n==1):
       print(a)
    else:
       print(a)   
       print(b)
       for i in range(2,n):
          c=a+b
          a=b
          b=c
          print(c)

 fibonacci(12)  

#output
0 1 1 2 3 5 8 13 21 34 55 89 144

