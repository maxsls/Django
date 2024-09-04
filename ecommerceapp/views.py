from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse,JsonResponse
from .models import storetype,items,itemsdetails,cart
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import login ,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CreateUserForm,LoginUserForm
# Create your views here.

def index(request):
    
    template=loader.get_template('index.html')
    return HttpResponse(template.render({'request':request}))

def listitems(request):
    p = items.objects.filter(st_id=1)
    template = loader.get_template('listitems.html')
    return HttpResponse(template.render({'items': p, 'request': request}))

def listmoblie(request):
    p = items.objects.filter(st_id=2)
    template = loader.get_template('listmoblie.html')
    return HttpResponse(template.render({'items': p, 'request': request}))

def listcomputer(request):
    p = items.objects.filter(st_id=3)
    template = loader.get_template('listcomputer.html')
    return HttpResponse(template.render({'items': p, 'request': request}))
def listbook(request):
    p = items.objects.filter(st_id=4)
    template = loader.get_template('listbook.html')
    return HttpResponse(template.render({'items': p, 'request': request}))


def detials(request,id):
      
      template=loader.get_template('details.html')
      data=itemsdetails.objects.select_related('items').filter(id=id).first()
      data.total=data.qty*data.items.price
      return HttpResponse(template.render({'data':data,'request':request}))




@login_required(login_url='/auth_login/')
def checkout(request):
    # Fetching item IDs from the cart
    cart_items_ids = cart.objects.values_list('itmesid', flat=True)

    # Fetching item details from itemsdetails based on the IDs in the cart
    items = itemsdetails.objects.select_related('items').filter(items_id__in=cart_items_ids)

    # Loading the checkout template
    template = loader.get_template('checkout.html')

    # Rendering the template with the items
    return HttpResponse(template.render({'items': items, 'request': request}))

@csrf_exempt
def add_to_cart(request):
     count=0
     id=request.POST.get("id")
     quantity = request.POST.get("quantity")
     item = itemsdetails.objects.get(pk=id)
     if cart.objects.filter(itmesid=id).exists():
        item.qty += int(quantity)
        item.save()
    
     else:
        p=cart(itmesid=id)
        p.save()

     row=cart.objects.all()
     for item in row:
        count=count+1   

     request.session["cart"]=count

     return JsonResponse({'count':count})

@csrf_exempt
def auth_login(request):
     form=LoginUserForm()
     if request.method=="POST":
          form=LoginUserForm(data=request.POST)
          if form.is_valid():
              username=form.cleaned_data['username']
              password=form.cleaned_data['password']
              print(username)

              user=authenticate(username=username,password=password)
              if user:
                   if user.is_active:
                        login(request,user)
                        return render(request,'checkout.html')
     context={'form':form}
     return render(request,'auth_login.html',context)

          
@csrf_exempt                   
def auth_register(request):
    template = loader.get_template('auth_register.html')
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('auth_login')
    context = {'registerform': form}
    return HttpResponse(template.render(context=context))

def auth_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('auth_login')


@login_required(login_url='/auth_login/')
def payment(request):
    return render(request, 'payment.html')