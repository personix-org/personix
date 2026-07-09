---
title: "Konsensus dan Proses Verifikasi"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: v1
---

# Konsensus dan Proses Verifikasi

Untuk membangun konsensus tentang aturan mana yang, secara rata-rata, harus dijunjung dan ditegakkan sebuah masyarakat, mekanisme berikut dapat membantu. Sebagai peserta DID, saya mendeklarasikan aturan yang saya langgani dan akan saya jalani, dan saya memublikasikannya. (Bayangkan itu seperti anggaran dasar dan anggaran rumah tangga yang, menurut saya, menyusun dunia ideal saya — dunia di mana saya tidak merasa dibatasi, melainkan aman.)

Saya dapat memperkirakan lebih dulu bagaimana kontak-kontak DID saya akan bereaksi — dan menilai seberapa kuat, dan oleh siapa, saya akan dikenai sanksi dalam interaksi sosial atau bisnis biasa, seandainya interaksi itu secara hipotetis terjadi.

Evaluasi definitif terjadi ketika Anda meminta informasi dari DID lain, atau meminta mereka memverifikasi sebuah klaim (atau meminta jasa suatu otoritas, dan seterusnya) yang ingin Anda publikasikan ke jaringan reputasi. Hasilnya seharusnya sama seperti ketika Anda menjalankan evaluasi itu sendiri, dalam mode simulasi (dry run), terhadap kebijakan yang dideklarasikan pihak lawan — dan jika tidak, ada yang tidak beres di pihak lawan: mereka mencoba memainkan permainan yang tidak jujur.

Hasilnya adalah entah penerimaan, dengan harga yang ditawarkan untuk verifikasi (dalam hal jasa verifikator atau otoritas), atau penolakan. Baik sanksi maupun bonus atas penyimpangan dari kebijakan sang penilai dilebur ke dalam harga yang ditawarkan. Peminta kemudian memutuskan apakah akan menerima syaratnya, atau melanjutkan ke putaran verifikasi berikutnya dalam algoritma alokasi — mengulang proses itu sampai puas, atau sampai perhitungan ekonominya membuat percuma untuk melanjutkan.

> [!note] Graf Sosial
> Jaringan reputasi, pertama dan terutama, adalah jaringan sosial. Anda menambahkan kontak — orang-orang yang menyetujui koneksi itu. Mereka punya kontak, dan kontak-kontak itu punya kontak. Algoritma mencari verifikator dalam kedalaman yang dapat dikonfigurasi (misalnya tiga tingkat: kontak langsung Anda, kontak mereka, dan satu tingkat lebih jauh). Tidak diperlukan blockchain global — jaringan secara alami membentuk komunitas dengan tumpang tindih ke komunitas lain.
>
> Algoritma bersifat non-deterministik: ia menghitung hash dokumen klaim Anda, memetakan hash itu ke sebuah posisi pada cincin identitas yang dikenal di dalam lingkaran ini, dan memilih yang terdekat sebagai kandidat verifikator. Anda tidak dapat memprediksi atau memengaruhi siapa yang akan memverifikasi klaim Anda.

Setiap penolakan verifikator memperbesar dokumen Anda dan menaikkan biaya pemrosesannya — itulah saluran biaya pertama (pertumbuhan dokumen). Setiap verifikator baru mengenakan imbalan berdasarkan volume data, reputasi Anda, dan seberapa jauh isi klaim Anda menyimpang dari kebijakan verifikasi yang mereka deklarasikan — itulah saluran biaya kedua (premi risiko). Dan setiap iterasi menghabiskan waktu dan energi — itulah saluran biaya ketiga.

