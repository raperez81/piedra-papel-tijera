import random
import time

# Retorna un string con la seleccion de la computadora: piedra, papel o tijera
# la opcion es generada aleatoriamente con la funcion random.randrange


def elegir_pc():
    opcion_pc = random.randrange(0, 3)
    if opcion_pc == 0:
        return 'piedra'
    elif opcion_pc == 1:
        return 'papel'
    elif opcion_pc == 2:
        return 'tijera'
    else:
        pass

# Evalua si el jugador ha ganado contra la computadora
# Recibe dos strings que deben tener uno de los siguientes valores: piedra, papel o tijera
# Retorna 'jugador' si el jugador gana; 'pc' si gana la computadora; 'empate' si fue un empate


def evaluar_ganador(opcion_jugador, opcion_pc):
    if opcion_jugador == opcion_pc:
        return 'empate'
    elif(opcion_jugador == 'piedra' and opcion_pc == 'tijera') or (opcion_jugador == 'papel' and opcion_pc == 'piedra') or (opcion_jugador == 'tijera' and opcion_pc == 'papel'):
        return 'jugador'
    else:
        return 'pc'


# Evalua si el parametro opcion es una opcion válida
def es_opcion_valida(opcion):
    if opcion == 'piedra' or opcion == 'papel' or opcion == 'tijera':
        return True
    else:
        return False


def run():
    # Declaracion de variables
    puntaje_jugador, puntaje_pc = 0, 0
    opcion_valida = False
    nombre_jugador = ''
    opcion_jugador = ''
    quien_gana = ''
    partida = 0
    jugar = 'SI'

    print('*********************************')
    print('***** PIEDRA PAPEL O TIJERA *****')
    print('*********************************')
    nombre_jugador = input('\nCual es tu nombre: ')
    while jugar == 'SI':
        # Solicitar opcion del usuario, si el string ingresado no es válido, lo solicita de nuevo
        # Si es una opción válida continua el juego
        opcion_valida = False
        partida += 1
        print ('\n\n*********** Ronda ' + str(partida) + ' ***********')
        while opcion_valida == False:
            opcion_jugador = input('\nEscribe piedra, papel o tijera: ')
            opcion_valida = es_opcion_valida(opcion_jugador)
            if not opcion_valida:
                print('⚠ ' + opcion_jugador + ' no es una opción válida')
        time.sleep(1)
        opcion_pc = elegir_pc()
        print('\nLa computadora escogió: ' + opcion_pc)

        quien_gana = evaluar_ganador(opcion_jugador, opcion_pc)
        if quien_gana == 'jugador':
            puntaje_jugador += 1
            print('\nGanaste!!!')
        elif quien_gana == 'empate':
            print('\nEmpate')
        else:
            puntaje_pc += 1
            print('\nPerdiste :(')

        time.sleep(1)
        print('\n   ********* Puntuacion *********')
        print('   ' + nombre_jugador + ': ' + str(puntaje_jugador) +
              '    Computadora: ' + str(puntaje_pc))
        time.sleep(1)
        jugar = input('\n¿Quieres jugar de nuevo? Escribe si o no: ')
        # asigna falso para que en el  primer while se solicite al usuario su opcion
        opcion_valida = False
        while opcion_valida == False:
            # quitando espacios y convirtiendo respuesta a mayusculas
            jugar = jugar.strip()
            # print('quitando espacios y convirtiendo respuesta a mayusculas: ' + jugar)
            jugar = jugar.upper()
            if jugar == 'SI':
                opcion_valida = True
            elif jugar == 'NO':
                print('Hasta pronto ' + nombre_jugador + '!!!')
                break
            else:
                jugar = print(
                    'Tu respuesta no es una opción válida. Escribe si o no: ')

        """count_0, count_1, count_2 = 0, 0, 0
    for i in range(10):
        opcion_pc = random.randrange(0, 3)
        # print(opcion_pc)
        if opcion_pc == 0:
            count_0 += 1
        elif opcion_pc == 1:
            count_1 += 1
        elif opcion_pc == 2:
            count_2 += 1
        else:
            pass
    print('0: ' + str(count_0))
    print('1: ' + str(count_1))
    print('2: ' + str(count_2)) """


if __name__ == '__main__':
    run()
