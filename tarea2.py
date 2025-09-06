
import re

# Definiciones de patrones
patrones = {
    "Palabra Clave": r"^(if|else|for|while|return|int|float|bool)$",
    "Identificador": r"^[a-zA-Z_][a-zA-Z0-9_]*$",
    "Numero Entero": r"^[0-9]+$",
    "Numero Decimal": r"^[0-9]+\.[0-9]+$",
    "Operador Aritmetico": r"^[\+\-\*/%]$",
    "Operador Asignacion": r"^(=|\+=|-=|\*=|/=|%=)$",
    "Operador Incremento/Decremento": r"^(--|\+\+)$",
    "Operador Relacional": r"^(==|!=|<=|>=|<|>)$",
    "Operador Logico": r"^(&&|\|\||!)$",
    "Operador Condicional/Ternario": r"^[\?:]$",
    "Signos de Puntuacion": r"^[\(\)\{\}\[\],;.]$",
}


# Lista de cadenas de prueba
expresiones = [
    "x + 2"
]

for expr in expresiones:

    tokens = expr.split()
    
    for t in tokens:
        reconocido = False
        
        for tipo, patron in patrones.items():
            
            if re.match(patron, t):
                print(f"{t} → {tipo}")
                reconocido = True
                break

        if not reconocido:
            print(f"{t} → Token inválido")
