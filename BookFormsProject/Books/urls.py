
from django.urls import path
from Books.views import bookCreate,listBook,viewBook,deleteBook,updateBook

urlpatterns = [
    path('create',bookCreate,name="create"),
    path('list',listBook,name="list"),
    path('view/<int:pk>',viewBook,name="viewbook"),
    path('delete/<int:pk>',deleteBook,name="deletebook"),
    path('update/<int:pk>',updateBook,name="update")
]