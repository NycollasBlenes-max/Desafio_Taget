string = input("Digite a string para inverter: ")

string_invertida = ""
for caractere in string:
    string_invertida = caractere + string_invertida

print(f"String invertida: {string_invertida}")