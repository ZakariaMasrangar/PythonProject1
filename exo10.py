[N = int(input("Number of elements in Fibonacci Series, N, (N>=10) : ")) #initialize the list with starting elements: 0, 1 #

fibonacciSeries = [0,1,1,2,3,5,8,13,21,34]
if N>=10:
	for i in range(10, N):  #next elment in series = sum of its previous two numbers
		nextElement = fibonacciSeries[i-1] + fibonacciSeries[i-2] #append the element to the series fibonacciSeries.append(nextElement)
        print(fibonacciSeries)