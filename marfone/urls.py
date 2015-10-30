from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.views.generic.base import TemplateView
from registration.backends.simple.views import RegistrationView
from whatsappins.views import about
from django.contrib.auth.models import User

#django_users_api = UsersApi()
#django_users_api.register(UsersResource())


class UsersView(TemplateView):
    template_name = 'registration/users.html'

    def get_context_data(self,**kwargs):
        context = super(UsersView,self).get_context_data(**kwargs)
        context['object_list'] = User.objects.all()
        return context



class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/avatar/change'

admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', TemplateView.as_view(template_name="base.html"), name='index'),
    #url(r'^whatsapp0i5n2s0a1r5k1e242m/register/user_profile/$', 'whatsappins.views.user_profile', name="user_profile"),
    url(r'', include('django.contrib.auth.urls')),
    url(r'^whatsapp0i5n2s0a1r5k1e242m/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^whatsapp0i5n2s0a1r5k1e242m/', include('registration.backends.simple.urls')),
    url(r'^whatsapp0i5n2s0a1r5k1e242m/about','whatsappins.views.about', name='about' ),
    url(r'^admin/', include(admin.site.urls)),
    (r'^avatar/', include('avatar.urls')),
    #url(r'', include('users_api.urls')),
    url(r'^$', UsersView.as_view(), name='index'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


