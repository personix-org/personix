---
title: "Konsensus dan Proses Pengesahan"
chapter: 3
part: "Bagaimana Pengesahan Berfungsi"
lang: en
version: v6
source: v1
---

# Konsensus dan Proses Pengesahan

Untuk membina konsensus tentang peraturan mana yang secara purata patut dijunjung dan dikuatkuasakan oleh sesebuah masyarakat, mekanisme berikut boleh membantu. Sebagai peserta DID, saya mengisytiharkan peraturan yang saya langgani dan akan jalani, dan saya menerbitkannya. (Anggaplah ia sebagai undang-undang kecil dan perlembagaan yang, pada pandangan saya, membentuk dunia ideal saya — sebuah dunia di mana saya tidak berasa dikekang, tetapi selamat.)

Saya boleh menganggarkan terlebih dahulu bagaimana kenalan DID saya akan bertindak balas — dan menilai betapa kuat, dan oleh siapa, saya akan dikenakan sekatan dalam interaksi sosial atau perniagaan biasa, sekiranya ia secara hipotetis berlaku.

Penilaian yang muktamad berlaku apabila anda meminta maklumat daripada DID lain, atau meminta mereka mengesahkan sesuatu tuntutan (atau meminta perkhidmatan daripada sesuatu autoriti, dan sebagainya) yang anda mahu terbitkan ke rangkaian reputasi. Ia sepatutnya ternyata sama seperti apabila anda menjalankan penilaian itu sendiri, dalam larian kering (dry run), terhadap polisi yang diisytiharkan pihak lawan — dan jika ia tidak begitu, ada sesuatu yang tidak kena pada pihak lawan: mereka cuba bermain permainan yang tidak jujur.

Hasilnya sama ada penerimaan, dengan harga yang disebut bagi pengesahan (dalam kes perkhidmatan pengesah atau autoriti), atau penolakan. Kedua-dua sekatan dan bonus bagi penyimpangan daripada polisi penilai dimasukkan ke dalam harga yang disebut. Pemohon kemudian memutuskan sama ada untuk menerima terma itu, atau beralih ke pusingan pengesahan seterusnya dalam algoritma peruntukan — mengulangi proses itu sehingga berpuas hati, atau sehingga ekonomi menjadikannya tidak berbaloi untuk diteruskan.

> [!note] Graf Sosial
> Rangkaian reputasi ialah, pertama sekali, sebuah rangkaian sosial. Anda menambah kenalan — orang yang bersetuju dengan sambungan itu. Mereka mempunyai kenalan, dan kenalan itu mempunyai kenalan. Algoritma mencari pengesah dalam kedalaman yang boleh dikonfigurasi (cth., tiga peringkat: kenalan langsung anda, kenalan mereka, dan satu peringkat di sebalik itu). Tiada blockchain global diperlukan — rangkaian secara semula jadi membentuk komuniti dengan pertindihan ke dalam komuniti lain.
>
> Algoritma bersifat tidak berketentuan: ia meng-hash dokumen tuntutan anda, memetakan hash itu ke sesuatu kedudukan pada gelang identiti yang diketahui dalam lingkaran ini, dan memilih yang terdekat sebagai calon pengesah. Anda tidak boleh meramal atau mempengaruhi siapa yang akan mengesahkan tuntutan anda.

Setiap penolakan pengesah membesarkan dokumen anda dan meningkatkan kos pemprosesannya — itulah saluran kos pertama (pertumbuhan dokumen). Setiap pengesah baharu mengenakan fi berdasarkan jumlah data, reputasi anda, dan sejauh mana kandungan tuntutan anda menyimpang daripada polisi pengesahan yang diisytiharkan mereka — itulah saluran kos kedua (premium risiko). Dan setiap lelaran memakan masa dan tenaga — saluran kos ketiga.

