def Knapsack(n,W,Weight,Value):
	if W==0 or n==0:
		return 0
	elif Weight[n-1]>W:
		return Knapsack(n-1,W,Weight,Value)
	else :
		return max(Knapsack(n-1,W,Weight,Value),Value[n-1]+Knapsack(n-1,W-Weight[n-1],Weight,Value))
W = 50
n = 3
Weight = [10,20,30]
Value = [230,100,120]
print(str(Knapsack(n,W,Weight,Value)))


