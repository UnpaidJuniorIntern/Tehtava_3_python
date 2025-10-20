# decorators/user_repository

from repositories.factories import create_users_repository

def get_users_repository(route_handler_func):
    def wrapper(*args, **kwargs):
        # käytetään tässä vanhaa jo käytössä olevaa create_users_repository-factorya
        users_repository = create_users_repository()
        # palautetaan nyt route_handler_func mukanaan users_repository
        return route_handler_func(users_repository, *args, **kwargs)
    # muista wrapper funktio pitää palauttaa dekoraattorin lopussa, mutta ilman sulkuja
    return wrapper