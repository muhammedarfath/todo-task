from django.http import Http404
from django.shortcuts import redirect, render
from django.views import View
from .forms import SignupForm
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout





# Create your views here.
class Signup(View):
    def get(self, request):
        return render(request, "user_signup.html")
    def post(self, request):
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                request.session['user']=form.cleaned_data['username']
                messages.success(request, 'Your account has been created')
                return render(request,'user_login.html',{'user':form.cleaned_data['email']})            
            else:
                messages.warning(request, form.errors)
                return redirect('/UserAuth/signup/')
            


# User login area and checking cart item
@method_decorator(never_cache, name='dispatch')       
class Login(View):
    def get(self, request):
        return render(request, 'user_login.html')
    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get('username')
            password = request.POST.get('password')
            
            if name.strip() == '' or password.strip() == '':
                messages.warning(request, 'Please fill in all required fields.')
                return redirect('/UserAuth/login/')
            
            user = authenticate(request, username=name, password=password, is_active=True)
            
            if user is not None:       
                login(request, user)
                messages.success(request, 'Login successful')
                return redirect('/')
            else:
                messages.error(request, 'Invalid login credentials')
                return redirect('/')
        raise Http404("Page not found") 




# User logout and using never cache 
@method_decorator(never_cache, name='dispatch')          
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/')