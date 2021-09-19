import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Ecomm.settings")

import django
django.setup()

from django.core.management import call_command
from django.core.files import File
from bs4 import BeautifulSoup
from pathlib import Path
from product.models import Category, Product
from django.db.utils import IntegrityError
import threading as th
import time
import requests
import time


class GetData:
    def __init__(self):
        self.categories = Category.objects.all()
        self.home = Path.cwd() / 'static' / 'img' / 'products'
        if not Path.exists(self.home):
            Path.mkdir(self.home)
        self.main()

    def get_page(self, cat):
        url = f"https://www.google.com/search?q={cat.name.replace(' ', '+')}&source=lnms&tbm=shop&sa=X&ved=2ahUKEwiu6_CU3JTyAhVxzTgGHafJCQIQ_AUoAnoECAIQBA&biw=1422&bih=1014"
        res = requests.get(url)
        page = BeautifulSoup(res.content, 'html.parser')
        div = page.find_all('div', {'class': 'KZmu8e'})[:5]
        for key, product in enumerate(div):
            filename = cat.name
            img = product.find('img')   
            title = product.find('div', {'class': 'sh-np__product-title'})
            price = product.find('span', {'class': 'T14wmb'})
            img = requests.get(img['src'])
            filename = cat.name.replace(' ', '_') + f"{key}.jpg"
            with open(self.home / filename, 'wb') as f:
                for chunk in img.iter_content(1024):
                    f.write(chunk)
            try:
                p = Product(
                        name=title.text.split('(')[0],
                        description=title.text,
                        price=float(price.text[1:].replace(',', '').split()[0]),
                        category=cat,
                        pic=str(self.home / filename),
                    )
                p.pic.save(filename, File(open(self.home / filename, 'rb')))
                p.category = cat
                p.save()
            except IntegrityError:
                pass

    def main(self):
        for cat in self.categories:
            # self.get_page(cat)
            th.Thread(target=self.get_page, args=(cat, )).start()
            # break


if __name__ == '__main__':
    start = time.time()
    GetData()
    print("Time Consumed")
    print("% s seconds" % (time.time() - start))

