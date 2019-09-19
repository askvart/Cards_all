class BaseValidationError(ValueError):
    pass

class NameTooShortError(BaseValidationError):
    pass

def validate(name):
    if len(name) < 10:
        raise NameTooShortError(name)

try:
    validate('Jpo')
except BaseValidationError as err:
    handle_validation_error(err)
