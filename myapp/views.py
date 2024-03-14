import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt


contacts = [] #список с оставленными контактами 13 задание

reviews = []  #список с оставленными отзывами 14 задание


#отображение главной страницы
def show_main(request):
    return render(request, 'main/main.html')


#отображение страницы с алгоритмом
def show_algo(request):
    return render(request, 'algorithm/algo.html')


# POST запрос на получение числа для размена
@csrf_exempt #вылетала ошибка нашла в интернете такое решение
def get_num(request):

    num = int(request.POST.get('num', 0)) #получаемое число

    #500
    five_hundred = num//500 #количество 500 купюр
    num = num%500 #остаток

    #100
    one_hundred = num//100
    num = num % 100
    #10
    ten = num // 10
    num = num % 10
    #2
    two = num // 2
    rest = num % 2

    # словарик для заполнения полей в html
    context = {'five_hundred': five_hundred, 'one_hundred':one_hundred, 'ten': ten, 'two': two, 'rest': rest }

    return render(request, 'algorithm/algo.html', context)


#отображение страницы с отзывами
def show_review(request):
    context = {'contacts': contacts, 'reviews': reviews}
    return render(request, 'review/review.html', context)


# POST запрос на получение контактных данных
@csrf_exempt
def show_post_contact_us(request):

    name = request.POST.get('name')
    surname = request.POST.get('surname')
    group = request.POST.get('group')
    phone = request.POST.get('mobile')
    email = request.POST.get('email')

    # заполняю массив всех контактов
    contacts.append({'name': name, 'surname': surname, 'group': group, 'phone': phone, 'email': email })

    # Redirect тоже нашла в интернете т.к. при обновлении страницы запрос выполнялся повторно
    return HttpResponseRedirect('/review')


# POST запрос на получение данных отзыва
@csrf_exempt
def show_post_review(request):

    name = request.POST.get('username')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    agree = request.POST.get('agree')
    birthdate = request.POST.get('birthdate')
    password = request.POST.get('password')
    comment = request.POST.get('comment')
    date = datetime.datetime.now()

    # заполняю массив всех отзывов
    reviews.append({'name': name, 'age': age, 'gender': gender, 'agree': agree, 'birthdate': birthdate, 'password': password, 'comment': comment, 'date': date })

    return HttpResponseRedirect('/review')