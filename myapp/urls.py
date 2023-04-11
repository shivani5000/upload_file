# from django.contrib import admin
# from django.urls import path,include
# from myapp import views
# urlpatterns=[
#     # path('admin/',admin.site.urls),
#     path('',views.index),
#     # path('home/',views.index),
#     path('about/',views.about),
#     path('contact/',views.contact),
#     path('menu/',views.menu),
#     path('reservation/',views.reservation),
#     path('service/',views.service),
#     path('testimonial/',views.testimonial)
    
    
# ]
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    #Your url patterns here
    # path('admin/',admin.site.urls),
    path('',views.index),
    # path('home/',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('menu/',views.menu),
    path('reservation/',views.reservation),
    path('service/',views.service),
    path('testimonial/',views.testimonial),
    path('detail/',views.indexdetail1),
]

# urlpatterns += staticfiles_urlpatterns()
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)