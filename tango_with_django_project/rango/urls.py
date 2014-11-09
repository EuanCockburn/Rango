from django.conf.urls import patterns, url
from rango import views
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'), # NEW MAPPING!
url(r'^category/(?P<category_name_url>\w+)$', views.category, name='category'),
url(r'^login/$', views.user_login, name='login'),
    url(r'^category/(?P<category_name_url>\w+)$/add_page/$', views.add_page, name='add_page'),
    url(r'^logout/$', views.user_logout, name='logout'),
url(r'^register/$', views.register, name='register'),) # ADD NEW PATTERN!

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )