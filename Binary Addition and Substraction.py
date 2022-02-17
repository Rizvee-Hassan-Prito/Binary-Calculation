# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 18:27:38 2022

@author: User
"""
#ps=[1,2,8,16,32,64,128,256,512,1024,2048,4096,8192,16384]
print("\n\t Decimal to Binary Conversion and Addition for two Numbers")
print("\n***NB: Subtraction can be done by giving the input in addition form***")
a=int(input("Enter Decimal Number:"))
b=int(input("Enter Decimal Number:"))
sum_dec=a+b

a_bin=bin(a).replace("0b", "")
b_bin=bin(b).replace("0b", "")

a_bin_lst=list(a_bin)
b_bin_lst=list(b_bin)



if a<0:
    one=False
    a_bin_lst.remove('-')
    
    for i in range(len(a_bin_lst)-1,-1,-1):
        
        if(one==True):
            if(a_bin_lst[i]=='1'):
                a_bin_lst[i]='0'
            else:
                a_bin_lst[i]='1'
        if(a_bin_lst[i]=='1' and one==False):
            one=True
    
    pos_wt=1; pos_wt_sum=0
    if(a_bin_lst[len(a_bin_lst)-1]=='1'):
        pos_wt_sum+=1
    
    for i in range(len(a_bin_lst)-2,-1,-1):
        pos_wt*=2
        
        if(a_bin_lst[i]=='1' and i==0):
            pos_wt_sum+=(pos_wt*(-1))
        
        elif(a_bin_lst[i]=='1'):
            pos_wt_sum+=pos_wt
    
    if(pos_wt_sum!=a):
        new_bin_lst=[]
        while(1):
            pos_wt*=2
            new_bin_lst.append('1')
            if(pos_wt_sum+(pos_wt*(-1))==a):
                break
            else:
                 pos_wt_sum+=pos_wt
    
    a_bin_lst=new_bin_lst+a_bin_lst

if b<0:
    one=False
    b_bin_lst.remove('-')
    
    for i in range(len(b_bin_lst)-1,-1,-1):
        
        if(one==True):
            if(b_bin_lst[i]=='1'):
                b_bin_lst[i]='0'
            else:
                b_bin_lst[i]='1'
        if(b_bin_lst[i]=='1' and one==False):
            one=True
    
    pos_wt=1; pos_wt_sum=0
    if(b_bin_lst[len(b_bin_lst)-1]=='1'):
        pos_wt_sum+=1
    
    for i in range(len(b_bin_lst)-2,-1,-1):
        pos_wt*=2
        
        if(b_bin_lst[i]=='1' and i==0):
            pos_wt_sum+=(pos_wt*(-1))
        
        elif(b_bin_lst[i]=='1'):
            pos_wt_sum+=pos_wt
    
    if(pos_wt_sum!=b):
        new_bin_lst=[]
        while(1):
            pos_wt*=2
            new_bin_lst.append('1')
            if(pos_wt_sum+(pos_wt*(-1))==b):
                break
            else:
                 pos_wt_sum+=pos_wt
    
    b_bin_lst=new_bin_lst+b_bin_lst
 
if(len(a_bin_lst)>len(b_bin_lst)):
    lst=[]; n=len(a_bin_lst)
    x=n-len(b_bin_lst)
    if(b<0):
       for i in range(0,x):
           lst.append('1')
    else:
        for i in range(0,x):
           lst.append('0')
    b_bin_lst=lst+b_bin_lst

else:
   lst=[];n=len(b_bin_lst)
   x=n-len(a_bin_lst)
   if(a<0):
       for i in range(0,x):
           lst.append('1')
   else:
        for i in range(0,x):
           lst.append('0')
   a_bin_lst=lst+a_bin_lst
    
a_bin_str=str();b_bin_str=str()
for i in (a_bin_lst):
    a_bin_str=a_bin_str+i
for i in (b_bin_lst):
    b_bin_str=b_bin_str+i

"""
print('\nA=',a_bin,"\nB=",b_bin)
print('\nA=',a_bin_lst,"\nB=",b_bin_lst)
print('\nA=',a_bin_str,"\nB=",b_bin_str)
"""
sum_bin=int(a_bin_str, 2) + int(b_bin_str, 2)
result=bin(sum_bin).replace("0b", "")
if(len(result)<n):
    x=str()
    for i in range(0,(n-len(result))):
        x+="0"
    result=x+result

range1=-2**(n-1)
range2=(2**(n-1))-1

print("\n\nRange:")
print("\n-2(n-1) to (2^(n-1))-1")
print("\n= -2 ^ (",n-1,") to ( 2 ^ (",n-1,"))-1")
print("\n= ",range1,"to",range2)

print("\n\nConvertion:")
if a<0:
    print("\n(",a*(-1),")\u2081\u2080","=","(",a_bin.replace("-", ""),")\u2082","----(2's Comp.)--->",
          "(",a_bin_str,")\u2082","= (",a,")\u2081\u2080")

if b<0:
    print("\n(",b*(-1),")\u2081\u2080","=","(",b_bin.replace("-", ""),")\u2082","----(2's Comp.)--->",
          "(",b_bin_str,")\u2082","= (",b,")\u2081\u2080")

print("\n\nCalculation:")
print("\n",a,"->  ",a_bin_str)
print("\n",b,"->(+)",b_bin_str)
print("---------------------")

status=""
if(sum_dec<range1):
        status='(Underflow)'
elif(sum_dec>range2):
        status='(Overflow)'

if(len(result)>n):
    r=list(result)
    del(r[0]);r="".join(r)
    print("\n",sum_dec,"     ",result,"(",int(r,2),")\u2082",status)
else:
    print("\n",sum_dec,"     ",result,status)

if(len(result)>n):
    print("\n          ^           ")
    print("\n          |--Discard MSB")    