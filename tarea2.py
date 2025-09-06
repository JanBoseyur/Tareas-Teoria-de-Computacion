
import re

# Definición de patrones de tokens
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

def analizar_expresion(expr):
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

def main():
    print("=== Analizador Léxico ===")
    print("Escriba 'salir' para terminar.")

    while True:
        expr = input("\nIngrese expresión: ")
        
        if expr.lower() == "salir":
            print("Saliendo del analizador...")
            break
        analizar_expresion(expr)

if __name__ == "__main__":
    main()

