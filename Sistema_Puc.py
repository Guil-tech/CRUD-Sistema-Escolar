# Nome: Guilherme Moreira Pinto
# Curso: ADS(Análise e Desenvolvimento de Sistemas)
import json


def salvar_json(data, file_name, tipo="w"):
    '''
    Salva dados em um arquivo json

    :param data: Dados que queira que sejam alocados em um arquivo json
    :param file_name: Nome do arquivo para acessar, ou criar.
    :param tipo: Tipo de ação que queira realizar ao salvar, adicionando ou zerar e criar outra
    '''
    with open(file_name + ".json", tipo, encoding="utf-8") as arquivo:
        json.dump(data, arquivo, ensure_ascii=False)
        arquivo.close()
    return None


def ler_json(file_name):
    '''
    Acessa um arquivo do tipo .json e retorna seus dados

    :param file_name: Nome do arquivo que deseja acessar
    :return: retorna um array com os dados do arquivo
    '''

    try:
        with open(file_name + ".json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            arquivo.close()
    except FileNotFoundError:
        dados = []
        return dados
    return dados


def menu_home():
    print("\n|# # # # # # # # #|MENU|# # # # # # # # #|")
    print()
    print("            > Estudantes  |1|")
    print()
    print("            > Disciplinas |2|")
    print()
    print("            > Professores |3|")
    print()
    print("            > Turmas      |4|")
    print()
    print("            > Matrículas  |5|")
    print()
    print("            > Sair        |6|\n")
    return None


def menu_operacoes():
    print("\n11001001...|MENU DE OPERAÇÕES|...11001001")
    print()
    print("            > Incluir               |1|")
    print()
    print("            > Listar                |2|")
    print()
    print("            > Atualizar             |3|")
    print()
    print("            > Excluir               |4|")
    print()
    print("            > Voltar para home      |5|\n")


def verifica_codigo(codigo, file_name, codigo_tipo):
    """
    Vai verificar se o código presente na lista já não está presente, e vai apenas continuar se for fornecido um código válido

    :param codigo: Código que deverá ser verificado
    :param codigo_tipo: Refere se o código é de turma, professor etc.
    :return: Retorna um valor booleano dizendo se o código informado já existe
    """
    codigo_existe = False
    dados = ler_json(file_name)
    if dados == {}:
        salvar_json(dados, file_name)
    dados = ler_json(file_name)
    for _, dado in enumerate(dados):
        if codigo == dado[codigo_tipo]:
            codigo_existe = True
    return codigo_existe


def operacao_incluir(file_name):

    print("\nIncluir foi selecionado...")
    print("\n+ + + + +INCLUIR+ + + + +")
    dados = ler_json(file_name)
    if len(dados) == 0:
        print("lista vazia...", dados)

    if file_name == "disciplinas":
        while True:
            try:
                while True:
                    numero = int(
                        input("Informe o ID de registro da disciplina : "))
                    if verifica_codigo(numero, file_name, 'codigo_disciplina') == False:
                        break
                    print("Código informado já existe, informe outro")
            except ValueError:
                print("valor informado está incorreto")
                continue
            nome_disciplina = input("digite o nome da disciplina: ")
            novo = {
                "codigo_disciplina": numero,
                "nome_disciplina": nome_disciplina,
            }

            if numero <= 0:
                dados.insert(0, novo)
                break
            else:
                dados.insert(numero - 1, novo)
                salvar_json(dados, file_name, "w")
                break
    elif file_name == "estudantes" or file_name == "professores":
        while True:
            try:
                while True:
                    numero = int(input("Informe o ID de registro:"))
                    if verifica_codigo(numero, file_name, 'codigo') == False:
                        break
                    print("Código informado já existe, informe outro")
            except ValueError:
                print("valor informado está incorreto")
                continue
            pessoa = input("digite o nome: ")
            cpf = input("fale o cpf do mesmo: ")
            novo = {
                "codigo": numero,
                "nome": pessoa,
                "CPF": cpf
            }

            if numero <= 0:
                dados.insert(0, novo)
                break
            else:
                dados.insert(numero - 1, novo)
                salvar_json(dados, file_name, "w")
                break

    elif file_name == "turmas":
        while True:
            try:
                while True:
                    numero_turma = int(input("Informe o código da turma: "))
                    if verifica_codigo(numero_turma, file_name, 'codigo_turma') == False:
                        break
                    print("Código informado já existe, informe outro")
            except ValueError:
                print("valor informado está incorreto")
                continue
            codigo_disciplina = int(input("digite o codigo da disciplina: "))
            codigo_professor = int(input("digite o codigo do professor: "))
            novo = {
                "codigo_turma": numero_turma,
                "codigo_professor": codigo_professor,
                "codigo_disciplina": codigo_disciplina
            }

            if numero_turma <= 0:
                dados.insert(0, novo)
                salvar_json(dados, file_name)
                break
            else:
                dados.insert(numero_turma - 1, novo)
                salvar_json(dados, file_name, "w")
                break

    elif file_name == "matriculas":
        while True:
            try:
                while True:
                    numero_turma = int(input("Informe o código da turma: "))
                    if verifica_codigo(numero_turma, file_name, 'codigo_turma') == False:
                        break
                    print("Código informado já existe, informe outro")
            except ValueError:
                print("valor informado está incorreto")
                continue

            codigo_aluno = int(input("digite o codigo do estudante: "))
            novo = {
                "codigo_turma": numero_turma,
                "codigo_estudante": codigo_aluno,
            }

            if numero_turma <= 0:
                dados.insert(0, novo)
                salvar_json(dados, file_name)
                break
            else:
                dados.insert(numero_turma - 1, novo)
                salvar_json(dados, file_name, "w")
                break


def opcao_listar(file_name):
    print("\nListar foi selecionado...")
    print("\nListando {}..." .format(file_name))
    dados = ler_json(file_name)
    if len(dados) == 0:
        print("Não foram adicionados estudantes, adicione alguém para aparecer.")
    else:
        match file_name:
            case "estudantes" | "professores":
                for pessoa in dados:
                    print(
                        f'Código: {pessoa['codigo']} Nome: {pessoa["nome"]} CPF: {pessoa["CPF"]}')
            case "disciplinas":
                for disciplina in dados:
                    print(
                        f"Código: {disciplina["codigo"]} Nome da disciplina: {disciplina['nome']}")
            case "turmas":
                for turma in dados:
                    print(
                        f"Código da turma: {turma['codigo']} Código do professor: {turma['codigo_professor']} Código da disciplina: {turma['codigo_disciplina']}")
            case "matriculas":
                for matricula in dados:
                    print(
                        f"Código da turma: {matricula['codigo']} Código do estudante: {matricula['codigo_estudante']}")


def opcao_editar(file_name):
    dados = ler_json(file_name)

    def editar_estudante_Professor(file_name):
        while True:
            try:
                codigo_encontrar = int(
                    input("Informe o código para localizar: "))
            except ValueError:
                print("digite um valor correto")
                continue
            break
        for i, elemento in enumerate(dados):
            if codigo_encontrar == elemento['codigo']:
                while True:
                    try:
                        numero_novo = int(input(f"fale o novo código: "))
                        if verifica_codigo(numero_novo, file_name, "codigo") == False:
                            break
                        if numero_novo == codigo_encontrar:
                            break
                        print("Código já cadastrado")
                    except ValueError:
                        print("digite um valor correto")
                        continue
                pessoa = input("digite o nome: ")
                cpf = input("fale o cpf do mesmo: ")
                novos_dados = {
                    "codigo": numero_novo,
                    "nome": pessoa,
                    "CPF": cpf
                }

                del dados[i]
                if numero_novo > len(dados):
                    dados.append(novos_dados)
                    break
                elif numero_novo <= 0:
                    dados.insert(0, novos_dados)
                    break
                elif numero_novo > 0:
                    dados.insert(i, novos_dados)
                    salvar_json(dados, file_name, "w")
                    break
                else:
                    print("Código informado não existe")

    def editar_disciplina(file_name):
        while True:
            try:
                codigo_encontrar = int(
                    input("Informe o código para localizar: "))
            except ValueError:
                print("digite um valor correto")
                continue
            break
        for i, elemento in enumerate(dados):
            if codigo_encontrar == elemento['codigo']:
                while True:
                    try:
                        codigo_disciplina = int(
                            input(f"fale o novo código da disciplina: "))
                        if verifica_codigo(codigo_disciplina, file_name, "codigo") == False:
                            break
                        if codigo_disciplina == codigo_encontrar:
                            break
                        print("Código já cadastrado")
                    except ValueError:
                        print("digite um valor correto")
                        continue
                nome_disciplina = input("digite o nome: ")
                novos_dados = {
                    "codigo": codigo_disciplina,
                    "nome": nome_disciplina,
                }

                del dados[i]
                if codigo_disciplina > len(dados):
                    dados.append(novos_dados)
                    salvar_json(dados, file_name, "w")
                    break
                elif codigo_disciplina <= 0:
                    dados.insert(0, novos_dados)
                    salvar_json(dados, file_name, "w")
                    break
                elif codigo_disciplina > 0:
                    dados.insert(i, novos_dados)
                    salvar_json(dados, file_name, "w")
                    break
                else:
                    print("Código informado não existe")

    def editar_turmas(file_name):
        while True:
            try:
                codigo_encontrar = int(
                    input("Informe o código para localizar: "))
            except ValueError:
                print("digite um valor correto")
                continue
            break
        for i, elemento in enumerate(dados):
            if codigo_encontrar == elemento['codigo']:
                while True:
                    try:
                        codigo_turma = int(
                            input(f"fale o novo código da turma: "))
                        if verifica_codigo(codigo_disciplina, file_name, "codigo_turma") == False:
                            break
                        if codigo_disciplina == codigo_encontrar:
                            break
                        print("Código já cadastrado")
                    except ValueError:
                        print("digite um valor correto")
                        continue
                codigo_professor = input("digite o codigo do professor: ")
                codigo_disciplina = int(
                    input("informe o codigo da disciplina: "))
                novos_dados = {
                    "codigo": codigo_disciplina,
                    "codigo_professor": codigo_professor,
                    "codigo_disciplina": codigo_disciplina
                }

                del dados[i]
                if codigo_turma > len(dados):
                    dados.append(novos_dados)
                    salvar_json(dados, file_name, "w")
                    break
                elif codigo_turma <= 0:
                    dados.insert(0, novos_dados)
                    salvar_json(dados, file_name, "w")
                    break
                elif codigo_turma > 0:
                    dados.insert(i, novos_dados)
                    salvar_json(dados, file_name, "w")
                    break
                else:
                    print("Código informado não existe")

    def editar_matriculas(file_name):
        while True:
            try:
                codigo_encontrar = int(
                    input("Informe o código para localizar: "))
            except ValueError:
                print("digite um valor correto")
                continue
            break
        for i, elemento in enumerate(dados):
            if codigo_encontrar == elemento['codigo']:
                while True:
                    try:
                        codigo_turma = int(
                            input(f"fale o novo código da turma: "))
                        if verifica_codigo(codigo_turma, file_name, "codigo_turma") == False:
                            break
                        if codigo_turma == codigo_encontrar:
                            break
                        print("Código já cadastrado")
                    except ValueError:
                        print("digite um valor correto")
                        continue
                codigo_estudante = input("digite o codigo do estudante: ")
                novos_dados = {
                    "codigo": codigo_turma,
                    "codigo_estudante": codigo_estudante,
                }

                del dados[i]
                if codigo_turma > len(dados):
                    dados.append(novos_dados)
                    salvar_json(dados, file_name, "w")
                    break
                elif codigo_turma <= 0:
                    dados.insert(0, novos_dados)
                    salvar_json(dados, file_name, "w")
                    break
                elif codigo_turma > 0:
                    dados.insert(i, novos_dados)
                    salvar_json(dados, file_name, "w")
                    break
                else:
                    print("Código informado não existe")
    print('editar selecionado...')
    print('-+-+-+-+EDITAR-+-+-+-+')
    if len(dados) == 0:
        print("Não a nada para editar...")
        return None
    match file_name:
        case "estudantes" | "professores":
            editar_estudante_Professor(file_name)
        case "disciplinas":
            editar_disciplina(file_name)
        case "turmas":
            editar_turmas(file_name)
        case "matriculas":
            editar_matriculas(file_name)


def operacao_excluir(file_name):
    dados = ler_json(file_name)
    print('excluir selecionado...')
    print('---------EXCLUIR---------')
    while True:
        try:
            codigo_del = int(
                input("Informe o código para localizar e remover da lista: "))
            verificador = 0
        except ValueError:
            print("Valor informado incorreto")
            continue
        break
    for indice, elemento in enumerate(dados):
        if codigo_del == elemento['codigo']:
            if input(f"O elemento será deletado. Tem certeza? (y/n) ") == 'y':
                del dados[indice]
                salvar_json(dados, file_name)
                print("elemento deletado com sucesso")
                verificador = 1
                break
            else:
                verificador = 1
                print('processo cancelado')
                break
    if verificador == 0:
        print("Código informado não existe")


def acoes_operacao_menu(file_name):
    while True:
        opcao = 0
        verificado = 0
        menu_operacoes()

        try:
            opcao = int(input("Qual operação deseja realizar? "))
        except ValueError:
            print("\nDigite um valor correto")
            verificado = 1

        match opcao:
            case 1:
                operacao_incluir(file_name)
            case 2:
                opcao_listar(file_name)
            case 3:
                opcao_editar(file_name)
            case 4:
                operacao_excluir(file_name)
            case 5:
                print("voltando para home...")
                break
            case _:
                if verificado == 1:
                    pass
                else:
                    print("\n{} não é uma das opções." .format(opcao))


while True:
    estudantes = []
    opcao = 0
    verificado = 0

    menu_home()

    try:
        opcao = int(input("Por favor, selecione uma das opções: "))
    except ValueError:
        print("\nDigite um valor correto")
        verificado = 1

    match opcao:
        case 1:
            print("\nEstudantes foi selecionado...")
            acoes_operacao_menu('estudantes')
        case 2:
            print("\nDisciplinas foi selecionado...")
            acoes_operacao_menu('disciplinas')
        case 3:
            print("\nProfessores foi selecionado...")
            acoes_operacao_menu('professores')
        case 4:
            print("\nTurmas foi selecionado...")
            acoes_operacao_menu('turmas')
        case 5:
            print("\nMatrículas foi selecionado...")
            acoes_operacao_menu('matriculas')
        case 6:
            print("\nSair foi selecionado... Adeus!")
            break
        case _:
            if verificado == 1:
                pass
            else:
                print("\n{} não é uma das opções." .format(opcao))
