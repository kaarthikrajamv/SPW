# a=float(input('Enter Values:\n'))
# b=float(input())
# c=float(input())
# print a,b,c
# front=-b/(2*a)
# d=b*b-4*a*c
# if d>0:
# 	print "Root 1 :" , front +d**0.5
# 	print "Root 2 :" , front -d**0.5
# elif d==0:
# 	print "Root :",front
# else:
# 	print "Root 1:",front+((-d)**0.5)*1j
# 	print "Root 1:",front-((-d)**0.5)*1j 

# s=raw_input("Enter String to Reverse:")
# print s, s[::-1],s[-4:]
a=[2,3,4,5,7]
sum=0
b=[]
for i in a:
	sum+=i
	b.append(sum)
print a,b