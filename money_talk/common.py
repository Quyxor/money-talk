import os.path as path


def get_path_resourses(resourse):
    return path.join(path.dirname(__file__), 'resourses', resourse)


def dict_unpack(pack):
    return (pack.get('date'), pack.get('amount'), pack.get('owner'), pack.get('source'))