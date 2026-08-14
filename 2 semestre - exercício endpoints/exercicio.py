endpoint = ["/login", "/produtos", "/pedidos"]

status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]


def calcular_porcentagem(status):
    sucesso = 0

    for codigo in status:
        if 200 <= codigo <= 299:
            sucesso += 1

    porcentagem = (sucesso / len(status)) * 100
    return porcentagem


def verificar_criticidade(status):
    for i in range(len(status) - 1):
        if not (200 <= status[i] <= 299) and not (200 <= status[i + 1] <= 299):
            return True

    return False


def classificar_endpoint(status, porcentagem):
    if porcentagem >= 80:
        return "ESTÁVEL"

    elif porcentagem >= 60:
        return "INSTÁVEL"

    else:
        if verificar_criticidade(status):
            return "CRÍTICO"
        else:
            return "INSTÁVEL"


porcentagem_endpoints = []
classificacao_endpoints = []

for i in range(len(endpoint)):
    porcentagem = calcular_porcentagem(status[i])

    porcentagem_endpoints.append(porcentagem)

    classificacao = classificar_endpoint(status[i], porcentagem)
    classificacao_endpoints.append(classificacao)


for i in range(len(porcentagem_endpoints)):
    print(
        f"Porcentagem de sucessos do endpoint {endpoint[i]}: "
        f"{porcentagem_endpoints[i]}% | {classificacao_endpoints[i]}\n"
    )


print(
    f"Endpoint com mais erros: "
    f"{endpoint[porcentagem_endpoints.index(min(porcentagem_endpoints))]}"
)