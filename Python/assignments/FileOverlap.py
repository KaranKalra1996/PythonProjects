import math
primeNumbersList = [2,3]
for i in range(4,1000):
	flag = 0
	for j in primeNumbersList and j<sqrt(i):
		if(i%j ==0):
			flag = 1
			break;
	if(flag == 0):
		primeNumbersList.append(i)
primeNumbersString = " ".join([str(num) for num in primeNumbersList])
with open("PrimeNumbers.txt","w") as PrimeNumbers:
	PrimeNumbers.write(str(primeNumbersString))
happyNumbersList = [1]
for i in range(2,1000):
	num  = i
	while(True):
		if num==1 :
			happyNumbersList.append(i)
			break
		else : 
			testNumberList = [int(x) for x in str(num)]
			num = 0
			for j in testNumberList:
				num = num + j**2
			if num == 4 or num == 16 or num ==  37 or num ==  58 or num ==  89 or num ==  145 or num ==  42 or num == 20 :
				break
# print("Happy numbers are :- \n")
# print(str(happyNumbersList))
with open("HappyNumbers.txt","w") as HappyNumbers:
	HappyNumbers.write(str(happyNumbersList))

# with open("PrimeNumbers.txt","r") as PrimeNumbers:
# 	primeNumbersList =  PrimeNumbers.read()

# with open("HappyNumbers.txt","r") as HappyNumbers:
# 	happyNumbersList =  HappyNumbers.read()

# print("Prime numbers after reading are :- "+primeNumbersList)

for primeNumber in primeNumbersList:
	if primeNumber in happyNumbersList:
		fileOverlapList.append(primeNumber)
print("Overlap list = "+str(fileOverlapList))
with open("OverLappedFile.txt","w") as OverLappedFile:
	OverLappedFile.write(str(fileOverlapList))
# with open("OverLappedFile.txt","r") as OverLappedFile:
# 	print(OverLappedFile.read())

