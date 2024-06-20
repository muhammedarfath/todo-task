
from django.urls import path
from .views import Signup,Login,Logout
from django.views.decorators.cache import never_cache


app_name = 'UserAuth'

urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'), 
    path('login/', never_cache(Login.as_view()), name='login'),  
    path('logout/', never_cache(Logout.as_view()), name='logout'), 
]
