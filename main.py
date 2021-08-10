import re

test = input()
test1 = test.split()
print(test1)


l1 = []
def extract(lit): 
    for i in lit:
        pattern = '[^a-z][0-9]+'
        tes2 = re.findall(pattern, i)
        l1.append(''.join( tes2))
    return l1
b = extract(test1)  



l2 = []
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
#print(b1)



l4 = ['1','2','3','4','5','6','7','8','9']


l5 =[]
for i in b1:
    for j in i:
        if "0" in j:       
            e=j.replace('0','')
            l5.append(int(e))
        else:
            l5.append(int(j))       

print(l5) 



l3 = []
for i in range(0,200):
    l3.append(i)
    #print(l3)
    
 
l0 = []
for i in l3:
    z1=l5.count(i)
    l0.append(z1)
print(l0)

l9 =[]
for i in b:
    l9.append(i)
    #print(l9)

s1 = set(l9)   
print(s1) 

print(test1[0])
for f in s1:
    k=f[0:2]
    k1=int(k)
    k2=int(f[4:])+ l0[k1] 
    if test1[0:5] == 'sd_fx':
        print(l0[k1],'sd_fx',k,'.%04d.rgb',f[4:],'-',k2)
        print(test1[-1])
    else:
        print(l0[k1],'file',k,'.%04d.rgb',f[4:],'-',k2)
        print(test1[-1])    
            
            
    


