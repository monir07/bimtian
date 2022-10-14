
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from userinfo.views import LoginView, SingupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SingupView.as_view(), name='signup'),

    path('user_info/', include('userinfo.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# ADMIN PANEL HEADER AND TITLE TEXT CHANGE.
admin.site.site_header = "BIMTIAN Admin"
admin.site.site_title = "BIMTIAN Admin Portal"
admin.site.index_title = "Welcome to BIMTIAN Portal"