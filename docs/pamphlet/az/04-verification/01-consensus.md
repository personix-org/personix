---
title: "Konsensus və Doğrulama Prosesi"
chapter: 3
part: "Doğrulama Necə İşləyir"
lang: en
version: v6
source: v1
---

# Konsensus və Doğrulama Prosesi

Cəmiyyətin orta hesabla hansı qaydalara riayət etməli və onları tətbiq etməli olduğu barədə konsensus qurmaq üçün aşağıdakı mexanizm kömək edə bilər. DID iştirakçısı kimi mən üzv olduğum və yaşayacağım qaydaları bəyan edir və onları dərc edirəm. (Bunu, mənim baxışımda ideal dünyamı təşkil edən daxili qaydalar və nizamnamələr kimi düşünün — özümü məhdud yox, təhlükəsiz hiss etdiyim bir dünya.)

Mən əvvəlcədən təxmin edə bilərəm ki, DID kontaktlarım necə reaksiya verər — və hipotetik olaraq baş verərsə, adi sosial ya da biznes qarşılıqlı əlaqələrində nə qədər güclü və kim tərəfindən sanksiya olunacağımı qiymətləndirə bilərəm.

Yekun qiymətləndirmə başqa bir DID-dən məlumat istədiyiniz, ya da onlardan reputasiya şəbəkəsinə dərc etmək istədiyiniz bir iddianı doğrulamağı xahiş etdiyiniz (ya da bir avtoritetdən xidmət istədiyiniz və s.) zaman baş verir. Nəticə qarşı tərəfin bəyan etdiyi siyasətə qarşı özünüz quru sınaqda qiymətləndirmə apardıqda çıxan nəticə ilə eyni olmalıdır — və əgər olmursa, qarşı tərəfdə nəsə səhvdir: onlar dürüst olmayan bir oyun oynamağa çalışırlar.

Nəticə ya doğrulama üçün qiymət təklifi ilə qəbul (doğrulayıcı ya da avtoritet xidmətləri halında), ya da rəddedilmədir. Qiymətləndiricinin siyasətindən sapmaya görə həm sanksiyalar, həm də bonuslar təklif olunan qiymətə qatılır. Sonra sorğu verən şərtləri qəbul etməyə, ya da bölüşdürmə alqoritmində növbəti doğrulama raunduna keçməyə qərar verir — prosesi razı qalana qədər, ya da iqtisadiyyat davam etməyi mənasız edənə qədər təkrarlayaraq.

> [!note] Sosial Qraf
> Reputasiya şəbəkəsi hər şeydən əvvəl bir sosial şəbəkədir. Kontaktlar əlavə edirsiniz — əlaqəyə razılıq verən insanlar. Onların kontaktları var, o kontaktların da kontaktları. Alqoritm konfiqurasiya oluna bilən dərinlik daxilində (məsələn, üç səviyyə: sizin birbaşa kontaktlarınız, onların kontaktları və bir səviyyə o yana) doğrulayıcılar axtarır. Qlobal blokçeynə ehtiyac yoxdur — şəbəkə təbii şəkildə digər icmalara üst-üstə düşmələrlə icmalar formalaşdırır.
>
> Alqoritm qeyri-deterministikdir: o, iddia sənədinizi heşləyir, heşi bu dairə daxilində tanınan kimliklər halqasında bir mövqeyə uyğunlaşdırır və ən yaxınını namizəd doğrulayıcı kimi seçir. İddianızı kimin doğrulayacağını nə proqnozlaşdıra, nə də ona təsir edə bilərsiniz.

Hər doğrulayıcının rəddedilməsi sənədinizi böyüdür və onun emal xərcini artırır — bu, birinci xərc kanalıdır (sənədin böyüməsi). Hər yeni doğrulayıcı məlumat həcminə, reputasiyanıza və iddianızın məzmununun onların bəyan etdiyi doğrulama siyasətindən nə qədər saptığına əsaslanan ödəniş tutur — bu, ikinci xərc kanalıdır (risk mükafatı). Və hər iterasiya vaxt və enerjiyə başa gəlir — üçüncü xərc kanalı.

