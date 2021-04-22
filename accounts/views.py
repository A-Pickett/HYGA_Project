from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# from django.urls import reverse_lazy
# from django.views import generic

# Using a CreateView class to render a sign up form using djangos built in UserCreationForm
# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'


# Using a function view to render a sign up form using djangos built in UserCreationForm
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')

    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)
