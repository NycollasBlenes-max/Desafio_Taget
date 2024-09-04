import json

faturamento = json.loads(open('dados.json').read())

valores_faturamento = []
for dia in faturamento:
    if dia["valor"] > 0:
        valores_faturamento.append(dia["valor"])

menor_valor = min(valores_faturamento)
maior_valor = max(valores_faturamento)
media_mensal = sum(valores_faturamento) / len(valores_faturamento)

dias_acima_da_media = 0
for valor in valores_faturamento:
    if valor > media_mensal:
        dias_acima_da_media += 1

print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")