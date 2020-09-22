from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from order.models import Order

def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'Вы вошли в систему')
      return redirect('listings')
    else:
      messages.error(request, 'Неверные учетные данные')
      return redirect('login')
  else:
    return render(request, 'accounts/login.html')



def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'Вы вышли из системы')
    return redirect('index')


def register(request):
  if request.method == 'POST':
    # Get form values
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    # Проверьте, совпадают ли пароли
    if password == password2:
      # Проверьте имя пользователя
      if User.objects.filter(username=username).exists():
        messages.error(request, 'это имя занято')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request, 'Этот адрес электронной почты используется')
          return redirect('register')
        else:
          # Выглядит хорошо
          user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
          # Войти после регистрации
          # auth.login (запрос, пользователь)
          # messages.success (запрос «Вы вошли в систему»)
          # return redirect ('index')
          user.save()
          messages.success(request, 'Вы зарегистрированы и можете войти')
          return redirect('login')
    else:
      messages.error(request, 'Пароли не соответствуют')
      return redirect('register')
  else:
    return render(request, 'accounts/register.html')


def dashboard(request):
  user_contacts = Order.objects.order_by('-contact_date').filter(user_id=request.user.id)

  context = {
    'contacts': user_contacts
  }
  return render(request, 'accounts/dashboard.html', context)