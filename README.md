Membuat sebuah README.md yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Link Tautan :

   https://bookcollection.adaptable.app

-   Membuat Proyek Django Baru

   Saya membuat proyek Django baru dengan nama "bookcollection".

   ```
   django-admin startproject bookcollection

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

Berikut adalah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya:

sequenceDiagram

- Client ->> Server: HTTP request
- Server ->> urls.py: Mengambil URL yang sesuai dengan request
- urls.py ->> views.py: Menjalankan fungsi view yang sesuai
- views.py ->> models.py: Mengakses data dari model
- views.py ->> berkas html: Menghasilkan output HTML
- Server ->> Client: HTTP response

   Penjelasan:

1. Client mengirimkan request HTTP ke server
2. Server mengambil URL yang sesuai dengan request
3. Server menjalankan fungsi view yang sesuai dengan URL
4. Fungsi view mengakses data dari model
5. Fungsi view menghasilkan output HTML
6. Server mengirimkan response HTTP ke client

Berikut adalah penjelasan lebih lanjut tentang keterkaitan antara urls.py, views.py, models.py, dan berkas HTML:

   - urls.py adalah file yang berisi daftar URL yang dilayani oleh aplikasi. URL ini kemudian dipetakan ke fungsi view yang sesuai.
   - views.py adalah file yang berisi fungsi view yang digunakan untuk menangani request dari client. Fungsi view ini dapat mengakses data dari model dan menghasilkan output HTML.
   - models.py adalah file yang berisi model data aplikasi. Model data ini digunakan untuk menyimpan dan mengelola data aplikasi.
   - berkas HTML adalah file yang berisi kode HTML yang digunakan untuk menampilkan data kepada pengguna.

Dalam bagan tersebut, kita dapat melihat bahwa urls.py adalah titik awal dari request client. urls.py mengambil URL yang sesuai dengan request dan kemudian menjalankan fungsi view yang sesuai. Fungsi view ini kemudian mengakses data dari model dan menghasilkan output HTML. Output HTML ini kemudian dikirimkan kembali ke client sebagai response HTTP.

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

- Tujuan menggunakan virtual environment adalah untuk mengisolasi Python environment yang digunakan untuk setiap proyek atau aplikasi. Hal ini brtujuan agar : 
   1. Mencegah konflik paket Python yang berbeda
   2. Menjaga integritas sistem
   3. Mempermudah manajemen proyek
- Untuk membuat aplikasi web berbasis Django tanpa virtual environment tetap bisa dilakukan, akan tetapi akan menimbulkan beberapa masalah, antara lain:
   1. Kemungkinan konflik antar paket Python yang berbeda
   2. Kemungkinan rusaknya sistem
   3. Kesulitan dalam manajemen proyek

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

- MVC adalah pola arsitektur yang paling umum digunakan oleh para pengembang. Dalam pola ini, controller bertindak sebagai jembatan antara model dan view. Controller menerima input dari pengguna dan kemudian menggunakan model untuk memproses input tersebut. Controller kemudian menggunakan view untuk menampilkan hasil pemrosesan ke pengguna.
- MVT adalah varian dari pola MVC. Dalam pola ini, view juga bertanggung jawab untuk menangani input dari pengguna. View kemudian menggunakan model untuk memproses input tersebut dan menghasilkan output.
- MVVM adalah varian dari pola MVC yang lebih modern. Dalam pola ini, view dan model tidak berinteraksi langsung satu sama lain. View berinteraksi dengan view model, yang kemudian berinteraksi dengan model. Hal ini memungkinkan view untuk tetap terpisah dari model, sehingga view dapat lebih mudah diuji dan dirawat.
- Perbedaan di antara ketiganya terletak pada interaksi antara view dan model. Dalam MVC, view dan model berinteraksi langsung satu sama lain. Dalam MVT, view juga bertanggung jawab untuk menangani input dari pengguna. Dalam MVVM, view dan model tidak berinteraksi langsung satu sama lain, melainkan melalui view model.
