# w plikach typu service, przechowuje sie metody ktore maja za zadanie np pobrac jakies dane z repo, wykonac jakas logike i zwrocic odpowiednio przetworzone dane

from repository import contributorRepository


def get_all_contributors():
    contributorRepository.initiate_db()
    return contributorRepository.get_all_contributors()
    contributorRepository.drop_table()
