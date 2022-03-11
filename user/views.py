
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages
from django.conf import settings

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token
from .forms import SignUpForm, LoginForm
from .models import MyUser
from .serializers import LoginSerializer



def index(request):
    return render(request, 'user/index.html')


@login_required
def fork(request):
    if request.user.is_staff:
        return render(request, 'user/fork.html')
    return redirect('patient:dashboard')


class Registeration(CreateView):
    form_class = SignUpForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('user:index')
    
    def form_valid(self, form):
        # first save form
        super().form_valid(form)
    
        # then login
        national_id = form.cleaned_data.get('national_id')
        password = form.cleaned_data.get('password1')
        username = MyUser.objects.get(national_id = national_id).username
        user = authenticate(username = username, password = password)
        login(self.request, user)
        
        return HttpResponseRedirect(self.get_success_url())
    


def get_username(user_name):
    try   :
            username = MyUser.objects.get(email=user_name).username
    except:
        try   :
                username = MyUser.objects.get(phone=user_name).username
        except:
            try   :
                    username = MyUser.objects.get(national_id=user_name).username
            except:
                    username = user_name
    return username



@requires_csrf_token
@csrf_exempt
@csrf_protect
def login_view(request):
    context = {'error':''}
    
    if request.user.is_authenticated: 
        return redirect("user:index")
    
    
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        
        username = get_username(username)
        
        user = authenticate(username=username, password=password)
        if user :
            login(request, user)
            return redirect("user:index")
        else :
            context['error'] = "Invalid Login" 
    return render(request, "user/login.html", context)
  
  
    
    
@api_view(['POST'])
def login_api(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            password = serializer.data['password']
            username = get_username(username)
            user = authenticate(username=username, password=password)
            if user :
                login(request, user)
                return Response({'error':False, 'url':'/'}, status=status.HTTP_200_OK)
            else :
                return Response({'error':'Invalid login'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@login_required
def del_user(request):
    if request.POST:
        request.user.is_active = False  
        request.user.save()
    return  redirect('user:index')
    
    
def logout_view(request):
    logout(request)
    return redirect('user:login')


def handle_404(request, exception):
    return render(request, 'user/404.html' , status=404 )


def handle_500(request, exception=None):
    return render(request,'user/500.html', status=500 )


def handle_403(request, exception=None):
    return render(request,'user/403.html', status=403 )





def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = MyUser.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "user/password_reset_email.txt"
                    c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'SHS.link',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, settings.EMAIL_HOST_USER , [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')

                    return redirect ("/password_reset/done/")
            messages.error(request, 'An invalid email has been entered.')
    password_reset_form = PasswordResetForm()
    return render(request, "user/password_reset.html", {"password_reset_form":password_reset_form})

