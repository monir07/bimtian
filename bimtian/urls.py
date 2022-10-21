
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from userinfo.views import SingupView, CustomLoginView, CustomLogoutView, UserPasswordChangeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', SingupView.as_view(), name='signup'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('change-user-password/', UserPasswordChangeView.as_view(), name='user_change_password'),

    path('user_info/', include('userinfo.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# ADMIN PANEL HEADER AND TITLE TEXT CHANGE.
admin.site.site_header = "BIMTIAN Admin"
admin.site.site_title = "BIMTIAN Admin Portal"
admin.site.index_title = "Welcome to BIMTIAN Portal"