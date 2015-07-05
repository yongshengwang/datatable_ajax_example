from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import json
# Create your views here.
from django.template import RequestContext
from tracy.models import User
from django.db.models import Q
def test(request):
    return render_to_response('test.html', locals(), context_instance=RequestContext(request))

def get_data(request):
    order_list = ['name','age']
    order_dict = {'asc':'','desc':'-'}
    order = order_list[int(request.GET.get('order[0][column]', '0'))]
    order_dir = order_dict[request.GET.get('order[0][dir]','asc')]
    search =  request.GET.get('search[value]','')
    if search:
        search_q = Q(name__contains=search) | Q(age__contains=search)
    start = request.GET.get('start',0)
    end = start + request.GET.get('length',10)
    total = User.objects.all().count()
    if search:
        t = User.objects.filter(search_q).order_by(order_dir+order)
        filter_total = User.objects.filter(search_q).count()
    else:
        t = User.objects.all().order_by(order_dir+order)
        filter_total = total
    users = t[start:end]
    return HttpResponse(json.dumps(
        {"draw": int(request.GET['draw']),
         "recordsTotal": total,
         "recordsFiltered": filter_total,
         'data':[{'name': u.name, 'age': u.age, 'link':{'action': get_action(u.id), 'id': u.id}} for u in users]},
        cls=DjangoJSONEncoder))

def get_action(id):
    return 'View' if id%2 ==0 else 'Edit'