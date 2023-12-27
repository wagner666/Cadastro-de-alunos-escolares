lista = {}

def cadastro_aluno():

    print('------------ Cadastro de Alunos e Notas Bimestrais ------------')

    print('\n')

    nome = input('Nome do aluno(a): ')
    serie = input('serie do Aluno(a): ')
    bimestre1 = float(input('1° Bimestre: '))
    bimestre2 = float(input('2° Bimestre: '))
    bimestre3 = float(input('3° Bimestre: '))
    bimestre4 = float(input('4° Bimestre: '))

    nota = (bimestre1 + bimestre2 + bimestre3 + bimestre4)/4
    print(f'Nota Final {nota}')
    # lista.append({'nome': nome,'serie': serie,'nota': nota})
    print('\n')

    lista[nome] = {'serie': serie, 'bimestre1': bimestre1, 'bimestre2': bimestre2, 'bimestre3': bimestre3, 'bimestre4': bimestre4, 'nota': nota}
    print(f'{nome} adicionado com sucesso.')

    print('\n')

def lista_aluno():
    print('------------ Lista de Alunos(a) ------------')

    print('\n')

    for nome, info in lista.items():
        print(f'Nome: {nome}, Serie: {info["serie"]}, Bimestre1: {info["bimestre1"]}, Bimestre2: {info["bimestre2"]}, Bimestre3: {info["bimestre3"]}, Bimestre4: {info["bimestre4"]}, Nota: {info["nota"]}')

    # for listas in lista:
    #     print(f"Nome:{lista['nome']}")
    #     print(f"Serie:{lista['serie']}")
    #     print(f"1° Bimestre:{lista['biestre1']}")
    #     print(f"2° Bimestre2:{lista['bimestre2']}")
    #     print(f"3° Bimestre3:{lista['bimestre3']}")
    #     print(f"4° Bimestre4:{lista['bimestre4']}")
        
    print('\n')

def excluir_aluno():
    print('---------- Excluir Alunos(a) ----------')
    
    print('\n')

    nome = input('Nome do aluno a ser excluido: ')
    if nome in lista:
        del lista[nome]
        print(f'{nome} foi excluido.')
    else:
        print(f'{nome} não foi excluido.')

    print('\n')

def modificar_nota():
    print('---------- Modificar Notas ----------')
    
    print('\n')
    
    nome = input('Nome do aluno(a) a se modificado: ')
    
    print('\n')
    
    if nome in lista:
        novo_Bimestre1 = float(input('Nova nota: '))
        novo_Bimestre2 = float(input('Nova nota: '))
        novo_Bimestre3 = float(input('Nova nota: '))
        novo_Bimestre4 = float(input('Nova nota: '))

        nova_nota = (novo_Bimestre1 + novo_Bimestre2 + novo_Bimestre3 + novo_Bimestre4)/4

        lista[nome]['bimestre1'] = novo_Bimestre1
        lista[nome]['bimestre2'] = novo_Bimestre2
        lista[nome]['bimestre3'] = novo_Bimestre3
        lista[nome]['bimestre4'] = novo_Bimestre4
        lista[nome]['nota'] = nova_nota

        print(f'Nota Final {nova_nota}')

        print(f'{nome} foi modificado.')

    else:
        print(f'{nome} não foi modificado.')


def sair():
    print('------------ Sair do Progama ------------')

while True:

    print('\nEscolha uma opção:')
    print('1 - Cadastra aluno(a)')
    print('2 - Lista aluno(a)')
    print('3 - Excluir aluno(a)')
    print('4 - Modificar nota')
    print('5 - Sair')

    opcao = input('Digite a opção que deseja conforme mostra a cima: ')

    if opcao == '1':
        cadastro_aluno()
    elif opcao == '2':
        lista_aluno()
    elif opcao == '3':
        excluir_aluno()
    elif opcao == '4':
        modificar_nota()
    elif opcao == '5':
        break
    else:
        print("Opção invalida. Tente novamente")