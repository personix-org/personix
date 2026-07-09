---
title: "Ikhtisar Peran"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Ikhtisar Peran

Kita sudah menyinggung sebagian peran ini secara singkat dalam bab tentang jaringan dan sifat-sifat dasarnya. Kini saatnya memandangnya kembali secara lebih rinci dan menambahkan peran-peran lain yang kita perlukan untuk membuat jaringan lebih tangguh. Setiap transaksi verifikasi melibatkan beberapa peran — mari kita lihat bagaimana mereka berperilaku.

> [!note] Peran dalam Transaksi Verifikasi
> Setiap verifikasi melibatkan hingga enam peran berbeda, dirangkum dalam tabel di bawah. Semuanya dapat memiliki DID mereka sendiri dalam jaringan reputasi terdesentralisasi.

| Peran | Deskripsi |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Penerbit** | Orang yang memublikasikan informasi ke jaringan — mengeklaim bahwa sesuatu telah terjadi (sebuah DID diciptakan, disunting, atau dibubarkan, sebuah klaim, kebijakan suatu DID, dll.) |
| **Subjek** | Orang yang menjadi pokok informasi — penerima klaim |
| **Otoritas** | Entitas tepercaya yang mempertaruhkan namanya atas mutu klaim dengan menyelidikinya dan entah menelaah bukti yang disajikan atau secara aktif mengumpulkannya |
| **Pengamat** | Pihak ketiga independen yang menyimpan catatan tentang bagaimana verifikator menangani klaim — memastikan verifikator tidak berdiam diri maupun menyimpang dari kebijakan yang mereka deklarasikan |
| **Verifikator** | Peserta yang dipilih secara algoritmis yang memproses transaksi |
| **Delegat** | Orang yang bertindak atas nama peserta lain |
