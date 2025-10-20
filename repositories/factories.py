
# repositories/factories.py

from repositories.users_sqlite_repository import UsersSQLiteRepository
from repositories.products_sqlite_repository import ProductsSQLiteRepository

# pythonin tapauksessa voidaan luoda jokaiselle repositoriolle oma
# funktio, jota kutsutaan controllerissa
def create_users_repository(con):
    # jos repositorio muuttuu tietokannan vaihtuessa,
    # muutos voidaan tehdä vain tänne yhteen paikkaan
    # ja kaikki controllerit, joissa usersRepositorya tarvitaan
    # käyttävät palautettavaa instanssia
    
    return UsersSQLiteRepository(con)

def create_products_repository(con):

    return ProductsSQLiteRepository(con)