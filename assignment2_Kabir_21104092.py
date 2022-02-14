#Question No.1

a="Python is a case sensitive language"

A.) Part
print(len(a))

#output
35


#B.) Part
 def myfunction(x):
     return x[::-1]
 result=myfunction(a)   
 print(result) 

#output
egaugnalevitisnesesacasinohtyp



#C.) Part
 b=a[10:27]
 print(b)

#output
a case sensitive




#D.) Part
 x=a.replace("a case sensitive","object oriented")
 print(x)

#output
Python is object oriented language




#E.) Part
 x=a.index("a")
 print(x)

#output
11




#F.) Part
 x=a.replace(" ","_")
 print(x)

#output
Python_is_a_case_sensitive_language








#Question No.2
 a=str(input("Enter Your Name: "))
 b=str(input("Enter Your Department: "))
 c=int(input("Enter Your SID: "))
 d=float(input("Enter Your CGPA: "))
 print("Hey"+","+str(a)  +  " Here!")
 print("My SID is "+ str(c))
 print("I am from "+ str(b) + " department and my CGPA is "+ str(d))
    
 #output
Enter Your Name: Kabir 
Enter Your Department: Electrical
Enter Your SID: 21104092
Enter Your CGPA: 10
Hey Kabir Here!
My SID is 21104092
I am from Electrical department and my CGPA is 10

    












#Question No.3
 a=56
 b=10
#A.) Part
 c=a&b
 print(c)

#output
8


#B.) Part
 c=a|b
 print(c)

#output
58


#C.) Part
 c=a^b
 print(c)

#output
50


#D.) Part
 a=a<<2
 b=b<<2
 print(a&b)
    
#output 
32



#E.) Part
 a=a>>2
 b>>=4
 print(a&b)
 
#output
0






#Question No.4
 a=int(input("Enter No.1: "))
 b=int(input("Enter No.2: "))
 c=int(input("Enter No.3: "))
 d=max((a,b,c))
 print(d)
    
 #output
Enter No.1: 3
Enter No.2: 5
Enter No.3: 99
99    




#Question No.5
 a=str(input("Enter any string: "))
 b="name"
 if(a.count(b)>0):
     print("YES")
 else:
     print("NO")    
        
#output
Enter any string: My name is Kabir Sharma.
YES






#Question No.6
 a=int(input("Enter length of shortest side: "))
 b=int(input("Enter length of side 2: "))
 c=int(input("Enter length of longer side: "))
 if(a+b<c):
     print("NO")
 else:
     print("YES")    
        
#output
Enter length of shortest side: 3
Enter length of side 2: 4
Enter length of longer side: 5

YES    
    














