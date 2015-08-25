from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import app01.urls
from app01 import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bbs_pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}), 
    url(r'^login/$', views.Login ),
    url(r'^acc_login/$', views.acc_login),
    url(r'^logout/$', views.logout_view),   
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(app01.urls)), 
)