> [!note] Apa yang Diperiksa Pengesah, Mengikut Urutan
> Setelah dipilih, seorang pengesah menilai sesuatu tuntutan dalam lebih kurang empat langkah yang berurutan — penapis yang paling murah dahulu, pemeriksaan kandungan yang mahal terakhir:
>
> 1. **Pengehadan polisi.** Adakah jenis tuntutan ini termasuk dalam apa yang disahkan pengesah secara terbuka? Jika tidak, permintaan ditolak terus.
> 2. **Kepercayaan autoriti.** Adakah autoriti yang menyokong tuntutan itu cukup dipercayai di bawah polisi yang diisytiharkan pengesah sendiri? Sesuatu autoriti di bawah ambang kepercayaan pengesah menjadi alasan penolakan tanpa mengira kandungan tuntutan.
> 3. **Reputasi pengeluar.** Adakah pengeluar memenuhi ambang reputasi yang diisytiharkan pengesah bagi jenis tuntutan ini? Reputasi yang rendah mungkin sama ada menaikkan fi atau mencetuskan penolakan.
> 4. **Pemeriksaan kandungan.** Hanya apabila tiga pintu pertama lulus barulah pengesah menilai tuntutan itu sendiri — tandatangan, kekonsistenan dalaman, ketepatan formal, dan sejauh mana ia menyimpang daripada polisi pengesah. Fi yang dikenakan bagi langkah terakhir ini mencerminkan risiko sebenar yang diambil.
>
> Pengesah menerbitkan polisi yang mengawal setiap pintu ini, jadi langkah-langkah itu bukan atas budi bicara mereka — mereka terikat dengan apa yang telah mereka isytiharkan. Penyimpangan daripada polisi yang diterbitkan itu sendiri ialah tuntutan yang boleh diterbitkan terhadap mereka, dan mereka membayarnya dengan reputasi mereka.

Hasilnya: menerbitkan tuntutan yang boleh dipercayai dan berguna hampir tidak berkos apa-apa. Menerbitkan tuntutan yang radikal berkos lebih. Menerbitkan pembohongan menjadi sangat mahal sehingga menghalang — anda mesti melelar melalui pengesah demi pengesah, dan setiap yang menolak anda menambah kos. Pasaran meletakkan harga pada tuntutan anda, dan harga itu memberitahu anda di mana anda berdiri berbanding komuniti tempat anda bergerak.

Tidak cukup untuk mengisytiharkan bahawa anda mematuhi sesuatu peraturan sedangkan pada hakikatnya anda tidak. Dalam kes itu, DID anda berisiko diterbitkan rekod negatif yang mendedahkan sikap munafik itu — yang menjadikan anda risiko bagi semua orang lain. Hasilnya sepatutnya lebih sedikit tetapi peraturan yang lebih konsisten dipatuhi, dan pembersihan rimba undang-undang dan peraturan yang para profesional undang-undang pun hampir tidak dapat menavigasinya.

![HYPOCRISY IS THE MOST EXPENSIVE BEHAVIOR](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Konsensus lawan Kebertanggungjawaban
> Supaya rangkaian berfungsi sebagai sumber maklumat yang bernilai, sesuatu DID tidak sepatutnya terlalu radikal — jika tidak, yang lain akan menolaknya. Tekanan sosial akan mencari keseimbangan, dan cubaan untuk mengganggu kestabilannya berkemungkinan akan dihukum.

![DECLARE YOUR RULES, PAY THE PRICE](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] Bilangan Undi Tidak Sama dengan Bobot Suara
> Juraj Karpiš berkata bahawa "wang ialah ingatan perbuatan baik." Saya menambah bahawa reputasi ialah ingatan perbuatan buruk.
>
> Ia berikutan bahawa, secara meritokratik, sesiapa yang menyumbang lebih dan tidak mempunyai reputasi buruk berhak mendapat bobot suara yang lebih besar dalam komuniti. Dilihat melalui kanta hubungan dua hala: apabila saya menimbang tekanan konsensus mana yang perlu diakomodasi, bobot terbesar diberikan kepada hubungan yang daripadanya saya memperoleh manfaat ekonomi terbesar. Sepuluh orang yang dengannya saya tidak mempunyai perdagangan aktif akan mempengaruhi saya jauh lebih kurang daripada seorang rakan perniagaan tetap. Paradigma ini tidak terhad kepada perdagangan — ia meluas ke hubungan sosial, politik dan lain-lain.
