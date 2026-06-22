ocorrencias = []
historico = []

def gerar_id(nome):
    soma = 0

    for letra in nome:
        soma = soma + ord(letra)

    codigo = soma % 10000
    prefixo = nome[:3].upper()

    return prefixo + "-" + str(codigo)


def cadastrar_ocorrencia():
    print("\nCADASTRAR OCORRÊNCIA")

    nome = input("Nome do requisitante: ")
    id_ocorrencia = gerar_id(nome)

    tipo = input("Tipo da ocorrência: ")
    descricao = input("Descrição: ")
    prioridade = input("Prioridade de 1 a 5: ")

    novas_ocorrencias = {
        "id": id_ocorrencia,
        "nome": nome,
        "tipo": tipo,
        "descricao": descricao,
        "prioridade": prioridade,
        "status": "Aberto"
    }

    ocorrencias.append(novas_ocorrencias)
    historico.append("Cadastro da Ocorrência " + id_ocorrencia)

    print("\nOcorrência cadastrada!")
    print("ID:", id_ocorrencia)
    print("Nome:", nome)
    print("Tipo:", tipo)
    print("Descrição:", descricao)
    print("Prioridade:", prioridade)


def listar_ocorrencias():
    print("\nLISTAR OCORRÊNCIAS")
    if len(ocorrencias) == 0:
        print("Nenhuma ocorrência cadastrada.")
    else:
        for ocorrencia in ocorrencias:
            print(ocorrencia)


def buscar_ocorrencia():
    print("\nBUSCAR OCORRÊNCIA")
    id_busca = input("Digite o ID para buscar: ")
    print("Buscando ocorrência com ID:", id_busca)

def ver_historico():
    print("\nHISTÓRICO DE AÇÕES")
    if len(historico) == 0:
        print("Nenhuma ação registrada.")
    else:
        for acao in historico:
            print(acao)

def desfazer_acao():
    print("\nDESFAZER ÚLTIMA AÇÃO")
    if len(historico) == 0:
        print("Nenhuma ação para desfazer.")
    else:
        ultima_acao = historico.pop()
        print("Ação desfeita:", ultima_acao)

while True:
    print("\n===== MENU =====")
    print("1 - Cadastrar ocorrência")
    print("2 - Listar ocorrências")
    print("3 - Buscar ocorrência")
    print("4 - Ver histórico de ações")
    print("5 - Desfazer última ação")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_ocorrencia()
    elif opcao == "2":
        listar_ocorrencias()
    elif opcao == "3":
        buscar_ocorrencia()
    elif opcao == "4":
        ver_historico()
    elif opcao == "5":
        desfazer_acao()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")