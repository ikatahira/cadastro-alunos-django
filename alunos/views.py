# alunos/views.py

from django.shortcuts import render, redirect
from .forms import AlunoForm
from .models import Aluno

def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlunoForm()
    return render(request, 'alunos/cadastrar_aluno.html', {'form': form})
