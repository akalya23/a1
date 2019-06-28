sh1=input()
flagg=0
for i in range(0,len(sh1)-1):
  for j in range(i+1,len(sh1)):
    if sh1[i]<sh1[j]:
      flagg=1
      print(sh1[j:])
      break
  if flagg==1:
    break
else:
  print(sh1)
