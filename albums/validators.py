from datetime import datetime

from django.core.validators import RegexValidator
from django.forms import ValidationError


def validate_text(value):
    language_validator = RegexValidator(
        regex=r'^[A-Za-z0-9А-Яа-яЇїІіЄєҐґ:?!\-\+\(\)\.,ʼ=№#& ]+$',
        message='Text format is not allowed',
    )
    
    try:
        language_validator(value)
    except ValidationError as e:
        raise ValidationError(e.message, code='invalid_text')


def validate_release_date(value):
    if not value.isdigit():
        raise ValidationError('Invalid year: Please enter a valid year.')
    year = int(value)
    current_year = datetime.now().year
    if year < 1900 or year > current_year:
        raise ValidationError(f'Invalid year: The year must be between 1900 and {current_year}.')


