---
title: "Gözlemci"
chapter: 3
part: "Doğrulama Nasıl İşler"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Gözlemci

Gözlemci rolü, doğrulayıcının kuralları eğip bükme teşvikini ortadan kaldırır. Bir doğrulayıcının ihraççının ya da otoritenin talebinden hoşlanmadığı durumlarda, basitçe sessiz kalabilir — yanıt vermeyip algoritmik dizilimi bloke edebilir. Gözlemci — ya da bir gözlemciler kümesi — doğrulayıcıya nasıl başvurulduğunu belgelemek üzere itibarını ortaya koyar. Doğrulayıcı, aksini söyleyen ilan edilmiş bir politikaya karşın sessiz kalırsa, protokolü ihlal etmekten mahkûm edilebilir.

![THE OBSERVER — KEEPS A RECORD OF THE VERIFIER](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Mekanizma: zaman damgası ve meydan okuma kodu

Bir iddiayı doğrulayıcıya göndermeden önce, onu gözlemciler üzerinden yönlendirirsiniz — güvendiğiniz insanlar ya da küçük bir ücret alan uzmanlaşmış gözlemci-hizmet sağlayıcıları. Her gözlemci sunumunuzu alır, ona zaman damgası vurur, dışarı çıktığını gördüğüne dair imza atar ve bir meydan okuma kodu üretir — imzasının kriptografik bir hash'i. Kodlar talebinize eklenir. Doğrulayıcı bunları görür ama gözlemcilerin kim olduğuna, hatta kodların gerçek olup olmadığına dair hiçbir fikri yoktur. Böylece gözlemciler, ihraççı ile doğrulayıcı arasında vekil olarak hareket eder ve iddianın sunulduğuna ve ne içerdiğine dair bağımsız bir kayıt tutar. Sıfırdan N'ye kadar gözlemci olabilir.

Doğrulayıcı dürüst davrandığında — ilan ettiği politikaya uygun biçimde kabul ya da ret ederek — kodlar örtük kalır. Kimse açığa çıkmaz.

Ama doğrulayıcı, uygun bir politikaya karşın sessiz kalırsa ya da yayımladığıyla çelişen biçimde yanıt verirse, elinizde özgün gözlemci imzaları vardır. Bunları, iddianın sunulduğunun ve doğrulayıcının protokolü izlemediğinin vekil tanıklığı olarak yayımlayabilirsiniz. İmzaların meydan okuma kodlarıyla eşleştiğini herkes doğrulayabilir.

## Can alıcı nokta: gerçek gözlemcilere ihtiyacınız yok

Ve en zarif kısmı burası: **gerçek gözlemcilere hiç ihtiyacınız yok.** Tam olarak meydan okuma kodlarına benzeyen rastgele sayılar üretebilirsiniz. Doğrulayıcı farkı anlayamaz — itibarını riske atıp atmama konusunda zar atmak zorundadır. Aldığı her talebin ardında, kimliğini gizleyerek izleyen saygın bir gözlemci olabilir — ya da salt gürültü. Doğrulayıcı bunu bilmez. Ve o belirsizlik mekanizmanın ta kendisidir.

Dürüst baskıyı sürdürmenin maliyeti: neredeyse sıfır (rastgele sayılar bedava). Dürüst olmamanın doğrulayıcı için olası maliyeti: felaket. Dürüst davranış, kimse aslında izlemiyorken bile teşvik edilir.

Sistem işler çünkü herkes biraz paranoyaktır. Belirsizlik, gözetimden ucuzdur.

![THE BLUFF THAT KEEPS THE VERIFIER HONEST](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Tek bir yinelemede birden çok doğrulayıcı
> Doğrulayıcı ulaşılabilirliği için pekiştirici bir tamamlayıcı kural, tek bir yinelemede yalnızca bir tane değil, bir aday doğrulayıcılar kümesi döndüren algoritmik bir uzantı olabilir.
