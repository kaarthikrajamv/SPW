#FILTERER FINISHED
# def filterer(l,n):
# 	return [x for x in l if len(x)>n]
# l="Given a dictionary consisting of words from a document as keys and the frequency of the words in the document as values, write a function which takes as parameters this dictionary and a number n, and returns a list of top n most frequent words in the dictionary."
# l=l.split()
# n=input("Number")

# print filterer(l,n)
# print filter(lambda x:len(x)>n,l)

#2

# def addtime(t1,t2):
# 	s=t1[2]+t2[2]
# 	m=t1[1]+t2[1]
# 	h=t1[0]+t2[0]
# 	if t1[2]+t2[2]>60:
# 		s-=60
# 		m+=1
# 	if t1[1]+t2[1]>60:
# 		m-=60
# 		h+=1
# 	return (h,m,s)
# t1=input("First time :")
# t2=input("Second time :")
# print addtime(t1,t2)

#3

# def pig_latin(s):
# 	vowel = ["a","e","i","o","u"]
#  	if s[0].lower() in vowel:
#  		return  s+"hay"
#  	else:
#  		return s[1:]+s[0]+'ay'
# print pig_latin("Hello")
# print pig_latin("hello")
# print pig_latin("ello")
# print pig_latin("Ello")

#4
# import  numpy as np
# l="Given a dictionary consisting of words from a document as keys and the frequency of the words in the document as values, write a function which takes as parameters this dictionary and a number n, and returns a list of top n most frequent words in the dictionary"
# l=l.split()
# l=map(lambda x:len(x),l)
# print np. argmax(l) +1

#5
# dict=input("Enter : ")
# d={'a':32,'the':12,'an':5}
# n=input("Num : ")
# data=d.items()
# data.sort(key=lambda tup: tup[1],reverse=True)
# data ={key:val for key,val in data[:n]}
# print data

#6


# print reduce(lambda x,y:x if x>y else y,[1,3,4,2,6])
# print reduce(lambda x,y:max(x,y),[1,3,4,2,6])
#
# print [(x,y,(x*x+y*y)**0.5) for x in range(1,51) for y in range(1,51) if (x*x+y*y)**0.5==(int((x*x+y*y)**0.5))  ]
# 
m1=[[1,2,3],[2,4,5]]
m2=[[3,4],[3,6],[6,1]]


# input("m1:")
# input("m2:")
# if(len(m2)!=len(m1[0])):
# 	print "Incompatible"
# else:
# 	mr=[[0 for j in range (len(m2[0])) ] for i in range(len(m1)) ]
# 	mr = [[sum(m1[i][k]*m2[k][j] for k in range(len(m2))) for j in range(len(m2[0]))] for i in range(len(m1))]
# 	print mr


# try: 
# 	print 1/0
# except :
# 	print  
# finally:
# 	print "In finally"
# print "I too tried it"
# fin =open('sampleawe4y.txt','r')


 # 	line =fin.readline()
	# line=line.strip()
	# line=list(line)
	# line=[x for x in line if x.isalpha()]
	# print line
	# rev=line[:]
	# rev.reverse()
	# if line==rev:
	# 	print "Palind"
	# else:
		# print "No Palind"
# d={i:0 for i in range (1,20)}

# try:
# 	fin = None
# 	fin =open('palind.txt','r')
# 	for i in fin.readlines():
# 		for j in i.split():
# 			d[len(j)]+=1

# except IOError:
# 	# print fin
# 	print("File Not Found")
# except TypeError:
# 	print("Invalid File Error")
# finally:
# 	print
# 	if fin:
# 		fin.close()
# print d.items()
d={}

try:
	fin = None
	fin =open('sample.txt','r')
	for i in fin.readlines():
		for j in i.split():
			if d.has_key(j):
				d[j]+=1
			else :
				d[j]=1


except IOError:
	# print fin
	print("File Not Found")
except TypeError:
	print("Invalid File Error")
finally:
	print
	if fin:
		fin.close()
print {k:v for k,v in d.items() if v==1}.keys()