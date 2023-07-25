def fibonacci_sequence(n):
   if(n==1):
       return [1]
   elif(n==0):
       return []
   sequence=[0,1]
   for i in range(2,n):
       sequence.append(sequence[i-1]+sequence[i-2])

   return sequence

print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))

