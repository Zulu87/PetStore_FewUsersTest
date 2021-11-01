import yaml


def config_setter(file_to_open):
    with open(file_to_open, 'r') as file:
        configs = yaml.load(file, Loader=yaml.FullLoader)

        return configs
