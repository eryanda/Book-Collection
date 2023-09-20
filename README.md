TUGAS 2

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
        title = models.CharField(max_length=255)
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


TUGAS 3

Checklist untuk tugas ini adalah sebagai berikut:

 v Membuat input form untuk menambahkan objek model pada app sebelumnya.

 v Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

 v Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

 v Menjawab beberapa pertanyaan berikut pada README.md pada root folder.

1. Apa perbedaan antara form POST dan form GET dalam Django?

      - **POST**: Metode ini digunakan untuk mengirimkan data secara langsung ke file lain. Data yang dikirimkan melalui metode ini biasanya bersifat penting atau rahasia, seperti kata sandi. Data yang dikirimkan tidak ditampilkan pada URL.

      - **GET**: Metode ini mengirimkan data secara tidak langsung. Data yang dikirimkan melalui metode ini akan ditampilkan pada URL dan dapat dilihat oleh orang lain. Metode ini biasanya digunakan untuk mengirimkan data yang tidak bersifat penting.

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

      - **XML**: XML (Extensible Markup Language) adalah format data yang fleksibel dan digunakan untuk mengelola dan menyimpan data. XML menggunakan struktur pohon dalam membentuk datanya dengan menggunakan tag dan atribut. XML memisahkan data dari HTML dan dapat digunakan dalam berbagai bahasa pemrograman seperti Java, Python, atau C. XML juga digunakan dalam web service, message passing, dan pembuatan dokumen¹.

      - **JSON**: JSON (JavaScript Object Notation) adalah format data yang ringan dan mudah dipahami oleh mesin dan manusia. JSON menggunakan struktur data yang mirip dengan objek-objek JavaScript. JSON biasanya digunakan dalam aplikasi web dan mobile untuk mengirim data dari server ke client. JSON mendukung semua browser dan sebagian besar teknologi backend mendukung JSON.

      - **HTML**: HTML (Hypertext Markup Language) adalah bahasa markup yang paling populer digunakan untuk membuat halaman web. HTML digunakan untuk membuat struktur dan tampilan halaman web. HTML tidak digunakan untuk mengelola atau menyimpan data.

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena beberapa alasan berikut:

   "1. **Ringan**: JSON adalah format data yang ringan dan mudah dipahami oleh mesin dan manusia. Hal ini memungkinkan data dikirim dengan cepat dan efisien melalui jaringan.

   2. **Mudah Diproses**: JSON menggunakan struktur data yang mirip dengan objek-objek JavaScript. Ini membuatnya mudah diproses dan dimanipulasi menggunakan JavaScript atau bahasa pemrograman lainnya.

   3. **Kompatibilitas**: JSON didukung oleh semua browser modern dan sebagian besar teknologi backend. Ini membuatnya menjadi pilihan yang baik untuk pertukaran data antara aplikasi web yang berbeda.

   4. **Pemahaman Manusia**: JSON menggunakan struktur data yang mirip dengan objek-objek JavaScript, sehingga mudah dipahami oleh pengembang. Ini memudahkan pengembang untuk membaca dan memahami data yang dikirim dan diterima oleh aplikasi web.

   5. **Fleksibilitas**: JSON dapat digunakan untuk mengirim data yang kompleks dan terstruktur. Ini memungkinkan pengembang untuk mengirim data yang lebih kompleks daripada format data lainnya seperti XML atau HTML."

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

   v Membuat input form untuk menambahkan objek model pada app sebelumnya.

   - Membuat berkas baru pada direktori main dengan nama forms.py untuk membuat struktur form yang dapat menerima data produk baru. Kemudian menambahkan kode berikut.

      ```python
      from django.forms import ModelForm
      from main.models import Product

      class ProductForm(ModelForm):
         class Meta:
            model = Product
            fields = ["genre", "title", "amount" ,"description"]

      ```
   v Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

   - Menambahkan 5 kode fungsi di bawah ini pada berkas views.py 

      ```python

      #HTML
      def show_main(request):        
         products = Product.objects.all()
         context = {
            'name': 'Eryanda Arian Rouuf',
            'class' : "PBP B",
            'products': products,
         }
         return render(request, "main.html", context)

      #XML
      def show_xml(request):
         data = Product.objects.all()
         return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

      #JSON
      def show_json(request):
         data = Product.objects.all()
         return HttpResponse(serializers.serialize("json", data), content_type="application/json")

      #XML by id
      def show_xml_by_id(request, id):
         data = Product.objects.filter(pk=id)
         return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

      #JSON by id
      def show_json_by_id(request, id):
         data = Product.objects.filter(pk=id)
         return HttpResponse(serializers.serialize("json", data), content_type="application/json")

      ```

   v Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2

   - Mengimport kode di bawah ini terlebih dulu sebelum melakukan routing URL

      ```python

      from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 

      ```
   - Kemudian membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2 tadi

      ```python

      urlpatterns = [
      path('', show_main, name='show_main'),
      path('xml/', show_xml, name='show_xml'),
      path('json/', show_json, name='show_json'),
      path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
      path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
      ]

      ```

5. Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

   ![alt text](https://github.com/eryanda/Book-Collection/blob/main/Pict/html.png?raw=true)
   ![alt text](https://github.com/eryanda/Book-Collection/blob/main/Pict/json.png?raw=true)
   ![alt text](https://github.com/eryanda/Book-Collection/blob/main/Pict/json_by_id.png?raw=true)
   ![alt text](https://github.com/eryanda/Book-Collection/blob/main/Pict/xml.png?raw=true)
   ![alt text](https://github.com/eryanda/Book-Collection/blob/main/Pict/xml_by_id.png?raw=true)
