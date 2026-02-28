rows=int(input("Number of rows: "))
cols=int(input("Number of columns: "))

serv1 = []   

for i in range(rows):
    row = []            
    for j in range(cols):
        row.append(int(input()))
    serv1.append(row) 
 
serv2=serv1
serv3=serv1
serv4=serv1

s1=list(bin(int(input("Enter query for server 1 (row): ")))[2:])
t1=list(bin(int(input("Enter query for server 1 (column): ")))[2:])
cs=int(input("Enter CHANGE index of row: "))
ct=int(input("Enter CHANGE index of column: "))
s2=[] 
t2=[]

for i in range(len(s1)):
    if i==cs:
        if s1[i]=='0':  
            s2.append('1')
        else:
            s2.append('0')
    else:
        s2.append(s1[i])
    if i==ct:
        if t1[i]=='0':
            t2.append('1')
        else:
            t2.append('0')
    else:
        t2.append(t1[i])

sum1=0
sum2=0
sum3=0
sum4=0

for i in range(len(s1)):
    for j in range(len(t1)):
        if (s1[i]==t1[j]) and s1[i]=='1':
            sum1^=serv1[i][j]
        if (s2[i]==t1[j]) and s2[i]=='1':
            sum2^=serv2[i][j]
        if (s1[i]==t2[j]) and s1[i]=='1':
            sum3^=serv3[i][j]
        if (s2[i]==t2[j]) and s2[i]=='1':
            sum4^=serv4[i][j] 

res=sum1^sum2^sum3^sum4
print("Result: ",res)
