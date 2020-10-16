from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from .decorators import *
from .models import User
from django.views.generic import View
from django.contrib import messages

def agree(request):
    return render(request , 'agree.html')


@method_decorator(logout_message_required, name='dispatch')
class AgreementView(View):
    def get(self, request, *args, **kwargs):
        request.session['agree'] = False
        return render(request, 'agree.html')

    def post(self, request, *args, **kwarg):
        if request.POST.get('agreement1', False) and request.POST.get('agreement2', False):
            request.session['agreement'] = True

            if request.POST.get('csregister') == 'csregister':       
                return redirect('csregister/')
            else:
                return redirect('register/')
        else:
            messages.info(request, "약관에 모두 동의해주세요.")
            return render(request, 'agree.html')