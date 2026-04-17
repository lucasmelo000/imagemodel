def is_prime(n):
    """
    Verifica se um número inteiro é primo.

    Um número primo é maior que 1 e divisível apenas por 1 e por si mesmo.

    Args:
        n (int): O número a ser verificado.

    Returns:
        bool: True se n for primo, False caso contrário.

    Raises:
        TypeError: Se n não for um inteiro.
    """
    if not isinstance(n, int):
        raise TypeError("O argumento deve ser um inteiro.")
    
    if n <= 1:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    limite = int(n**0.5) + 1
    for i in range(3, limite, 2):
        if n % i == 0:
            return False
    
    return True

# Testes
print(is_prime(2))  # True
print(is_prime(3))  # True
print(is_prime(4))  # False
print(is_prime(17)) # True
print(is_prime(18)) # False