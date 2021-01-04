# Existen múltiples formas de calcular el máximo común divisor de un conjunto de números, escriba una función de nombre mcd que reciba dos números n1 y n2 como argumentos,
# y retorne el máximo común divisor. Por ejemplo para los argumentos 10 y 15 debe retornar 5.

def mcd(n1, n2):
    k = min(n1, n2);
    while k > 1:
        if n1 % k == 0 and n2 % k == 0:
            break;
        k -= 1;
    return k


def exponente(n):
    i = 1;
    while 2 ** i <= n:
        i = i + 1
    return i - 1


def panprimo(n):
    def isprime(n):
        for x in range(2, n):
            if n % x == 0:
                return False;
        return True;

    r = str(n);
    return '0' in r and '1' in r and '2' in r and '3' in r and '4' in r and '5' in r and '6' in r and '7' in r and '8' in r and '9' and isprime(
        n % 1000)


print(mcd(10, 15))
print(exponente(65))
print(panprimo(2424643))
print(panprimo(1234567890))
print(panprimo(10123485769))










