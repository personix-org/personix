---
title: "Rangkaian Sosial Berasaskan Reputasi"
chapter: 2
part: "Alat Itu"
lang: en
version: v6
source: v1
---

# Rangkaian Sosial Berasaskan Reputasi

Untuk membawa perubahan, kita memerlukan sebuah alat yang direka dengan teliti. Mula-mula kita akan melakarkannya secara ringkas; dalam bab-bab kemudian kita akan meneliti setiap bahagian dengan lebih terperinci dan menambah lagi. Bayangkan sebuah rangkaian sosial yang tidak boleh ditapis, global, dan terdesentralisasi di mana anda boleh dengan selamat mencipta dan menguruskan identiti proksi anda — apa yang dipanggil Identiti Terdesentralisasi (DID). DID ialah identiti digital yang anda cipta dan kawal sendiri, tanpa bergantung pada mana-mana autoriti pusat. Tiada siapa yang boleh merampasnya atau memalsukannya, kerana ia ditandatangani secara kriptografi dengan kunci peribadi anda (atau kunci-kunci, melalui multisig).

> [!note] Nota
> Satu implikasinya ialah identiti sebegini boleh secara beransur-ansur menggantikan dokumen pengenalan yang dikeluarkan negara — tetapi lebih lanjut tentang itu dalam bab mengenai peralihan.

