from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def text(title, html):
    return f'<h1>Интернет магазин</h1>' \
           f'<h2>{title}</h2>' \
           f'<p>{html}</p>'


def main_page(request):
    title = 'Главная страница сайта'
    html = 'Здесь будет распологаться информация о товаре<br>' \
           '<a href="/">Главная страница</a><br>' \
           '<a href = "/about">О себе </a>'
    logger.info(f'Page "main" is open')
    return HttpResponse(text(title, html))


def about_me(request):
    title = 'О себе'
    html = 'Контактная и другая информация<br>' \
           '<a href="/">Главная страница</a><br>' \
           '<a href = "/about"> О себе </a>'
    logger.info(f'Page "about_me" is open')
    return HttpResponse(text(title, html))
