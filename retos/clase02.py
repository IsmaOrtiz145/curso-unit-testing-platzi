"""Reto clase 02"""
def calculate_total(products):
    """Realiza el calculo de todos los precios
    con el descuento correspondiente"""
    total = 0
    for product in products:
        discount_total = product['price'] * (product['discount'] / 100)
        total += discount_total

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
            'price': 100,
            'discount' : 50
        }
    ]
    assert calculate_total(products) == 50

def test_calculate_total_with_multiple_product():
    """Verifica que el resultado sea el correcto"""
    print('prueba multiple')
    products = [
        {
            'name' : 'Notebook',
            'price': 100,
            'discount' : 50
        },
        {
            'name' : 'Table',
            'price': 50,
            'discount' : 50
        }
    ]
    assert calculate_total(products) == 75


if __name__ == '__main__':
    test_calculate_total_with_empty_list()
    test_calculate_total_with_single_product()
    test_calculate_total_with_multiple_product()