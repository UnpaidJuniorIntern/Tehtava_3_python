# decorators/user_repository

import sqlite3
import functools

from repositories.factories import create_users_repository

def get_users_repository(route_handler_func):
    @functools.wraps(route_handler_func)
    def wrapper(*args, **kwargs):

        #avataan tietokantayhteys tässä
        with sqlite3.connect('tuntiharjoitus1.db') as con:

            # annetan con-muuttuja factorylle parametrina
            users_repository = create_users_repository(con)
            
            return route_handler_func(users_repository, *args, **kwargs)
    #muista wrapper funktio pitää palauttaa dekoraattorin lopussa ilman sulkuja
    return wrapper 