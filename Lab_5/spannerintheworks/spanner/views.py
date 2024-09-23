from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from django.urls import reverse

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'},
]

data_dp = [
    {'id': 1, 'title': 'Эй, Арнольд!(Hey Arnold!)','content':
     '''<h1>Главный герой сериала — школьник Арнольд</h1>, живущий со своими дедушкой Филом и бабушкой Гертрудой в пансионе «Сансет-Армз», владельцами которого они являются. 
     Его родители Стелла и Майлз пропали, когда принимали участие в спасательной операции в далекой стране. Место действия — вымышленный город Хиллвуд.''','is_publish':True},
    {'id': 2, 'title': 'Утиные истории (DuckTales)', 'content':
        'Мультсериал 1987 года выпуска','is_publish':False},
    {'id': 3, 'title': 'Черный Плащ (Darkwing Duck)', 'content':
        'Мультсериал 1991 года выпуска','is_publish':True},
]

cats_db = [
    {'id': 1, 'name': 'Мультсериалы'},
    {'id': 2, 'name': 'Сериалы'},
    {'id': 3, 'name': 'Другое'},
]

# Create your views here.
class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_dp,
        'cat_selected': 0,
    }
    return render(request, 'spanner/index.html', data)

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id ={post_id}")

def show_category(request, cat_id):
     data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': data_dp,
        'cat_selected': cat_id,
    }
     return render(request, 'spanner/index.html', context= data)
def about(reqest):
    data = {'title' : 'О нас'}
    return render(reqest,'spanner/about.html', {'title': 'О сайте','menu': menu})
def addpage(request):
    return HttpResponse("Добавление статьи")
def contact(request):
    return HttpResponse("Обратная связь")
def login(request):
    return HttpResponse("Авторизация")
