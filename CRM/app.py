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
    print(leads)

def main():
    while True:
        print("\nMini CRM de leads")
        print("[1] Adicionar leads")
        print("[2] listar leads")
        print("[0] Sair do programa")

        opt = input("Escolha uma opção: ")
        if opt == "1":
            print("Lead adicionado")
            add_lead()

        elif opt == "2":
            list_leads()

        elif opt == "0":
            print("Até mais...")
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()