from django.db import models


def get_valid_fields():
    props = dir(models)
    options = list()
    for prop in props:
        try:
            if issubclass(getattr(models, prop), models.Field):
                options.append(prop)
        except Exception as e:
            pass
    return options

choice_fields = [(o, o) for o in get_valid_fields()]


__all__ = [
    'get_valid_fields',
    'choice_fields',
]