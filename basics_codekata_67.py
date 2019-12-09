s=input()
s=list(s)
l=len(s)
for i in range(0,l,2):
    s[i],s[i+1]=s[i+1],s[i]    
print("".join(s))
