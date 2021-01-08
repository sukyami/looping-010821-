#Prime numbers are numbers that have only 2 factors: 1 and themselves.
prime_num = [] #create list 
for prime in range(1,100): # prime start 1 end 99 
  for i in range(2, prime+1): # i start 2 end 100 (because the range is 2,101), prime+1 because make same number of index 
    if (i == prime): #prime divided with themselves
      prime_num.append(prime) #add prime in prime_num list
    elif (prime % i == 0): #If prime and i are not the same number, but divided, it is not prime
      break #stop for i loop and go back to first for prime loop 
    #If i is not same as prime and not divided, nothing happend just continue executing the for i loop. 
    #when i 
print(prime_num)
