
'''
Altere a solução do exercício anterior para que, caso o usuário i nforme algum valor i ncorreto que
provoque erro de execução, seja exibida uma mensagem de erro ao usuário e o valor seja
solicitado novamente, até que o valor informado esteja correto.
'''
repetir = True

while repetir == True:
    try:
        x = int(input('Primeiro valor:'))
        y = int(input('Segundo valor:'))
        z = x / y
        print('O resultado da divisão é:', z)
    except ZeroDivisionError:
        print('Ocorreu uma divisão por zero.')
    except ValueError:
        print('Ocorreu um erro de conversão de tipos. O valor deve ser inteiro.')
    except Exception:
        print('Ocorreu um erro inesperado.')
    else:
        print('Programa finalizado com sucesso')
        repetir = False