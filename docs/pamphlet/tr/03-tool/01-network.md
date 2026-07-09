---
title: "İtibara Dayalı Sosyal Ağ"
chapter: 2
part: "Araç"
lang: en
version: v6
source: v1
---

# İtibara Dayalı Sosyal Ağ

Değişimi getirmek için özenle tasarlanmış bir araca ihtiyacımız var. Önce onu kısaca çizeceğiz; sonraki bölümlerde her parçayı daha ayrıntılı inceleyip üzerine ekleyeceğiz. Sansürlenemez, küresel, merkeziyetsiz bir sosyal ağ hayal edin; burada kendi vekil kimliğinizi — yani Merkeziyetsiz Kimliği (DID) — güvenle oluşturup yönetebilirsiniz. DID, herhangi bir merkezî otoriteye bağımlı olmadan kendinizin oluşturup denetlediği bir dijital kimliktir. Onu kimse elinizden alamaz ya da sahtesini üretemez, çünkü özel anahtarınızla (ya da çoklu imza yoluyla anahtarlarınızla) kriptografik olarak imzalanmıştır.

> [!note] Not
> Bunun bir çıkarımı, böyle bir kimliğin devletin verdiği kimlik belgelerinin yerini yavaş yavaş alabilmesidir — ama bu konuda daha fazlası geçiş bölümünde.

