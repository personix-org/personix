---
title: "Bariz Kuşkuların Yanıtlanması"
chapter: 2
part: "Araç"
lang: en
version: v6
source: "v1 callouts extended in v4"
---

# Bariz Kuşkuların Yanıtlanması

Anlatılan sistem doğal olarak bir dizi soru doğuruyor. En sık karşılaşılanları ele alalım.

## Teknolojiye Bağımlılık

Muhtemelen zaten fark etmişsinizdir: yaklaşık 150 yıldır bizimle olan modern devletin aksine, burada anlatıldığı biçimdeki itibar ağı çözümü, küresel/yerel internet teknolojisine büyük ölçüde bağlıdır. Bir kesinti durumunda böyle bir ağın işleyişi risk altındadır.

Kesinti geçiciyse, verilerde ya da ağdaki iddiaların tutarlılığında bir kayıp olmaz ve topluluklar içinde elde edilen itibar dengeleri de bozulmamalıdır. Karşılaştırılabilir ödeme ağlarının aksine, bu ağ çok düşük süreç ve veri kalemi sıklıklarını varsayar. Bu bakımdan merkeziyetsiz itibar ağı, bugünün devletinden farklı değildir; devlet de artık teknolojiye büyük ölçüde bağımlıdır ve kâğıt kart dosyalarıyla çalışmayı unutmuştur (gerçi kriz planlarında başka çaresi olmazdı).

Devletin, bir itibar ağı biçimindeki evrimsel ardılı, kalıcı bir kesinti (benzeri görülmemiş ölçekte bir felaket) durumunda daha ilkel bir merkezî sisteme — devlete — geri çekilebilir.

Teknoloji, insanlığın daha yüksek yönetişim uygarlık biçimlerine ulaşmasını sağlar ve bize yararlar getirir, ama riskler de getirir.

## Ağda Yayımlayarak Parayı Pencereden mi Atıyorum?

İtibar ağında bir iddia yayımlamanın maliyetleri büyük ölçüde batık değildir. Bir yayımcının ağa koyduğu mesajın yararı — gerçek şikâyetler, doğrulanmış deneyimler, ilgili uyarılar hakkında bilgi — daha uzun bir zaman ufkunda, istatistiksel olarak, topluluktaki başkalarının iddialarını doğrulama ücretleri biçiminde geri döner. Topluluk yarar sağlar, yayımcı itibar inşa eder ve böylece doğru bilgiyi yayımlamanın maliyetleri, yalnızca gerçek ağ bakım maliyetlerinin küçük bir bölümünün çıkarılması gereken, iade edilebilir bir teminata yaklaşır. Buna karşılık, doğru olmayan ya da önemsiz kayıtlar geri dönmez — maliyetleri net bir kayıptır. Dürüstlük bu yüzden yalnızca ahlaki bir seçim değil, aynı zamanda ekonomik olarak rasyonel bir stratejidir.

Ağ bakım maliyetleri çıkarıldıktan sonra bu ilkeye ekonomik nötrlük ilkesi denebilir — toplulukla birlikte olduğumda kaybetmem, ona karşı olduğumda kaybederim.

Topluluğun ayrıca üyelerinin dürüst yaklaşımını takdir etmek için dayanışma kanalları da vardır. Ama hayale kapılmayalım: dayanışma çağrıları çoğunlukla topluluk toplumsal baskısından doğar; dolayısıyla bu, sözcüğün gönüllü anlamıyla bir dayanışma olmayabilir.

## Ya Biri Birden Çok Kimlik Oluşturursa?

Bir kişi paralel olarak birden çok DID kimliği işletebilir. Ancak her kimlik için itibar inşa etmek bağımsız çaba gerektirir — zaman, enerji, para.

Kestirme yol yoktur: her kimlik, kendi geçmiş kaydını[^trackrecord] gerçek etkinlik yoluyla biriktirmelidir. Bu yüzden paralel kimlikleri sürdürmek kasıtlı olarak pahalıdır.

Özgür toplumlarda maliyetler kötüye kullanımı caydırır.

Diktatörlüklerde ise paralel kimlikler bir hayatta kalma aracına dönüşür: yeraltı ağlarının örgütlenmesini, kara borsada daha güvenli hareket etmeyi ve bir kimliğin ele geçirilmesinin diğerlerini açığa çıkarmadığı bölmelenmiş[^compartmentalization] direnişi mümkün kılar — ve rejim düştükten sonra, kamusal yaşama ve orada inşa edilmiş itibara pürüzsüz bir dönüşe, hatta önceden resmî ve gizli olan DID'in bir iddia aracılığıyla tek bir birleşik kayıt kümesinde birleştirilmesine olanak tanır.

