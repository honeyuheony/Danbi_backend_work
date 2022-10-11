import string
from django.core.exceptions import ValidationError

def contains_special_charater(pw):
    for c in pw:
        if c in string.punctuation:
            return True
    return False

def contains_number(pw):
    for c in pw:
        if c.isdigit():
            return True
    return False


class CustomPasswordValidator:
    def validate(self, password, user=None):
        if (
            len(password) < 8 or
            not contains_number(password) or
            not contains_special_charater(password)
        ):
            raise ValidationError("8자 이상의 숫자와 특수문자가 포함된 조합을 입력해주세요.")
    
    def get_help_text(self):
        return "8자 이상의 숫자와 특수문자가 포함된 조합을 입력해주세요."
