name=["aa","bb","cc","dd"]
def fn (x):
	return x.upper()
newname=map(fn,name)
print newname

str=raw_input("Enter name:")
if str=="guvi":
	print ("Hello "+str)
else:
	print("error")


n=int(input("Enter number:"))
count=1
while(count<=10):
	print(n,"x",count,"=",count*n)
	count=count+1


	

print ("Table:")
print("1. Rectangle")
print("2. Square")
print("3. Triangle")
n=int(input("Enter choice:"))
ar,l,b=0,0,0
if n==1:
	l=int(input("Enter length:"))
	b=int(input("Enter breadth:"))
	ar=l*b
elif n==2:
	l=int(input("Enter length:"))
	ar=l*l
else:
	l=int(input("Enter length of base:"))
	b=int(input("Enter height:"))
	ar=.5*l*h
print("area=",ar)	
 



d=int(input("Enter distance:"))
print("table")
print("1. cm")
print("2.m")
n=int(input("Enter choice:"))
c=0
if n==1:
	c=d*100000
else:
	c=d*1000
print("converted distance:",c)	




temp=int(input("Enter temp:"))
print("table")
print("1. celsius to fahrenheit")
print("2. fahrenheit to celsius")
n=int(input("enter choice:"))
if n==1:
	temp=temp+32
else:
	temp=temp-32
print("Converted temp:",temp)	




str=raw_input("Enter string:")
str=str.upper()
print str

n=int(input("Enter number:"))
i=1
while(i<=n):
	print("*"*i)
	i=i+1	
