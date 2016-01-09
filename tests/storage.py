from alabama import storage

database = {}


def put(model):
    if model.__class__.__name__ in database:
        database[model.__class__.__name__].append(model)
    else:
        database[model.__class__.__name__] = [model]
    return model

storage.put = put


def find(model):
    if model.__class__.__name__ in database:
        return database[model.__class__.__name_]
    else:
        return []

storage.find = find
