#este archivo se utiliza para que se puede ejecutar el paquete utilizando unicamente el nombre
# python -m pack_cfacilito
# -m ejecuta por nombre de paquete

from pack_cfacilito import unreleased

if __name__ == '__main__':
    print('>>> Comienza ejecucion desde dentro de __main__.py\n')
    workshops = unreleased()
    print(workshops)
    print('\n>>> Finaliza ejecucion desde dentro de __main__.py')