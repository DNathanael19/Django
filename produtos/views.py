from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ver_produto(request):
    if request.method == "GET":
        return render(request, 'ver_produto.html', {'nome':'diego'})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        print(f'Seu nome é {nome}')
        print(f'Sua idade é {idade}')
        return HttpResponse('Fui chamado')

def inserir_produto(request):
    return HttpResponse('Estou no ver')