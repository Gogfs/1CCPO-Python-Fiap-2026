endpoint = ["/login", "/produtos", "/pedidos"]

status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]

def calcular_porcentagem(endpoint, status):
    sucesso = 0
    for i in status:
        if i >= 200 and i <= 299:
            sucesso += 1

    porcentagem = (sucesso / len(status)) * 100
    return porcentagem

porcentagem_endpoints = []
for i in range(len(endpoint)):
    porcentagem_endpoints.append(calcular_porcentagem(endpoint[i], status[i]))

for i in range(len(porcentagem_endpoints)):
    print(f"Porcentagem de sucessos do endpoint {endpoint[i]}: {porcentagem_endpoints[i]}%\n")

print(f"Endpoint com mais erros: {endpoint[porcentagem_endpoints.index(min(porcentagem_endpoints))]}")
