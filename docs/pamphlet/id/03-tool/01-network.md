---
title: "Jaringan Sosial Berbasis Reputasi"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: v1
---

# Jaringan Sosial Berbasis Reputasi

Untuk mewujudkan perubahan, kita membutuhkan sebuah perkakas yang dirancang dengan cermat. Pertama-tama kita akan menggambarkannya secara singkat; dalam bab-bab berikutnya kita akan mengkaji setiap bagiannya secara lebih rinci dan menambahkan yang lain. Bayangkan sebuah jaringan sosial global, terdesentralisasi, dan tidak dapat disensor, di mana Anda dapat dengan aman menciptakan dan mengelola identitas proksi Anda — yang disebut Decentralized Identity (DID). DID adalah identitas digital yang Anda ciptakan dan kendalikan sendiri, tanpa ketergantungan pada otoritas pusat mana pun. Tidak ada yang dapat merampasnya atau memalsukannya, karena ia ditandatangani secara kriptografis dengan kunci privat Anda (atau beberapa kunci, melalui multisig).

> [!note] Catatan
> Salah satu implikasinya adalah bahwa identitas semacam itu dapat secara bertahap menggantikan dokumen identifikasi yang diterbitkan negara — tetapi lebih lanjut mengenai itu dalam bab tentang transisi.

