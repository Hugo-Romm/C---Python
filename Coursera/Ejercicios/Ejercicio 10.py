# Para muchas aplicaciones matemáticas, conocer la potencia de 2 más grande que es menor o igual a cierto número, es muy útil. Escribe una función exponente, que dado un número n,
# retorne el exponente de dicha potencia de 2 más grande. Por ejemplo, si el número es 65, tu programa debe retornar 6, ya que 2⁶ = 64.

def exponente (n):
   for i in range (1,n):
       if  2**(i)==n:
           print (i)
           break
       if 2**(i)>n:
           print (i-1)
           break