![WHAT IF SOMEONE CREATES MULTIPLE IDENTITIES?](../../Info%20Graphics/v5/v5-04a-vice-identit.webp)

> [!note] Ters Çevrilmiş Algı
> Devletin aksine, merkeziyetsiz kimlik üzerine kurulu bir itibar ağı ilkesi, algılanan öncelik paradigmasını tersine çevirir:
>
> - Önemli olan itibardır — yani karşı tarafla etkileşimin risklerini değerlendirmek için kullanılan geçmiş — ve ad, adres gibi kişisel veriler bir nezaket veri alışverişi meselesi olabilir
> - Oysa devlet öncelikle kişisel verileri talep eder, itibar verilerini biriktirir ve topluluğun yalnızca kendi işine gelenleri görmesine izin verir

## Zengin Biri Yalnızca Daha Fazla Kimlik (ya da Sanal Topluluk) “Satın” Alamaz mı?

Paralel merkeziyetsiz kimlikler oluşturma olasılığı, ilk bakışta daha fazla ekonomik olanağı olan insanların daha az olanı olanlara karşı haksız bir avantajı gibi görünür. Yine de şunu vurgulamak gerekir: belirli suçları ortadan kaldırmak için güç piramidindeki birkaç noktayı yozlaştırmanın yettiği merkezî bir sistemin aksine, merkeziyetsiz bir sistemde tüm topluluğu yozlaştırmak gerekirdi.

Yedek merkeziyetsiz kimlikler bu amaca hizmet edebilir, ama itibarları zaman içinde diğer gerçek topluluk üyeleriyle gerçek etkileşim yoluyla inşa edilmelidir — kolayca satın alınamaz, çünkü ağ, belirli bir kimliğin nasıl performans gösterdiğini doğrulanabilir kılar.

Dahası, bir otorite gibi davranarak, birkaç merkeziyetsiz kimliğin aslında aynı kişi olduğuna dair kanıt üreten soruşturmalar sunan hizmetler piyasada var olabilir (ve muhtemelen var olacaktır). İtibar ağına girilen tek bir kayıt böylece, paralel kimlikler inşa etmeye harcanan tüm zaman, enerji ve para yatırımını, maliyetin küçük bir bölümüne geçersiz kılabilir.

Ekonomik olarak, bu yüzden topluluğu aldatmamak — ve gerekirse eylemlerini gözden geçirip telafiye çalışmak — kârlıdır; öyle ki itibar kabul edilebilir bir düzeye geri döner ve taşıyıcısı topluluğun öfkesinden ekonomik ya da başka bir açıdan zarar görmez.

Kendi topluluğunda itibarını yitirmiş, ekonomik olarak güçlü bir kimlik, hedef kimliklerle el altından anlaşmalar yoluyla topluluğun öfkesinden kaçmaya çalışabilir — ama o zaman onlar da kendi itibarlarını yitirme riskine girer.

Yine de yeni bir kimlikle başka bir topluluğa kaçış hâlâ vardır — ama bu, tüm başarıları geride bırakmak ve sıfır itibarla bir yerde sıfırdan başlamak demektir. Bazen bu anlaşılır bir yol ve tek çıkış olabilir.

