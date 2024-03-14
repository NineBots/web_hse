from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [

    path('', show_main), # главное меню
    path('algo/', show_algo), # алгоритм
    path('algo/post-num', get_num), # отправка числа у алгоритма
    path('review/', show_review), # отзыв
    path('review/post-contact-us', show_post_contact_us), # отправка контакта
    path('review/post-review', show_post_review), # отправка отзыва

]