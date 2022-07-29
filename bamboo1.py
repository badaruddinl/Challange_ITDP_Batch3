bamboos = [3,2,2]
cuts = 3
print("bamboos :",bamboos)
print("cuts:"   ,cuts-1)
for w in range(cuts):
  if w == 0:
    print("initials:")
  else:
    print("cycle cuts: "+str(w))
  for x in range(len(bamboos)):
    temp = "|"
    for y in range(bamboos[x]):
      temp = temp+"-"
    print(temp)
    bamboos[x] = bamboos[x]-1