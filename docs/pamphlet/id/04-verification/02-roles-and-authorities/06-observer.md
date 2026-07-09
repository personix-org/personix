---
title: "Pengamat"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Pengamat

Peran pengamat menghapus insentif verifikator untuk membengkokkan aturan. Dalam situasi di mana seorang verifikator tidak menyukai permintaan penerbit atau otoritas, mereka bisa saja sekadar berdiam diri — tidak menanggapi, dan memblokir urutan algoritmis. Pengamat — atau sekumpulan pengamat — mempertaruhkan reputasi mereka untuk mendokumentasikan bagaimana verifikator diminta. Jika verifikator berdiam diri meski kebijakan yang dideklarasikannya menyatakan sebaliknya, mereka dapat dinyatakan bersalah melanggar protokol.

![PENGAMAT — MENYIMPAN CATATAN TENTANG VERIFIKATOR](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Mekanismenya: cap waktu dan kode tantangan

Sebelum Anda mengirim sebuah klaim ke verifikator, Anda merutekannya melalui para pengamat — orang-orang yang Anda percaya, atau penyedia jasa pengamat khusus yang mengenakan imbalan kecil. Setiap pengamat menerima kiriman Anda, memberinya cap waktu, menandatangani bahwa mereka melihatnya keluar, dan menghasilkan sebuah kode tantangan — hash kriptografis dari tanda tangan mereka. Kode-kode itu dilampirkan pada permintaan Anda. Verifikator melihatnya tetapi tidak tahu sedikit pun siapa para pengamatnya, atau apakah kode-kode itu bahkan nyata. Para pengamat dengan demikian bertindak sebagai proksi antara penerbit dan verifikator, menyimpan catatan independen bahwa klaim itu telah diajukan dan apa isinya. Mereka bisa berjumlah nol hingga N.

Ketika verifikator berperilaku jujur — menerima atau menolak sejalan dengan kebijakan yang dideklarasikannya — kode-kode itu tetap buram. Tidak ada yang terpapar.

Tetapi jika verifikator berdiam diri meski kebijakannya akomodatif, atau menanggapi dengan cara yang bertentangan dengan apa yang mereka publikasikan, Anda memegang tanda tangan pengamat yang asli. Anda dapat memublikasikannya sebagai kesaksian proksi bahwa klaim itu diajukan dan bahwa verifikator tidak mengikuti protokol. Siapa pun dapat memverifikasi bahwa tanda tangan itu cocok dengan kode tantangannya.

## Intinya: Anda tidak butuh pengamat sungguhan

Dan inilah bagian yang paling elegan: **Anda sama sekali tidak butuh pengamat sungguhan.** Anda dapat menghasilkan angka acak yang tampak persis seperti kode tantangan. Verifikator tidak dapat membedakannya — mereka harus melempar dadu apakah akan mempertaruhkan reputasi mereka. Di balik setiap permintaan yang mereka terima bisa jadi ada seorang pengamat terhormat yang mengawasi secara inkognito — atau itu bisa jadi hanya derau belaka. Verifikator tidak tahu. Dan ketidakpastian itulah mekanismenya.

Biaya untuk mempertahankan tekanan yang jujur: nyaris nol (angka acak itu gratis). Potensi biaya ketidakjujuran bagi verifikator: katastrofik. Perilaku jujur terinsentifkan bahkan ketika sebenarnya tidak ada yang mengawasi.

Sistem ini bekerja karena setiap orang sedikit paranoid. Ketidakpastian lebih murah daripada pengawasan.

![GERTAKAN YANG MENJAGA VERIFIKATOR TETAP JUJUR](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Beberapa verifikator dalam satu iterasi
> Aturan pendamping yang memperkuat ketersediaan verifikator dapat berupa perluasan algoritmis yang mengembalikan, dalam satu iterasi, sekumpulan kandidat verifikator alih-alih hanya satu.
