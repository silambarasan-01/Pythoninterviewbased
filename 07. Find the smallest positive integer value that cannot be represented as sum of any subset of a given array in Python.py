def get_smallest_element(A):
   n = len(A)
   answer = 1
   for i in range (0, n):
      if A[i] <= answer:
         answer = answer + A[i]
      else:
         break
   return answer
A = [1, 2, 6, 5]
print(get_smallest_element(A))