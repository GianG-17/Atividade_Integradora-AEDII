from datetime import datetime

ocorrencias = []
historico = []
hash_nome = {}
hash_tipo = {}

def gerar_id(nome):
    soma = 0
    for letra in nome:
        soma = soma + ord(letra)
    codigo = soma % 10000
    prefixo = nome[:3].upper()
    return prefixo + "-" + str(codigo)


def inserir_hash_nome(ocorrencia):
    chave = ocorrencia["nome"].lower()
    if chave not in hash_nome:
        hash_nome[chave] = []
    hash_nome[chave].append(ocorrencia)


def inserir_hash_tipo(ocorrencia):
    chave = ocorrencia["tipo"].lower()
    if chave not in hash_tipo:
        hash_tipo[chave] = []
    hash_tipo[chave].append(ocorrencia)


def cadastrar_ocorrencia():
    print("\nCADASTRAR OCORRÊNCIA")
    nome = input("Nome do requisitante: ")
    id_ocorrencia = gerar_id(nome)
    tipo = input("Tipo da ocorrência: ")
    descricao = input("Descrição: ")
    hora_atual = datetime.now().strftime("%H:%M:%S")

    while True:
        prioridade_texto = input("Prioridade de 1 a 5: ")
        if prioridade_texto.isdigit() and 1 <= int(prioridade_texto) <= 5:
            prioridade = int(prioridade_texto)
            break
        print("Digite um número inteiro entre 1 e 5.")

    nova_ocorrencia = {
        "id": id_ocorrencia,
        "nome": nome,
        "tipo": tipo,
        "descricao": descricao,
        "prioridade": prioridade,
        "status": "Aberto"
    }

    ocorrencias.append(nova_ocorrencia)

    inserir_hash_nome(nova_ocorrencia)
    inserir_hash_tipo(nova_ocorrencia)

    historico.append("Cadastro da Ocorrência: " + id_ocorrencia + " às " + hora_atual)

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

def buscar_por_nome():
    print("\nBUSCAR POR NOME")
    nome_busca = input("Digite o nome do solicitante: ").lower()
    if nome_busca in hash_nome:
        print("\nOcorrências encontradas:")
        for ocorrencia in hash_nome[nome_busca]:
            print(ocorrencia)
    else:
        print("Nenhuma ocorrência encontrada para esse nome.")

def buscar_por_tipo():
    print("\nBUSCAR POR TIPO")
    tipo_busca = input("Digite o tipo da ocorrência: ").lower()
    if tipo_busca in hash_tipo:
        print("\nOcorrências encontradas:")
        for ocorrencia in hash_tipo[tipo_busca]:
            print(ocorrencia)
    else:
        print("Nenhuma ocorrência encontrada para esse tipo.")

def ver_historico():
    print("\nHISTÓRICO DE AÇÕES")
    if len(historico) == 0:
        print("Nenhuma ação registrada.")
    else:
        for acao in historico:
            print(acao)

def salvar_historico():
    arquivo = open("historico.txt", "w")
    for acao in historico:
        arquivo.write(acao + "\n")
    arquivo.close()
    print("\nHistórico salvo no historico.txt")

def carregar_historico():
    arquivo = open("historico.txt", "r")
    for linha in arquivo:
        historico.append(linha)
    arquivo.close()
    print("\nHistórico carregado de historico.txt")

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
    print("3 - Buscar ocorrência por ID")
    print("4 - Buscar ocorrência por nome")
    print("5 - Buscar ocorrência por tipo")
    print("6 - Ver histórico de ações")
    print("7 - Salvar/Carregar histórico")
    print("8 - Desfazer última ação")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_ocorrencia()
    elif opcao == "2":
        listar_ocorrencias()
    elif opcao == "3":
        buscar_ocorrencia()
    elif opcao == "4":
        buscar_por_nome()
    elif opcao == "5":
        buscar_por_tipo()
    elif opcao == "6":
        ver_historico()
    elif opcao == "7":
        opcao_historico = input("Deseja Salvar ou Carregar histórico?(S/C): ")
        if opcao_historico.upper() == "S":
            salvar_historico()
        elif opcao_historico.upper() == "C":
            carregar_historico()
        else:
            print("Opção inválida.")
    elif opcao == "8":
        desfazer_acao()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")