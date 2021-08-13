from enum import unique
import re

input = input()
splited = input.split()


#using regex extraction of only digits #file01_0040.rgb refered this pattern
l1 = []
def extract(lit): 
    for i in lit:
        pattern = '[^a-z][0-9]+'
        tes2 = re.findall(pattern, i)
        l1.append(''.join( tes2))
    return l1
b = extract(splited) 


l2 = []

#removing . and -
def remove(fn):
    for i in range(0,len(fn)):
        st = str(fn[i])
        d=re.findall('_',st)
        if d:
            tes4 = fn[i].split('_')
            l2.append(tes4)
            
        else:    
            tes4 = fn[i].split('.')
            l2.append(tes4)
    
    return l2

b1 = remove(b)


l9 =[] #l9
for i in b1:
        l9.append(i)
               
    


l3 = ['1','2','3','4','5','6','7','8','9'] #l4


l4 = [] #l5
l5 = [] #l7
l6 = [] #l8
def stripz(fn,lst,lst1,lst2): # Striping zeros 
    for i in fn:
        for j in i:
            print("lk",j)
            str = j.lstrip("0")       
            lst.append(str)
    print("op",lst)
    for k in lst:
            if len(k)>1:
                lst1.append(int(k))
            elif len(k)<2:
                lst2.append(int(k))
    return lst,lst1,lst2

st = stripz(l9,l4,l5,l6)        
print("123",st)  


l7 = [] #l3
l8 = [] #l0
def count(lst,lst1,value):# counting files
    for i in range(0,10):
        lst.append(i)
   
    for i in lst:
        z1=value[0].count(str(i))
        lst1.append(z1)
    return lst,lst1 

cn = count(l7,l8,st) 
print("cn",cn)      


j = st[2]

s0 = set(j)

s4 = list(s0)

s1 = list(b)
s2 = list(b)

z = st[1]

   

def dirtory(lst1,lst2,cv,cv1,op):#combining files
    flag=False        
    for j ,i in enumerate(lst2,start=0):
        if str(cv[cv1]) == i[1] and str(op[0]) < i[5:]:  
            lst1.remove(i)          
    flag=True
    return lst1, flag

d1 = dirtory(s1,s2,s4,0,z)

def loop(value,lst1,lst2,id):
    for i in lst1:
        if value[1] == True:
            if lst1.index(i) == id:
                a = lst2[i:]
                return a            

l1 = loop(d1,cn[1],st[1],1)
d2 = dirtory(d1[0],s2,s4,1,l1)


l2 = loop(d2,cn[1],st[1],2)
d3 = dirtory(d2[0],s2,s4,2,l2)

l4 = loop(d3,cn[1],st[1],3)
d4 = dirtory(d3[0],s2,s4,3,l4)


l5 = loop(d4,cn[1],st[1],4)
d5 = dirtory(d4[0],s2,s4,4,l5)


l6 = loop(d5,cn[1],st[1],5)
d6 = dirtory(d5[0],s2,s4,5,l6)


l7 = loop(d6,cn[1],st[1],6)
d7 = dirtory(d6[0],s2,s4,6,l7)



l8 = loop(d7,cn[1],st[1],7)
d8 = dirtory(d7[0],s2,s4,7,l8)

l9 = loop(d8,cn[1],st[1],8)
d9= dirtory(d8[0],s2,s4,8,l9)

l10 = loop(d9,cn[1],st[1],9)
d10= dirtory(d9[0],s2,s4,9,l10)




for f in s2:
    k=f[0:2]
    k1=int(k)
    k2=int(f[4:])+ cn[1][k1] -1 
    if splited [0:5] == 'sd_fx':
        print(cn[1][k1],'sd_fx',k,'.%04d.rgb',f[4:],'-',k2)
        
    else:
        print(cn[1][k1],'file',k,'.%04d.rgb',f[4:],'-',k2)
        
print(splited [-1])    