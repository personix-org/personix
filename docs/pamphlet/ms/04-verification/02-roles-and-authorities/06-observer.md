---
title: "Pemerhati"
chapter: 3
part: "Bagaimana Pengesahan Berfungsi"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Pemerhati

Peranan pemerhati menghapuskan insentif pengesah untuk memesongkan peraturan. Dalam situasi di mana seorang pengesah tidak menyukai permintaan pengeluar atau autoriti, mereka boleh sahaja berdiam diri — tidak menjawab, dan menyekat jujukan algoritma. Pemerhati — atau satu set pemerhati — mempertaruhkan reputasi mereka atas pendokumenan bagaimana pengesah itu ditanya. Jika pengesah berdiam diri walaupun terdapat polisi yang diisytiharkan yang menyatakan sebaliknya, mereka boleh disabitkan kerana melanggar protokol.

![THE OBSERVER — KEEPS A RECORD OF THE VERIFIER](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Mekanismenya: cap masa dan kod cabaran

Sebelum anda menghantar sesuatu tuntutan kepada pengesah, anda menyalurkannya melalui pemerhati — orang yang anda percayai, atau penyedia perkhidmatan pemerhati khusus yang mengenakan fi kecil. Setiap pemerhati menerima serahan anda, memberikannya cap masa, menandatangani bahawa mereka melihatnya dihantar keluar, dan menjana suatu kod cabaran — suatu hash kriptografi bagi tandatangan mereka. Kod-kod itu dilampirkan pada permintaan anda. Pengesah melihatnya tetapi tidak tahu siapa pemerhati itu, atau sama ada kod itu memang benar. Pemerhati dengan itu bertindak sebagai proksi antara pengeluar dan pengesah, memegang rekod yang bebas bahawa tuntutan itu telah dikemukakan dan apa yang terkandung di dalamnya. Bilangan mereka boleh sifar hingga N.

Apabila pengesah berkelakuan jujur — menerima atau menolak selaras dengan polisi yang diisytiharkan mereka — kod-kod itu kekal legap. Tiada siapa yang terdedah.

Tetapi jika pengesah berdiam diri walaupun terdapat polisi yang mengakomodasi, atau bertindak balas dengan cara yang bercanggah dengan apa yang mereka terbitkan, anda memegang tandatangan pemerhati yang asal. Anda boleh menerbitkannya sebagai kesaksian proksi bahawa tuntutan itu telah dikemukakan dan bahawa pengesah tidak mematuhi protokol. Sesiapa sahaja boleh mengesahkan bahawa tandatangan itu sepadan dengan kod cabaran.

## Kejutan akhirnya: anda tidak perlukan pemerhati sebenar

Dan inilah bahagian yang paling elegan: **anda tidak perlukan pemerhati sebenar langsung.** Anda boleh menjana nombor rawak yang kelihatan persis seperti kod cabaran. Pengesah tidak dapat membezakannya — mereka terpaksa membaling dadu sama ada untuk mempertaruhkan reputasi mereka. Di sebalik setiap permintaan yang mereka terima, mungkin ada seorang pemerhati yang dihormati memerhati secara menyamar — atau ia mungkin hanyalah bunyi bising semata-mata. Pengesah tidak tahu. Dan ketidakpastian itulah mekanismenya.

Kos untuk mengekalkan tekanan yang jujur: hampir sifar (nombor rawak adalah percuma). Kos berpotensi bagi ketidakjujuran pengesah: dahsyat. Kelakuan jujur diberi insentif walaupun tiada siapa yang sebenarnya memerhati.

Sistem ini berfungsi kerana setiap orang sedikit paranoid. Ketidakpastian lebih murah daripada pengawasan.

![THE BLUFF THAT KEEPS THE VERIFIER HONEST](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Berbilang pengesah dalam satu lelaran tunggal
> Peraturan pendamping yang mengukuhkan bagi ketersediaan pengesah boleh berupa lanjutan algoritma yang memulangkan, dalam satu lelaran tunggal, satu set calon pengesah dan bukan hanya seorang.
