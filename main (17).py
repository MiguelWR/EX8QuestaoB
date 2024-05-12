#Exercício 8

#b)

def Sb(n):
  if n < 1:
    return 2
  else:
    return Sb(n - 1) * (1 / 2)


print(Sb(5))