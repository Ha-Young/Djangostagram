from django.shortcuts import redirect
from .models import Dsuser

def login_required(func):
    def wrap(request, *args, **kwargs):
        user_id = request.session.get('user')
        
        if user_id is None or not user_id:
            return redirect('/user/login/')
        else:
            dsuser = Dsuser.objects.get(pk=user_id)
            if dsuser is None or not dsuser:
                return redirect('/user/login/')
        
        return func(request, *args, **kwargs)

    return wrap