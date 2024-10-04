from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import ContactForm, RegistrationForm  # Both forms should be correctly imported


# Contact View (with login required)
@login_required
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return render(request, 'thanks.html', {'name': name})
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

# Register View
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User = form.save()
            login(request, User)
            return redirect('contact')  # Assuming 'contact' is the name of the contact view
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})

