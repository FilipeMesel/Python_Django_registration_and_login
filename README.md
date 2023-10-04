# Projeto de Autenticação de Usuários usando Django

Este é um projeto simples de autenticação de usuários usando o framework Django. O projeto permite que os usuários se registrem, façam login, alterem suas senhas e visualizem uma lista de todos os usuários cadastrados.

## URLs

A configuração de URL para este projeto está definida no arquivo `urls.py` e inclui as seguintes URLs:

- `/admin/`: Acesso à interface de administração do Django.
- `/home/`: Página inicial após fazer login.
- `/login/`: Página de login.
- `/logout/`: Rota para efetuar logout.
- `/register/`: Página de registro de novos usuários.
- `/password_change/`: Página para alteração de senha.
- `/password_change/password_change_done/`: Página exibida após a alteração de senha bem-sucedida.
- `/list_users/`: Página que lista todos os usuários cadastrados.
- `/delete_user/<int:user_id>/`: Rota para excluir um usuário específico.

## Modelos

O projeto possui um modelo personalizado chamado `CustomUser`, que estende o modelo `AbstractUser` do Django para adicionar campos personalizados. Também define relacionamentos com os modelos `Group` e `Permission` para controle de permissões de usuário.

```python
class CustomUser(AbstractUser):
    # Outros campos personalizados, se houver
    # ...

    # Defina o related_name para evitar conflitos
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_set',
    )
```

# Como Usar

1. Clone este repositório para o seu ambiente de desenvolvimento.

```python
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto
```

2. Instale as dependências.

```python
pip install -r requirements.txt
```

3. Aplique as migrações do Django.

```python
python manage.py migrate
```

4. Execute o servidor de desenvolvimento.

```python
python manage.py runserver
```

Agora você pode acessar o projeto no navegador em http://localhost:8000/login

# Projeto de referência

```python
https://www.interviewbit.com/blog/django-projects/
```