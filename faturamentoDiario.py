#3) Cálculo de Faturamento Diário

import json

# Exemplo de faturamento diário em JSON
faturamento_diario = {
    "01": 22174.1664, "02": 24537.6698, "03": 26139.6134, "04": 0.0,
    "05": 0.0, "06": 26742.6612, "07": 0.0, "08": 42889.2258,
    "09": 46251.174, "10": 11191.4722, "11": 0.0, "12": 0.0,
    "13": 3847.4823, "14": 373.7838, "15": 2659.7563, "16": 48924.2448,
    "17": 18419.2614, "18": 0.0, "19": 0.0, "20": 35240.1826,
    "21": 43829.1667, "22": 18235.6852, "23": 4355.0662, "24": 13327.1025,
    "25": 0.0, "26": 0.0, "27": 25681.8318, "28": 1718.1221,
    "29": 13220.495, "30": 8414.61, "31": 0.0
}

# Remove dias sem faturamento
valores = [v for v in faturamento_diario.values() if v != 0]

menor_faturamento = min(valores)
maior_faturamento = max(valores)
media_mensal = sum(valores) / len(valores)
dias_acima_da_media = len([v for v in valores if v > media_mensal])

print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias acima da média: {dias_acima_da_media}")
