
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models import CustomUser

class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('login')  # Redireciona para a página de login após a alteração de senha

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirecione para a página de login após o registro bem-sucedido
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def home(request):
    user_id = request.user.id  # Obtém o ID do usuário logado
    user_name = request.user.username  # Obtém o nome do usuário logado
    context = {
        'user_id': user_id,
        'user_name': user_name,
    }
    return render(request, 'home.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

def list_users(request):
    # Crie usuários usando o modelo CustomUser
    # user1 = User.objects.create_user(username='usuario3', password='senha1')
    # user2 = User.objects.create_user(username='usuario4', password='senha2')

    # # Salve os usuários no banco de dados
    # user1.save()
    # user2.save()

    # Recupere todos os usuários do modelo User (modelo padrão do Django)
    users = User.objects.all()

    return render(request, 'list_users.html', {'users': users})

def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
    except User.DoesNotExist:
        pass  # Trate a situação em que o usuário não existe

    return redirect('list_users')