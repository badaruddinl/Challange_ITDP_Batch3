bambu = [3,2,2] 
cuts = 3
print("cuts:"   ,cuts-1)
print("Cycle : "+str(w))
  for x in range(len(bambu)):
    temp = "|"
    for y in range(bambu[x]):
      temp = temp+"-"
    print(temp)
    bambu[x] = bambu[x]-1