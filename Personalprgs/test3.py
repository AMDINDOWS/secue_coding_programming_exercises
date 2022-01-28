#n = 20

#primes = [i for i in range(2, n + 1) if all(i%j != 0 for j in range(2, int(i ** 0.5) + 1))]

#print(primes)



matrix = [[j for j in range(5)] for i in range(5)]
  
print(matrix)
