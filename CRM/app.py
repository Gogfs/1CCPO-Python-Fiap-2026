from CRM.model import model_lead
import control


def add_lead():
    name = input("Nome: ")
    email = input("E-mail: ")
    company = input("Empresa: ")
    stage = input("Etapa de vendas: ")

    # Verificar a validade dos campos

    control.create_lead(model_lead(name, email, company, stage))
    
def list_leads():
    leads = control.read_leads()

    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]:<10} | {lead["email"]:<20} | {lead["company"]:<10} | {lead["stage"]:<10}")

def search_leads():
    query = input("Buscar por: ").strip().lower()
    if not query:
        print("Consulta vazia")
        return

    # vou agora enviar a busca do usuário (query) para o control
    # o control vai comparar a busca com a base de dados
    # e vai retornar uma lista com o resultado

    leads_finded = control.read_search_leads(query)
    for i, lead in leads_finded:
        print(f"{i:02d} | {lead["name"]:<10} | {lead["email"]:<20} | {lead["company"]:<10} | {lead["stage"]:<10}")


def export_leads():
    path_csv = control.export_csv()

    if path_csv is None:
        print("Não foi possivel exportar os leads")
    else:
        print(f"Exportado para {path_csv}")

def main():
    while True:
        print("\nMini CRM de leads")
        print("[1] Adicionar leads")
        print("[2] Listar leads")
        print("[3] Buscar (nome/email/empresa)")
        print("[4] Exportar CSV")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ")
        if opt == "1":
            print("Lead adicionado")
            add_lead()

        elif opt == "2":
            list_leads()

        elif opt == "3":
            search_leads()

        elif opt == "4":
            export_leads()

        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()