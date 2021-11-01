from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from shablon.models import Gullar, Kategoriya
from shablon.form import CreateGullarForm
from shablon.form import CreateKategoriyaForm

# Create your views here.
# Create your views here.
def import_data(request):
    import csv         
    import os

    settings_dir = os.path.dirname(__file__)
    # print(settings_dir)
    # path = settings_dir + "\maxway.csv"
    info = ''
    kategoriyalar = {}
    with open(settings_dir + "\gul_kategoriya.csv") as f:
            reader = csv.reader(f)                        
            for row in reader:                
                kategoriyalar[row[0]]=Kategoriya.objects.create(
                    pk = int(row[0]),
                    nomi = row[1]
                    )
                info = f"{info}\n{row[0]}. {row[1]}"

    info = info + "\n\n\n"
    with open(settings_dir + "\gul.csv") as f:
            reader = csv.reader(f, delimiter=";")                        
            for row in reader:
                price = int(row[2].rstrip('UZS').replace(" ", "")) if row[2] else 0
                Gullar.objects.create(
                    nomi=row[1],
                   
                    narxi=price,
                    rasmi = row[0],
                    kategoriya = kategoriyalar[row[3]]
                    )
                info = f"{info}\n {row[1]}\n"
    
    return HttpResponse("Success")



def get_product(request):
    kategoriyalar = Kategoriya.objects.all()
    products = Gullar.objects.all()
    products_by_categoes = {}



    for c in kategoriyalar:

        lst = []
        for p in products:
            if c == p.kategoriya:
                lst.append(p)
        if len(lst) != 0:          
            products_by_categoes[c.nomi] = lst
      
    context = {
        "kategoriyalar": kategoriyalar, 
        "products_by_categoes": products_by_categoes}
    return render(request, "gul/maxway.html", context)


def get_by_category_id(request, kategoriya_id):
    kategoriyalar = Kategoriya.objects.all()
    products = Gullar.objects.filter(kategoriya = kategoriya_id)
    products_by_categoes = {}



    for c in kategoriyalar:

        lst = []
        for p in products:
            if c == p.kategoriya:
                lst.append(p)
        if len(lst) != 0:          
            products_by_categoes[c.nomi] = lst
      
    context = {
        "kategoriyalar": kategoriyalar, 
        "products_by_categoes": products_by_categoes}
    return render(request, 'gul/maxway.html', context)


class CreateGullarView(CreateView):
    template_name = 'gul/create.html'
    form_class = CreateGullarForm
    success_url = ''

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['kategoriya'] = Kategoriya.objects.all()
        return context

class CreateKategoriyaView(CreateView):
    template_name = 'gul/create.html'
    form_class = CreateKategoriyaForm
    success_url = '/'

# Create your views here.
