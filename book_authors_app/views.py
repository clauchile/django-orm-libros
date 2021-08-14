from django.shortcuts import render, redirect
from .models import Author, Book

def index(request):
   
    if request.method == 'GET':

        print(Book)
    
        context = {
            'libros': Book.objects.all(),
        }
        print('libros.title')
        return render(request, 'index.html', context)

    if request.method == 'POST':
            print("metodo post")
        
            # print(request.POST)
            u = Book.objects.create(
                title = request.POST ['titulo'],
                desc = request.POST ['descript'],
            )
            return redirect("/")

def books(request, dato):
   
    if request.method == 'GET':
        autoresExcluidos = Author.objects.exclude( books = Book.objects.get(id=dato))
        print(request.GET)
    
        context = {
            'libros': Book.objects.get(id =dato),
            'autores': Author.objects.all(),
            'no_tiene_autores' : autoresExcluidos
        }
        # print(dato)
        # print('autor.first_name')
        print(autoresExcluidos)
        return render(request, 'books.html', context)        

    if request.method == 'POST':
        print(request.POST)
        libro =Book.objects.get(id=dato)
        autor= Author.objects.get(id=request.POST['autor'])
        # autores = libro.
        libro.authors.add(autor)

        return redirect(f"/books/{dato}")

def authors(request):
     
    if request.method == 'GET':

        print(Book)
    
        context = {
            'autores': Author.objects.all(),
        }
        print(Author.objects.all())
        return render(request, 'authors.html', context)

    if request.method == 'POST':
            print("metodo post")
        
            # print(request.POST)
            a = Author.objects.create(
                first_name = request.POST ['nombre'],
                last_name = request.POST ['apellido'],
                notas = request.POST ['txtnotas'],

            )
            return redirect("/authors")    
def authorsid(request, dato):
   
    if request.method == 'GET':
        # autores2 = Book.objects.get(id =dato).authors.all()
        print(request.GET)
        excluidos = Book.objects.exclude( authors =  Author.objects.get(id=dato))
        context = {
            'autores': Author.objects.get(id =dato),
            # 'autores2': Book.objects.get(id =dato).authors.all(),
            'libros': Book.objects.all(),

            'no_tiene': excluidos
            
        }
        print(excluidos)
        # print(Book.objects.get(id =dato).authors.all())
        # print(dato)
        # print(Author.objects.exclude(id__in=autores2.values_list('id',flat=True)))
       
        return render(request, 'authors_desc.html', context)        

    if request.method == 'POST':
        print(request.POST)
        autor =Author.objects.get(id=dato)
        libro= Book.objects.get(id=request.POST['libro'])
        # autores = libro.
        autor.books.add(libro)
        # libro.authors.add(autor)

        return redirect(f"/authors/{dato}")