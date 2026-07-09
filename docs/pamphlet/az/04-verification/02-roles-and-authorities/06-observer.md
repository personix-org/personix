---
title: "Müşahidəçi"
chapter: 3
part: "Doğrulama Necə İşləyir"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Müşahidəçi

Müşahidəçi rolu doğrulayıcının qaydaları əyməyə olan stimulunu aradan qaldırır. Doğrulayıcının naşirin ya da avtoritetin sorğusunu bəyənmədiyi vəziyyətlərdə o, sadəcə susa bilər — cavab verməyib alqoritmik ardıcıllığı bloklaya bilər. Müşahidəçi — ya da müşahidəçilər dəsti — doğrulayıcının necə sorğulandığını sənədləşdirməyə öz reputasiyalarını qoyur. Əgər doğrulayıcı əksini deyən bəyan edilmiş siyasətə baxmayaraq susursa, o, protokolu pozmaqda təqsirli bilinə bilər.

![MÜŞAHİDƏÇİ — DOĞRULAYICININ QEYDİNİ SAXLAYIR](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Mexanizm: zaman möhürü və çağırış kodu

İddianı doğrulayıcıya göndərməzdən əvvəl onu müşahidəçilərdən keçirirsiniz — etibar etdiyiniz insanlar, ya da kiçik ödəniş tutan ixtisaslaşmış müşahidəçi-xidmət təchizatçıları. Hər müşahidəçi sizin təqdimatınızı alır, ona zaman möhürü vurur, onun çıxdığını gördüyünü imzalayır və çağırış kodu — öz imzasının kriptoqrafik heşini — yaradır. Kodlar sizin sorğunuza əlavə olunur. Doğrulayıcı onları görür, amma müşahidəçilərin kim olduğu, ya da kodların ümumiyyətlə real olub-olmadığı barədə heç bir təsəvvürü yoxdur. Beləliklə, müşahidəçilər naşir ilə doğrulayıcı arasında vəkil kimi çıxış edir, iddianın təqdim edildiyinə və nələr ehtiva etdiyinə dair müstəqil qeyd saxlayır. Onların sayı sıfırdan N-ə qədər ola bilər.

Doğrulayıcı dürüst davrandıqda — bəyan etdiyi siyasətə uyğun qəbul ya da rədd etdikdə — kodlar qapalı qalır. Heç kim ifşa olunmur.

Amma əgər doğrulayıcı güzəştli bir siyasətə baxmayaraq susursa, ya da dərc etdiyinə zidd bir şəkildə cavab verirsə, ilkin müşahidəçi imzaları sizdə qalır. Onları iddianın təqdim edildiyinə və doğrulayıcının protokola riayət etmədiyinə dair vəkil şahidliyi kimi dərc edə bilərsiniz. İstənilən kəs imzaların çağırış kodlarına uyğun gəldiyini yoxlaya bilər.

## Vurğu nöqtəsi: real müşahidəçilərə ehtiyacınız yoxdur

Və ən zərif hissə budur: **sizə ümumiyyətlə real müşahidəçilər lazım deyil.** Tam da çağırış kodları kimi görünən təsadüfi ədədlər yarada bilərsiniz. Doğrulayıcı fərqi ayırd edə bilmir — o, reputasiyasını riskə atıb-atmamaq üçün zər atmalıdır. Aldığı hər sorğunun arxasında inkoqnito izləyən hörmətli bir müşahidəçi ola bilər — ya da xalis səs-küy ola bilər. Doğrulayıcı bilmir. Və o qeyri-müəyyənlik məhz mexanizmdir.

Dürüst təzyiqi saxlamağın xərci: demək olar ki, sıfır (təsadüfi ədədlər pulsuzdur). Doğrulayıcı üçün dürüstsüzlüyün potensial xərci: fəlakətli. Dürüst davranış hətta əslində heç kim izləmədikdə belə stimullaşdırılır.

Sistem işləyir, çünki hər kəs bir az paranoyaldır. Qeyri-müəyyənlik nəzarətdən ucuzdur.

![DOĞRULAYICINI DÜRÜST SAXLAYAN BLEF](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Bir iterasiyada bir neçə doğrulayıcı
> Doğrulayıcının əlçatanlığı üçün gücləndirici tamamlayıcı qayda bir iterasiyada yalnız bir yox, namizəd doğrulayıcılar dəsti qaytaran alqoritmik genişlənmə ola bilər.
