from django.shortcuts import render
from quizzy.forms.signup import SignUpForm


def sign_up_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(*args, **kwargs)
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.is_active = True
            user.save(*args, **kwargs)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
