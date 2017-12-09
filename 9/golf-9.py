i=open("9").read()
g=h=o=s=t=0
for c in i:
 if s:s=0;continue
 if g:
  if c=="!":s=1
  elif c==">":g=0
  else:t+=1
 else:
  if c=="{":h+=1
  elif c=="}":o+=h;h-=1
  elif c=="<":g=1
print(o,t)
