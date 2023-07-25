def fibonacci_sequence(n):
   if(n==1):
       return [0]
   if(n<=0):
       return []
   sequence=[0,1]
   for i in range(2,n):
       sequence.append(sequence[i-1]+sequence[i-2])

   return sequence



