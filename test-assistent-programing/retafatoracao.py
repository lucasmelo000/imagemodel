def calculate_list_statistics(numbers: list) -> tuple:
    """
    Calcula estatísticas de uma lista de números.
    
    Args:
        numbers: Lista de números para análise
        
    Returns:
        Tupla contendo (total, média, máximo, mínimo)
    """
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    return total, average, maximum, minimum


# Lista de números para análise
data = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]

# Desempacotar resultados das estatísticas
total, average, maximum, minimum = calculate_list_statistics(data)

# Exibir resultados
print("Total:", total)
print("Média:", average)
print("Maior:", maximum)
print("Menor:", minimum)