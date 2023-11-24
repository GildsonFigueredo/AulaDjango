from django.shortcuts import render, get_object_or_404, redirect
from .models import usuario
from .forms import usuarioForm

# Create your views here.

def home(request):
#renderizar a página inicial.
    return render(request,'home.html')

#função para salvar os dados no banco de dados
def cadastro(request):
        form = usuarioForm(request.POST)
        if form.is_valid():
             novo_usuario = form.save()
             form = usuarioForm()
        
        context ={
             'form':form
        }
        return render (request, 'cadastro.html',{'form':form})

def listagem_usuarios(request):
    usuarios = usuario.objects.all()
    return render (request, 'listagem.html',{'usuarios': usuarios})

def excluir_usuario(request, id):
    usuarios = get_object_or_404(usuario, pk=id)
    if request.method == 'GET':
        usuarios.delete()
        return redirect(listagem_usuarios)
    
def atualizar_usuarios(request, id):
    usuarios = get_object_or_404(usuario, pk=id)
    if request.method == 'POST':
        form = usuarioForm(request.POST, instance=usuarios)
        if form.is_valid():
            form.save()
            return redirect(listagem_usuarios)
    else:
        form = usuarioForm(instance=usuarios)
    return render(request, 'atualizacao.html', {'form': form})    
