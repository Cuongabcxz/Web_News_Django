# authentication/validators.py
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                'Mật khẩu phải chứa một chữ cái', code='password_no_letters')

    def get_help_text(self):
        return 'Your password must contain at least one upper or lower case letter.'


class UppercaseValidator(object):

    '''The password must contain at least 1 uppercase letter, A-Z.'''

    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _("Mật khẩu phải chứa ít nhất 1 chữ cái viết hoa, A-Z."),
                code='password_no_upper',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 uppercase letter, A-Z."
        )


class SpecialCharValidator(object):

    ''' The password must contain at least 1 special character @#$%!^&* '''

    def validate(self, password, user=None):
        if not re.findall('[@#$%!^&*]', password):
            raise ValidationError(
                _("Mật khẩu của bạn phải chứa ít nhất 1 ký tự đặc biệt: " +
                  "@#$%!^&*"),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _(
            "Mật khẩu của bạn phải chứa ít nhất 1 ký tự đặc biệt: " +
            "@#$%!^&*"
        )