# decorators/product_repository

from repositories.factories import create_products_repository

def get_products_repository(route_handler_func):
    def wrapper(*args, **kwargs):

        #avataan tietokantayhteys tässä
        with sqlite3.connect('tuntiharjoitus1.db') as con:

            # annetan con-muuttuja factorylle parametrina
            users_repository = create_products_repository(con)
            
            return route_handler_func(products_repository, *args, **kwargs)
        #muista wrapper funktio pitää palauttaa dekoraattorin lopussa ilman sulkuja
        return wrapper 