n = int(input("Enter the numbers of Fibonacci terms to print: "))
n1, n2 = 0, 1
initial_no = 0
if n <= 0:
    print("Enter a positive integer")
elif n == 1:
    print("Fibonacci numbers upto ", n, "terms:")
    print(n1)
else:
    print("Fibonacci numbers upto ", n, " terms:")
    while initial_no < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        initial_no += 1
