from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import json
# Create your views here.
from django.template import RequestContext
from tracy.models import User

def test(request):
    return render_to_response('test.html', locals(), context_instance=RequestContext(request))

def get_data(request):
    order_list = ['name','age']
    order_dict = {'asc':'','desc':'-'}
    order = order_list[int(request.GET.get('order[0][column]', '0'))]
    order_dir = order_dict[request.GET.get('order[0][dir]','asc')]
    print request.GET.get('search[value]','')
    start = request.GET.get('start',0)
    end = start + request.GET.get('length',10)
    print end
    t = User.objects.all().order_by(order_dir+order)
    users = t[start:end]
    return HttpResponse(json.dumps({"draw": int(request.GET['draw']),"recordsTotal": len(t),"recordsFiltered": len(t),'data':[{'name':u.name,'age':u.age} for u in users]}, cls=DjangoJSONEncoder))