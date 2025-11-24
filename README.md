# Sistema de Automação com Django

Este é um sistema de automação desenvolvido com Django + Selenium, permitindo uma gama de funções capazes de auxiliar no processo administrativo da automação, como o campo responsavel por criar um novo cliente, deletar e editar cliente ja existente e enviar mensagens para clientes não matriculados.

## Requisitos

- Python 3.x
- Django 5.1
- Bootstrap (para estilização)
- Selenium
  
## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/HugoCBB/Automacao-com-django.git
    cd Automacao-com-django
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # No Windows
    source venv/bin/activate  # No macOS/Linux
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure o banco de dados:
    ```bash
    python manage.py migrate
    ```

5. Crie um superusuário para acessar o admin do Django:
    ```bash
    python manage.py createsuperuser
    ```

6. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

## Configuração

### Arquivo `settings.py`

No arquivo `settings.py`, as seguintes configurações são importantes:

- **Internationalization**:
    ```python
    LANGUAGE_CODE = 'pt-br'
    TIME_ZONE = 'America/Sao_Paulo'
    USE_I18N = True
    USE_TZ = True
    ```

- **Static Files**:
    ```python
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    ```

## Sistema

### Página de Mensagens Salvas

A página `mensagens_salvas.html` exibe uma tabela com as mensagens salvas. Cada mensagem possui opções para enviar, editar e deletar.

#### Exemplo de código:

```html
{% extends 'shared/base.html' %} 
{% load static %}  

{% block titulo %}
<title>Mensagens Salvas</title>
{% endblock %}

{% block content %}
    {% if mensagem %}
    <div class="d-flex justify-content-center">
        <table class="table table-striped" style="width: 70%">
            <thead>
                <tr>
                    <th scope="col">ID</th>
                    <th scope="col">Data de criação</th>
                    <th scope="col">Mensagem</th>
                    <th scope="col">Enviar Mensagem</th>
                    <th scope="col">Editar Mensagem</th>
                    <th scope="col">Deletar Mensagem</th>
                </tr>
            </thead>
            <tbody>
                {% for mensagens in mensagem %}
                <tr>
                    <th scope="row">{{ mensagens.id }}</th>
                    <td>{{ mensagens.data }}</td>
                    <td>{{ mensagens.mensagem }}</td>
                    
                    <td>
                        <a href="{%url 'enviar-mensagem' mensagens.id %}">
                            <img style="height: 30px;width: 30px;" src="{% static 'assets/icon/enviar_icon.png' %}" alt="">
                        </a>
                    </td>
                    <td>
                        <a href="{% url 'editar-mensagem' mensagens.id %}">
                            <img style="height: 30px;width: 30px;" src="{% static 'assets/icon/editar_icon.png' %}" alt="Editar mensagem">
                        </a>
                        </a>
                    </td>
                    <td>
                        <a href="{% url 'deletar-mensagem' mensagens.id %}">
                            <img style="height: 30px;width: 30px;" src="{% static 'assets/icon/deletar_icon.png' %}" alt="Deletar mensaem">
                        </a>
                    </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
    {% endif %}

    
{% endblock %}
```
![image](https://github.com/user-attachments/assets/8151cfce-5c8f-4102-9d01-22842885126e)

## Pagina de clientes Salvos

Ja na página `clientes_salvos.html` exibe uma tabela com os clientes salvos. Nessa parte do sistema é possivel editar cliente ou deletar cliente.

```html
{% extends 'shared/base.html' %} 
{% load static %}  

{% block titulo %}
<title>Clientes Salvos</title>
{% endblock %}

{% block content %}
    {% if clientes %}
    <div class="d-flex justify-content-center">
        <table class="table table-striped" style="width: 70%">
            <thead>
                <tr>
                    <th scope="col">ID</th>
                    <th scope="col">Nome</th>
                    <th scope="col">Numero</th>
                    <th scope="col">Matriculado</th>
                    <th scope="col">Editar Cliente</th>
                    <th scope="col">Deletar Cliente </th>
                </tr>
            </thead>
            <tbody>
                {% for cliente in clientes %}
                    <tr>
                        <th scope="row">{{ cliente.id }}</th>
                        <td>{{ cliente.nome }}</td>
                        <td>{{ cliente.numero }}</td>
                        <td>{{ cliente.matriculado }} </td>
                        <td>
                            <a href="{% url 'editar-cliente' cliente.id %}">
                                <img style="height: 30px;width: 30px;" src="{% static 'assets/icon/editar_icon.png' %}" alt="Editar Cliente">
                            </a>
                        </td>
                        <td>
                            <a href="{% url 'deletar-cliente' cliente.id %}">
                                <img style="height: 30px;width: 30px;" src="{% static 'assets/icon/deletar_icon.png' %}" alt="Deletar Cliente">
                            </a>
                            </a>
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
    {% endif %}

    
{% endblock %}
```

![image](https://github.com/user-attachments/assets/67fd8b7a-d4f0-4c43-bbd1-85b669ee7b7d)



