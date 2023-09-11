from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Eryanda Arian R',
        'amount': '10',
        'description': '''Buku adalah Jendela Dunia'''
    }

    return render(request, "main.html", context)