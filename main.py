def q1():
        
        """ Dado um número inteiro x, retorne verdadeiro se x for um palíndromo, e falso caso contrário."""

        numero = input().strip()
        if numero == numero[::-1] and not numero.startswith('-'):
            print("True")
        else:
            print("False")



def q2():

    """Dado um numeral romano, converta-o para um número inteiro."""

    romanoInteiro = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    n = input().strip()
    total = 0
    previstoValor = 0

    for char in reversed(n):
        valor = romanoInteiro[char]
        if valor < previstoValor:
            total -= valor
        else:
            total += valor
        previstoValor = valor

    print(total)