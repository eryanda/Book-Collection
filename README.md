**TUGAS 2**

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


**TUGAS 3**

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

   - **Ringan**: JSON adalah format data yang ringan dan mudah dipahami oleh mesin dan manusia. Hal ini memungkinkan data dikirim dengan cepat dan efisien melalui jaringan.

   - **Mudah Diproses**: JSON menggunakan struktur data yang mirip dengan objek-objek JavaScript. Ini membuatnya mudah diproses dan dimanipulasi menggunakan JavaScript atau bahasa pemrograman lainnya.

   - **Kompatibilitas**: JSON didukung oleh semua browser modern dan sebagian besar teknologi backend. Ini membuatnya menjadi pilihan yang baik untuk pertukaran data antara aplikasi web yang berbeda.

   - **Pemahaman Manusia**: JSON menggunakan struktur data yang mirip dengan objek-objek JavaScript, sehingga mudah dipahami oleh pengembang. Ini memudahkan pengembang untuk membaca dan memahami data yang dikirim dan diterima oleh aplikasi web.

   - **Fleksibilitas**: JSON dapat digunakan untuk mengirim data yang kompleks dan terstruktur. Ini memungkinkan pengembang untuk mengirim data yang lebih kompleks daripada format data lainnya seperti XML atau HTML.

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


**TUGAS 4**

