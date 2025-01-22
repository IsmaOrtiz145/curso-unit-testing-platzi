# Clase 2 
""""
ESTE TIRA UN ERROR POR EL *
def calculate_total(products):
     total = 0
     for product in products:
         total *= product['price']
     return total
"""

def calculate_total(products):
    """Realiza el calculo de todos los precios"""
    total = 0
    for product in products:
        total += product['price']

    return total

def test_calculate_total_with_empty_list():
    """Verifica que el resultado sea el correcto"""
    print('prueba empty')
    assert calculate_total([]) == 0

def test_calculate_total_with_single_product():
    """Verifica que el resultado sea el correcto
    si ponemos == 10, tira un error"""
    print('prueba single')
    products = [
        {
            'name' : 'Notebook',
            'price': 5
        }
    ]
    assert calculate_total(products) == 5

def test_calculate_total_with_multiple_product():
    """Verifica que el resultado sea el correcto"""
    print('prueba multiple')
    products = [
        {
            'name' : 'Notebook',
            'price': 10
        },
        {
            'name' : 'Table',
            'price': 2
        }
    ]
    assert calculate_total(products) == 12


if __name__ == '__main__':
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product()
