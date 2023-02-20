from Site import Site
from Admin import Admin

page_site_first = Site("Главная страница","Содержимое главной страницы...")
page_site_second = Site("Услуги","Содержимое страницы с услугами...")
page_site_third = Site("Контакты","Контактная информация....")

admin_site_first = Admin("Главная страница","Содержимое главной страницы...")
admin_site_second = Admin("Услуги","Содержимое страницы с услугами...")
admin_site_third = Admin("Контакты","Контактная информация....")

pages = [page_site_first,page_site_second,page_site_third,
         admin_site_first,admin_site_second,admin_site_third]

for page in pages:
    page.render()