from repository import contributorRepository

def add_contributors(payload):
    print("Adding new contributors")
    contributorRepository.save_contributors(payload)

def get_all_contributors():
    print(f"Getting all contributors")
    return contributorRepository.get_all_contributors()

def get_contributor_by_name(name):
    print("Getting contributor with name: " + name)
    return contributorRepository.get_contributor_by_name(name)
