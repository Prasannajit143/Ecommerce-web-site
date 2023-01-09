from django.shortcuts import render
from .models import Products,ContactUs,OrderUpdate,abc
from math import ceil
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum
import json
from django.http import JsonResponse,HttpResponse

MERCHANT_KEY = "kbzk1DSbJiV_03pS"
# Create your views here.
def product(request):
    # products = Products.objects.all()
    # n = len(products)
    # nofSlides = n//4 + ceil((n/4)-(n//4))
    # # params = {"product" : products, "No_of_slides" : nofSlides, "range" : range(1,nofSlides)}
    # allProds=[[products, range(1, nofSlides), nofSlides],[products, range(1, nofSlides), nofSlides]]
    allProds = []
    catProducts = Products.objects.values('category','id')
    cats = {item['category'] for item in catProducts}
    for cat in cats:
        prod = Products.objects.filter(category=cat)
        n = len(prod)
        nofSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nofSlides),nofSlides])
    params={'allProds':allProds }
    return render(request,'shop/index.html',params)

def searchMatch(query, item):
    if query in item.product_name.lower() or query in item.category.lower() or query in item.product_desc.lower():
        return True
    else:
        return False

def search(request):
    query= request.GET.get('search')
    allProds = []
    catprods = Products.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Products.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod)!= 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg":""}
    if len(allProds)==0 or len(query)<2:
        params={'msg':"Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)


def about(request):
    return render(request,'shop/about.html')

def contactUs(request):
    pk = False
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('Email','')
        phone = request.POST.get('Phone','')
        text = request.POST.get('Text','')
        contact = ContactUs(Name=name,Email=email,Phone=phone,Text=text)
        contact.save()
        pk = True
    return render(request,'shop/contactUs.html',{'pk':pk})

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = abc.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.time_stamp})
                    response = json.dumps({'status':'success','updates':updates,'itemsJson':order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"Noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"Error"}')
    return render(request, 'shop/tracker.html')

def productView(request,myid):
    product = Products.objects.filter(id=myid)
    return render(request,'shop/productView.html',{'product':product[0]})

def checkout(request):
    if (request.method == "POST"):
        items_json = request.POST.get('itemsJosn','')
        amount = request.POST.get('amount','')
        name = request.POST.get('Name','')
        email = request.POST.get('Email','')
        Address = request.POST.get('Address1','') + ' ' + request.POST.get('Address2','')
        city = request.POST.get('City','')
        state = request.POST.get('State','')
        zip_code = request.POST.get('zip_code','')
        phone = request.POST.get('phone','')
        contact = abc(items_json=items_json,name=name,email=email,address=Address,city=city,state=state,zip_code=zip_code,Phone=phone,amount=amount)
        contact.save()
        id = contact.order_id 
        update = OrderUpdate(order_id=id,update_desc='Your order has been placed')
        update.save()
        thank = True
        
        param_dict = {
                'MID': 'VMLsKh33374131769871',
                'ORDER_ID': str(abc.order_id),
                'TXN_AMOUNT': str(amount),
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'shop/paytm.html', {'param_dict': param_dict})
    return render(request, 'shop/checkout.html')

        # return render(request,'shop/checkout.html',{'thank':thank,'id':id})
@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'shop/paymentstatus.html', {'response': response_dict})


def autocomplete(request):
    if 'term' in request.GET:
        qs = Products.objects.filter(product_name__istartswith = request.GET.get('term'))
        prodsname=list()
        for product in qs:
            prodsname.append(product.product_name)
        return JsonResponse(prodsname,safe=False)
    return render(request,"shop/basic.html")



