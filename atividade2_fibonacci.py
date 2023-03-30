def fibonacci(nº):
    """
    Recebe um número inteiro 'nº' e retorna uma lista com os
    primeiros números da sequência fibonacci 
    """
    if nº <= 0:
        return []
    elif nº == 1:
        return [0]
    elif nº == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, nº):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib 

def pertence_fibonacci(nº):
    """
    recebe um número inteiro e verifica se ele pertence ou não a sequencia
    gerada da lista fib da função fibonacci.
    """
    fib = fibonacci(nº)
    if nº in fib:
        return f"O nº: {nº}, pertence a sequência de Fibonacci!"
    else:
        return f"O nº: {nº} , não pertence a sequência de Fibonacci!"


num = int(input('insira um numero: '))

print(f"{pertence_fibonacci(num)}")
