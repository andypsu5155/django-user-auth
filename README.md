# django-user-auth
## Create login_user, logout_user, register_user, and error_login
### Add to urls.py
```python
path("login_user", views.login_user, name='login-user'),
path("logout_user", views.logout_user, name='logout-user'),
path("register", views.register, name='register'),
path("error_login", views.error_login, name="error_login"),
```

### Create template HTML files
#### login_user.html
```html
{% extends 'base.html' %}

{% block content %}

<h1>Login Account</h1>
<p>login your account here!</p>

<form method="POST" action="">
    {% csrf_token %}
    <label>Username:</label>
    <input type="text" name="username" />
    <label>Password:</label>
    <input type="password" name="password" />

    <input type="submit" />
</form>

<hr>

<a href="{% url 'home' %}">Home</a>
{% endblock %}

```
#### register.html
```html
{% extends 'base.html' %}

{% block content %}
<h1>Register Account</h1>
<p>register your account here!</p>
<form method="POST" action="">
    {% csrf_token %}
    <label>Enter Email Address: </label>
    <input type="email" name="email">
    <label>Enter Username:</label>
    <input type="text" name="username" />
    <label>Enter Password:</label>
    <input type="password", name="password" />
    <input type="submit" />
</form>
<hr>
<a href="{% url 'home' %}">Home</a>
{% endblock %}
```
#### error_login.html
```html
{% extends 'base.html' %}

{% block content %}
<h1>Error login!</h1>
<a href="{% url 'home' %}">Return to Homepage</a>
{% endblock %}
```

### Add to views.py
```python
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            return redirect('error_login')

    return render(request, 'main/login_user.html', {})

def logout_user(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        new_user = User.objects.create_user(username, email, password)
        new_user.save()

        return redirect('home')

    return render(request, 'main/register.html', {})

def error_login(request):
    return render(request, "main/error_login.html", {})
```

## Add functionality to index.html page
### index.html
```html
{% extends 'base.html' %}

{% block content %}

{% if user.is_authenticated %}
    <p>Hello {{ user.get_username }}</p>
{% endif %}

<h1>Welcome to my site!</h1>

{% if user.is_authenticated %}
    <a href="{% url 'logout-user' %}">Logout</a>
    <hr>
{% else %}
    <a href="{% url 'login-user' %}">Login</a>
    <hr>
    <a href="{% url 'register' %}">Register</a>
{% endif %}


{% endblock %}
```