![YOU CAN'T CORRUPT AN ENTIRE COMMUNITY](../../Info%20Graphics/v5/v5-04b-centralizace-vs-decentralizace.webp)

> [!note] Not
> Benzer biçimde, topluluklar, birinin sanal bir kimlik oluşturmak için kaynak ayırdığı bir saldırıyla da başa çıkardı: o kimlik için, doğrulama olmadan başka bir toplulukla etkileşime girmek — yani diğer topluluğun kimlikleri hakkındaki bilgiyi eleştirmeden kabul etmek — risklidir. İtibarlar her zaman bir topluluk içinde inşa edilir, küresel olarak değil.

## Yalnızca Okumak İsteyip Topluluğa Hiçbir Şey Vermeyen Beleşçilere Ne Demeli?

Bilgiye erişim, merkeziyetsiz bir kimlik oluşturmanın ilk gününden itibaren sınırsız değildir. Yeni katılımcılar — henüz gerçek etkinlik yoluyla itibar inşa etmemiş olanlar — kademeli kısıtlamalarla karşılaşır: daha az bilgi, daha uzun bekleme süreleri, daha yüksek sorgu maliyetleri. Ağ, pasif tüketimi ve keyfi veri toplamayı değil, katılımı ödüllendirir.

Merkeziyetsiz bir kimlik, itibarını başka bir kişiye (ki bu kişi DID itibar ağında bile olmayabilir) ödeme karşılığında ödünç verdiğinde de itibarını riske atar. Burada da aynı ilke geçerlidir: topluluğa yönelik böyle bir ihanet (mahremiyet ihlali) haine itibarında yansıyabilir ve bu eylem, merkezî bir sistemde olduğu gibi el altından bir anlaşmayla silinemez. Topluluğun öfkesiyle, başarıların yitirilmesi dahil, hesaplaşmak zorundadır — çünkü topluluk, örneğin taşınır ve taşınmaz mülk sahibi olma ayrıcalığının, onların gözünde teminatçısıdır.

> [!note] Gerçek Dünyaya Bir Çıpa
> Riski değerlendirirken, daha riskli özne doğal olarak belirli bir topluluk tarafından tanınan mülkiyet ayrıcalığından yararlanmayan kişidir — işlemlerinde yitirecek daha az şeyi vardır (dijital varlıkları hareket ettirmek daha kolaydır).
>
Küçük bir ayrıntı gibi görünebilir, ama büyük sonuçları vardır. Topluluğun üyeleri üzerinde bir kaldıraca sahip olmasını istemek, mülkiyeti bir ayrıcalık olarak ima eder — en özgür toplumlarda neredeyse dokunulmaz, ama yine de bir hak değil, temel bir ilke de değil, uç durumlarda geri alınabilecek bir ayrıcalık (örneğin silahlı çatışmada topluluğun savunmasında hizmeti reddetmeyi düşünebilirim).
>
Ayrıca, topluluğun üyelerine nasıl davranacağını ve bir üyenin — ayrıcalıklarını korumak için — topluluk uğruna savaşmak için nasıl bir güdüsü olduğunu da bilinçaltından yanıtlar. Bir kişi topluluğa karşı sorumluluğunda başarısız olabilir, ama zorlukla kazanılmış ayrıcalıkları korumaya gelince ahlaken hoşgörü bekleyemez.

![THE NETWORK REWARDS PARTICIPATION](../../Info%20Graphics/v5/v5-04c-prizivnici.webp)

## Finansal Nötrlük

Merkeziyetsiz, sansürlenemez, yozlaştırılamaz gibi sözcükler okunduğunda, insan bunları bu terimlerle tanımlanabilen en tanınmış kripto paralarla — Bitcoin, Monero ve diyelim Kaspa — ilişkilendirmeden edemiyor. Ancak sezgi burada yanıltıcıdır: otoritelerin hizmetleri, doğrulama ve yayımlama vb. için ücretler herhangi bir para birimiyle ya da parayla ödenebilir. DID ağındaki sosyal ağın bağlı katılımcıları (yani sizin topluluğunuz) ve çevresi için önemli olan, ödemenin yapıldığına dair itibarla desteklenmiş bir onaydır. Bir iddianın yayımlanması, bir aktörün enerji, para ve zaman harcamadan istediği kadar ve istediği iddiayı yayımlayamaması için, tek tek makul, doğrulanabilir bir maliyet taşımalıdır — bu, bugünün yolsuzluğa bulanmış devlet sistemlerindeki seçkinlerin ayrıcalığına karşılık gelen, son derece istenmeyen bir durumdur.

Bu bakımdan sözü edilen kripto paraların küçük bir avantajı vardır: ağları, belirli bir ödemenin gerçekleştiğini doğrulamak için, küçük bir mahremiyet kaybı ve bazı adreslerin ifşası pahasına, güvenilir otoriteler gibi davranır.

[^trackrecord]: **Geçmiş kayıt (track record)** — genel olarak: bir kişinin ya da kuruluşun geçmiş sonuçlarının, başarılarının ve başarısızlıklarının geçmişi. Burada: belirli bir DID kimliğinin ağdaki tüm geçmiş etkileşimlerinin toplamı — doğrulanmış iddialar, kabul edilen ve reddedilen kayıtlar — itibarının bunlardan türetildiği toplam.

[^compartmentalization]: **Bölmeleme (compartmentalization)** (İng. *compartment*, bölme) bilgiyi, bir birimin ifşasının diğerlerini tehlikeye atmayacağı biçimde izole birimlere ayırmak demektir. İstihbarat servislerinden bilinen bir ilke: bir ajan operasyonun yalnızca kendi kısmını bilir, dolayısıyla baskı altında bile bütünü açığa çıkaramaz.
