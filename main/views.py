from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Book',
        'title' : 'How to play Volley',
        'amount': 10,
        'description': '''Buku adalah Jendela Dunia'''
    }

    return render(request, "main.html", context)