def solution(n):
  count =0
  for c in range(3,n+1):
    for a in range(1,c):
      for b in range(a,c):
         if a**2 + b**2 == c**2:
          count+=1
  return count        

sol = solution(5)
print(sol)