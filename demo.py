s1=input("enter a sentence")
s2="john"
count=0
s=s1.split(' ')
for i in s:
    if(s2 in i):
        count+=1
print(count) 