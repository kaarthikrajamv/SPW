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
d={'a':32,'the':12,'an':5}
n=input("Num : ")
data=d.items()
data.sort(key=lambda tup: tup[1],reverse=True)
data ={key:val for key,val in data[:n]}
print data

#6


