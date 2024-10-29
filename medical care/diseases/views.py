from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Disease

# View to list all diseases
@login_required
def disease_list(request):
    diseases = Disease.objects.all()  # Get all diseases from the database
    return render(request, 'disease_list.html', {'diseases': diseases})

# View to display disease details
@login_required
def disease_detail(request, pk):
    disease = get_object_or_404(Disease, pk=pk)  # Get disease by primary key (pk)
    return render(request, 'disease_detail.html', {'disease': disease})

# View for user login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('disease_list')  # Redirect to disease list after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

# View for user registration
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Automatically log the user in after registration
            return redirect('disease_list')  # Redirect to disease list
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


from django.contrib.auth import logout
from django.shortcuts import redirect

# View for user logout
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout
