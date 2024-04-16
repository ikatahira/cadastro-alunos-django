from django.urls import path
from alunos import views

urlpatterns = [
    
    path('cadastrar/', views.cadastrar_aluno, name='cadastrar_aluno'),
]
