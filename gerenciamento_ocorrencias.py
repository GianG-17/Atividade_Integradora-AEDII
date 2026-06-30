from datetime import datetime

ocorrencias = []
historico = []
fila_atendimento = []
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

    fila_atendimento.append(nova_ocorrencia)

    inserir_hash_nome(nova_ocorrencia)

    inserir_hash_tipo(nova_ocorrencia)


    historico.append(
        "Cadastro da Ocorrência: " +
        id_ocorrencia +
        " às " +
        hora_atual
    )


    print("\nOcorrência cadastrada!")

    print("ID:", id_ocorrencia)



def listar_ocorrencias():

    print("\nLISTAR OCORRÊNCIAS")

    if len(ocorrencias) == 0:

        print("Nenhuma ocorrência cadastrada.")

    else:

        for ocorrencia in ocorrencias:

            print(ocorrencia)



def buscar_ocorrencia():

    print("\nBUSCAR POR ID")

    id_busca = input("Digite o ID para buscar: ")

    encontrou = False


    for ocorrencia in ocorrencias:

        if ocorrencia["id"] == id_busca:

            print("\nOcorrência encontrada:")

            print(ocorrencia)

            encontrou = True


    if encontrou == False:

        print("Nenhuma ocorrência encontrada.")



def buscar_por_nome():

    print("\nBUSCAR POR NOME")

    nome_busca = input("Digite o nome: ").lower()


    if nome_busca in hash_nome:

        for ocorrencia in hash_nome[nome_busca]:

            print(ocorrencia)

    else:

        print("Nenhuma ocorrência encontrada.")



def buscar_por_tipo():

    print("\nBUSCAR POR TIPO")

    tipo_busca = input("Digite o tipo: ").lower()


    if tipo_busca in hash_tipo:

        for ocorrencia in hash_tipo[tipo_busca]:

            print(ocorrencia)

    else:

        print("Nenhuma ocorrência encontrada.")



def ver_historico():

    print("\nHISTÓRICO")

    if len(historico) == 0:

        print("Nenhuma ação registrada.")

    else:

        for item in historico:

            print(item)



def salvar_historico():

    arquivo = open("historico.txt", "w")


    for item in historico:

        arquivo.write(item + "\n")


    arquivo.close()

    print("Histórico salvo.")



def carregar_historico():

    arquivo = open("historico.txt", "r")


    for linha in arquivo:

        historico.append(linha.strip())


    arquivo.close()

    print("Histórico carregado.")



def desfazer_acao():

    if len(historico) == 0:

        print("Nenhuma ação para desfazer.")

    else:

        acao = historico.pop()

        print("Ação desfeita:", acao)



def mostrar_fila():

    print("\nFILA DE ATENDIMENTO")


    if len(fila_atendimento) == 0:

        print("Fila vazia.")

    else:

        for posicao, ocorrencia in enumerate(fila_atendimento):

            print(
                posicao + 1,
                "-",
                ocorrencia["id"],
                "-",
                ocorrencia["nome"]
            )



def atender_ocorrencia():

    print("\nATENDER OCORRÊNCIA")


    if len(fila_atendimento) == 0:

        print("Não existem ocorrências na fila.")

    else:

        ocorrencia = fila_atendimento.pop(0)

        ocorrencia["status"] = "Atendido"


        hora_atual = datetime.now().strftime("%H:%M:%S")


        historico.append(
            "Ocorrência atendida: " +
            ocorrencia["id"] +
            " às " +
            hora_atual
        )


        print("Atendimento realizado:")

        print(ocorrencia)



def ordenar_por_prioridade():

    print("\nOCORRÊNCIAS ORDENADAS POR PRIORIDADE")


    lista_ordenada = ocorrencias.copy()

    tamanho = len(lista_ordenada)


    for i in range(tamanho):

        for j in range(0, tamanho - i - 1):

            if lista_ordenada[j]["prioridade"] < lista_ordenada[j + 1]["prioridade"]:

                auxiliar = lista_ordenada[j]

                lista_ordenada[j] = lista_ordenada[j + 1]

                lista_ordenada[j + 1] = auxiliar



    for ocorrencia in lista_ordenada:

        print(
            "ID:",
            ocorrencia["id"],
            "| Nome:",
            ocorrencia["nome"],
            "| Prioridade:",
            ocorrencia["prioridade"],
            "| Status:",
            ocorrencia["status"]
        )



while True:

    print("\n===== MENU =====")

    print("1 - Cadastrar ocorrência")

    print("2 - Listar ocorrências")

    print("3 - Buscar ocorrência por ID")

    print("4 - Buscar por nome")

    print("5 - Buscar por tipo")

    print("6 - Ver histórico")

    print("7 - Salvar/Carregar histórico")

    print("8 - Desfazer última ação")

    print("9 - Ver fila de atendimento")

    print("10 - Atender próxima ocorrência")

    print("11 - Ordenar ocorrências por prioridade")

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

        escolha = input("Salvar ou carregar? (S/C): ")


        if escolha.upper() == "S":

            salvar_historico()

        elif escolha.upper() == "C":

            carregar_historico()



    elif opcao == "8":

        desfazer_acao()


    elif opcao == "9":

        mostrar_fila()


    elif opcao == "10":

        atender_ocorrencia()


    elif opcao == "11":

        ordenar_por_prioridade()


    elif opcao == "0":

        print("Saindo...")

        break


    else:

        print("Opção inválida.")