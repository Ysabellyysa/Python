lockdown = True 
grana = 30

status = 'Em casa' if lockdown or grana <=100 else 'Uhuuuuu'
print(f'O status é: {status}')