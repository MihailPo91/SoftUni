from django.core.exceptions import ValidationError


def validate_if_value_contains_only_nums_chars_and_underscore(value: str):
    error = False
    for ch in value:
        if not ch.isalpha() and not ch.isdigit() and ch not in '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


def validate_value_is_above_zero(value: int):
    if value < 0:
        raise ValidationError
