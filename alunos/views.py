from django.shortcuts import render, redirect
from .forms import AlunoForm

def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirecionar para a página inicial após o cadastro
    else:
        form = AlunoForm()
    return render(request, 'cadastrar_aluno.html', {'form': form})
