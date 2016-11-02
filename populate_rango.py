import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from rango.models import Category, Page

def populate():
    python_cat = add_cat('Python', 128, 64)

    add_page(cat=python_cat, title="Official Py", url="http://docs.python.org/2/tutorial/", views=45)

    add_page(cat=python_cat, title="Learn Py in 10", url="www.goo.com", views=3)

    add_page(cat=python_cat, title="Think Like Comp Sci", url="http://www.greenteapress.com/", views=66)

    django_cat = add_cat("Django", 64, 32)

    add_page(cat=django_cat, title="Official Django Tutorial", url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/", views=7)

    add_page(cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/", views=13)

    add_page(cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/", views=5)

    frame_cat = add_cat("Other Frameworks", 32, 16)

    add_page(cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/", views=20)

    add_page(cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org", views=8)

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views=views
    c.likes=likes
    c.save()
    return c

if __name__ == '__main__':
    print "Starting Rango pop script"
    populate()
