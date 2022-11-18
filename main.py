
#cuando se inicializa el modulo en el __init__.py, acá ya no hace falta llamarlo {workshops}
# se hace referencia al paquete principal {pack_cfacilito}
from pack_cfacilito import unreleased

if __name__ == '__main__':
    print('Estamos dentro de main.py')
    workshops = unreleased()
    print(workshops)
