from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


app_name = "usuario"

urlpatterns = [
    path('',views.index,name="index"),
    path('base/',views.base,name="base"),
    path('inicio/',views.inicio,name="inicio"),
    path('inicio_staff/',views.iniciostaff,name="iniciostaff"),
    path('registrar_staff/',views.registrar_staff,name="regstaff"),
    path('campeones/',views.campeones,name="campeones"),
    path('registrar/',views.registrar,name="registrar"),
    path('registrar_campeones/',views.registrar_campeones,name="regcampeon"),
    path('cerrarsesion/',views.cerrar_sesion,name="cerrar_sesion"),
    path('subir_items/',views.item,name="item"),
    path('listar/',views.campeon_list,name="listar"),
    path('editar_campeon/<int:id_campeon>/',views.campeon_editar,name="campeon_editar"),
    path('borrar_campeon/<int:id>',views.campeon_borrar,name="campeon_borrar"),
    path('lista_items',views.listar_item,name="lista_items"),
    path('reset/password_reset', PasswordResetView.as_view(template_name='registration/password_reset_form.html',
    email_template_name="registration/password_reset_email.html", success_url='password_reset_done'), name = 'password_reset'),
    path('reset/password_reset_done', TemplateView.as_view(template_name='registration/password_reset_done.html'), name = 'password_reset_done'),
    url(r'reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name = 'password_reset_confirm'),
    path('reset/done',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html') , name = 'password_reset_complete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)