from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
import hashlib
from django.core.urlresolvers import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.decorators import login_required

# login route. authenticated from accounts/backends.py


def user_login(request):
    messages = get_messages(request)
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        hash_password = hashlib.md5(password).hexdigest()
        userName = authenticate(username=username)
        if userName:
            if userName.password == hash_password:
                if userName.is_active:
                    login(request, userName)
                    return HttpResponseRedirect(reverse('admin-panel'))
                else:
                    error = "Your id is not active!"
                    context = {"error": error}
                    return render(request, 'login/login.html', context)
            else:
                context = RequestContext(request)
                error = "Incorrect Password!"
                context={"errorpass":error}
                return render(request,'login/login.html',context)
        else:
            #context = RequestContext(request)
            error = "Your Email is incorrect"
            context={"erroremail":error}
            return render(request,'login/login.html',context)
    else:
        context={'messages':messages}
        return render(request,'login/login.html')


def user_logout(request):
    user = request.user
    #messages.add_message(request, messages.INFO, 'Your are successfully logged out. Thank You :)')
    logout(request)
    return HttpResponseRedirect(reverse('login'))