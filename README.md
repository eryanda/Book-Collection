Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Link Tautan :

..............................

-   Membuat Proyek Django Baru

   Saya membuat proyek Django baru dengan nama "bookcollection".

   ```
   django-admin startproject bookcollection
   cd bookcollection
   ```

-   Membuat Aplikasi "main"

   Membuat sebuah aplikasi dengan nama "main" pada proyek "bookcollection".

   ```
   python manage.py startapp main
   ```

-   Konfigurasi Routing

   Konfigurasi routing dilakukan agar proyek dapat menjalankan aplikasi "main". Routing ini ditambahkan ke berkas `urls.py` pada proyek.

   ```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('main.urls')),
   ]
   ```

-   Membuat Model "Item"

   Dalam berkas `models.py` pada aplikasi "main", model "Item" dibuat dengan atribut yang sesuai:

   ```python
    class Product(models.Model):
        name = models.CharField(max_length=255)
        title = models.CharField(max_length=255, default="Title")
        amount = models.IntegerField()
        description = models.TextField()
   ```

-   Fungsi Views dan Template HTML

   Fungsi dibuat pada berkas `views.py` dalam aplikasi "main" untuk merender template HTML dengan informasi nama aplikasi dan nama serta kelas.

   ```python
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
   ```

-   Routing untuk View dan URL

   Dalam berkas `urls.py` pada aplikasi "main", routing ditambahkan yang menghubungkan view yang telah dibuat dengan URL yang sesuai:

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.display_info, name='display_info'),
   ]
   ```

-   Deployment ke Adaptable

   Jika semua step telah dilakukan, maka dapat dilakukan add, commit, dan push. Setelah semuanya berhasil, menghubungkan Adaptable dan GitHub dan mengikuti langkah di tutorial 0. Dan ketika repositori GitHub diperbarui, Adaptable secara otomatis akan melakukan deploy kembali

-   README.md

   Berkas `README.md` dibuat dengan informasi tentang cara menjalankan proyek ini, tautan ke aplikasi yang telah di-deploy di Adaptable, dan jawaban dari pertanyaan yang diberikan dalam checklist.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.