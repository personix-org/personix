---
title: "Uzlaşı ve Doğrulama Süreci"
chapter: 3
part: "Doğrulama Nasıl İşler"
lang: en
version: v6
source: v1
---

# Uzlaşı ve Doğrulama Süreci

Bir toplumun ortalama olarak hangi kuralları savunması ve uygulaması gerektiği üzerine uzlaşı kurmak için, aşağıdaki mekanizma yardımcı olabilir. Bir DID katılımcısı olarak, abone olduğum ve göre yaşayacağım kuralları ilan eder ve yayımlarım. (Bunu, bana göre ideal dünyamı — kendimi kısıtlanmış değil güvende hissettiğim bir dünyayı — oluşturan tüzük ve yönetmelikler gibi düşünün.)

DID bağlantılarımın nasıl tepki vereceğini önceden tahmin edebilir — ve sıradan toplumsal ya da ticari etkileşimlerde, varsayımsal olarak gerçekleşseler, ne kadar sert ve kim tarafından yaptırıma uğrayacağımı değerlendirebilirim.

Kesin değerlendirme, başka bir DID'den bilgi talep ettiğinizde ya da ondan bir iddiayı doğrulamasını istediğinizde (ya da bir otoriteden bir hizmet istediğinizde vb.) — itibar ağına yayımlamak istediğiniz bir iddiayı — gerçekleşir. Sonucun, kuru deneme (dry run) olarak, karşı tarafın ilan ettiği politikaya göre değerlendirmeyi kendiniz çalıştırdığınızdaki gibi çıkması gerekir — çıkmıyorsa, karşı tarafta bir şeyler yanlıştır: dürüst olmayan bir oyun oynamaya çalışıyorlardır.

Sonuç ya kabuldür — doğrulama için verilmiş bir fiyatla (doğrulayıcı ya da otorite hizmetleri durumunda) — ya da rettir. Değerlendiricinin politikasından sapmaya ilişkin hem yaptırımlar hem de primler, verilen fiyata katılır. Talep eden sonra, koşulları kabul edip etmeyeceğine ya da tahsis algoritmasında bir sonraki doğrulama turuna geçip geçmeyeceğine karar verir — süreci, tatmin olana ya da ekonomik açıdan devam etmek anlamsızlaşana dek yineler.

> [!note] Sosyal Graf
> İtibar ağı her şeyden önce bir sosyal ağdır. Kişiler eklersiniz — bağlantıya rıza gösteren insanlar. Onların kişileri vardır, o kişilerin de kişileri. Algoritma, doğrulayıcıları yapılandırılabilir bir derinlik içinde arar (örneğin üç düzey: doğrudan kişileriniz, onların kişileri ve bir düzey ötesi). Küresel bir blok zincirine gerek yoktur — ağ, diğer topluluklara örtüşmeleri olan toplulukları doğal olarak oluşturur.
>
> Algoritma deterministik değildir: iddia belgenizi hash'ler, hash'i bu çevre içindeki bilinen kimliklerin oluşturduğu bir halka üzerindeki bir konuma eşler ve en yakınını aday doğrulayıcı olarak seçer. İddianızı kimin doğrulayacağını öngöremez ya da etkileyemezsiniz.

Her doğrulayıcının reddi belgenizi büyütür ve işleme maliyetini artırır — bu ilk maliyet kanalıdır (belge büyümesi). Her yeni doğrulayıcı, veri hacmine, itibarınıza ve iddianızın içeriğinin onların ilan ettiği doğrulama politikasından ne kadar saptığına göre bir ücret alır — bu ikinci maliyet kanalıdır (risk primi). Ve her yineleme zaman ve enerji harcar — üçüncü maliyet kanalı.

