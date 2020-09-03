n=input()
res=" "
for i in n:
    if i=='C':
        res=res+'G'
    elif i=='G':
        res=res+'C'
    elif i=='T':
        res=res+'A'
    elif i=='A':
        res=res+'U'   
    else:
        res='Invalid Input'
        break
print(res)
