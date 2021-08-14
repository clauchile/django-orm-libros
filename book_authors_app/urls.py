from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('authors', views.authors),
    path('books/<int:dato>', views.books),
    path('authors/<int:dato>', views.authorsid),

    #path('second/<name>', views.second)
]
print(id)