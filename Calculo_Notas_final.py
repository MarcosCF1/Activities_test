def escolha_disciplina(): #FUNÇÂO PARA AS ESCOLHAS PARA CASO DE NÂO ESCOLHA DE UMA DAS OPÇÕES REPETIR O CÓDIGO ENQUANTO NÃO OCORRER UMA ENTRADA CORRETA:
    disciplina = str(input('Digite o número da disciplina na qual você deseja saber a sua nota final e situação\n'
        'Matemática Aplicada (1)\n'
        'Fundamento de Banco de Dados (2)\n'
        'Linguagem de Programação (3)\n'
        'Lógica de Programação (4)\n'
        'SoftSkills (5)\n'
        '____________________________________________________\n: '
    ))
    return disciplina

D = escolha_disciplina()

while D not in ('1', '2','3','4', '5'):
    print(''), print('Escolha novamente dentre as escolhas abaixo!'), print('')
    D = escolha_disciplina()

if D == '1': # NOTA REFERENTE A MATEMATICA APLICADA:

    AP1 = float(input('Qual é a sua nota na AP1?: '))
    AP2 = float(input('Qual é a sua nota na AP2?: '))
    PF = float(input('Qual é a sua nota na Prova Final?: '))
    
    def matematica_nota_final(AP1, AP2, PF):
        x = (AP1+AP2)/2
        y = (x*0.5)+(PF*0.5)
        return y

    Nota_final = matematica_nota_final(AP1, AP2, PF)
    print('')
    print(f'A sua nota final é: {Nota_final:.2f}')

    if Nota_final >= 6.0:
        situação = 'Você foi aprovado, parábens!'

    else:
            situação = 'Você foi reprovado, melhore no próximo semestre'
    print(situação)

elif D == '2': #NOTA REFERENTE A BANCO DE DADOS:

    PREs = float(input('Qual é a média da sua nota em todas as atividades preparatórias?: '))
    AP1 = float(input('Qual é a sua nota na AP1?: '))
    AP2 = float(input('Qual é a sua nota na AP2?: '))
    PF = float(input('Qual é a sua nota na Prova Final?: '))

    def bd_nota_final(PREs, AP1, AP2, PF):
        x = (AP1*0.6)+(PREs*0.4)
        y = (AP2*0.6)+(PREs*0.4)
        w = (x+y)/2
        z = (w*0.5)+(PF*0.5)
        return z

    Nota_final = bd_nota_final(AP1, PREs, AP2, PF)

    print('')
    print(f'A sua nota final é: {Nota_final:.2f}')

    if Nota_final >= 6.0:
        situação = 'Você foi aprovado, parábens!'

    else:
            situação = 'Você foi reprovado, melhore no próximo semestre'

    print(situação)

elif D == '3': #NOTA REFERENTE A LINGUAGEM DE PROGRAMAÇÂO:

    PREs = float(input('Qual é a média da sua nota em todas as atividades preparatórias(PRE)?: '))
    AP1 = float(input('Qual é a sua nota na AP1?: '))
    AP2 = float(input('Qual é a sua nota na AP2?: '))
    PF = float(input('Qual é a sua nota na Prova Final?: '))

    def linguagem_de_programacao_nota_final(PREs, AP1, AP2, PF):
        x = (AP1+AP2)/2
        y = (PREs*0.5)+(x*0.5)
        return y

    Nota_final = linguagem_de_programacao_nota_final(PREs, AP1, AP2, PF)
    print('')
    print(f'A sua nota final é: {Nota_final:.2f}')

    if Nota_final >= 6.0:
        situação = 'Você foi aprovado, parábens!'

    else:
            situação = 'Você foi reprovado, melhore no próximo semestre'

    print(situação)

elif D == '4': #NOTA REFERENTE A LÓGICA DE PROGRAMAÇÃO:

    PREs = float(input('Qual é a média da sua nota em todas as atividades preparatórias(PRE)?: '))
    AP1 = float(input('Qual é a sua nota na AP1?: '))
    AP2 = float(input('Qual é a sua nota na AP2?: '))
    PF = float(input('Qual é a sua nota na Prova Final?: '))

    def logica_de_programacao_nota_final(PREs, AP1, AP2, PF):
        x = (AP1+AP2)/2
        y = (PREs*0.5)+(x*0.5)
        return y

    Nota_final = logica_de_programacao_nota_final(PREs, AP1, AP2, PF)

    print('')
    print(f'A sua nota final é: {Nota_final:.2f}')

    if Nota_final >= 6.0:
        situação = 'Você foi aprovado, parábens!'

    else:
            situação = 'Você foi reprovado, melhore no próximo semestre'

    print(situação)

elif D == '5': #NOTA REFERENTE A SOFTSKILLS
    print (f'Ainda não é possivel saber o calculo das notas de SOFTSKILLS, não houve uma \ndisponibilização do plano de aula!\n'
           'Agurde agurdando pelas próximas notas de aula')

    import time #REPRETIÇÃO DO MENU EM CONJUNTO COM PONTOS REPETIVOS

    for i in range(6):
        time.sleep(1)
        print('.', end='')
    print('')
    print('____________________________________________________\n')
    D = escolha_disciplina()


    
    

    



