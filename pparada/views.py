from django.shortcuts import render
from django.urls import reverse_lazy
from .models import paradasegura, passagemmodel
from .forms import paradaForm,PassagemModelForm
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.utils import timezone
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from .models import paradasegura

class paradaCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = paradasegura
    template_name = 'parada_create.html'
    form_class = paradaForm
    success_url = reverse_lazy('paradaseguraform')
    permission_required = "parada.add_paradasegura"

class passagemCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = passagemmodel
    template_name = 'passagem.html'
    form_class = PassagemModelForm
    success_url = reverse_lazy('passagemCreateView')
    permission_required = "parada.add_paradasegura"

    


from django.views.generic import ListView
from .models import passagemmodel

class PassagemListView(ListView):
    model = passagemmodel
    template_name = 'historico_passagem.html'
    context_object_name = 'passagens'
    paginate_by = 10  # Defina quantas entradas por página você deseja

    def get_queryset(self):
        return passagemmodel.objects.all().order_by('-data_criacao') 


from django.db.models import Q

class historicoListView(ListView):
    model = paradasegura
    template_name = 'historico_paradas.html'
    context_object_name = 'pa'
    paginate_by = 10  # Quantas entradas por página

    def get_queryset(self):
        queryset = paradasegura.objects.all().order_by('-data_criacao')
        
        # Filtrar pelo parâmetro 'embarcador' se estiver presente na URL
        embarcador = self.request.GET.get('embarcador')
        if embarcador:
            queryset = queryset.filter(embarcador__icontains=embarcador)

        return queryset
    


from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

class Parada2DetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = paradasegura
    template_name = 'parada_detail2.html'
    context_object_name = 'parada'
    permission_required = "requisicao.change_requisicoes"

    


from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView
from .models import paradasegura

class paradaListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = paradasegura
    template_name = 'pa_list.html'
    context_object_name = 'pa'
    paginate_by = 12
    permission_required = 'parada.view_paradasegura'

    def get_queryset(self):
        # Obter todos os objetos de paradasegura cujo status seja "Aguardando"
        queryset = paradasegura.objects.filter(status='AGUARDANDO').order_by('-id')

        # Obter o valor do campo 'embarcador' do request GET
        embarcador = self.request.GET.get('embarcador', None)

        # Filtrar pelo campo 'embarcador' se houver valor fornecido
        if embarcador:
            queryset = queryset.filter(Q(embarcador__icontains=embarcador))

        return queryset

class RegistrarSaidaView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = 'parada.change_paradasegura'

    def get(self, request, pk, *args, **kwargs):
        parada = get_object_or_404(paradasegura, pk=pk)

        # Atualizar o status para 'EM VIAGEM' e definir a data de saída
        parada.status = 'EM VIAGEM'
        parada.saida = timezone.now()
        parada.save()

        # Redirecionar de volta para a lista de paradas
        return redirect('paradaseguralist')
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import paradasegura

class ParadaDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = paradasegura
    template_name = 'parada_detail.html'
    context_object_name = 'parada'
    permission_required = "requisicao.change_requisicoes"



from django.http import JsonResponse

def get_choices(request):
    tipo_posto = request.GET.get('tipo_posto')
    print(f'Tipo de posto: {tipo_posto}')  # Debugging
    response_data = {
        'iscas': [],
        'cadeados': [],
        'pa': []
    }

    if tipo_posto:
        if tipo_posto in paradasegura.POSTOS_INFO1:
            iscas = paradasegura.POSTOS_INFO1[tipo_posto].get('iscas', [])
            cadeados = paradasegura.POSTOS_INFO1[tipo_posto].get('cadeados', [])
            response_data['iscas'] = iscas
            response_data['cadeados'] = cadeados
            print(f'Iscas: {iscas}, Cadeados: {cadeados}')  # Debugging

        if tipo_posto in paradasegura.POSTOS_INFO2:
            pa = paradasegura.POSTOS_INFO2[tipo_posto].get('pa', [])
            response_data['pa'] = pa
            print(f'PA: {pa}')
    return JsonResponse(response_data)

def get_pa_choices(request):
    tipo_posto = request.GET.get('tipo_posto')
    print(f'Tipo de posto: {tipo_posto}')  # Debugging
    if tipo_posto and tipo_posto in passagemmodel.POSTOS_INFO2:
        pa = passagemmodel.POSTOS_INFO2[tipo_posto]['pa']
        print(f'PA: {pa}')  # Debugging
        return JsonResponse({
            'pa': pa,
        })
    return JsonResponse({'pa': []})