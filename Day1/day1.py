# a=3 
# b=5
# print a,b
# name='joe'
# print 'hello %s' %(name)
# a= input("Enter something : ")

# print a+10,
# print (' is entered')
# a=input("if a list is entered it takes as list in input")
# print a,' is a list'
# a=raw_input("if a list is entered it takes as list in input")
# print a,' is a string'
# print 1+3,1.5*4,2**5,2+1j+3+2j
# s="hello"
# print s
# a=raw_input("first letter :")
# s=a+s[1:]
# print s
# s='HELLO'
# print s[0:-1]+ " Mahesh"
s="IITM Conducts its SPW program Now"
# print s[::2] +"  "+s[1::2]
# print s.find("IT")
# help (s.find) where s is string to see how find works
# dir(s) to see all s (String Methds)
# print dir(s)
# help(s.strip)
# help(list)
l=['hi',True,5,3.14]
# (l.reverse())
# print l
# d={'a':2,'b':4,'c':5}
# d['d']=7
# d['a']=1
# print d," aand keys" ,d.keys()," $ values" ,d.values()," and haskey a", d.has_key('a')
# x=set('abcde')
# y=set('bdxyz')
# a='b' if True else 'w'
# b='b' if '' else 'w' #'' means false
# c='b' if 'dfsf' else 'w' #'dfsf' means true
# print a,b,c
# for i in [1,2,3,4,5,6,7]:
# 	print i
# 	if (i%7==0):
# 		break
# else: print 'None is div by 7'

y=input('Enter Num :')
x=int(y**0.5)
while x>1:
	if y%x==0:
		print y, 'has a factor', x 
		break
	x=x-1
else:
	print y," is prime"