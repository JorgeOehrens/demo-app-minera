from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import  messages

# Create your views here.

def login(request):

    if request.method == "GET":
        
        return render ( request , 'Client/Login/index.html')

    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']

        if '@' in username:
            useremail_log = User.objects.filter(email=username)
            if not useremail_log:   

                messages.warning(request, 'Verificar correo o contraseña incorrecta')

                return render(request, 'Client/Login/index.html' )
            else:

                useremail_log = User.objects.get(email=username)

                username = useremail_log.username
        else:
            username = username

        if username and password:
            user=auth.authenticate(username=username , password=password)

            if user:
                staff=user.is_staff
                print(staff)

                if staff == True:
                    auth.login(request,user)
                    return redirect('home-admin')


                else:
                    auth.login(request,user)
                    messages.success(request,"Bienvenido "+ user.first_name  + ", a tu dashboard de cliente")
                    return redirect('home')
                

                messages.warning(request, 'Cuenta no esta activa, porfavor revisar correo')

                return redirect('login')

            messages.warning(request, 'Verificar correo o contraseña incorrecta')

            return redirect('login')

        messages.warning(request, 'Porfavor, completar los campos requeridos')

        return redirect('login')




        
        return redirect('login')



        

def logout(request):
    auth.logout(request)
    messages.success(request, "Has cerrado sesion")
    return redirect('login')

    

    
