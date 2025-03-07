from django import forms

class Emprestimo_form(forms.Form):
    renda = forms.DecimalField(label='Renda anual R$', max_digits=8, decimal_places=2)
    emprestimo =  forms.DecimalField(label='Empréstimo desejado',max_digits=8, decimal_places=2)