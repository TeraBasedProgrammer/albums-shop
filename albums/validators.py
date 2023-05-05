import os
import json

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

