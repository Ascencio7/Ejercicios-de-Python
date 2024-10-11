import re
from collections import defaultdict
from fractions import Fraction

def parse_terms(expression):
    # Expresión regular para capturar correctamente coeficientes, variables y exponentes
    term_pattern = r'([+-]?\d*\/?\d*)?([a-zA-Z][a-zA-Z0-9\^]*)'
    terms = re.findall(term_pattern, expression)
    
    parsed_terms = []
    for coeff, var in terms:
        if coeff == '' or coeff == '+':
            coeff = '1'
        elif coeff == '-':
            coeff = '-1'
        parsed_terms.append((Fraction(coeff), var))
    return parsed_terms

def reduce_terms(terms):
    # Diccionario para almacenar la suma de los coeficientes de los términos semejantes
    term_dict = defaultdict(Fraction)
    
    for coeff, var in terms:
        term_dict[var] += coeff
    
    # Reconstruir la expresión reducida
    reduced_expression = ''
    for var, coeff in term_dict.items():
        if coeff == 0:
            continue
        sign = '+' if coeff > 0 else ''
        reduced_expression += f'{sign}{coeff}{var}'
    
    # Quitar el signo + inicial si existe
    if reduced_expression.startswith('+'):
        reduced_expression = reduced_expression[1:]
    
    return reduced_expression

def simplify_expression(expression):
    terms = parse_terms(expression)
    reduced_expression = reduce_terms(terms)
    return reduced_expression

# Ejemplo de uso
#expresion = "-2/5bx^2 + 1/5bx^2 + 3/4bx^2 + -4bx^2 + bx^2"
expresion = "5a - 8a + a - 6a + 21a"
resultado = simplify_expression(expresion)
print("\nExpresión reducida: ", resultado)