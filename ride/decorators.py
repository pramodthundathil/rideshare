from django.shortcuts import render,redirect


def RideClassifier(view_func,*args):
    def wrapper_function(request, *args, **kwargs):
        group = None
        
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
        if group == None:
            return view_func(request, *args, **kwargs)
            
        if group == 'user':
            return view_func(request, *args, **kwargs)
        
        if group == 'admin':
            return redirect('AdminHome')
            
        
    return wrapper_function