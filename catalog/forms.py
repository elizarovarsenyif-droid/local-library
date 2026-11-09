import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(
        help_text="Укажите дату продления (не более чем на 4 недели)."
    )

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']

        if data < datetime.date.today():
            raise ValidationError(
                _('Дата продления не может быть в прошлом.')
            )

        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(
                _('Дата продления не может быть дальше чем через 4 недели.')
            )

        return data