Checklist untuk tugas ini adalah sebagai berikut:

 v Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

 v Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

 v Menghubungkan model Item dengan User.

 v Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

 Menjawab beberapa pertanyaan berikut pada README.md pada root folder (silakan modifikasi README.md yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas).

 1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

   - **Django UserCreationForm** adalah sebuah formulir yang disediakan oleh Django untuk memudahkan proses pembuatan pengguna baru dalam aplikasi web. Formulir ini memungkinkan pengguna untuk memasukkan informasi seperti nama pengguna dan kata sandi, serta memvalidasi input tersebut sebelum menyimpannya ke dalam basis data.

   - Kelebihan dari **Django UserCreationForm** antara lain:

      a. **Mudah digunakan**: Formulir ini telah disediakan oleh Django dan dapat digunakan langsung tanpa perlu menulis kode tambahan.

      b. **Validasi otomatis**: Formulir ini secara otomatis memvalidasi input pengguna, seperti memastikan kata sandi yang dimasukkan cukup kuat dan memeriksa apakah nama pengguna sudah digunakan sebelumnya.

      c. **Integrasi dengan Django**: Formulir ini terintegrasi dengan baik dengan fitur otentikasi dan otorisasi Django, sehingga memudahkan pengembangan aplikasi web yang aman dan terpercaya.

   - Namun, **Django UserCreationForm** juga memiliki beberapa kekurangan, antara lain:

      a. **Keterbatasan fungsionalitas**: Formulir ini hanya menyediakan fitur dasar untuk pembuatan pengguna baru. Jika Anda membutuhkan fungsionalitas tambahan, seperti mengumpulkan informasi tambahan dari pengguna, Anda perlu menyesuaikan formulir ini atau membuat formulir kustom.

      b. **Tampilan bawaan yang sederhana**: Formulir ini tidak menyediakan tampilan yang sangat menarik secara default. Jika Anda menginginkan tampilan yang lebih menarik, Anda perlu menyesuaikan tampilan formulir menggunakan HTML dan CSS.

 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

   - Dalam konteks Django, **autentikasi** adalah proses untuk memverifikasi identitas pengguna yang mencoba mengakses sistem aplikasi. Autentikasi memastikan bahwa pengguna adalah siapa yang mereka klaim dan memungkinkan mereka untuk masuk ke dalam sistem. Di sisi lain, **otorisasi** adalah proses untuk menentukan apa yang pengguna diizinkan lakukan setelah mereka diautentikasi. Otorisasi memeriksa hak akses pengguna terhadap sumber daya atau fungsi tertentu dalam aplikasi.

   - Kedua konsep ini penting dalam Django karena:

      a. **Autentikasi** memastikan bahwa hanya pengguna yang sah yang dapat mengakses sistem. Ini membantu melindungi data dan mencegah akses yang tidak sah.

      b. **Otorisasi** memastikan bahwa pengguna hanya dapat melakukan tindakan yang sesuai dengan peran dan izin mereka. Ini membantu menjaga keamanan dan integritas sistem dengan membatasi akses ke sumber daya yang sensitif.

   - Dalam kombinasi, autentikasi dan otorisasi membantu menjaga keamanan dan privasi pengguna, serta mencegah penyalahgunaan dan kerusakan pada sistem aplikasi.

 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

   - **Cookies** adalah file teks kecil yang disimpan pada komputer pengguna ketika mereka mengunjungi situs web. Cookies digunakan untuk menyimpan informasi tentang pengguna, seperti preferensi dan riwayat aktivitas, dan memungkinkan situs web untuk mengenali pengguna ketika mereka kembali ke situs tersebut. 

   - Dalam konteks Django, cookies digunakan untuk mengelola data sesi pengguna. Django membuat dan menyimpan cookie sesi, mengirimkannya ke server saat pengguna berinteraksi dengan situs web, dan digunakan untuk mengidentifikasi dan menyimpan data sesi pengguna. Penggunaan cookies memungkinkan pengalaman pengguna yang lebih baik, meskipun harus memperhatikan masalah keamanan seperti serangan XSS.

 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

   - Penggunaan cookies dalam pengembangan web memiliki beberapa risiko potensial yang harus diwaspadai. Beberapa risiko tersebut antara lain:

      a. **Kerentanan terhadap serangan XSS**: Cookies dapat digunakan untuk menyimpan informasi sensitif, seperti token otentikasi, yang dapat digunakan oleh penyerang untuk melakukan serangan cross-site scripting (XSS).

      b. **Pelacakan pengguna**: Cookies pihak ketiga dapat digunakan untuk melacak aktivitas pengguna di seluruh situs web dan melintasi domain.

      c. **Pelanggaran privasi**: Cookies dapat digunakan untuk mengumpulkan informasi pribadi tentang pengguna, seperti preferensi dan riwayat aktivitas, yang dapat digunakan untuk tujuan yang tidak diinginkan.

   - Namun, penggunaan cookies juga memiliki manfaat, seperti memungkinkan situs web untuk menyimpan preferensi pengguna dan menyediakan pengalaman yang disesuaikan. Untuk meminimalkan risiko, pengembang web harus memperhatikan praktik keamanan terbaik, seperti mengenkripsi data cookies dan membatasi penggunaan cookies pihak ketiga .

 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

 - Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

   a. Menambahkan kode program di bawah ini pada berkas views.py di subdirektori main/templates

   ```python

   def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

   def login_user(request):
      if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = authenticate(request, username=username, password=password)
         if user is not None:
               login(request, user)
               response = HttpResponseRedirect(reverse("main:show_main")) 
               response.set_cookie('last_login', str(datetime.datetime.now()))
               return response
         else:
               messages.info(request, 'Lu salah masukin password sama username kawan')
      context = {}
      return render(request, 'login.html', context)

   def logout_user(request):
      logout(request)
      response = HttpResponseRedirect(reverse('main:login'))
      response.delete_cookie('last_login')
      return response
   
   ```
 - Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

   ![alt text](https://github.com/eryanda/Book-Collection/blob/main/Pict/bookCollection_1.png?raw=true)
   ![alt text](https://github.com/eryanda/Book-Collection/blob/main/Pict/bookCollection_2.png?raw=true)

 - Menghubungkan model Item dengan User.

   a. Untuk menghubungkan model ke user, pertama melakukan import di bawah ini

   ```python
   from django.contrib.auth.models import User
   ```
   b. Selanjutnya menambahkan potongan kode ini di berkas models.py

   ```python
   class Product(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
   ```

   c. Mengubah dua fungsi di berkas views.py seperti di bawah ini

   ```python
   def show_main(request):
    products = Product.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'class' : "PBP B",
        'products': products,
        'last_login': request.COOKIES['last_login'],
        'add_amount': add_amount,
        'sub_amount': sub_amount,
    }

    return render(request, "main.html", context)

   def create_product(request):
      form = ProductForm(request.POST or None)

      if form.is_valid() and request.method == "POST":
         product = form.save(commit=False)
         product.user = request.user
         product.save()
         return HttpResponseRedirect(reverse('main:show_main'))

      context = {'form': form}
      return render(request, "create_product.html", context)
   ```
   d. Dan yang terakhir adalah menjalankan 2 perintah di bawah ini:
   - python manage.py makemigrations --> pencet 1 + enter + 1 + enter jika terjadi error saat menjalankan perintah ini
   - python manage.py migrate

 - Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

   a. Mengimport kode di bawah ini ke berkas views.py
   ```python
   import datetime
   from django.http import HttpResponseRedirect
   from django.urls import reverse
   ```

   b. Memodifikasi fungsi login_user seperti di bawah ini pada berkas views.py
   ```python
   def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Lu salah masukin password sama username kawan')
    context = {}
    return render(request, 'login.html', context)
   ```

   c. Menambahkan kode di bawah ini pada fungsi show_main pada berkas views.py
   ```python
   'last_login': request.COOKIES['last_login'],
   ```

   d. Mengubah fungsi logout_user seperti di bawah ini pada berkas views.py
   ```python
   'last_login': request.COOKIES['last_login'],
   ```
   
   e. Menambahkan potongan kode di bawah ini pada berkas main.html
   ```html
   <h5>Sesi terakhir login: {{ last_login }}</h5>
   ```

   f. Berikut tampilan detailnya
   ![alt text](https://github.com/eryanda/Book-Collection/blob/main/Pict/bookCollection_3.png?raw=true)