from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Nome da Tag')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nome do Produto')
    description = models.TextField(blank=True, verbose_name='Descrição')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Quantidade')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Imagem')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    tags = models.ManyToManyField(Tag, blank=True, related_name='products', verbose_name='Tags')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', verbose_name='Usuário')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('inventory:product_detail', args=[str(self.id)])
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['-created_at']

class ProductDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='details', verbose_name='Produto')
    serial_number = models.CharField(max_length=100, verbose_name='Número de Série')
    additional_info = models.TextField(blank=True, verbose_name='Informações Adicionais')
    expiry_date = models.DateField(blank=True, null=True, verbose_name='Data de Validade')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    
    def __str__(self):
        return f"{self.product.name} - {self.serial_number}"
    
    class Meta:
        verbose_name = 'Detalhe do Produto'
        verbose_name_plural = 'Detalhes dos Produtos'
        ordering = ['-created_at']