![IDENTITAS ANDA, KUNCI ANDA, ATURAN ANDA](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

Dalam jaringan semacam itu, Anda dapat melaporkan melalui identitas Anda bahwa seseorang telah menimbulkan kerugian pada Anda (dan kemudian, mungkin, bahwa mereka telah memulihkannya atau dipaksa untuk melakukannya). Agar umpan balik ini — yang ditujukan kepada pihak yang menimbulkan kerugian — memiliki nilai sebagai sumber yang relevan, memasukkan informasi ke dalam jaringan haruslah menghabiskan waktu, energi, dan uang — dan di atas itu, harus dihasilkan bukti yang dapat diverifikasi bagi orang lain bahwa ini bukan sekadar obrolan iseng.

Membaca informasi akan mudah dan relatif murah, tetapi membuat catatan individual akan mahal dan menuntut usaha. Menulis akan mengikuti protokol yang jelas, di mana komputasi menurut algoritma yang dipilih secara ketat menentukan DID mana yang harus diminta untuk memverifikasi informasi yang diajukan dan bagaimana melangkah lebih jauh sehingga peserta terpilih memproses informasi atas nama Anda, memublikasikannya, dan menjadi verifikatornya.

> [!note] Algoritma vs radikalisme
> Pemilihan verifikator secara algoritmis memastikan bahwa para pemublikasi informasi yang tidak radikal, seiring waktu, akan mempertahankan keseimbangan yang nyaris netral antara biaya informasi yang dipublikasikan dan imbalan atas verifikasi.

![MEMUBLIKASIKAN MENGHABISKAN WAKTU, ENERGI, DAN UANG](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Mari kita lihat bagaimana algoritma memilih seorang verifikator.

> [!note] Algoritma
> Pemilihan algoritmis secara non-deterministik memilih verifikator yang berbeda (atau sekumpulan verifikator yang mungkin) untuk potongan informasi yang berbeda. Sebuah hash (fungsi matematis satu arah yang menghasilkan "sidik jari" unik dari masukan apa pun — seperti sidik jari sebuah dokumen) dari keseluruhan dokumen DID menentukan posisi pada cincin hash yang konsisten dan memilih kandidat verifikator.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> Dalam bahasa sederhana: algoritma mengambil seluruh dokumen DID Anda, menghitung sidik jari darinya, dan sidik jari itu menentukan verifikator Anda.

![BAGAIMANA ALGORITMA MEMILIH VERIFIKATOR ANDA](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Dengan verifikator pertama yang dipilih algoritma, Anda sebagai pemublikasi mungkin tidak berhasil — reputasi Anda atau pengaturan yang Anda deklarasikan mungkin tidak memenuhi persyaratan mereka. Anda akan secara algoritmis melanjutkan pencarian ke verifikator berikutnya dengan melakukan iterasi rekursif lain, yang menugaskan Anda seorang verifikator lagi. Pada setiap langkah, "jarak" ke verifikator sasaran bertambah, dan demikian pula metadata pendamping yang harus dipublikasikan. Seiring bertambahnya data, biaya secara alami naik (tidak hanya karena ukuran awal klaim, tetapi juga karena metadata yang menumpuk pada setiap penolakan). Informasi yang kredibel lolos jauh lebih mudah daripada kehendak yang tidak masuk akal. Terserah masing-masing orang seberapa tinggi harga yang bersedia mereka tanggung dan seberapa penting catatan itu bagi mereka — radikalisme dijamin akan menjadi mahal.

![BAGAIMANA VERIFIKATOR MENJAWAB](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Apa pun yang diputuskan verifikator sebagai tanggapan atas permintaan verifikasi Anda, bola kembali ke tangan pemublikasi: mereka dapat menerima tawaran verifikator untuk layanan verifikasi, memasukkan tanggapan itu ke dalam kronologi dan mencoba lagi (dengan biaya lebih mahal), atau berjalan pergi dan menelan biaya yang telah hangus.

![PILIHAN SANG PENERBIT](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Untuk memberi informasi Anda bobot yang lebih besar dan peluang penerimaan yang lebih baik di mata para verifikator, Anda — sebagai pemublikasi yang berkepentingan atas informasi yang diterbitkan — dapat menggunakan jasa **otoritas tepercaya**. Otoritas itu bisa menolak informasi yang diajukan atau menerimanya dan mempertaruhkan nama baiknya (reputasinya) untuk itu. Otoritas biasanya meminta bukti dari dunia nyata, memverifikasinya, dan mengklasifikasikannya. Keluarannya adalah protokol penilaiannya atas kasus tertentu pada waktu tertentu. Bayangkan otoritas sebagai spesialis dalam jenis layanan tertentu, baik di dunia nyata maupun digital — misalnya seorang penyelidik, auditor, penanggung asuransi, pemasok kelas barang tertentu (pada intinya, pelaku ekonomi mana pun di pasar).

![BAGAIMANA SEBUAH CATATAN TERCIPTA DALAM JARINGAN](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Pada saat Anda mencoba memublikasikan informasi ke dalam jaringan, jaringan itu kemungkinan sudah memuat informasi tentang para pelakunya — inilah sinyal-sinyal reputasi. Menavigasi cara membaca sinyal reputasi — apa artinya bagi Anda dalam situasi berbeda dan risiko apa yang dibawanya — mungkin tidak sepele. Setiap peserta dapat memandang catatan reputasi secara berbeda melalui DID mereka, tergantung situasi yang mereka hadapi terkait pihak lawan. Apakah pihak lawan adalah pembayar yang dapat diandalkan, atau saya perlu meminta uang di muka untuk sebuah transaksi bisnis? Apakah produk yang ditawarkan memiliki ulasan tentang penipuan atau cacat yang tersembunyi? Apakah mereka mencoba mengelak dari tanggung jawab kontraktual ketika terjadi masalah? Kadang pandangan yang lebih kompleks tentang keseluruhan konsistensi pihak lawan berguna — itu tergantung preferensi siapa pun yang meminta ikhtisar tersebut. Pasar dapat menawarkan produk dan layanan yang menyederhanakan, mengolah, dan menjernihkan pembacaan reputasi dalam konteks situasi yang dihadapi. Berbagai otoritas dan layanan yang mereka tawarkan juga dapat melayani tujuan ini.

![CARA MEMBACA REPUTASI](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Contoh
> Informasi tipikal yang menarik bagi para pemublikasi — dan berharga bagi orang lain — menyangkut peristiwa di luar komunikasi antarpribadi biasa di dunia nyata atau virtual.
>
> Contoh negatif:
> - bukti tindak pidana (misalnya diaudit oleh badan penyelidik tepercaya)
> - bukti tidak langsung (lemah jika berdiri sendiri, tetapi kumulatif secara statistik) — misalnya kehadiran berulang di dekat beberapa pencurian dalam waktu singkat → masihkah itu kebetulan?
> - pelanggaran kontrak
>
> Contoh positif:
> - kerugian yang telah dipulihkan (secara sukarela atau di bawah tekanan komunitas sebagai hukuman)
> - penerimaan dan penjalanan hukuman yang diusulkan oleh otoritas X
> - otoritas X mencabut pengakuan atas hak milik pelaku sampai batas tertentu
>
> Terserah masing-masing orang untuk mengumpulkan informasi yang tersedia tentang pihak lawan dan menilai risikonya menurut preferensi mereka.

![APA YANG DAPAT ANDA CATAT DALAM JARINGAN?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Apakah informasi tentang Anda muncul dalam jaringan bergantung secara eksklusif pada perilaku Anda sendiri.
> Anda tidak pernah harus bergabung dengan jaringan semacam itu, namun informasi tentang Anda tetap dapat muncul di dalamnya. Itu bergantung secara eksklusif pada tindakan Anda dan dampak yang ditimbulkannya terhadap orang lain.

![KOMUNITAS DAPAT MEMBUKAKAN SATU UNTUK ANDA](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

Apa yang baru saja saya gambarkan secara singkat adalah bagaimana sebuah jaringan sosial yang terinspirasi oleh Decentralized Identity (DID) dapat bekerja. Tujuan utama konsep DID adalah memperkuat privasi dan kebebasan melalui prinsip berlangganan aturan yang akan saya ikuti dan jalani — memberi pengguna kemampuan untuk memutuskan informasi apa yang akan dibagikan dan dalam kondisi apa.

Saya mengusulkan untuk lebih jauh menghubungkan DID-DID ke dalam sebuah jaringan komunikasi di mana para pemegangnya saling bertukar umpan balik bahkan di luar situasi ketika sesuatu telah menimpa seseorang dan komunitas atau individu perlu bereaksi. Perbandingan preventif semacam itu atas aturan yang telah kita langgani — dengan opsi untuk menghitung konsekuensi ekonomi dan lainnya dari penyimpangan timbal balik dalam ekspektasi tentang bagaimana pihak lain seharusnya beroperasi — dapat dianggap sebagai motivasi untuk menemukan konsensus. Alih-alih kebebasan, sistem semacam itu akan menekankan pengambilan keputusan secara sukarela yang dipadukan dengan tanggung jawab atas perilaku di dunia nyata.

Seorang individu tidak dapat mematahkan sistem sendirian — sekelompok orang punya peluang lebih besar, dan sekelompok orang dengan konsensus yang dirundingkan serta motivasi untuk bahu-membahu dalam banyak isu punya peluang yang lebih besar lagi untuk melawan kecenderungan otoritarian. Prasyarat pengorganisasian dari bab pertama akan terpenuhi begitu dua syarat tercapai: jaringan reputasi DID mencakup komunitas-komunitas secara cukup representatif sehingga penggunaannya tidak lagi eksotis. Dan pada saat yang sama, segmen komunitas ini menjadi minoritas yang signifikan secara ekonomi yang dapat berunding dengan tegas dengan masyarakat lainnya.

> [!note] Kesukarelaan vs kebebasan
> Kebebasan — dalam arti positif — akan menjadi efek sekunder dari penyeimbangan dua faktor: kesukarelaan dan tekanan lingkungan seseorang menuju tanggung jawab.

> [!note] Era AI dan Nilai Reputasi
> Di era kecerdasan buatan, segala hal yang terkait dengan pemikiran kognitif sedang diotomatiskan — dan mungkin bisa lebih jauh lagi. Lalu apa yang tersisa dalam aktivitas manusia sebagai keunggulan kompetitif? Jawabannya sulit, dan sesuatu pasti akan ditemukan, tetapi satu hal dapat kita katakan dengan pasti: reputasi akan menentukan. Riwayat perilaku Anda yang dapat diverifikasi, komitmen Anda dan pemenuhannya — itulah sesuatu yang tidak akan dibangun AI untuk Anda.

![AI TIDAK DAPAT MEMBANGUN REPUTASI ANDA — HANYA ANDA YANG BISA](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![EKONOMI KEBENARAN](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
