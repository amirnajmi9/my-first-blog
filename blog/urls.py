from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
path('',views.index,name='index'),
path('<int:post_id>',views.detail,name='detail'),
re_path(r'^(?P<daste>[\w-]+)$',views.dste,name='dste'),
path('post/new/', views.post_new, name='post_new'),
path('post/new/code/', views.kave, name='code'),
path('post/new/<int:post_id>', views.detail, name='detailn_new'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
