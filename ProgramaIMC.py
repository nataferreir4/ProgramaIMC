from time import sleep as tp
from tkinter import messagebox
import time
import datetime
import os
import math
# BIBLIOTECAS IMPORTADAS A CIMA
v = open('../../Downloads/Dados_Usuário.txt', 'w', encoding='UTF-8')#ARQUIVO CRIADO PARA SALVAR OS DADOS DO USUARIO.
with open('../../Downloads/Dados_Usuário.txt', 'a', encoding='UTF-8') as dados:
    dados.writelines('                                          Dados do Usuário sobre o IMC                                        \n')
temp = datetime.datetime.today()
temp = str(temp)
local = os.getcwd() # Pega o Local onde o programa está sendo executado.
escrevelocal = str(local)
with open('../../Downloads/LOG_time', 'w', encoding='UTF-8') as log:
    log.writelines(f'LOG..TIME.....(->{temp}<-)....\n')  # LOG para Data e Horário da Execução do software
    log.writelines(f'Local da Execução (->{local}<-)\n') # Escreve no LOG o diretório onde foi executado o programa
c = time.localtime()
day = c[2]
day = str(day) # Convertendo a variavel day para string
mounth = c[1]
mounth = str(mounth) # Convertendo a variavel mounth para string
year = c[0]
year = str(year) # Convertendo a variavel year para string
with open('../../Downloads/Dados_Usuário.txt', 'a', encoding='UTF-8') as dados:
    dados.writelines('                                                                                                              \n')
    dados.writelines(f'Data da Execução   --------------------------------------------------------------    {day}/{mounth}/{year} \n',)
# FUNÇÕES (CASO PRECISE)
def cronometro(time):
    for n in range(time, -1, -1):
        print(f'{n}' ) #FUNÇÃO CRONOMETRO QUE ATIVA UM TIMING DE ACORDO COM A ESCOLHA DO USUARIO QUE COMEÇA DO NUMERO ESCOLHIDO E VAI ATÉ 0.
        tp(1)
def IMCideal(altura, sexo):
    calculo = 0       #FUNÇÃO PRA CALCULAR O IMC DO USUARIO.
    if sexo == 'HOMEM':
        calculo = 72.7 * altura - 58
        return calculo
    elif sexo == 'MULHER':
        calculo = 62.1 * altura - 44.7
        return calculo
    else:
        print('Você digitou um SEXO inválido !')

# FORMATAÇÕES:
""" Azul = '\033[34m'+'TEXTO'+'\033[0;0m'
"""
# LISTAS E VARIAVEIS IMPORTANTES

ExAbaixoPeso = 0
exPesoIdeal = 0
exSobrePeso = 0
exObesidade = 0
sair = ["2", "NÃO", "NAO", "N", "SAIR", "EXIT", "QUIT"]
escolhas = [ 'exercicio', 'malhar','exercicios' ] # Palavras Chaves
escolhas2 = ['dieta', 'emagrecer', 'dietas'] # Palavras chaves
ListaNomesHM = ['HOMEM', 'MASCULINO', 'MAN', 'MALE', 'M'] # Palavras chaves
ListaNomesML = ['MULHER', 'FEMININO', 'WOMAN', 'FEMALE', 'F'] # Palavras chaves
tabelaPESOS = '\033[34m'+'Baixo peso muito grave'+'\033[0;0m'+' = abaixo de 16 kg/m².\n'+'\033[34m'+'Baixo peso grave'+'\033[0;0m'+' = entre 16 e 16,99 kg/m².\n'+'\033[34m'+'Baixo peso'+'\033[0;0m'+' = entre 17 e 18,49 kg/m².\n'+'\033[34m'+'Peso normal'+'\033[0;0m'+' = entre 18,50 e 24,99 kg/m².\n'+'\033[34m'+'Sobrepeso'+'\033[0;0m'+' = entre 25 e 29,99 kg/m².\n'+'\033[34m'+'Obesidade grau I'+'\033[0;0m'+' = entre 30 e 34,99 kg/m².\n'+'\033[34m'+'Obesidade grau II'+'\033[0;0m'+' = entre 35 e 39,99 kg/m².\n'+'\033[34m'+'Obesidade grau III (obesidade mórbida)'+'\033[0;0m'+' = maior que 40 kg/m.\n'

SEX = '' # Variavel que recebe o SEXO da pessoa
calcIMC = 0 # Variavel contendo o Calculo do IMC
situacao = '' # Variavel que recebe a situação da pessoa de acordo com os calculos feitos.

#1 Cabeçalho explicando a ideia do projeto.

print('\033[34m'+'PROJETO IMC CJ'+'\033[0;0m\n')
tp(1)
print('\n\033[34m'+'INTEGRANTES'+'\033[0;0m\n')
tp(1)
print('Ayrton Leandro Campos de Oliveira.--RA: 4332156')
tp(1)
print('Natã Barboza Oliveira Ferreira.-----RA: 4675614')
tp(1)
print('Charles Rafhael Martins Pereira.----RA: 4636678')
tp(1)
print('Pedro Henrique Leandro.-------------RA: 4656440')
tp(1)
print('Marcus Vinicius Cavalcante Salvino.-RA: 4325567')
tp(1.5)
print('\n\033[34m'+'UNICA CURSO:'+'\033[0;0m',' Analise e Desenvolvimento de Sistemas.', '\033[34m'+'Periodo:'+'\033[0;0m',' Noturno')
print('\n\033[34m'+'MATÉRIA:'+'\033[0;0m',' Projeto Integrador\n')
tp(2)
# 2 - pede peso, nome, altura e sexo do usuario.

