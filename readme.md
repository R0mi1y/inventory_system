<div align="center">
  <h1>📦 Sistema de Gestão de Estoque</h1>
  <p>Uma aplicação completa e responsiva desenvolvida com Django</p>
  <img src="https://img.shields.io/badge/Django-4.0%2B-green" alt="Django 4.0+">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/Bootstrap-5.0-purple" alt="Bootstrap 5.0">
  <img src="https://img.shields.io/badge/Status-Pronto%20para%20uso-success" alt="Status: Pronto para uso">
</div>

---

## 🌟 Recursos Principais

- 🔐 **Sistema de autenticação completo** - Login, registro e controle de acesso
- 📝 **Cadastro detalhado de produtos** - Nome, descrição, preço, quantidade e imagens
- 📋 **Detalhamento específico por unidade** - Números de série e informações individuais
- 🏷️ **Organização por tags** - Categorize e filtre produtos facilmente
- 📱 **Design responsivo** - Interface adaptável para todos os dispositivos
- 🔍 **Busca avançada** - Encontre produtos por nome, descrição ou tags

## 📸 Capturas de Tela

<div align="center">
  <table>
    <tr>
      <td align="center"><strong>Tela Inicial</strong></td>
      <td align="center"><strong>Lista de Produtos</strong></td>
      <td align="center"><strong>Detalhes do Produto</strong></td>
    </tr>
    <tr>
      <td><img src="/api/placeholder/400/300" alt="Tela Inicial" width="100%"></td>
      <td><img src="/api/placeholder/400/300" alt="Lista de Produtos" width="100%"></td>
      <td><img src="/api/placeholder/400/300" alt="Detalhes do Produto" width="100%"></td>
    </tr>
  </table>
</div>

## 🚀 Começando

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- Conhecimento básico de linha de comando

### 📥 Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/sistema-estoque-django.git
   cd sistema-estoque-django
   ```

2. **Crie um ambiente virtual**
   ```bash
   # Criar o ambiente
   python -m venv venv
   
   # Ativar no Windows
   venv\Scripts\activate
   
   # Ativar no macOS/Linux
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install django pillow django-crispy-forms crispy-bootstrap5
   ```

4. **Configure o banco de dados**
   ```bash
   python manage.py makemigrations inventory
   python manage.py migrate
   ```

5. **Crie um superusuário (administrador)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor de desenvolvimento**
   ```bash
   python manage.py runserver
   ```

7. **Acesse a aplicação** em http://127.0.0.1:8000/

## 🛠️ Estrutura do Projeto

```
inventory_system/
├── inventory_system/    # Configurações do projeto
├── inventory/           # Aplicação principal
│   ├── models.py        # Definição dos dados
│   ├── forms.py         # Formulários
│   ├── views.py         # Lógica da aplicação
│   └── urls.py          # Rotas da aplicação
├── templates/           # Templates HTML
├── static/              # Arquivos estáticos
├── media/               # Arquivos de usuários
└── manage.py            # Script de gerenciamento
```

## 📋 Funcionalidades Detalhadas

### Gestão de Produtos

- ✅ Cadastro de produtos com informações completas
- ✅ Upload de imagens para melhor visualização
- ✅ Controle de estoque com quantidade disponível
- ✅ Histórico de atualizações com timestamps

### Detalhamento de Itens

- ✅ Registro individual por unidade de produto
- ✅ Controle de números de série
- ✅ Informações adicionais personalizadas
- ✅ Datas de validade (opcional)

### Sistema de Tags

- ✅ Criação e gerenciamento flexível de tags
- ✅ Associação de múltiplas tags a produtos
- ✅ Filtragem avançada por combinação de tags
- ✅ Busca inteligente por palavras-chave

### Interface do Usuário

- ✅ Design limpo e profissional com Bootstrap 5
- ✅ Navegação intuitiva e responsiva
- ✅ Formulários validados e de fácil preenchimento
- ✅ Feedback visual para todas as ações importantes

## 🔧 Personalizando o Sistema

O sistema foi projetado para ser facilmente adaptável às suas necessidades específicas:

1. **Adicione novos campos** modificando os modelos em `inventory/models.py`
2. **Personalize o visual** ajustando os templates em `templates/`
3. **Estenda as funcionalidades** criando novas views em `inventory/views.py`
4. **Configure permissões específicas** para diferentes tipos de usuários

## 📚 Guia para Desenvolvedores

Para estender ou modificar o sistema:

1. Siga as melhores práticas de Django
2. Mantenha a estrutura MVC (Model-View-Controller)
3. Documente novos recursos adequadamente
4. Execute testes antes de implementar grandes mudanças

## 🤝 Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma Branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Faça Commit das suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Faça Push para a Branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

## 📞 Suporte

Para suporte, envie um email para seu-email@exemplo.com ou abra uma issue no repositório do GitHub.

---

<div align="center">
  <p>Desenvolvido com ❤️ para simplificar o gerenciamento de estoque</p>
</div>