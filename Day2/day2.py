# def hello(greet="Hello",name="Raja",number=3):
# 	print greet ," ",name," ",'!'*number


# hello ();
# hello('hi',number=1);
# hello('hi',3)#will give wrong value prints hi 3

# lambda function is used to def function without name as in  java
# map ()
# filter () samw as map but returns bool amd new list has only true bool ones

# l=[1,2,3,4,5,6,7]
# l2=[2,4,6,8,10,11,21]

# print map(lambda x: x+2,l) #[3, 4, 5, 6, 7, 8, 9]
# #map can also be used for two lists like
# print map(lambda x,y: x+y,l,l2) #[3, 6, 9, 12, 15, 17, 28]
# # lambda can also be used to name function which are short
# print (x)
# f=lambda x:x+2
# print f(3) #5
# f("hi")

#reduce continuously applies the function to first to elements of list to finally give a single value
# print reduce(lambda x,y:x+y,l) #28
# print reduce(lambda x,y:x+y,range(1,101)) ##5050

# print filter(lambda x:x>10, l2) #[11, 21]
# d={1:2,2:2,3:5}
# # print {v:v }
# d={v:k for k,v in d.items()} #since two values has value 2 in original the key 2 getsw the latest value
# print d
# print d.items()#[(1, 2), (2, 2), (3, 5)]
# fin=open('words.txt','r')
# fout=open('write.txt','a')
# i=1
# lines= fin.readlines()
# fout.write("\nSTART OF THIS PROGRAM \n")
# for line in lines:
# 	line=line.strip()
# 	if line =='':continue
# 	print str(i)," : ", line
# 	fout.write(str(i)+" : "+ line+"\n")
# 	i+=1
# fout.write("\nEND OF THIS RUN\n")
# fin.close()
# fout.close()
