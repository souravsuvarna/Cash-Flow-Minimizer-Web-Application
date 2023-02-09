import sys

# Access passed variables
var1 = int(sys.argv[1])
var2 = int(sys.argv[2])
var3 = int(sys.argv[3])
var4 = int(sys.argv[4])
var5 = int(sys.argv[5])
var6 = int(sys.argv[6])
var7 = int(sys.argv[7])
var8 = int(sys.argv[8])
var9 = int(sys.argv[9])

n1 = str(sys.argv[10])
n2 = str(sys.argv[11])
n3 = str(sys.argv[12])
#Test pass

graph=[[var1,var2,var3],[var4,var5,var6],[var7,var8,var9]]



## Test pass

N = 3


def getMin(arr):
	
	minInd = 0
	for i in range(1, N):
		if (arr[i] < arr[minInd]):
			minInd = i
	return minInd


def getMax(arr):

	maxInd = 0
	for i in range(1, N):
		if (arr[i] > arr[maxInd]):
			maxInd = i
	return maxInd


def minOf2(x, y):

	return x if x < y else y

def minCashFlowRec(amount):

	mxCredit = getMax(amount)
	mxDebit = getMin(amount)
 
  
	
	
	if (amount[mxCredit] == 0 and amount[mxDebit] == 0):
		return 0

   
	   
	# Find the minimum of two amounts
	min = minOf2(-amount[mxDebit], amount[mxCredit])
	amount[mxCredit] -=min
	amount[mxDebit] += min

   
		
	#Test Begins
	if mxDebit==0:
		p1=n1
	elif mxDebit==1:
		p1=n2
	elif mxDebit==2:
		p1=n3
     
	if mxCredit==0:
		p2=n1
	elif mxCredit==1:
		p2=n2
	elif mxCredit==2:
		p2=n3

	# If minimum is the maximum amount to be
	print(p1+" pays Rs." , min
		, " to " +p2+". ")

	#Test ends	
	minCashFlowRec(amount)


def minCashFlow(graph):

	
	amount = [0 for i in range(N)]

	for p in range(N):
		for i in range(N):
			amount[p] += (graph[i][p] - graph[p][i])

	minCashFlowRec(amount)
	



minCashFlow(graph)


