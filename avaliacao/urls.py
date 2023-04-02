from django.urls import path

from .views import alunoCreateView, alunoListView, alunoUpdateView, alunoDetailView
from .views import avaliacaoCreateView, avaliacaoListView, avaliacaoUpdateView, avaliacaoDetailView
from .views import treinoCreateView, treinoListView, treinoDetailView, treinoUpdateView, PDFtreinoDetailView
from .views import fichaCreateView, fichaListView, fichaUpdateView, fichaDetailView


urlpatterns = [
    path('aluno', alunoCreateView.as_view(), name="cadastrar_aluno"),
    path('lista/aluno', alunoListView.as_view(), name="lista_aluno"),
    path('atualizar/aluno/<int:pk>', alunoUpdateView.as_view(), name="editar_aluno"),
    path('detalhar/aluno/<int:pk>', alunoDetailView.as_view(), name="detalhar_aluno"),


    path('avaliacao', avaliacaoCreateView.as_view(), name="cadastrar_avaliacao"),
    path('lista/avaliacao', avaliacaoListView.as_view(), name="lista_avaliacao"),
    path('atualizar/avaliacao/<int:pk>', avaliacaoUpdateView.as_view(), name="editar_avaliacao"),
    path('detalhar/avaliacao/<int:pk>', avaliacaoDetailView.as_view(), name="detalhar_avaliacao"),


    path('treino', treinoCreateView.as_view(), name="cadastrar_treino"),
    path('lista/treino', treinoListView.as_view(), name="lista_treino"),
    path('atualizar/treino/<int:pk>', treinoUpdateView.as_view(), name="editar_treino"),
    path('detalhar/treino/<int:pk>', treinoDetailView.as_view(), name="detalhar_treino"),
    path('treino/imprimir/<int:pk>', PDFtreinoDetailView.as_view(), name="pdf_treino"),


    path('ficha', fichaCreateView.as_view(), name="cadastrar_ficha"),
    path('lista/ficha', fichaListView.as_view(), name="lista_ficha"),
    path('atualizar/ficha/<int:pk>', fichaUpdateView.as_view(), name="editar_ficha"),
    path('detalhar/ficha/<int:pk>', fichaDetailView.as_view(), name="detalhar_ficha"),
]
