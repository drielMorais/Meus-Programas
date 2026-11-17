#---------FUNÇÃO cadastrar funcionários + parâmetro------------
def cadastrar_funcionario(id):
    while True:
#---------ARMAZENAMENTO DO NOME, SETOR, SALÁRIO E ID-----------
        armazenamento["Id"] = (id)
        armazenamento["Funcionario"] = input("DIGITE O NOME DO FUNCIONÁRIO: ")
        armazenamento["Setor"] = input("DIGITE O SETOR DO FUNCIONÁRIO:")
        armazenamento["Salario"] = int(input("DIGITE O SALÁRIO DO FUNCIONÁRIO:"))
#---------TRANSFERÊNCIA DOS ÍTENS DO DICIONÁRIO PARA A LISTA----------
        lista_funcionarios.append(armazenamento.copy())
#---------LIMPANDO O DICIONÁRIO APÓS A TRANSFERÊNCIA PARA ADICIONAR OUTROS---------
        armazenamento.clear()
        return cadastrar_funcionario

#----------FUNÇÃO CONSULTAR FUNCIONÁRIO--------------
def consultar_funcionarios():
#----------MENU DE ESCOLHA DE OPÇÕES------------
    print("ESCOLHA UMA OPÇÃO DO MENU:")
    print("1 - CONSULTAR TODOS OS FUNCIONÁRIOS")
    print("2 - CONSULTAR FUNCIONÁRIO POR ID")
    print("3 - CONSULTAR FUNCIONÁRIO POR SETOR")
    print("4 - RETORNAR AO MENU")
    opConsulta = int(input(">>>"))

#----------ESCOLHA DE LISTAR TODOS OS FUNCIONÁRIOS-----------
    if (opConsulta == 1):
        for list_todos in lista_funcionarios:
            for chaves, valor in list_todos.items():
                print(f"{chaves} = {valor}")
            print("-" * 40)
#----------ESCOLHA DE CONSULTAR ID + PRINT INFs DO FUNCIONARIO----------
    elif(opConsulta == 2):
        opConsultaId = int(input("DIGITE O ID DO FUNCIONÁRIO: "))
#-----------CRIAÇÃO DE UMA VARIÁVEL BOOLEANA INICIANDO COM FALSE------------
        idEncontrado = False
# ----------A VARIÁVEL idFuncionários ESTÁ RECEBENDO ALGO A CADA ITERAÇÃO COM A LISTA lista_funcionarios
        for idFuncionarios in lista_funcionarios:
            if (idFuncionarios["Id"] == opConsultaId):
                print("-" * 40)
                for chave, valor in idFuncionarios.items():
                    print(f"{chave} = {valor}")
                    idEncontrado = True
                print("-" * 40)
#-----------NEGAÇÃO DA VARIÁVEL BOOLEANA FALSE ---> TRUE ----------
        if not idEncontrado:
#----------AVISO CASO O ID NÃO SEJA ENCONTRADO-----------------
            print("NÃO FOI ENCONTRADO UM FUNCIONÁRIO COM ESSE ID. TENTE NOVAMENTE")
            return consultar_funcionarios()

#-------------ESCOLHA PELO SETOR DO FUNCIONÁRIO---------------
    elif(opConsulta == 3):
        opConsultaSetor = input("DIGITE O SETOR DO FUNCIONÁRIO: ")
#-------------CRIAÇÃO DE UMA VARIÁVEL BOOLEANA COM FALSE PARA INDICAR QUE INICIA NÃO TENDO ENCONTRADO NADA--------
        setorEncontrado = False
        for setorFuncionarios in lista_funcionarios:
            if(setorFuncionarios["Setor"] == opConsultaSetor):
                print("-" * 40)
                for chaves, valor in setorFuncionarios.items():
                    print(f"{chaves} = {valor}")
#-------------CASO SEJA ACHADO O SETOR, A VARIÁVEL VIRA TRUE-------------
                    setorEncontrado = True
                print("-" * 40)
#------------IF NEGANDO A VARIÁVEL BOLEANA PARA CASO NÃO ENCONTRE NENHUM SETOR COM O NOME DADO AO INPUT
#------------EVITANDO QUE O PRINT SEJA EXECUTADO EM TODAS AS SITUAÇÕES, MESMO QUANDO HOUVER
        if (setorEncontrado == False):
            print("NÃO FOI ENCONTRADO NENHUM SETOR COM ESTE NOME.")
            return consultar_funcionarios()
    elif(opConsulta == 4):
        return
    elif(opConsulta != 1 and opConsulta != 2 and opConsulta != 3 and opConsulta != 4):
        print("OPÇÃO INVÁLIDA")
        return consultar_funcionarios()
#-------------FUNÇÃO REMOVER FUNCIONÁRIOS---------------
def remover_funcionario():
#---------PREENCHIMENTO DO ID DO FUNCIONÁRIO-----------
    remove = int(input("DIGITE O ID DO FUNCIONÁRIO PARA REMOÇÃO: "))
    for listaRemove in lista_funcionarios:
        if listaRemove["Id"] == remove:
#---------REMOÇÃO DO FUNCIONÁRIO DA LISTA----------
            lista_funcionarios.remove(listaRemove)
            print("FUNCIONÁRIO REMOVIDO COM SUCESSO!")
#---------ESSE return SOZINHO FAZ O PROGRAMA RETORNAR PARA O MENU QUE ESTÁ FORA DAS FUNÇÕES
            return

    print("OPS...O ID DIGITADO NÃO FOI ENCONTRADO! TENTE NOVAMENTE")
    return remover_funcionario()


#------------LISTA E VARIÁVEL COM RU------------
lista_funcionarios = []
armazenamento = {}
id_global = 5455502

#--------------------MENU PRINCIPAL--------------------
print("SEJA BEM-VINDO(A) A EMPRESA DO ADRIEL MORAIS")
while True:
        print("|" + "-" * 40 + "|")
        print("|" + "              MENU PRINCIPAL" + "            |")
        print("|" + "-" * 40 + "|")
        print("|" + ("-" * 7) + "Escolha a Opção desejada:" + ("-" * 8) + "|")
        print("|" + "-" * 40 + "|")
        print("1 - CADASTRAR FUNCIONÁRIO(A)")
        print("2 - CONSULTAR FUNCIONÁRIO(A)")
        print("3 - REMOVER FUNCIONÁRIO(A)")
        print("4 - ENCERRAR PROGRAMA")
#-----------------CASO O USUÁRIO DIGITE LETRAS/CARACTERES, O TRY IMPEDE QUE O PROGRAMA DÊ ERRO---------------
        try:
            opEscolha = int(input(">>>"))
            if(opEscolha == 1):
                cadastrar_funcionario(id_global)
                id_global += 1
            elif(opEscolha == 2):
                consultar_funcionarios()
            elif(opEscolha == 3):
                remover_funcionario()
            elif(opEscolha == 4):
                break
            elif(opEscolha != 1 and opEscolha != 2 and opEscolha != 3 and opEscolha != 4):
                print("OPÇÃO INVÁLIDA...TENTE NOVAMENTE")
        except ValueError:
            print("OPS...NÃO USE LETRAS, NÚMEROS DECIMAIS OU CARACTERES\n")

