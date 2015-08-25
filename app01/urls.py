from django.conf.urls import patterns, include, url

import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bbs_pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index),
    url(r'^detail/(\d+)/$', views.bbs_detail),
    url(r'^sub_comment/$', views.sub_comment),
)
