
from django.contrib import admin
from django.urls import path
from product.views import home,about,car,Contact,sign,form
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home, name = 'home'),
    path('car/', car, name = 'car'),
    
    path('contact/',Contact, name = 'contact'),
    path('sign/', sign, name = 'sign'),
    path('about/',about,name = 'about'),
    path('form/',form,name='form')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)