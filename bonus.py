A = int(80000)
B = int(200000)

#Taxa do País A = 3% -> 1.03
#Taxa do País B = 1.5% -> 1.015

Anos=int(0)
while A<B :
    A=A*1.03
    B=B*1.015
    Anos+=1

print(f"{Anos}")