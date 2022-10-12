from django.core.exceptions import ValidationError

def contains_special_charater(pw):
    special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
    if not any(char in special_characters for char in pw):
        return False
    else:
        return True

def contains_number(pw):
    if not any(char.isdigit() for char in pw):
        return False
    else:
        return True


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