> [!note] Doğrulayıcı Neyi, Hangi Sırayla Denetler
> Seçildikten sonra bir doğrulayıcı, bir iddiayı kabaca dört sıralı adımda değerlendirir — önce en ucuz filtreler, en sonda pahalı içerik denetimleri:
>
> 1. **Politika kapısı.** Bu tür bir iddia, doğrulayıcının kamuya açık olarak doğruladığı şeylerin içine giriyor mu? Girmiyorsa talep doğrudan reddedilir.
> 2. **Otorite güveni.** İddiayı onaylayan otorite, doğrulayıcının kendi ilan ettiği politikaya göre yeterince güvenilir mi? Doğrulayıcının güven eşiğinin altındaki bir otorite, iddianın içeriğinden bağımsız olarak ret gerekçesidir.
> 3. **İhraççı itibarı.** İhraççı, doğrulayıcının bu iddia türü için ilan ettiği itibar eşiklerini karşılıyor mu? Düşük itibar ya ücreti yükseltebilir ya da reddi tetikleyebilir.
> 4. **İçerik denetimi.** Yalnızca ilk üç kapı geçildiğinde doğrulayıcı iddianın kendisini değerlendirir — imzalar, iç tutarlılık, biçimsel doğruluk ve doğrulayıcının politikasından ne kadar saptığı. Bu son adım için alınan ücret, üstlenilen gerçek riski yansıtır.
>
> Doğrulayıcı, bu kapıların her birini yöneten politikayı yayımlar; dolayısıyla adımlar onların takdirine bağlı değildir — zaten ilan ettikleriyle bağlıdırlar. Yayımlanan politikadan sapma, onlara karşı yayımlanabilir bir iddiadır ve bunun bedelini itibarlarıyla öderler.

Sonuç: inandırıcı ve yararlı bir iddia yayımlamak neredeyse hiçbir şeye mal olmaz. Radikal bir iddia yayımlamak daha pahalıdır. Yalan yayımlamak fahiş derecede pahalı hale gelir — doğrulayıcı üstüne doğrulayıcı yinelemek zorundasınızdır ve sizi reddeden her biri maliyet ekler. Piyasa iddianızı fiyatlar ve fiyat, içinde hareket ettiğiniz topluluklarla ilişkide nerede durduğunuzu söyler.

Bir kurala uyduğunuzu ilan etmek, gerçekte uymuyorsanız yetmez. O durumda, DID'iniz ikiyüzlülüğü açığa vuran olumsuz bir kaydın yayımlanması riskini taşır — ki bu sizi herkes için bir riske dönüştürür. Sonuç, daha az ama daha tutarlı biçimde izlenen kurallar ve hukuk uzmanlarının bile içinde zar zor yolunu bulduğu o yasa ve yönetmelik ormanının temizlenmesi olmalıdır.

![HYPOCRISY IS THE MOST EXPENSIVE BEHAVIOR](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Uzlaşı ve Hesap Verebilirlik
> Ağın değerli bir bilgi kaynağı olarak hizmet etmesi için bir DID çok radikal olmamalıdır — yoksa diğerleri onu reddeder. Toplumsal baskı denge arayacaktır ve onu istikrarsızlaştırma girişimleri büyük olasılıkla cezalandırılacaktır.

![DECLARE YOUR RULES, PAY THE PRICE](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] Oyların Sayısı, Bir Sesin Ağırlığıyla Aynı Şey Değildir
> Juraj Karpiš, “paranın, iyi işlerin belleği olduğunu” söylüyor. Ben de itibarın, kötü işlerin belleği olduğunu eklerdim.
>
> Buradan şu çıkar: meritokratik olarak, daha fazla katkı yapan ve kötü bir itibarı olmayan, toplulukta daha büyük bir ses ağırlığını hak eder. İki taraflı ilişkiler merceğinden bakıldığında: hangi uzlaşı baskılarını dikkate alacağımı tartarken, en büyük ağırlık, en fazla ekonomik yarar sağladığım ilişkilere gider. Aktif bir ticaretimin olmadığı on kişi, beni tek bir kalıcı iş ortağından çok daha az etkiler. Bu paradigma ticaretle sınırlı değildir — toplumsal, siyasi ve diğer ilişkilere de uzanır.
