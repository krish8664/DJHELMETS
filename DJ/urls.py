from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DJ.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$','djhelmet.views.home'),
    url(r'^admin_home/$','djhelmet.views.admin_home'),
    url(r'^login/$','djhelmet.views.admin_login'),
    url(r'^add_helmet/$','djhelmet.views.add_helmet'),
    url(r'^add_jacket/$','djhelmet.views.add_jacket'),
    url(r'^add_riding_pant/$','djhelmet.views.add_riding_pant'),
    url(r'^add_riding_boot/$','djhelmet.views.add_riding_boot'),
#    url(r'^add_other/$','djhelmet.views.add_other'),
    url(r'^accounts/login/$', 'djhelmet.views.admin_login', name='login'),
)
