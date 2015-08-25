from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib import auth 
import models
from django.contrib import comments
from django.contrib.contenttypes.models import ContentType

# Create your views here.

def acc_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username,password=password)
    print username,password
    if user is not None: #and user.is_active:
        #correct password and user is marked "active"
        auth.login(request,user)
        content = '''
        Welcome %s !!!
           
        <a href='/logout/' >Logout</a>
                                               
        ''' % user.username
        #return HttpResponse(content)
        return HttpResponseRedirect('/')
    else:
        return render_to_response('login.html',{'login_err':'Wrong username or password!'})


def logout_view(request):
    user = request.user
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponse("<b>%s</b> logged out! <br/><a href='/'>Re-login</a>" % user)


def Login(request):
    return render_to_response('login.html')

def index(request):
    bbs_list = models.BBS.objects.all()
    return render_to_response('index.html', {'bbs_list': bbs_list, 'user':request.user})
    
def bbs_detail(request, bbs_id):
    bbs_obj = models.BBS.objects.get(id=bbs_id)
    return render_to_response('bbs_detail.html', {'bbs_obj':bbs_obj, 'user':request.user} )

def sub_comment(request):
    #print request.POST
    bbs_id = request.POST.get('bbs_id')
    _comment = request.POST.get('comment')
    bbs_table_obj = ContentType.objects.get(id = 7)

    comments.models.Comment.objects.create(
            cotent_type = bbs_table_obj,
            site_id = 1,
            user = request.user,
            comment = _comment,
            )
    return HttpResponseRedirect('/detail/%s/' % bbs_id )
