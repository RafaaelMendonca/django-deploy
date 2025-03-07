from django.shortcuts import render
from .forms import Emprestimo_form
from .utils import carregar_modelo

#a funcao esta no utils.py
modelo = carregar_modelo()

def view_formulario(request):
    resultado = None
    if request.method == 'POST':
        form = Emprestimo_form(request.POST)
        if form.is_valid(): #veerifica se o forms está valido com os campos preenchidos
            renda = form.cleaned_data['renda']
            emprestimo = form.cleaned_data['emprestimo']

            previsao = modelo.predict([[renda, emprestimo]])[0] #faz a previsao

            resultado = 'Aprovado' if previsao == 0 else 'negado'
    else:
        form = Emprestimo_form()

    return render(request, "emprestimo.html", {"form": form, "resultado": resultado})