![YOUR IDENTITY, YOUR KEYS, YOUR RULES](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

Böyle bir ağda, kimliğiniz aracılığıyla birinin size zarar verdiğini (ve daha sonra, muhtemelen, bunu telafi ettiğini ya da telafiye zorlandığını) bildirebilirsiniz. Zararın kaynağına yönelik bu geri bildirimin ilgili bir kaynak olarak değer taşıması için, ağa bilgi girmenin zaman, enerji ve para maliyeti olmalıdır — üstelik bunun boş bir laf olmadığına dair başkalarına doğrulanabilir kanıt üretilmelidir.

Bilgi okumak kolay ve görece ucuz olurdu, ama tek bir kaydı oluşturmak masraflı ve zahmetli olurdu. Yazma, seçilen algoritmaya göre hesaplamanın, sunulan bilginin doğrulanması için hangi DID'e başvurulacağını ve seçilen katılımcının bilgiyi sizin adınıza işleyip yayımlaması ve onun doğrulayıcısı haline gelmesi için nasıl ilerleneceğini kesin biçimde belirlediği açık bir protokolü izlerdi.

> [!note] Algoritma ve radikallik
> Doğrulayıcıların algoritmik seçimi, radikal olmayan bilgi yayımcılarının zamanla, yayımlanan bilginin maliyetleri ile doğrulama ödülleri arasında neredeyse nötr bir denge tutturmasını sağlar.

![PUBLISHING COSTS TIME, ENERGY, AND MONEY](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Algoritmanın bir doğrulayıcıyı nasıl seçtiğine bakalım.

> [!note] Algoritma
> Algoritmik seçim, farklı bilgi parçaları için deterministik olmayan biçimde farklı bir doğrulayıcı (ya da olası doğrulayıcılar kümesi) seçer. Tam DID belgesinin bir hash'i (herhangi bir girdiden benzersiz bir “parmak izi” üreten tek yönlü matematiksel işlev — bir belgenin parmak izi gibi) tutarlı bir hash halkası üzerindeki konumu belirler ve doğrulayıcı adaylarını seçer.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> Sade bir dille: algoritma tüm DID belgenizi alır, ondan bir parmak izi hesaplar ve o parmak izi doğrulayıcınızı belirler.

![HOW THE ALGORITHM SELECTS YOUR VERIFIER](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Algoritmanın seçtiği ilk doğrulayıcıda siz yayımcı olarak başarılı olamayabilirsiniz — itibarınız ya da ilan ettiğiniz ayarlar onun gereksinimlerini karşılamayabilir. Size bir sonraki doğrulayıcıyı atayan başka bir özyinelemeli yineleme gerçekleştirerek algoritmik olarak aramayı sürdürürdünüz. Her adımda hedef doğrulayıcıya olan “mesafe” büyür ve yayımlanması gereken beraberindeki üstveri de büyür. Veri büyüdükçe maliyetler doğal olarak artar (yalnızca iddianın başlangıçtaki boyutu yüzünden değil, aynı zamanda her retle biriken üstveri yüzünden). İnandırıcı bilgi, anlamsız heveslerden çok daha kolay geçer. Bir kaydın ne kadar önemli olduğuna ve ne kadar yüksek bir bedele katlanmaya razı olduğuna herkes kendi karar verir — radikalliğin pahalıya patlayacağı garantidir.

![HOW THE VERIFIER ANSWERS](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Doğrulayıcı, doğrulama talebinize karşılık ne karar verirse versin, top yeniden yayımcının sahasındadır: doğrulayıcının doğrulama hizmetleri için sunduğu teklifi kabul edebilir, yanıtı kronolojiye ekleyip yeniden deneyebilir (daha pahalıya) ya da çekip gidip batan maliyeti yutabilir.

![THE ISSUER'S CHOICE](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Bilginize daha fazla ağırlık ve doğrulayıcılar nezdinde kabul görmesi için daha iyi bir şans kazandırmak amacıyla — ihraç edilen bilgide payı olan bir yayımcı olarak — bir **güvenilir otoritenin** hizmetlerinden yararlanabilirdiniz. Otorite ya sunulan bilgiyi reddeder ya da kabul edip iyi adını (itibarını) onun üzerine koyar. Otorite tipik olarak gerçek dünyadan kanıt ister, onu doğrular ve sınıflandırır. Çıktı, verilen bir olguya ilişkin belirli bir zamanda yaptığı değerlendirmenin bir protokolüdür. Bir otoriteyi, hem gerçek hem dijital dünyada belirli türde bir hizmetin uzmanı olarak düşünün — örneğin bir müfettiş, bir denetçi, bir sigortacı, belirli bir mal sınıfının tedarikçisi (özünde piyasadaki herhangi bir ekonomik aktör).

![HOW A RECORD IS CREATED IN THE NETWORK](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Bilgiyi ağa yayımlamaya çalıştığınız zaman, ağ büyük olasılıkla aktörleri hakkında zaten bilgi içeriyor olacak — bunlar itibar sinyalleridir. İtibar sinyallerinin nasıl okunacağını çözmek — farklı durumlarda sizin için ne anlama geldiklerini ve hangi riskleri taşıdıklarını — pek de basit olmayabilir. Her katılımcı, karşı tarafla ilgili ele aldığı duruma bağlı olarak, itibar kayıtlarına DID'i üzerinden farklı bakabilir. Karşı taraf güvenilir bir ödeyici mi, yoksa bir ticari işlem için parayı peşin mi talep etmem gerekir? Sunulan ürün, gizli dolandırıcılık ya da kusurlar hakkında değerlendirmeler taşıyor mu? Bir şeyler ters gittiğinde sözleşmeden doğan sorumluluktan sıyrılmaya mı çalışıyorlar? Bazen karşı tarafın genel tutarlılığına ilişkin daha karmaşık bir bakış işe yarar — bu, genel görünümü kim talep ediyorsa onun tercihlerine bağlıdır. Piyasa, itibarın eldeki durum bağlamında okunmasını basitleştiren, işleyen ve netleştiren ürünler ve hizmetler sunabilir. Çeşitli otoriteler ve sundukları hizmetler de bu amaca hizmet edebilir.

![HOW TO READ REPUTATION](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Örnekler
> Yayımcıların ilgisini çeken — ve başkaları için değerli olan — tipik bilgiler, gerçek ya da sanal dünyadaki sıradan kişilerarası iletişimin ötesindeki olaylara ilişkindir.
>
> Olumsuz örnekler:
> - suç eylemlerine dair kanıt (örneğin güvenilir bir soruşturma organı tarafından denetlenmiş)
> - dolaylı kanıt (tek başına zayıf, ama istatistiksel olarak birikimli) — örneğin kısa bir zaman içinde birden çok hırsızlığın yakınında tekrar tekrar bulunmak → hâlâ rastlantı mı?
> - sözleşme ihlali
>
> Olumlu örnekler:
> - telafi edilen zarar (gönüllü ya da topluluğun ceza olarak uyguladığı baskı altında)
> - X otoritesi tarafından önerilen bir cezanın kabulü ve çekilmesi
> - X otoritesinin, failin mülkiyet haklarına belirli bir ölçüde tanımayı geri çekmesi
>
> Karşı taraf hakkında mevcut bilgileri toplamak ve riskleri tercihlerine göre değerlendirmek herkesin kendine kalmıştır.

![WHAT CAN YOU RECORD IN THE NETWORK?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Hakkınızda bir bilginin ağda görünüp görünmemesi yalnızca kendi davranışınıza bağlıdır.
> Böyle bir ağa katılmak zorunda hiç değilsiniz, yine de hakkınızda bilgi orada görünebilir. Bu, yalnızca eylemlerinize ve bunların başkaları üzerindeki etkisine bağlıdır.

![THE COMMUNITY CAN OPEN ONE FOR YOU](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

Az önce kısaca çizdiğim şey, Merkeziyetsiz Kimlikten (DID) esinlenen bir sosyal ağın nasıl işleyebileceğidir. DID kavramlarının başlıca amacı, izleyeceğim ve göre yaşayacağım kurallara abone olma ilkesi aracılığıyla mahremiyeti ve özgürlüğü güçlendirmektir — kullanıcılara hangi bilgiyi hangi koşullarda paylaşacaklarına karar verme yetisi verir.

DID'leri, sahiplerinin, birine bir şey olup topluluğun ya da bir bireyin tepki vermesi gereken durumların ötesinde de geri bildirim alışverişi yaptığı bir iletişim ağında birbirine bağlamayı öneriyorum. Abone olduğumuz kuralların böyle önleyici biçimde karşılaştırılması — karşı tarafın nasıl işlemesi gerektiğine dair beklentilerdeki karşılıklı sapmaların ekonomik ve diğer sonuçlarını hesaplama seçeneğiyle birlikte — uzlaşı bulmak için bir güdü sayılabilir. Böyle bir sistem, özgürlük yerine, gerçek dünyadaki davranışın sorumluluğuyla birleşmiş gönüllü karar vermeyi öne çıkarırdı.

Bir birey sistemi tek başına kıramaz — bir grup insanın şansı daha yüksektir; müzakere edilmiş uzlaşıya ve birçok konuda birlikte çekmek için güdülere sahip bir grup insanın otoriter eğilimlere direnme şansı daha da yüksektir. Birinci bölümdeki örgütlenme önkoşulu, iki koşul sağlandığında yerine gelecek: DID itibar ağının, kullanımı egzotik olmaktan çıkacak kadar temsili biçimde toplulukları kaplaması. Ve aynı zamanda bu topluluk kesiminin, toplumun geri kalanıyla iddialı biçimde müzakere edebilen, ekonomik olarak önemli bir azınlık haline gelmesi.

> [!note] Gönüllülük ve özgürlük
> Özgürlük — olumlu anlamda — iki etkenin dengelenmesinin ikincil bir etkisi olurdu: gönüllülük ve çevrenin sorumluluğa doğru baskısı.

> [!note] Yapay Zekâ Çağı ve İtibarın Değeri
> Yapay zekâ çağında, bilişsel düşünceye bağlı her şey otomatikleşiyor — ve daha da ileri gidebilir. O zaman insan etkinliğinde rekabet avantajı olarak geriye ne kalır? Yanıt zor ve mutlaka bir şeyler bulunacak, ama tek bir şeyi kesinlikle söyleyebiliriz: itibar belirleyici olacak. Davranışınızın, taahhütlerinizin ve bunların yerine getirilişinin doğrulanabilir bir geçmişi — işte bunu yapay zekâ sizin yerinize inşa etmeyecek.

![AI CANNOT BUILD YOUR REPUTATION — ONLY YOU CAN](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![THE ECONOMICS OF TRUTH](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
