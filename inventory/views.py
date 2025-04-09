
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import login
from django.contrib import messages

from .models import Product, ProductDetail, Tag
from .forms import ProductForm, ProductDetailForm, TagForm, UserRegisterForm, ProductSearchForm

class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'inventory/product/product_list.html'
    context_object_name = 'products'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Product.objects.filter(user=self.request.user)
        
        form = ProductSearchForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            tags = form.cleaned_data.get('tags')
            
            if query:
                queryset = queryset.filter(
                    Q(name__icontains=query) | 
                    Q(description__icontains=query)
                )
            
            if tags:
                queryset = queryset.filter(tags__in=tags).distinct()
                
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = ProductSearchForm(self.request.GET)
        return context

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'inventory/product/product_detail.html'
    context_object_name = 'product'
    
    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['details'] = self.object.details.all()
        return context

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/product/product_form.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Produto criado com sucesso!')
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/product/product_form.html'
    
    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
    
    def form_valid(self, form):
        messages.success(self.request, 'Produto atualizado com sucesso!')
        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'inventory/product/product_confirm_delete.html'
    success_url = reverse_lazy('inventory:product_list')
    
    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Produto excluído com sucesso!')
        return super().delete(request, *args, **kwargs)

@login_required
def add_product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id, user=request.user)
    
    if request.method == 'POST':
        form = ProductDetailForm(request.POST)
        if form.is_valid():
            detail = form.save(commit=False)
            detail.product = product
            detail.save()
            messages.success(request, 'Detalhe do produto adicionado com sucesso!')
            return redirect('inventory:product_detail', pk=product.id)
    else:
        form = ProductDetailForm()
    
    return render(request, 'inventory/product/add_product_detail.html', {
        'form': form,
        'product': product
    })

@login_required
def delete_product_detail(request, detail_id):
    detail = get_object_or_404(ProductDetail, id=detail_id, product__user=request.user)
    product_id = detail.product.id
    detail.delete()
    messages.success(request, 'Detalhe do produto excluído com sucesso!')
    return redirect('inventory:product_detail', pk=product_id)

class TagListView(LoginRequiredMixin, ListView):
    model = Tag
    template_name = 'inventory/tag/tag_list.html'
    context_object_name = 'tags'

class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'inventory/tag/tag_form.html'
    success_url = reverse_lazy('inventory:tag_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Tag criada com sucesso!')
        return super().form_valid(form)

class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'inventory/tag/tag_form.html'
    success_url = reverse_lazy('inventory:tag_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Tag atualizada com sucesso!')
        return super().form_valid(form)

class TagDeleteView(LoginRequiredMixin, DeleteView):
    model = Tag
    template_name = 'inventory/tag_confirm_delete.html'
    success_url = reverse_lazy('inventory:tag_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Tag excluída com sucesso!')
        return super().delete(request, *args, **kwargs)

def home(request):
    return render(request, 'inventory/home.html')