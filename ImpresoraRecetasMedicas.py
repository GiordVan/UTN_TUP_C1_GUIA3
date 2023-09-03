def datos_clinica():
    print('####################')
    print('~~~~~ CLINICA UTN ~~~~~')
    print('Av. Universidad 450, X5900 Villa María, Córdoba')


def datos_paciente(a, b):
    print('####################')
    print('Nombre del paciente: ', a)
    print('Fecha de naciemiento: ', b)


def datos_medicamento(a, b, c):
    print('####################')
    print('Nombre del medicamento: ', a)
    print('Dosis: ', b)
    print('Instrucciones de uso: ', c)


nombreP = input('Ingrese el nombre del paciente: ')
fechaP = input('Ingrese la fecha de nacimiento del paciente: ')
nombreM = input('Ingrese el nombre del medicamento: ')
dosisM = input('Ingrese la dosis a tomar del medicamento: ')
instruccionesM = input('Ingrese las instrucciones de uso del medicamento: ')
print('\n')
datos_clinica()
datos_paciente(nombreP, fechaP)
datos_medicamento(nombreM, dosisM, instruccionesM)
print('####################')
