def es_divisible(n,d):
  if n % d == 0:
    return True
  else:
    return False

def es_primo(n):
  comp = 0
  for i in range(2,n+1):
    if es_divisible(n,i):
      comp=0
    else:
      comp = 1
    if comp == 1:
      return True
    else:
      return False
