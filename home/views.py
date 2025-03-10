from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Dispositivos

# View para a página inicial
def home(request):
    if request.method == "GET":
        return render(request, 'home.html')
    else:
        query = request.POST.get('search_query')
        return redirect('selecao', query=query)

# View para a página de seleção
def selecao(request, query):
    try:
        dispositivo = Dispositivos.objects.get(id_tombamento=query)
        return render(request, 'selecao.html', {'dispositivo': dispositivo})
    except Dispositivos.DoesNotExist:
        return render(request, '404.html', status=404)

# View para a página de cadastro de computadores
def cadpc(request):
    if request.method == "POST":
        id_tombamento = request.POST.get('id_tombamento')
        marca = request.POST.get('marca')
        qnt_ram = request.POST.get('qnt_ram')
        qnt_armaz = request.POST.get('qnt_armaz')
        tipo_armaz = request.POST.get('tipo_armaz')
        funcionando = request.POST.get('funcionando')
        locat_do_disp = request.POST.get('locat_do_disp')
        descricao = request.POST.get('descricao')
        data_de_an = request.POST.get('data_de_an')

        dispositivo = Dispositivos(
            id_tombamento=id_tombamento,
            marca=marca,
            qnt_ram=qnt_ram,
            qnt_armaz=qnt_armaz,
            tipo_armaz=tipo_armaz,
            funcionando=funcionando,
            locat_do_disp=locat_do_disp,
            descricao=descricao,
            data_de_an=data_de_an
        )
        dispositivo.save()
        return HttpResponse(f'Dispositivo {id_tombamento} cadastrado com sucesso!')
    else:
        return render(request, 'cadpc.html')

# View para a página de cadastro de outros dispositivos
def cadother(request):
    if request.method == "POST":
        id_tombamento = request.POST.get('id_tombamento')
        marca = request.POST.get('marca')
        funcionando = request.POST.get('funcionando')
        locat_do_disp = request.POST.get('locat_do_disp')
        descricao = request.POST.get('descricao')
        data_de_an = request.POST.get('data_de_an')

        dispositivo = Dispositivos(
            id_tombamento=id_tombamento,
            marca=marca,
            funcionando=funcionando,
            locat_do_disp=locat_do_disp,
            descricao=descricao,
            data_de_an=data_de_an
        )
        dispositivo.save()
        return HttpResponse(f'Dispositivo {id_tombamento} cadastrado com sucesso!')
    else:
        return render(request, 'cadother.html')