# Explicação Técnica do Código: Verificação de Número Primo

Este documento explica tecnicamente o código em `num_primo.py`, que implementa uma função otimizada para verificar se um número inteiro é primo, aplicando princípios de clean code.

## Visão Geral
A função `is_prime(n)` determina se `n` é um número primo (maior que 1 e divisível apenas por 1 e por si mesmo). O algoritmo é baseado na verificação de divisibilidade por fatores potenciais, com otimizações para eficiência.

## Estrutura do Código

### 1. Definição da Função e Docstring
```python
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
```
- **Docstring**: Segue o padrão PEP 257, documentando propósito, argumentos, retorno e exceções. Promove legibilidade e manutenção.
- **Princípio Clean Code**: Código autodocumentado; evita comentários desnecessários.

### 2. Validação de Entrada
```python
if not isinstance(n, int):
    raise TypeError("O argumento deve ser um inteiro.")
```
- **Técnico**: Usa `isinstance()` para verificar tipo, lançando `TypeError` se `n` não for `int`. Previne erros em tempo de execução.
- **Clean Code**: Validação defensiva; torna a função robusta contra entradas inválidas.

### 3. Casos Base
```python
if n <= 1:
    return False

if n == 2:
    return True

if n % 2 == 0:
    return False
```
- **Técnico**: Trata casos especiais rapidamente. 2 é o único primo par; números pares >2 não são primos.
- **Clean Code**: Early returns evitam aninhamento desnecessário; lógica clara e direta.

### 4. Loop de Verificação Otimizado
```python
limite = int(n**0.5) + 1
for i in range(3, limite, 2):
    if n % i == 0:
        return False
```
- **Técnico**: Calcula limite como raiz quadrada de `n` (arredondada para cima). Loop começa em 3 com passo 2, testando apenas ímpares (já excluiu pares).
- **Eficiência**: Reduz iterações pela metade comparado ao loop original; complexidade O(√n).
- **Clean Code**: Variável `limite` nomeada evita "número mágico"; loop focado em lógica essencial.

### 5. Retorno Final
```python
return True
```
- **Técnico**: Se nenhum divisor for encontrado, `n` é primo.
- **Clean Code**: Simples e direto; função retorna booleano consistente.

## Testes
```python
print(is_prime(2))  # True
print(is_prime(3))  # True
print(is_prime(4))  # False
print(is_prime(17)) # True
print(is_prime(18)) # False
```
- **Técnico**: Exemplos manuais para validar casos: primo par (2), ímpar (3,17), compostos (4,18).
- **Clean Code**: Testes simples e legíveis; em produção, use frameworks como `unittest` para cobertura maior.

## Otimizações Aplicadas
- **Eliminação de pares**: Pula números pares após 2, reduzindo verificações.
- **Limite calculado uma vez**: Evita recálculo em cada iteração.
- **Validação de tipo**: Previne bugs por entradas não-inteiras.
- **Docstring completa**: Facilita uso e manutenção.

## Complexidade e Limitações
- **Tempo**: O(√n) – eficiente para n até ~10^12; para maiores, considere algoritmos probabilísticos.
- **Espaço**: O(1) – usa constantes variáveis.
- **Limitações**: Não trata números negativos (retorna False); assume entrada razoável.

Este código segue clean code: legível, modular, testável e eficiente.