> [!note] Apa yang Diperiksa Verifikator, secara Berurutan
> Setelah dipilih, seorang verifikator mengevaluasi klaim dalam kira-kira empat langkah berurutan — saringan termurah dulu, pemeriksaan isi yang mahal terakhir:
>
> 1. **Penyaringan kebijakan.** Apakah jenis klaim ini termasuk dalam apa yang diverifikasi verifikator secara publik? Jika tidak, permintaan langsung ditolak.
> 2. **Kepercayaan pada otoritas.** Apakah otoritas yang mendukung klaim itu cukup dipercaya menurut kebijakan yang dideklarasikan verifikator sendiri? Sebuah otoritas di bawah ambang kepercayaan verifikator adalah alasan penolakan terlepas dari isi klaimnya.
> 3. **Reputasi penerbit.** Apakah penerbit memenuhi ambang reputasi yang telah dideklarasikan verifikator untuk jenis klaim ini? Reputasi rendah bisa menaikkan imbalan atau memicu penolakan.
> 4. **Pemeriksaan isi.** Hanya ketika ketiga saringan pertama lolos, verifikator mengevaluasi klaimnya sendiri — tanda tangan, konsistensi internal, kebenaran formal, dan seberapa jauh ia menyimpang dari kebijakan verifikator. Imbalan yang dikenakan untuk langkah terakhir ini mencerminkan risiko sesungguhnya yang diambil.
>
> Verifikator memublikasikan kebijakan yang mengatur setiap saringan ini, sehingga langkah-langkahnya bukan kebijaksanaan mereka semata — mereka terikat oleh apa yang telah mereka deklarasikan. Penyimpangan dari kebijakan yang dipublikasikan itu sendiri merupakan klaim yang dapat dipublikasikan terhadap mereka, dan mereka membayarnya dengan reputasi mereka.

Hasilnya: memublikasikan klaim yang kredibel dan berguna nyaris tidak berbiaya. Memublikasikan klaim yang radikal berbiaya lebih. Memublikasikan kebohongan menjadi sangat mahal — Anda harus beriterasi dari verifikator ke verifikator, dan setiap yang menolak Anda menambah biaya. Pasar memberi harga pada klaim Anda, dan harga itu memberi tahu Anda di mana posisi Anda dalam kaitan dengan komunitas tempat Anda bergerak.

Tidak cukup mendeklarasikan bahwa Anda mematuhi suatu aturan padahal nyatanya tidak. Dalam hal itu, DID Anda berisiko dipublikasikannya catatan negatif yang membeberkan kemunafikan — yang mengubah Anda menjadi risiko bagi semua orang lain. Hasilnya seharusnya adalah aturan yang lebih sedikit tetapi lebih konsisten diikuti, dan pembersihan rimba hukum dan regulasi yang bahkan para profesional hukum pun nyaris tak mampu menavigasinya.

![KEMUNAFIKAN ADALAH PERILAKU PALING MAHAL](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Konsensus vs Akuntabilitas
> Agar jaringan berfungsi sebagai sumber informasi yang berharga, sebuah DID sebaiknya tidak terlalu radikal — jika tidak, yang lain akan menolaknya. Tekanan sosial akan mencari keseimbangan, dan upaya untuk mengacaukannya kemungkinan akan dihukum.

![DEKLARASIKAN ATURANMU, BAYAR HARGANYA](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] Jumlah Suara Tidak Sama dengan Bobot sebuah Suara
> Juraj Karpiš berkata bahwa "uang adalah memori perbuatan baik." Saya akan menambahkan bahwa reputasi adalah memori perbuatan buruk.
>
> Maka, secara meritokratis, siapa pun yang berkontribusi lebih banyak dan tidak punya reputasi buruk layak mendapat bobot suara yang lebih besar dalam komunitas. Dilihat melalui lensa hubungan bilateral: ketika saya menimbang tekanan konsensus mana yang harus saya akomodasi, bobot terbesar diberikan pada hubungan yang darinya saya memperoleh manfaat ekonomi terbesar. Sepuluh orang yang dengannya saya tidak punya perdagangan aktif akan memengaruhi saya jauh lebih sedikit daripada satu mitra bisnis permanen. Paradigma ini tidak terbatas pada perdagangan — ia meluas ke hubungan sosial, politik, dan lainnya.
