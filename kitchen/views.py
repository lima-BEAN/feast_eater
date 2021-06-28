import random
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.forms import inlineformset_factory
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#TODO: Require login to create App in LimaBeanLab Apps section
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required

from kitchen.forms import KitchenForm, FoodForm
from kitchen.models import Kitchen, Food

def home(request):
    return HttpResponse("It works")

#class HomePageView(TemplateView):
#    template_name = "kitchen/home.html"

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['number'] = random.randrange(1, 100)
#        context['latest_kitchen'] = Kitchen.objects.all()[:3]
#        return context

class KitchenListView(ListView):
    model = Kitchen
    context_object_name = 'kitchen'

def KitchenDetailView(request, pk):
    kitchen_obj = get_object_or_404(Kitchen, pk=pk)
    FoodFormSet = inlineformset_factory(Kitchen, Food, fields='__all__',extra=1, max_num=10)
    Form = FoodFormSet(instance=kitchen_obj)
    if request.method == 'POST':
        form = FoodFormSet(request.POST, instance=kitchen_obj)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'kitchen/kitchen_detail.html',{'kitchen': kitchen_obj, 'form': Form,'error': 'Bad data entry'})
        return redirect('kitchen:kitchen_detail', pk=kitchen_obj.id)
    return render(request, 'kitchen/kitchen_detail.html',{'kitchen': kitchen_obj, 'form': Form})

    # model = Kitchen
    # extra_context = {'Food': Food.objects.all()}

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['kitchen_list'] = Kitchen.objects.all()
    #     return context

# class KitchenCreateView(CreateView):
#     model = Kitchen
#     fields = ['name', 'open_time', 'close_time']
#     template_name = 'kitchen/kitchen_create.html'
#     success_url = reverse_lazy('kitchen:index')
#     #TODO: # login_url = '/login/'
def KitchenCreateView(request):
    form = KitchenForm()
    # FoodFormSet = inlineformset_factory(Kitchen, Food, fields=('name','diet','price'),extra=5, max_num=5)
    if request.method == 'POST':
        form = KitchenForm(request.POST)
        if form.is_valid():
            k_instance = Kitchen.objects.create(
                name=form.cleaned_data.get('k_name'),
                open_time=form.cleaned_data.get('open_time'),
                close_time=form.cleaned_data.get('close_time'),
                image=form.cleaned_data.get('image'),
                working_days=form.cleaned_data.get('working_days'),
            )
            k_instance.save()
            # foodForm = FoodFormSet(request.POST, instance=k_instance)
            # if foodForm.is_valid():
            #     # post = foodForm.save(commit=False)
            #     # post.kitchen = k_instance
            #     # post.save()
            #     foodForm.save()
            # else:
            #     return render(request, 'kitchen/kitchen_create.html',{'kitchen_form':form,'food_form': foodForm, 'error': 'Bad data entry'})
        else:
            return render(request, 'kitchen/kitchen_create.html',{'kitchen_form':form,'error': 'Bad data entry'})
        return HttpResponseRedirect(reverse_lazy('kitchen:kitchen_detail',args=(k_instance.id,)))
    return render(request, 'kitchen/kitchen_create.html',{'kitchen_form':form})

class KitchenUpdateView(UpdateView):
    model = Kitchen
    fields = ['name',  'open_time', 'close_time', 'working_days']
    template_name = 'kitchen/kitchen_update.html'
    success_url = reverse_lazy('kitchen:index')
    #TODO # login_url = '/login/'

class KitchenDeleteView(DeleteView):
    model = Kitchen
    template_name = 'kitchen/kitchen_confirm_delete.html'
    success_url = reverse_lazy('kitchen:index')
    #TODO: # login_url = '/login/'

def FoodCreateView(request, pk):
    kitchen_obj = get_object_or_404(Kitchen, pk=pk)
    form = FoodForm()
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.kitchen = kitchen_obj
            post.save()
        else:
            return render(request, 'food/food_create.html',{'form':form, 'kitchen_id':pk, 'error': 'Bad data entry'})
        return HttpResponseRedirect(reverse_lazy('kitchen:kitchen_detail',args=(pk,)))
    return render(request, 'food/food_create.html',{'form':form, 'kitchen_id':pk})
# class FoodDetailView(DetailView):
#     pass
def FoodUpdateView(request, kpk, fpk):
    # model = Food
    # fields = '__all__'
    # exclude = ['kitchen']
    # template_name = 'food/food_update.html'
    # success_url = reverse_lazy('kitchen:food_detail')
    pass

def FoodDeleteView(request, kpk, fpk):
    food_obj = get_object_or_404(Food, pk=fpk)
    if request.method == 'POST':
        food_obj.delete()
        return HttpResponseRedirect(reverse_lazy('kitchen:kitchen_detail',args=(kpk,)))
    return render(request, 'food/food_confirm_delete.html',{'name':food_obj.name, 'kitchen_id': kpk})

def check():
    pass

def error_500(request):
    return render(request, '500.html')