> [!note] Doğrulayıcı Nəyi, Hansı Sırayla Yoxlayır
> Seçildikdən sonra doğrulayıcı iddianı təxminən dörd sıralı addımda qiymətləndirir — əvvəlcə ən ucuz filtrlər, sonda baha məzmun yoxlamaları:
>
> 1. **Siyasət qapısı.** Bu növ iddia ümumiyyətlə doğrulayıcının açıq şəkildə doğruladığı çərçivəyə düşürmü? Əgər yox, sorğu birbaşa rədd edilir.
> 2. **Avtoritetə etibar.** İddianı təsdiq edən avtoritet doğrulayıcının öz bəyan etdiyi siyasətə görə kifayət qədər etibarlıdırmı? Doğrulayıcının etibar həddindən aşağı olan avtoritet iddianın məzmunundan asılı olmayaraq rəddedilmə üçün əsasdır.
> 3. **Naşirin reputasiyası.** Naşir doğrulayıcının bu növ iddia üçün bəyan etdiyi reputasiya hədlərini ödəyirmi? Aşağı reputasiya ya ödənişi qaldıra, ya da rəddedilməni işə sala bilər.
> 4. **Məzmun yoxlaması.** Yalnız ilk üç qapı keçdikdə doğrulayıcı iddianın özünü qiymətləndirir — imzalar, daxili ardıcıllıq, formal düzgünlük və onun doğrulayıcının siyasətindən nə qədər saptığı. Bu son addım üçün tutulan ödəniş götürülən faktiki riski əks etdirir.
>
> Doğrulayıcı bu qapıların hər birini idarə edən siyasəti dərc edir, ona görə də addımlar onların ixtiyarında deyil — onlar artıq bəyan etdikləri ilə bağlıdır. Dərc olunmuş siyasətdən sapma öz-özlüyündə onlara qarşı dərc edilə bilən bir iddiadır və onlar bunun bədəlini öz reputasiyaları ilə ödəyirlər.

Nəticə: etibarlı və faydalı bir iddia dərc etmək demək olar ki, heç nəyə başa gəlmir. Radikal bir iddia dərc etmək daha bahadır. Yalan dərc etmək məhz həddindən artıq baha olur — doğrulayıcıdan doğrulayıcıya iterasiya etməlisiniz və sizi rədd edən hər kəs xərc əlavə edir. Bazar iddianıza qiymət qoyur və qiymət sizə içində hərəkət etdiyiniz icmalara münasibətdə harada dayandığınızı deyir.

Bir qaydaya riayət etdiyinizi bəyan etmək, əslində etmədiyiniz halda, kifayət deyil. Bu halda DID-iniz ikiüzlülüyü ifşa edən mənfi bir qeydin dərcini riskə atır — ki bu da sizi hər kəs üçün riskə çevirir. Nəticə daha az, amma daha ardıcıl şəkildə riayət olunan qaydalar və hətta hüquq peşəkarlarının belə çətinliklə istiqamətlənə bildiyi o qanun və qaydalar cəngəlliyinin təmizlənməsi olmalıdır.

![İKİÜZLÜLÜK ƏN BAHA DAVRANIŞDIR](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Konsensus vs Hesabatlılıq
> Şəbəkənin dəyərli məlumat mənbəyi kimi xidmət etməsi üçün DID çox radikal olmamalıdır — əks halda başqaları onu rədd edəcək. Sosial təzyiq tarazlıq axtaracaq və onu qeyri-sabit etmək cəhdləri çox güman ki, cəzalandırılacaq.

![QAYDALARINI BƏYAN ET, QİYMƏTİNİ ÖDƏ](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] Səslərin Sayı Səsin Çəkisi ilə Eyni Şey Deyil
> Juraj Karpiš deyir ki, "pul yaxşı əməllərin yaddaşıdır." Mən əlavə edərdim ki, reputasiya pislərin yaddaşıdır.
>
> Bundan çıxır ki, meritokratik olaraq, kim daha çox töhfə verir və heç bir pis reputasiyası yoxdursa, icmada daha böyük səs çəkisinə layiqdir. İkitərəfli münasibətlər prizmasından baxdıqda: hansı konsensus təzyiqlərinə uyğunlaşacağımı ölçdüyümdə, ən böyük çəki ən böyük iqtisadi fayda əldə etdiyim münasibətlərə gedir. Aktiv ticarətim olmayan on nəfər mənə bir daimi biznes tərəfdaşından qat-qat az təsir edəcək. Bu paradiqma ticarətlə məhdudlaşmır — o, sosial, siyasi və digər münasibətlərə də uzanır.