while True:
    nome = input('\033[34m'+'Como deseja ser chamado: '+'\033[0;0m')
    with open('../../Downloads/Dados_Usuário.txt', 'a', encoding='UTF-8') as dados:
        dados.writelines(f'Nome do usuário: {nome}\n') # Escreve o nome do usuário no txt
    while True:
        try:
            altura = input('\033[34m'+'Digite sua altura: '+'\033[0;0m').replace(',','.')
            altura = float(altura)
        except:
            print('Altura inválida!')
        else:
            break

    while (altura < 1.30) or (altura > 2.50):
        try:
            altura = input('\n\033[34m'+'Altura inválida!'+'\033[0;0m\nInsira sua altura corretamente: ').replace(',','.')
            altura = float(altura)
        except ValueError:
            print('\n\033[34m'+'Ocorreu um erro em nosso sistema! Tente novamente mais tarde.'+'\033[0;0m').replace(',','.')
    with open('../../Downloads/Dados_Usuário.txt', 'a', encoding='UTF-8') as dados:
        dados.writelines(f'altura do usuário: {str(altura)} \n') # Escreve a altura do usuario no TXT
    while True:
        try:
            peso = input('\033[34m'+'Digite seu peso: '+'\033[0;0m').replace(',', '.')
            peso = float(peso)
        except:
            print('Peso inválido\n')
        else:
            break
    while (peso < 30) or (peso > 200):
        try:
            peso = float(input('\n\033[34m'+'Peso Inválido!'+'\033[0;0m\nInsira seu peso corretamente: '))
        except ValueError:
            print('\n\033[34m'+'Peso Inválido!'+'\033[0;0m\nInsira seu peso corretamente: ')
    with open('../../Downloads/Dados_Usuário.txt', 'a', encoding='UTF-8') as dados: # Escreve o peso do usuario no txt
        dados.writelines(f'peso do usuário: {str(peso)}\n')
    #CALCULO DO IMC
    calcIMC = peso / (altura * altura)
    if calcIMC < 18.5:
        situacao = 'Abaixo do peso normal'
    elif calcIMC >= 18.5 and calcIMC < 24.9:
        situacao = 'Peso normal'
    elif calcIMC >= 25 and calcIMC < 29.9:
        situacao = 'Sobrepeso'
    elif calcIMC >= 30 and calcIMC < 34.9:
        situacao = 'Obesidade Grau 1'
    elif calcIMC >= 35 and calcIMC < 39.9:
        situacao = 'Obesidade Grau 2'
    elif calcIMC > 40:
        situacao = 'Obesidade Grau 3(Mórbida)'
    #SEXO DO USUARIO.

    while True:
        sex = input('\nQual o seu sexo? (M para Masculino e F para Feminino)\n\033[34m'+'Digite: '+'\033[0;0m').upper()
        if sex in ListaNomesHM:
            SEX = 'HOMEM'
            with open('../../Downloads/Dados_Usuário.txt', 'a', encoding='UTF-8') as dados:
                dados.writelines(f'Sexo: {SEX}\n') # Escreve o SEXO do usuario se for Homem
            break
        elif sex in ListaNomesML:
            SEX = 'MULHER'
            with open('../../Downloads/Dados_Usuário.txt', 'a', encoding='UTF-8') as dados:
                dados.writelines(f'Sexo: {SEX}\n') # Escreve o SEXO do usuario se for Mulher
            break
        else:
            print('\nSexo Inexistente.')
    imcusuário = IMCideal(altura,SEX)
    # 3 - retorna a tabela do IMC e a posição do usuário nela.
    imc = ( peso / (altura*altura) )
    with open('../../Downloads/Dados_Usuário.txt', 'a', encoding='UTF-8') as dados: # Escreve o IMC do usuario no txt
        dados.writelines('                        \n')
        dados.writelines(f'IMC do Usuário: {str(imc)} \n')
    print('\n\n\033[34m'+'Abaixo uma tabela com os pesos ideais'+'\033[0;0m\n')
    tp(1)
    print(tabelaPESOS)
    with open('../../Downloads/Dados_Usuário.txt', 'a', encoding='UTF-8') as dados: # Escreve a tabela de pesos no TXT
        dados.writelines('ABAIXO A TABELA COM OS PESOS IDEAIS PARA CADA IMC \n')
        dados.writelines(f'{str(tabelaPESOS)}\n')
    tp(1)
    print('\033[34m'+'O seu IMC é: '+'\033[0;0m'+f'{imc:.2f} e o '+'\033[34m'+'peso ideal para sua altura é: '+'\033[0;0m'+f'{imcusuário:.2f}\n')
    with open('../../Downloads/Dados_Usuário.txt', 'a', encoding='UTF-8') as dados: # Escreve o IMC "IDEAL" pro usuario no TXT
        dados.writelines(f'O IMC Ideal para sua altura e sexo seria: {str(imcusuário)}\n')
    escolha = 0

    print('Baseado no seu peso, recomendamos uma lista específica de dietas e exercícios:\n')

    while True:
        escolha = input('\n\033[34m'+'1'+'\033[0;0m - para ter acesso a lista de exercícios\n\033[34m'+'2'+'\033[0;0m - para lista de dietas\n\033[34m'+'3'+'\033[0;0m - Sair.\n\n\033[34m'+'Digite: '+'\033[0;0m').lower()
        if escolha == '3':
            break
        elif escolha == '1' or '2':
            if SEX == 'HOMEM'or'MULHER':
                if situacao == 'Abaixo do peso normal':
                    while True:
                        if escolha == '1':
                            print('\n\033[34m'+'IMPORTANTE: '+'\033[0;0mAntes de começar a fazer qualquer treinamento ou exercício, é fundamental para qualquer pessoa se submeter a uma avaliação médica\npara se certificar de que está apto a praticar esse tipo de treino e saber em que nível de intensidade pode iniciar.')
                            tp(0.8)
                            print('\nExercicios recomendados:')
                            tp(0.9)
                            print('[1]Flexão tradicional e de braços abertos')
                            tp(1)
                            print('[2]Agachamento tradicional e estático')
                            tp(1)
                            print('[3]Tríceps com cadeira')
                            tp(1)
                            print('[4]Lunges alternado')
                            tp(1)
                            ExAbaixoPeso = input('\033[34m'+'Digite o número respectivo do exercício'+'\033[0;0m para ter\nmais informações sobre o mesmo ou digite 5 para sair: ')

                            if ExAbaixoPeso == '1':
                                print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                tp(1)
                                print('1. Existem vários tipos de flexões, o ideal é começar pela mais básica delas e depois decidir se vai para outros tipos.')
                                tp(1)
                                print('2. Na flexão tradicional, deixe os braços um pouco separados, tendo a largura do ombro como medida e, \n'
                                      'assim, realize um movimento de flexão e extensão dos cotovelos para baixo. Essa é a versão mais básica da flexão.')
                                tp(0.2)
                                print('------------------------------------------------------------------------------------------------------------------------')
                            elif exAbaixoPeso == '2':
                                print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                tp(1)
                                print('1. O necessário para um agachamento tradicional correto é manter a coluna alinhada.  Dessa forma, você não sentirá problemas posteriormente.')
                                tp(1)
                                print('2. Comece o agachamento tradicional abaixando-se relativamente próximo do chão, com os braços e mãos esticados para frente.')
                                tp(1)
                                print('3. Volte e repita o movimento por cerca de 30 segundos.')
                                tp(1)
                                print('4. No agachamento estático, em vez de subir e descer, mantenha a posição embaixo com os joelhos em relação ao chão.')
                                tp(1)
                                print('5. Não se esqueça de manter as costas retas. Mantenha essa posição e depois alterne para aliviar a dor. Esse movimento ajuda a fortalecer o tronco e as pernas.')
                                tp(1)
                                print('6. Como iniciante, o ideal é fazer 8 repetições desses exercícios a depender do desempenho.')

                            elif exAbaixoPeso == '3':
                                print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                tp(1)
                                print('1. Esse é o único exercício que necessita de um auxiliar para ser executado.')
                                tp(1)
                                print('2. Para iniciá-lo, coloque uma cadeira ou mesa próxima de você, depois com as palmas da mão crie apoio nela com as costas próximas.')
                                tp(1)
                                print('3. Seus braços devem estar flexionando para trás em relação ao corpo.')
                                tp(1)
                                print('4. Estique as pernas e flexione o corpo para o chão como se estivesse sentando.')
                                tp(1)
                                print('5. Se o exercício estiver difícil, tente aproximar mais os pés, pois isso irá diminuir o peso que é necessário para levantar o músculo. Esse exercício fortalece as pernas e tríceps.')
                                tp(1)
                                print('6. Faça mais ou menos 20 repetições desse exercício — dependendo da sua resistência.')

                            elif exAbaixoPeso == '4':
                                print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                tp(1)
                                print('1. Para o exercício de lunges alternados, é necessário ficar de pé, com as costas eretas e em seguida dar um passo para frente dobrando a perna, sua coxa deve ficar paralela ao chão.')
                                tp(1)
                                print('2. Apoie as mãos no joelho ou próximo dele e fique assim por 30 segundos, depois alterne para a outra perna.')
                                tp(1)
                                print('3. No lunges estático, coloque o pé direito à frente, e o pé esquerdo atrás. E dobre o joelho direto para baixar o corpo em direção ao chão.')
                                tp(1)
                                print('4. Fique no movimento por 30 segundos, descanse 15 segundos e depois repita no outro joelho.')
                                tp(1)
                                print('5. Esse exercício ajuda a fortalecer os joelhos e coluna. Recomenda-se fazer 10 repetições de cada lado ou menos caso seja iniciante.')
                                tp(1)
                                print('6. Se você fizer exercícios físicos aliados à uma dieta saudável e equilibrada, certamente atingirá os resultados esperados rapidamente.')
                                tp(1)
                                print('7. Ganhar massa muscular não é complicado se for por meio de exercícios eficientes e dedicação.')

                            elif exAbaixoPeso == '5':
                                break
                            else:
                                print('Número digitado inválido. Digite 1, 2, 3, 4 ou 5.')
                        elif escolha == '2':
                            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                            print('-Nunca pule refeições: faça ao menos 6 refeições fracionadas ao longo do dia;')
                            tp(1)
                            print('-Aumente gradativamente a ingestão calórica: dessa forma o estômago vai se acostumando aos poucos com maiores volumes de alimento;')
                            tp(1)
                            print('-Não se entupa de besteiras: evite alimentos industrializados e fast foods, além de darem a sensação de estufamento, não contribuem para a nutrição;')
                            tp(1)
                            print('-Varie o cardápio: o visual das refeições influencia no apetite, por isso faça pratos coloridos e com alimentos que agradam seu paladar;')
                            tp(1)
                            print('-Faça suas refeições em um local tranquilo: evite distrações como comer em frente à TV ou usando o celular por exemplo, dessa forma você se concentra mais na refeição;')
                            tp(1)
                            print('-Comer acompanhado também pode ser um estímulo, fazendo da refeição uma atividade social e uma hora mais agradável;')
                            tp(1)
                            print('-Inclua oleaginosas na dieta: amêndoas, castanhas e nozes são lanches práticos, boas fontes de gordura e com alto valor nutritivo;')
                            tp(1)
                            print('-Preste atenção no preparo dos alimentos: dê preferência à alimentos frescos e preparados da maneira mais natural possível, evite frituras e processados;')
                            tp(1)
                            print('-Consuma proteínas como o carnes, ovos, leite e derivados: eles são fontes essenciais para o ganho de massa magra;')
                            tp(1)
                            print('-Consulte um nutricionista para avaliar a necessidade de suplementação hipercalórica.')
                            tp(0.3)
                            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                            break
                elif situacao == 'Peso normal':
                    while True:
                        if escolha == '1':
                            print('\n\033[34m'+'IMPORTANTE: '+'\033[0;0mAntes de começar a fazer qualquer treinamento, é fundamental para qualquer pessoa se submeter a uma avaliação médica\n'+
                                  'para se certificar de que está apto a praticar esse tipo de treino e saber em que nível de intensidade pode iniciar.')
                            tp(0.7)
                            print('\n\n\033[34m'+'Exercícios recomendados:'+'\033[0;0m\n')
                            tp(1)
                            print('[1]Skkiping – 30 segundos')
                            tp(1)
                            print('[2]Agachamento – 30 segundos')
                            tp(1)
                            print('[3]Escalador – 30 segundos')
                            tp(1)
                            print('[4]Avanço alternado – 30 segundos')
                            tp(1)
                            print('[5]Flexão de braço – 30 segundos')
                            tp(1)
                            print('[6]Prancha – 1 minuto')
                            tp(1)
                            print('[7]Descansar por 2 minutos antes de começar uma nova série.\n')
                            tp(0.1)
                            exPesoIdeal = input('\033[34m'+'Digite o número respectivo do exercício'+'\033[0;0m para ter\nmais informações sobre o mesmo ou digite 8 para sair: ')

                            if exPesoIdeal == '1':
                                print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                tp(1)
                                print('1. De pé, levante um joelho até a altura do quadril, formando um ângulo 90 graus.')
                                tp(1)
                                print('2. O braço oposto acompanha o movimento. Ou seja, quando o joelho direito estiver à frente, o braço esquerdo também sobe flexionado.')
                                tp(1)
                                print('3. Inicie de forma lenta e controlada para coordenar o movimento.')
                                tp(1)
                                print('4. Aumente a intensidade gradativamente.')
                                tp(1)
                                print('------------------------------------------------------------------------------------------------------------------------')
                            elif exPesoIdeal == '2':
                                print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                tp(1)
                                print('1. Afaste os pés o suficiente para deixá-los alinhados com o quadril.')
                                tp(1)
                                print('2. Imagine que você está se sentando em uma cadeira: dobre os joelhos, empine levemente o bumbum e faça o movimento de descida.')
                                tp(1)
                                print('3. Você deve iniciar a flexão dos joelhos e do quadril simultaneamente. Desse modo, você não prejudica o desenvolvimento do movimento.')
                                tp(1)
                                print(''' 4. Para não flexionar o quadril excessivamente e sobrecarregar a lombar, preste atenção ao projetar o peitoral para o chão.
                            Dessa forma, o segredo para fazer o agachamento está no abdômen: Para uma excelente postura, mantenha o abdômen bem contraído durante todo o processo,
                            tanto de descida, quanto de subida.''')
                                tp(1)
                                print('5. Por último, estenda as pernas para voltar à posição inicial.')
                                tp(1)
                                print('------------------------------------------------------------------------------------------------------------------------')


                            elif exPesoIdeal == '3':
                                print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                tp(1)
                                print('1. O exercício escalador ou mountain climber inicia na postura da prancha e trabalha especialmente a musculatura estabilizadora do tronco, o core.')
                                tp(1)
                                print('2. Faça um movimento de puxar a perna ao peito, alternadamente')
                                tp(1)
                                print('3. Você pode aumentar a velocidade como numa corrida e, assim, elevar sua frequência cardíaca e a intensidade do exercício')
                                tp(1)
                                print('-------------------------------------------------------------------------------------------------------------------------')

                            elif exPesoIdeal == '4':
                                print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                tp(1)
                                print('1. De pé, abra bem o peito e contraia o abdômen.')
                                tp(1)
                                print('2. As mãos ficam à frente do corpo, na altura do peito e juntas. Assim, você consegue se equilibrar mais facilmente.')
                                tp(1)
                                print('3. Dê uma passada larga para frente com uma das pernas. O pé de trás fica em meia ponta.')
                                tp(1)
                                print('4. Flexione o joelho da perna de trás e desça em direção ao chão, abaixando o quadril. Ambos os joelhos dobram em um ângulo de 90 graus.')
                                tp(1)
                                print('5. Suba novamente e recolha a perna da frente, voltando à posição inicial.')
                                tp(1)
                                print('6. Repita o movimento alternando as pernas.')
                                tp(1)
                                print('-----------------------------------------------------------------------------------------------------------------------')

                            elif exPesoIdeal == '5':
                                print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                tp(1)
                                print('1. Deite-se no chão em decúbito ventral (peitoral, abdômen e coxas apoiadas sobre o solo).')
                                tp(1)
                                print('2. Apoie as mãos no solo na mesma linha do peitoral, afastadas em uma largura um pouco maior do que a dos ombros.')
                                tp(1)
                                print('3. Mantenha as escápulas na direção da lombar (ombros afastados da orelha).')
                                tp(1)
                                print('4. Contraia toda musculatura do abdômen, glúteos e coxas.')
                                tp(1)
                                print('5. Estenda os cotovelos, elevando o corpo todo de uma só vez.')
                                tp(1)
                                print('6. Mantenha a cabeça alinhada com o tronco e quadril, formando uma linha reta.')
                                tp(1)
                                print('7. Flexione os cotovelos e retorne praticamente para a posição inicial do exercício, sem encostar o corpo no solo.')
                                tp(1)
                                print('8. Dê uma pequena pausa e, em seguida, repita o movimento.')
                                tp(1)
                                print('9. Durante o exercício, apenas as mãos e os pés devem tocar o chão.')
                                tp(1)
                                print('------------------------------------------------------------------------------------------------------------------------')

                            elif exPesoIdeal == '6':
                                print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                tp(1)
                                print('1. Deite de barriga para baixo.')
                                tp(1)
                                print('2. Apoie os antebraços no chão')
                                tp(1)
                                print('''3. Preferencialmente, posicione a cabeça alinhada com olhar voltado para baixo.
Os ombros devem estar alinhados na linha do cotovelo, e as mãos devem estar voltadas para cima.''')
                                tp(1)
                                print('4. Com o corpo alinhado, levante o quadril.')
                                tp(1)
                                print('''5. Deixe a posição dos pés mais afastada, pois garante mais estabilidade, principalmente para iniciantes.
Conforme a condição física for aumentando, aproxime as pernas e use apenas uma base de membros inferiores para dar um ’pump‘ na intensidade do exercício.''')
                                tp(1)
                                print('6. Para finalizar, é necessário que o praticante faça uma contração com o abdômen, como se empurrasse o umbigo para dentro e para cima.')
                                tp(1)
                                print('------------------------------------------------------------------------------------------------------------------------')

                            elif exPesoIdeal == '7':
                                print("""Tome uma água e alongue-se para uma nova série!""")
                            elif exPesoIdeal == '8':
                                break
                            else:
                                print('Número digitado inválido. Digite 1, 2, 3, 4, 5, 6, 7 ou 8.')
                        elif escolha == '2':
                            print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                            tp(1)
                            print('-Consuma alimentos fontes de proteínas magras;')
                            tp(1)
                            print('-Consuma alimentos fontes de carboidratos integrais;')
                            tp(1)
                            print('-Evite as gorduras ruins: saturada e trans, inclua alimentos fontes de gorduras saudáveis: abacate, azeite extra virgem, oleaginosas (castanha, amêndoa, noz), peixe;')
                            tp(1)
                            print('-Consuma açúcar e sal com moderação;')
                            tp(1)
                            print('-Aumente a ingestão de água nos intervalos das refeições;')
                            tp(1)
                            print('-Evite consumo de alimentos industrializados ricos em calorias, gorduras, açúcares, sal, cafeína, realçadores de sabor e conservantes;')
                            tp(1)
                            print('-Faça sua lista de compras saudáveis e tente ser fiel a ela;')
                            tp(1)
                            print('-Planeje suas refeições. Se no trabalho não há opções saudáveis de almoço ou lanche, prepare em casa com todo carinho as suas marmitas e leve com você;')
                            tp(1)
                            print('-Nenhum alimento é proibido, mas evite os excessos;')
                            tp(1)
                            print('-Respeite os sinais de fome e saciedade;')
                            tp(1)
                            print('-Evite passar muito tempo sem se alimentar, para evitar querer descontar a abstinência de uma vez só.')
                            tp(1)
                            print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                            break
                elif situacao == 'Sobrepeso':
                    while True:
                        if escolha == '1':
                            print('\n\033[34m'+'IMPORTANTE: '+'\033[0;0mAntes de começar a fazer qualquer treinamento, é fundamental para qualquer pessoa se submeter a uma avaliação médica\n'
                                  +'para se certificar de que está apto a praticar esse tipo de treino e saber em que nível de intensidade pode iniciar.')
                            tp(1)
                            print('\n\n\033[34m'+'Exercícios recomendados:'+'\033[0;0m\n')
                            tp(1)
                            print('[1]Exercícios feitos na água')
                            print('[2]Caminhada')
                            print('[3]Ciclismo')
                            print('[4]Yoga')
                            print('[5]Corrida\n')
                            tp(1)
                            exSobrePeso = input('\033[34m'+'Digite o número respectivo do exercício'+'\033[0;0m para ter\nmais informações sobre o mesmo ou digite 6 para sair: ')
                            if exSobrePeso == '1':
                                print('\n\033[34m'+'Exercícios na água recomendados:'+'\033[0;0m\n')
                                tp(1)
                                print('[1]Prancha na piscina')
                                print('[2]Corrida na piscina')
                                print('[3]Exercício de uma perna só')
                                print('[4]Bicicleta')
                                print('[5]Crunch')
                                print('[6]Elevação lateral dos braços')
                                print('[7]Polichinelo\n')
                                tp(1)
                                exSobrepeso1 = input('\033[34m'+'Digite o número respectivo do exercício'+'\033[0;0m para ter mais informações sobre ele: ')
                                if exSobrepeso1 == '1':
                                    print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                    tp(1)
                                    print('1. Começar em pé na piscina e segurar um macarrão/espaguete de piscina verticalmente com as duas mãos.')
                                    tp(1)
                                    print('''2. Então, pressionar o macarrão para baixo na água e inclinar-se para a frente até que o corpo esteja
em uma inclinação plana e uniforme, com a cabeça para fora d’água.''')
                                    tp(1)
                                    print('3. Tentar se manter estável na posição durante um a dois minutos.')
                                    tp(1)
                                    print('------------------------------------------------------------------------------------------------------------------------')
                                    tp(1)

                                elif exSobrepeso1 == '2':
                                    print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                    tp(1)
                                    print('1. correr em zigue-zague de uma ponta a outra na piscina. Em seguida, correr diretamente em todas as correntes que acabou de criar.')
                                    tp(1)
                                    print('''2. É necessário que a corrida seja feita com um alinhamento apropriado do corpo, em que as orelhas, os ombros e os quadris
estejam em uma linha vertical, para que o core (musculatura localizada ao redor de toda a região do tronco, na linha da coluna lombar),
e não os ombros ou pernas, seja responsável por te manter ereto.''')
                                    tp(1)
                                    print('-----------------------------------------------------------------------------------------------------------------------')

                                elif exSobrepeso1 == '3':
                                    print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                    tp(1)
                                    print('''1. posicionar-se em pé em uma parte da piscina em que a água fique na altura da sua cintura, levantar o joelho esquerdo e colocar o meio
de um macarrão/espaguete de piscina embaixo do seu pé esquerdo, de modo que o acessório flutue para cima na forma de um “U”.''')
                                    tp(1)
                                    print('2. Manter as mãos ao lado do corpo e se equilibrar ao longo de um minuto com o pé esquerdo no macarrão.')
                                    tp(1)
                                    print('3. Mover o joelho esquerdo para fora lateralmente e se equilibrar por mais um minuto.')
                                    tp(1)
                                    print('4. Depois, trocar as pernas para repetir o movimento com o joelho direito levantado e o pé direito no macarrão/espaguete de piscina.')
                                    tp(1)
                                    print('------------------------------------------------------------------------------------------------------------------------')

                                elif exSobrepeso1 == '4':
                                    print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                    tp(1)
                                    print('1. Apoiar as costas na parede da piscina e estender os braços na borda.')
                                    tp(1)
                                    print('''2. Fazer o movimento de pedalada com as pernas, dobrá-las e levar uma de cada vez à superfície da água, em um ritmo veloz,
da mesma forma que ocorre quando pedalamos uma bicicleta.''')
                                    tp(1)
                                    print('-----------------------------------------------------------------------------------------------------------------------')

                                elif exSobrepeso1 == '5':
                                    print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                    tp(1)
                                    print('1. a partir da posição do exercício anterior, a bicicleta, estender as pernas, mantendo os pés juntos.')
                                    tp(1)
                                    print('2. Na sequência, puxar os dois joelhos em direção ao peito e retornar ao posicionamento inicial.')
                                    tp(1)
                                    print('------------------------------------------------------------------------------------------------------------------------')

                                elif exSobrepeso1 == '6':
                                    print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                    tp(1)
                                    print('1. Em pé, segurar um halter (ou uma garrafinha com água) em cada uma das mãos e estender os braços ao lado dos quadris.')
                                    tp(1)
                                    print('2. Elevar lateralmente os braços até a altura dos ombros e abaixar os halteres ou garrafinhas de volta aos quadris.')
                                    tp(1)
                                    print('3. A força deve ser colocada na subida e na descida dos braços.')
                                    tp(1)
                                    print('-----------------------------------------------------------------------------------------------------------------------')

                                elif exSobrepeso1 == '7':
                                    print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                    tp(1)
                                    print('1. Em pé, estender os braços verticalmente para os lados, com as mãos e os cotovelos posicionados na altura dos ombros.')
                                    tp(1)
                                    print('2. As pernas devem estar bem separadas, em uma distância maior do que a largura dos ombros.')
                                    tp(1)
                                    print('3. Então, abrir e fechar os braços, ao mesmo tempo em que realiza o mesmo movimento com as pernas.')
                                    tp(1)
                                    print('------------------------------------------------------------------------------------------------------------------------')

                                else:
                                    print('Número digitado inválido. Digite 1, 2, 3, 4, 5, 6 ou 7.')
                            elif exSobrePeso == '2':
                                print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                tp(1)
                                print('1. Usar roupas confortáveis.')
                                tp(1)
                                print('2. Fazer alongamento antes e depois das caminhadas.')
                                tp(1)
                                print('3. Caminhar em locais planos ou com aclives e declives suaves.')
                                tp(1)
                                print('4. Manter o tronco reto.')
                                tp(1)
                                print('5. Manter ombros e pescoço relaxados.')
                                tp(1)
                                print('6. Manter quadril, joelhos e pés alinhados.')
                                tp(1)
                                print('7. Respirar profundamente.')
                                tp(1)
                                print('-----------------------------------------------------------------------------------------------------------------------')

                            elif exSobrePeso == '3':
                                print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                tp(1)
                                print('1. Ir devagar no começo, somente após passar por um período de adaptação aos equipamentos e do seu próprio corpo é que você poderá ir mais rápido.')
                                tp(1)
                                print('2. O Artigo 201 do Código de Trânsito Brasileiro estabelece que a distância mínima entre os veículos e ciclistas deve ser de 1,5 metro.')
                                tp(1)
                                print('3. O uso de roupas com cores chamativas e material reflexivo é o mais indicado para que você se destaque entre veículos e pedestres.')
                                tp(1)
                                print('4. Use acessórios adequados para sua segurança, como capacetes luvas de proteção.')
                                tp(1)
                                print('-----------------------------------------------------------------------------------------------------------------------')

                            elif exSobrePeso == '4':
                                print('\n\033[34m'+'Posições de Yoga recomendadas:'+'\033[0;0m\n')
                                tp(1)
                                print('[1]Uttanasana')
                                print('[2]Bhujangasana')
                                print('[3]Trikonasana')
                                print('[4]Paripurna Navasana')
                                print('[5]Parivrtta Sukhasana')
                                tp(1)
                                exSobrePeso4 = input('\n\033[34m'+'Digite o número respectivo do exercício'+'\033[0;0m para ter mais informações sobre ela: ')
                                if exSobrePeso4 == '1':
                                    print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                    tp(1)
                                    print('1. Comece com as mãos na cintura. Dobre o tronco à frente, fazendo o movimento a partir da bacia')
                                    tp(1)
                                    print('2. Enquanto desce o tronco, alongue-se, esticando sempre o tronco.')
                                    tp(1)
                                    print('3. Mantenha as pernas bem esticadas, tentando apoiar as palmas das mãos no chão. Se não for possível, apoie as mãos nos pés, tornozelos ou pernas.')
                                    tp(1)
                                    print('4. As coxas devem estar firmes e o abdomen está activo.')
                                    tp(1)
                                    print('''5. Deixe a cabeça solta, pescoço relaxado. Evite forçar a cabeça na direcção dos joelhos. Abra o peito, levando o abdomen em direcção às coxas
e o topo da cabeça em direcção ao chão.''')
                                    tp(1)
                                    print('6. Para desfazer a posição, leve novamente as mãos à cintura e suba com as costas rectas.')
                                    tp(1)
                                    print('------------------------------------------------------------------------------------------------------------------------')

                                elif exSobrePeso4 =='2':
                                    print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                    tp(1)
                                    print('1. Deitado de barriga para baixo, apoie as palmas das mãos por baixo dos ombros, mantendo os cotovelos fechados, junto às costelas.')
                                    tp(1)
                                    print('2. Estique bem as pernas, activando-as e rodando uma na direcção da outra. Os calcanhares ficam virados para cima, peito do pé no chão, pés esticados.')
                                    tp(1)
                                    print('''3. Puxe o abdomen para dentro e para cima, vire o coccix em direcção aos calcanhares. O glúteo deve estar firme, mas não contraia demasiado,
para não colocar tensão na lombar.''')
                                    tp(1)
                                    print('4. Eleve o tronco, até onde for possível. A zona púbica deve manter-se apoiada no chão.')
                                    tp(1)
                                    print('5. Afaste os ombros das orelhas e baixe as omoplatas e estique o pescoço.')
                                    tp(1)
                                    print('''6. Só depois de o pescoço estar bem esticado e os ombros bem alinhados, é que deve inclinar um pouco a cabeça para trás
(não deixe a cabeça pendurada como um peso morto, para não colocar pressão na cervical).''')
                                    tp(1)
                                    print('7. Para desfazer a posição, baixe novamente o tronco até ao chão.')
                                    tp(1)
                                    print('------------------------------------------------------------------------------------------------------------------------')

                                elif exSobrePeso4 =='3':
                                    print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                    tp(1)
                                    print('''1. Pés afastados cerca de cinco palmos. Braços abertos, esticados à altura dos ombros, palmas das mãos voltadas para baixo.
Os braços devem estar firmes, como se alguém puxasse por cada uma das mãos.''')
                                    tp(1)
                                    print('''2. Rode o pé direito 90 graus para fora e o esquerdo um pouco para dentro (para a direita). Os calcanhares devem estar alinhados, coxas firmes.
Rode a musculatura da coxa direita para fora, de modo que a rótula do joelho esteja alinhada com o centro do tornozelo direito.''')
                                    tp(1)
                                    print('3. Alongue o tronco para a direita, como se quisésse tocar com a mão direita na parede do lado direito, esticando e alongando ambos os lados do tronco.')
                                    tp(1)
                                    print('''4. Flicta o tronco lateralmente para a direita, pousando a mão direita no chão do lado de fora do pé, ou onde for possível (tornozelo, ou perna).
O movimento deve ser feito a partir da bacia e não da cintura.''')
                                    tp(1)
                                    print('5. Ao descer o tronco, tenha atenção ao alinhamento, evitando fugir com a bacia para trás (o que fará com que o tronco se desvie para a frente).')
                                    tp(1)
                                    print('6. O braço esquerdo fica perpendicular ao chão, alinhado com o ombro direito.')
                                    tp(1)
                                    print('''7. Rode a cabeça para cima, olhando em direcção à mão esquerda.Caso haja muita tensão no pescoço e seja difícil olhar para a mão de cima,
mantenha a cabeça numa posição neutra.''')
                                    tp(1)
                                    print('''8. No momento de sair da posição, inspire subindo o tronco, pressionando com firmeza o calcanhar esquerdo em direcção ao chão.
Troque a posição dos pés e faça a postura para o lado contrário, da mesma forma e com a mesma permanência.''')
                                    tp(1)
                                    print('-------------------------------------------------------------------------------------------------------------------------')

                                elif exSobrePeso4 =='4':
                                    print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                    tp(1)
                                    print('''1.  Sente-se com as pernas juntas e esticadas à frente. Apoie as mãos no chão, um pouco atrás da linha da bacia, dedos voltados na direcção
dos pés e pressione as mãos contra o chão.''')
                                    tp(1)
                                    print('2. Incline um pouco o tronco para trás, sentando na zona entre os isquios e o sacro. Mantenha a coluna recta, evitando arredondar as costas.')
                                    tp(1)
                                    print('3. Peito aberto, rodando os ombros para trás. Estique bem a coluna, elevando o topo do esterno.')
                                    tp(1)
                                    print('''4. Dobre as pernas, aproximando as coxas do tronco. Em seguida, tire os pés do chão, elevando as pernas até estarem paralelas ao chão.
Depois, estique as pernas, permanecendo com os dedos dos pés acima da linha do olhar.''')
                                    tp(1)
                                    print('5. Com as pernas esticadas, ou flectidas, tire as mãos do chão, esticando os braços para a frente, junto às coxas, paralelos ao chão.')
                                    tp(1)
                                    print('''6. Inicialmente, faça permanências curtas. À medida que for avançando nas suas práticas, construindo gradualmente a força necessária, aumente a
permanência. Para desfazer a posição, baixe as pernas com uma expiração.''')
                                    tp(1)
                                    print('------------------------------------------------------------------------------------------------------------------------')

                                elif exSobrePeso4 =='5':
                                    print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                    tp(1)
                                    print('1. Sente-se confortavelmente no chão e cruze uma canela em frente a outra. Os joelhos estão sobre os tornozelos.')
                                    tp(1)
                                    print('2. Depois que você encontrou os seus ísquios, puxe a pele dos seus glúteos para trás e sente sobre os ísquios.')
                                    tp(1)
                                    print('''Empurre os ísquios para baixo na direção do chão, perceba como isso alonga a coluna e faz espaço em todo o tronco.
3. Traga o abdômen para dentro e para cima.''')
                                    tp(1)
                                    print('''4. Gire os ombros para cima, para trás e para baixo, quando faz isso sinta que as escápulas se movem para dentro das costas
e para baixo na direção do chão. Isso relaxa os ombros e abre o peito.  Pescoço sempre longo.''')
                                    tp(1)
                                    print('''5. Deixe seus braços semi flexionados, cotovelos na direção do tronco e apoie o topo das mãos sobre as coxas.
Vc pode também apoiar suas mãos sobre os joelhos mas sem pressioná-los para baixo.''')
                                    tp(1)
                                    print('''6. As palmas podem ficar viradas para baixo ou para cima, ainda, se preferir pode fazer o Chin Mudra que significa
o mudra da consciência para isso una o dedo polegar ao indicador''')
                                    tp(1)
                                    print('''7. Relaxe todo o corpo, inclusive a musculatura do rosto, mantenha o foco na sua respiração nasal, feche os olhos
e fique nessa postura por pelo menos 5 respirações lentas e longas.''')
                                    tp(1)
                                    print('----------------------------------------------------------------------------------------------------------------------')

                                else:
                                    print('Número digitado inválido. Digite 1, 2, 3, 4, ou 5.')
                            elif exSobrePeso == '5':
                                print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                tp(1)
                                print('1. Escolher o melhor percurso: Deve-se optar por correr na grama, em caminhos de terra planos ou mesmo na esteira e evitar correr no asfalto.')
                                tp(1)
                                print('''2. Calcular as batidas cardíacas: É importante também que seja calculado o máximo de batidas do coração por minuto que acontece no esforço
para que não haja sobrecarga do coração durante o exercício. Para calcular as batidas que o coração deve atingir durante a corrida,
pode-se aplicar a seguinte formula: 208 - (0,7 x idade em anos).Por exemplo, uma pessoa com 30 anos deve calcular: 208 - (0,7 x 30 anos) = 187,
que são o número de batidas por minuto que o coração deve atingir durante a corrida.''')
                                tp(1)
                                print('3. Definir uma meta: É fundamental definir uma distância, que não deve ultrapassar os 5 Km no primeiro mês e, que pode ser aumentada progressivamente.')
                                tp(1)
                                print('4. Respirar corretamente: Ao correr deve-se usar a respiração abdominal, usando o diafragma, inspirando durante 3 passadas e expirando durante 2 passadas.')
                                tp(1)
                                print('-------------------------------------------------------------------------------------------------------------------------')
                            elif exSobrePeso == '6':
                                break
                            else:
                                print('Número digitado inválido. Digite 1, 2, 3, 4, 5 ou 6.')
                        elif escolha == '2':
                            print('---------------------------------------------------------------------------')
                            tp(1)
                            print('-Comer 3 a frutas diariamente;')
                            tp(1)
                            print('-Colocar metade do prato com legumes e vegetais ou os comer antes da refeição principal;')
                            tp(1)
                            print('-Sua fonte de carboidrato deve ser só uma por refeição, as opções são: macarrão integral, batata doce ou arroz integral;')
                            tp(1)
                            print('-Para complementar escolha entre feijão, milho, ervilha, grão de bico ou soja (uma colher de sopa por refeição);')
                            tp(1)
                            print('-Retire todas as gorduras das carnes antes de as preparar.')
                            tp(1)
                            print('-Açúcar: esqueça doces, sobremeses, bolos, chocolates;')
                            tp(1)
                            print('-Sal: em carnes, temperos, molhos, sopas, etc;')
                            tp(1)
                            print('-Farinha de trigo branca presente em pães, salgadinhos, bolos;')
                            tp(1)
                            print('-Gorduras presente em frituras, carne vermelha, carne de porco, queijos amarelos;')
                            tp(1)
                            print('-Produtos industrializados como pizzas congeladas, comida pronta, sucos de caixinha e refrigerante.')
                            tp(1)
                            print('----------------------------------------------------------------------------')
                            tp(1)
                            break
                elif situacao == 'Obesidade grau 1' or 'Obesidade grau 2' or 'Obesidade Grau 3(Mórbida)':
                    while True:
                        if escolha == '1':
                            print('\n\033[34m'+'IMPORTANTE: '+'\033[0;0mAntes de começar a fazer qualquer treinamento, é fundamental para qualquer pessoa se submeter a uma avaliação médica\n'+
                                  'para se certificar de que está apto a praticar esse tipo de treino e saber em que nível de intensidade pode iniciar.')
                            print('\n\n\033[34m'+'Exercícios recomendados:'+'\033[0;0m\n')
                            tp(1)
                            print('[1]Caminhada')
                            print('[2]Subir escada')
                            print('[3]Hidroginástica')
                            print('[4]Zumba')
                            print('[5]Musculação')
                            tp(1)
                            exObesidade = input('\n\033[34m'+'Digite o número respectivo do exercício'+'\033[0;0m para ter\nmais informações sobre o mesmo ou digite 6 para sair: ')
                            if exObesidade =='1':
                                print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                tp(1)
                                print('1. correr em zigue-zague de uma ponta a outra na piscina. Em seguida, correr diretamente em todas as correntes que acabou de criar.')
                                tp(1)
                                print('''2. É necessário que a corrida seja feita com um alinhamento apropriado do corpo, em que as orelhas, os ombros e os quadris estejam
em uma linha vertical, para que o core (musculatura localizada ao redor de toda a região do tronco, na linha da coluna lombar),
e não os ombros ou pernas, seja responsável por te manter ereto.''')
                                tp(1)
                                print('------------------------------------------------------------------------------------------------------------------------')

                            elif exObesidade =='2':
                                print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                tp(1)
                                print('1. Fique próximo(a) ao corrimão para se segurar caso sinta tontura ou mal-estar.')
                                tp(1)
                                print('2. Suba um degrau de cada vez.')
                                tp(1)
                                print('3.Não corra nas escadas enquanto não tiver preparo físico.')
                                tp(1)
                                print('4.Não pratique com volumes nas mãos.')
                                tp(1)
                                print('5.Não pratique em escadas com pisos escorregadios.')
                                tp(1)
                                print('-------------------------------------------------------------------------------------------------------------------------')
                                tp(1)

                            elif exObesidade =='3':
                                print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                tp(1)
                                print('1. Comece lentamente. O objetivo é despertar os seus músculos, mas certifique-se de guardar energia para o próximo passo.')
                                tp(1)
                                print('2. Durante dois minutos, dentro da água, caminhe pela piscina em um ritmo rápido.')
                                tp(1)
                                print('''3. Levante os joelhos até o seu peito, um por vez, com os braços estendidos para o chão. Lembre-se de manter suas costas retas.
(Faça duas séries de 20 movimentos com um intervalo de 5 segundos entre cada uma).''')
                                tp(1)
                                print('''4. Execute um movimento chamado de “tesoura”. Com as mãos nos quadris, alterne movimentos dos quadris para ambos os lados.
(Duas séries de 20 repetições em cada lado com um descanso de 5 segundos entre cada série).''')
                                tp(1)
                                print('''5.Afaste suas pernas e pule para aproximá-las novamente. Não seja muito rígido com suas pernas, mantenha seus joelhos soltos.
Coloque seus braços nos quadris ou atrás, nas costas.(Duas séries de 20 repetições, com um descanso de 5 segundos).''')
                                tp(1)
                                print('-----------------------------------------------------------------------------------------------------------------------')
                                tp(1)

                            elif exObesidade =='4':
                                print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                tp(1)
                                print('1. Cave seu calcanhar direito no chão. Passo para trás. Cave seu dedo do pé direito no chão.')
                                tp(1)
                                print('''2. Viaje para a esquerda. Use os dois pés para viajar. Dê pequenos passos com o pé direito.
Mova-se mais com cada escavação frontal. Continue cavando para frente e para trás.''')
                                tp(1)
                                print('3.Volte para o meio.')
                                tp(1)
                                print('4. Repita o passo 1. Desta vez, cave o seu calcanhar esquerdo. Cave seu dedo do pé direito.')
                                tp(1)
                                print('5. Repetir o passo 2. Desta vez, viajar para a direita.')
                                tp(1)
                                print('6. Volte para o meio. ')
                                tp(1)
                                print('''7. Tente mais rápido. Escava frente e verso rapidamente. Solte seus ombros. Deixe seus braços caírem.
Coloque-os nos quadris se parecer estranho. Permita que seus quadris te movam.''')
                                tp(1)
                                print('-------------------------------------------------------------------------------------------------------------------------')

                            elif exObesidade =='5':
                                print('----------------------------------------------\033[34m'+'Siga os passos abaixo'+'\033[0;0m-----------------------------------------------------')
                                tp(1)
                                print('1. O indicado são pelo menos de 3 a 4 treinos na semana.')
                                tp(1)
                                print('2. Foco em exercícios multiarticulares.')
                                tp(1)
                                print('3. Volume total e intervalos de descanso equilibrados, ou seja, mais repetições e menos carga.')
                                tp(1)
                                print('4. Se possível, integre a musculação com aeróbico ao final da sessão')
                                tp(1)
                                print('5. evite exercícios com mais impacto')
                                tp(1)
                                print('------------------------------------------------------------------------------------------------------------------------')

                            elif exObesidade =='6':
                                break
                            else:
                                print('Número digitado inválido. Digite 1, 2, 3, 4, 5 ou 6.')
                        elif escolha == '2':
                            print('---------------------------------------------------------------------------')
                            tp(1)
                            print('-Azeite de oliva, óleos de canola, girassol, soja ou milho, margarinas light;')
                            tp(1)
                            print('-Leite e iogurte desnatados, queijos magros frescos: cottage ou ricota;')
                            tp(1)
                            print('-Pães integrais, pão light;')
                            tp(1)
                            print('-Massas confeccionadas sem molhos gordurosos, biscoitos tipo água e sal ou maizena, bolos sem recheios;')
                            tp(1)
                            print('-Carnes brancas (frango sem pele e peixe) frios (presunto magro, peito de peru);')
                            tp(1)
                            print('-Assados, grelhados e cozidos(evitar frituras);')
                            tp(1)
                            print('-Sucos naturais sem açucar.')
                            tp(1)
                            print('-----------------------------------------------------------------------------')
                            break
        else:
            print('\nOpção inválida!\n')
    if (ExAbaixoPeso == "5") or (exPesoIdeal == "8") or (exSobrePeso == "6") or (exObesidade == "6"):
        print('\n\033[34m'+'Deseja fazer um novo cálculo?'+'\033[0;0m\n')
        novoCalculo = input('1 - Sim\n2 - Não\n\n\033[34m'+'Digite: '+'\033[0;0m').upper()
        if novoCalculo in sair:
            break
        else:
            print('\nTudo bem!\n')
    else:
        print('\n\033[34m'+'Deseja fazer um novo cálculo?'+'\033[0;0m\n')
        novoCalculo = input('1 - Sim\n2 - Não\n\n\033[34m'+'Digite: '+'\033[0;0m').upper()
        if novoCalculo in sair:
            break
        else:
            print('\nTudo bem!\n')

#Linha final do codigo que retorna só onde está salvo o arquivo com o nome, altura, peso e IMC da pessoa após a execução do programa.
print(f'\n\033[34m'+'SEUS DADOS ESTAO SALVOS EM:'+'\033[0;0m\n'
      f'{local}')
