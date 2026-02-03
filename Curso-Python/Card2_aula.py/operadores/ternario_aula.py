# Operador Ternário expande uma condição if/else em uma única linha

lockdown = True
grana = 30

# Se lockdown é True OU grana <= 100, status = Em casa senão 'Uhuuuuu'
status = 'Em casa' if (lockdown or grana <= 100) else 'Uhuuuuu'
print(f'O status é: {status}')  # Imprime: O status é: Em casa
