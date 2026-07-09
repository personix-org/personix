---
title: "Verifikator"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Verifikator

Setiap DID dapat bertindak sebagai verifikator, entah secara langsung atau melalui hak verifikasi yang didelegasikan kepada DID ketiga. Agar saya — atau delegat saya — dapat memverifikasi, saya sebaiknya dapat dijangkau di jaringan (daring). Tidak semua orang akan mau berkomitmen pada itu, itulah sebabnya sebuah catatan DID dapat mencantumkan, dalam urutan prioritas, para pengganti yang akan menjalankan fungsi itu atas namanya selagi ia luring.

Setiap DID yang aktif dalam jaringan secara publik mendeklarasikan kebijakannya sendiri. Melalui aturan yang didefinisikan dalam kebijakan itu ia menilai, selama proses verifikasi, reputasi pihak lawan serta isi dan bentuk klaim yang telah ditandai penerbit untuk dipublikasikan ke jaringan reputasi. Bagian dari kebijakan itu adalah rumus perhitungan yang digunakan untuk menghitung imbalan bagi jasa verifikasi. Begitu itu tersedia, maka di seluruh sejumlah besar klaim secara statistik yang mengalir melalui jaringan, saya menunggu algoritma jaringan menarik saya ke sisi penerbit dan menugaskan saya, dalam iterasi tertentu, untuk memverifikasi informasi yang diterbitkan. Penerbit dapat menghitung lebih dulu bagaimana seorang verifikator yang berperilaku benar akan bereaksi, tetapi tidak dapat menghindar dari benar-benar menghubunginya (atau para penggantinya); iterasi dengan verifikator terpilih harus tetap dijalankan oleh penerbit bahkan ketika mereka tahu lebih dulu bahwa itu tidak akan lolos.

Bagaimana kita tahu bahwa penerbit menjalankan algoritma pemilihan verifikator atas himpunan kandidat DID verifikator yang benar? Bersama dengan kebijakan yang dideklarasikannya secara publik, setiap DID juga memublikasikan daftar terkini pengenal jaringan sosialnya di dalam jaringan reputasi. Jika seorang penerbit mendefinisikan jaringan sosialnya sebagai gelembung sosial yang sekadar menggemakan dan menguatkan pandangannya sendiri, informasi yang dipublikasikan melaluinya nyaris tidak akan diterima lebih luas oleh komunitas lain. Fakta bahwa saya berhasil, dengan biaya tinggi, mendorong sebuah klaim radikal ke dalam jaringan tidak berarti bahwa, ketika menilai reputasi pihak lawan, saya akan memberinya bobot apa pun. Beberapa klaim didesak komunitas saya untuk saya perhitungkan (vonis dan pembatasan yang dijatuhkan pada para pelanggar); yang lain sepenuhnya terserah saya — saya sendiri yang memutuskan nilai ekonomi dari memasukkan atau mengecualikan suatu potongan informasi.

![VERIFIKATOR — DIPILIH OLEH ALGORITMA](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
