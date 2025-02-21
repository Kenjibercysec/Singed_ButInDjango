# Projeto Django - FreshStart

Este é um projeto Django chamado **FreshStart**. Este projeto foi gerado usando Django 5.1.6 e serve como um ponto de partida para o desenvolvimento de aplicações web.

## Estrutura do Projeto

- **projeto/**: Contém as configurações principais do projeto Django.
- **home/**: Aplicação Django principal que contém as views, models, templates e arquivos estáticos.

## Configuração e Instalação

### Pré-requisitos

- Python 3.8 ou superior
- Django 5.1.6
- SQLite (ou outro banco de dados de sua escolha)

### Passos para Configuração

1. Clone o repositório:

    ```sh
    git clone https://github.com/seu-usuario/FreshStart.git
    cd FreshStart
    ```

2. Crie um ambiente virtual e ative-o:

    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```sh
    pip install -r requirements.txt
    ```

4. Execute as migrações do banco de dados:

    ```sh
    python manage.py migrate
    ```

5. Inicie o servidor de desenvolvimento:

    ```sh
    python manage.py runserver
    ```

6. Acesse o projeto no navegador:

    ```
    http://127.0.0.1:8000/
    ```

## Estrutura de Diretórios

- **projeto/**: Diretório principal do projeto Django.
  - **settings.py**: Arquivo de configuração do Django.
  - **urls.py**: Arquivo de roteamento de URLs.
  - **wsgi.py**: Arquivo de configuração do WSGI para implantação.
- **home/**: Aplicação Django principal.
  - **static/**: Arquivos estáticos (CSS, JavaScript, Imagens).
  - **templates/**: Templates HTML.
  - **views.py**: Arquivo de views.
  - **models.py**: Arquivo de models.

## Configurações Importantes

### Arquivos Estáticos

Certifique-se de que os arquivos estáticos estão configurados corretamente no `settings.py`:

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'home' / 'static'
]