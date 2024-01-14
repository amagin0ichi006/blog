from django.shortcuts import render,redirect
from .forms import SignUpForm
from .forms import UserUpdateForm
from .forms import ProfileUpdateForm

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
    else:
        form = SignUpForm()
    if form.is_valid():
        form.save()
        return redirect('user-reg')
    context = {
        'form':form,
    }
    return render(request, 'users.html',context)

def profile(request):
    if request.method == 'POST':
            u_form = UserUpdateForm(request.POST or None, instance=request.user)
            p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profilemodel)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user)

    context = {
         'u_form': u_form,
         'p_form': p_form,
    }
    return render(request, 'profile.html',context)


