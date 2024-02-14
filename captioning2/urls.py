from django.urls import path
from .views import index_page,clicking_on_predict_caption

urlpatterns=[
    path('',index_page,name='index_page'),
    path('predict_caption/',clicking_on_predict_caption,name='clicking_on_predict_caption'),

]