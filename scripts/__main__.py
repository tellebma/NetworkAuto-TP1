import json


def load_json_data_from_file(file_path):
    try:
        with open(file_path) as file:
            data = json.load(file)
    except FileNotFoundError:
        data = "ERREUR"
        print(f"ERREUR | Le fichier {file_path} n'existe pas.")
        exit()
    return data


def load_yaml_data_from_file(file_path):
    """
        A compléter ....
    """
    pass


def render_network_config(template_name, data):
    """
        A compléter ....
    """
    pass


def save_built_config(file_name, data):
    """
        A compléter ....
    """
    pass


if __name__ == "__main__":
    d = load_json_data_from_file("./data/R2.json")
    print(d["hostname"])