![YOUR IDENTITY, YOUR KEYS, YOUR RULES](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

Dalam rangkaian sebegini, anda boleh melaporkan melalui identiti anda bahawa seseorang telah menyebabkan kemudaratan kepada anda (dan kemudian, berkemungkinan, bahawa mereka telah membetulkannya atau dipaksa berbuat demikian). Supaya maklum balas ini — yang ditujukan kepada punca kemudaratan — mempunyai nilai sebagai sumber yang relevan, memasukkan maklumat ke dalam rangkaian mesti memakan masa, tenaga, dan wang — dan di samping itu, bukti yang boleh disahkan mesti dihasilkan untuk orang lain bahawa ini bukanlah leteran kosong.

Membaca maklumat adalah mudah dan agak murah, tetapi mencipta satu rekod individu adalah mahal dan menuntut. Penulisan mengikuti protokol yang jelas, di mana pengiraan menurut algoritma yang dipilih menentukan secara ketat DID mana yang perlu diminta untuk mengesahkan maklumat yang dikemukakan dan bagaimana untuk meneruskannya supaya peserta yang dipilih memproses maklumat bagi pihak anda, menerbitkannya, dan menjadi pengesahnya.

> [!note] Algoritma lawan radikalisme
> Pemilihan pengesah secara algoritma memastikan bahawa penerbit maklumat yang tidak radikal, dari masa ke masa, akan mengekalkan keseimbangan yang hampir neutral antara kos maklumat yang diterbitkan dan ganjaran bagi pengesahan.

![PUBLISHING COSTS TIME, ENERGY, AND MONEY](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Mari kita lihat bagaimana algoritma memilih seorang pengesah.

> [!note] Algoritma
> Pemilihan secara algoritma memilih secara tidak berketentuan seorang pengesah yang berbeza (atau satu set pengesah yang mungkin) untuk kepingan maklumat yang berbeza. Suatu hash (fungsi matematik sehala yang menghasilkan “cap jari” unik daripada sebarang input — seperti cap jari sesebuah dokumen) bagi dokumen DID yang lengkap menentukan kedudukan pada gelang hash yang konsisten dan memilih calon pengesah.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> Dalam bahasa mudah: algoritma mengambil keseluruhan dokumen DID anda, mengira cap jari daripadanya, dan cap jari itu menentukan pengesah anda.

![HOW THE ALGORITHM SELECTS YOUR VERIFIER](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Dengan pengesah pertama yang dipilih algoritma, anda sebagai penerbit mungkin tidak berjaya — reputasi anda atau tetapan yang diisytiharkan mungkin tidak memenuhi keperluan mereka. Anda akan secara algoritma meneruskan pencarian untuk yang seterusnya dengan melakukan satu lagi lelaran rekursif, yang menetapkan kepada anda seorang pengesah selanjutnya. Dengan setiap langkah, “jarak” ke pengesah sasaran bertambah, begitu juga metadata yang mengiringinya yang perlu diterbitkan. Apabila data bertambah, kos secara semula jadi meningkat (bukan sahaja kerana saiz awal tuntutan, tetapi juga kerana metadata yang terkumpul dengan setiap penolakan). Maklumat yang boleh dipercayai lulus dengan jauh lebih mudah berbanding karut yang mengarut. Terpulang kepada setiap orang berapa tinggi harga yang mereka sanggup tanggung dan sejauh mana rekod itu penting bagi mereka — radikalisme dijamin akan menjadi mahal.

![HOW THE VERIFIER ANSWERS](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Apa pun yang diputuskan pengesah sebagai jawapan kepada permintaan pengesahan anda, bola kembali ke gelanggang penerbit: mereka boleh menerima tawaran pengesah bagi perkhidmatan pengesahan, memasukkan jawapan itu ke dalam kronologi dan mencuba lagi (dengan lebih mahal), atau berundur dan menelan kos yang telah hangus.

![THE ISSUER'S CHOICE](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Untuk memberikan maklumat anda bobot yang lebih besar dan peluang penerimaan yang lebih baik dengan pengesah, anda — sebagai penerbit yang mempunyai kepentingan dalam maklumat yang dikeluarkan — boleh menggunakan perkhidmatan sesuatu **autoriti yang dipercayai**. Autoriti sama ada menolak maklumat yang dikemukakan atau menerimanya dan mempertaruhkan nama baiknya (reputasi) ke atasnya. Autoriti biasanya meminta bukti daripada dunia sebenar, mengesahkannya, dan mengklasifikasikannya. Keluarannya ialah protokol penilaiannya terhadap kes yang diberi pada masa yang diberi. Anggaplah autoriti sebagai pakar dalam sesuatu jenis perkhidmatan dalam dunia sebenar dan digital — contohnya seorang penyiasat, juruaudit, penanggung insurans, pembekal sesuatu kelas barangan (pada dasarnya, mana-mana pelaku ekonomi di pasaran).

![HOW A RECORD IS CREATED IN THE NETWORK](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Pada masa anda cuba menerbitkan maklumat ke dalam rangkaian, ia berkemungkinan sudah mengandungi maklumat tentang para pelakunya — inilah isyarat reputasi. Menavigasi cara membaca isyarat reputasi — apa maknanya bagi anda dalam situasi yang berbeza dan apakah risiko yang dibawanya — mungkin tidak remeh. Setiap peserta boleh melihat rekod reputasi secara berbeza melalui DID mereka, bergantung pada situasi yang mereka tangani berkenaan pihak lawan. Adakah pihak lawan seorang pembayar yang boleh dipercayai, atau adakah saya perlu menuntut wang di hadapan untuk sesuatu transaksi perniagaan? Adakah produk yang ditawarkan membawa ulasan tentang penipuan atau kecacatan yang tersembunyi? Adakah mereka cuba melepaskan diri daripada tanggungjawab berkontrak apabila sesuatu berjalan tidak kena? Kadangkala pandangan yang lebih kompleks tentang keseluruhan kekonsistenan pihak lawan berguna — ia bergantung pada keutamaan sesiapa yang meminta ringkasan itu. Pasaran boleh menawarkan produk dan perkhidmatan yang memudahkan, memproses, dan menjelaskan pembacaan reputasi dalam konteks situasi yang dihadapi. Pelbagai autoriti dan perkhidmatan yang mereka tawarkan juga boleh berfungsi untuk tujuan ini.

![HOW TO READ REPUTATION](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Contoh
> Maklumat tipikal yang menarik minat penerbit — dan bernilai kepada orang lain — berkaitan peristiwa di luar komunikasi antara manusia yang biasa dalam dunia sebenar atau maya.
>
> Contoh negatif:
> - bukti perbuatan jenayah (cth., diaudit oleh badan penyiasat yang dipercayai)
> - bukti tidak langsung (lemah pada dirinya sendiri, tetapi terkumpul secara statistik) — cth., kehadiran berulang berhampiran beberapa kecurian dalam masa yang singkat → masih kebetulan?
> - pelanggaran kontrak
>
> Contoh positif:
> - kemudaratan yang telah dibetulkan (secara sukarela atau di bawah tekanan komuniti sebagai hukuman)
> - penerimaan dan menjalani hukuman yang dicadangkan oleh autoriti X
> - autoriti X menarik balik pengiktirafan hak harta pesalah setakat tahap tertentu
>
> Terpulang kepada setiap orang untuk mengumpulkan maklumat yang tersedia tentang pihak lawan dan menilai risiko mengikut keutamaan mereka.

![WHAT CAN YOU RECORD IN THE NETWORK?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Sama ada maklumat tentang anda muncul dalam rangkaian bergantung secara eksklusif pada tingkah laku anda sendiri.
> Anda tidak sekali-kali perlu menyertai rangkaian sebegini, namun maklumat tentang anda mungkin tetap muncul di dalamnya. Ia bergantung secara eksklusif pada tindakan anda dan kesan yang ditimbulkannya terhadap orang lain.

![THE COMMUNITY CAN OPEN ONE FOR YOU](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

Apa yang baru sahaja saya lakarkan secara ringkas ialah bagaimana sebuah rangkaian sosial yang diilhamkan oleh Identiti Terdesentralisasi (DID) boleh berfungsi. Tujuan utama konsep DID ialah mengukuhkan privasi dan kebebasan melalui prinsip melanggani peraturan yang akan saya patuhi dan jalani — memberikan pengguna keupayaan untuk memutuskan maklumat apa yang hendak dikongsi dan di bawah syarat apa.

Saya mencadangkan untuk menghubungkan DID selanjutnya ke dalam sebuah rangkaian komunikasi di mana pemegangnya bertukar maklum balas walaupun di luar situasi di mana sesuatu telah berlaku kepada seseorang dan komuniti atau seorang individu perlu bertindak balas. Perbandingan pencegahan sebegini terhadap peraturan yang telah kita langgani — dengan pilihan untuk mengira akibat ekonomi dan lain-lain daripada penyimpangan bersama dalam jangkaan tentang bagaimana pihak lain sepatutnya beroperasi — boleh dianggap sebagai motivasi untuk mencari konsensus. Berbanding kebebasan, sistem sebegini akan menekankan pembuatan keputusan secara sukarela digabungkan dengan tanggungjawab atas tingkah laku dalam dunia sebenar.

Seorang individu tidak boleh mematahkan sistem sendirian — sekumpulan orang mempunyai peluang yang lebih besar, dan sekumpulan orang dengan konsensus yang dirundingkan serta motivasi untuk bersatu dalam banyak isu mempunyai peluang yang lebih besar lagi untuk menentang kecenderungan autoritarian. Prasyarat organisasi daripada bab pertama akan dipenuhi apabila dua syarat dipenuhi: rangkaian reputasi DID meliputi komuniti dengan cukup mewakili sehingga penggunaannya tidak lagi eksotik. Dan pada masa yang sama, segmen komuniti ini menjadi minoriti yang bermakna secara ekonomi yang boleh berunding dengan tegas dengan seluruh masyarakat.

> [!note] Kesukarelaan lawan kebebasan
> Kebebasan — dalam erti yang positif — akan menjadi kesan sekunder daripada mengimbangi dua faktor: kesukarelaan dan tekanan persekitaran seseorang ke arah tanggungjawab.

> [!note] Era AI dan Nilai Reputasi
> Dalam era kecerdasan buatan, segala yang berkaitan dengan pemikiran kognitif sedang diautomasikan — dan ia mungkin melangkah lebih jauh lagi. Apakah yang tinggal dalam aktiviti manusia sebagai kelebihan bersaing? Jawapannya sukar, dan sesuatu pasti akan ditemui, tetapi satu perkara boleh kita katakan dengan pasti: reputasi akan menentukan. Sejarah tingkah laku anda yang boleh disahkan, komitmen anda dan pemenuhannya — itulah sesuatu yang AI tidak akan bina untuk anda.

![AI CANNOT BUILD YOUR REPUTATION — ONLY YOU CAN](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![THE ECONOMICS OF TRUTH](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
