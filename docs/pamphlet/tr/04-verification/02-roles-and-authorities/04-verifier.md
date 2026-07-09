---
title: "Doğrulayıcı"
chapter: 3
part: "Doğrulama Nasıl İşler"
lang: en
version: v6
---

# Doğrulayıcı

Herhangi bir DID, doğrudan ya da üçüncü bir DID'e devredilmiş doğrulama hakları aracılığıyla doğrulayıcı olarak hareket edebilir. Benim — ya da vekilimin — doğrulayabilmesi için ağda ulaşılabilir (çevrimiçi) olmam gerekir. Herkes buna bağlanmak istemez; bu yüzden bir DID kaydı, o çevrimdışıyken işlevi onun adına yerine getirecek yedekleri öncelik sırasına göre listeleyebilir.

Ağda etkin olan her DID, kendi politikasını kamuya açık olarak ilan eder. O politikada tanımlanan kurallar aracılığıyla, doğrulama süreci boyunca karşı tarafın itibarını ve ihraççının itibar ağına yayımlanmak üzere işaretlediği iddianın içeriğini ve biçimini değerlendirir. Doğrulama hizmetleri için ücretleri hesaplamakta kullanılan hesaplama formülü politikanın bir parçasıdır. Bu yerine oturduğunda, ağdan akan istatistiksel olarak çok sayıda iddia arasında, ağın algoritmasının beni ihraççının tarafına çekmesini ve belirli bir yinelemede, ihraç edilen bilgiyi doğrulamam için bana atamasını beklerim. İhraççı, doğru davranan bir doğrulayıcının nasıl tepki vereceğini önceden hesaplayabilir, ama onlarla (ya da yedekleriyle) gerçekten iletişime geçmekten kaçınamaz; seçilen doğrulayıcıyla yineleme, önceden geçmeyeceğini bilse bile ihraççı tarafından yürütülmelidir.

İhraççının, doğrulayıcı seçim algoritmasını doğru aday doğrulayıcı DID kümesi üzerinde çalıştırdığını nereden biliriz? Her DID, kamuya açık olarak ilan ettiği politikasıyla birlikte, itibar ağı içindeki sosyal ağının güncel tanımlayıcı listesini de yayımlar. Bir ihraççı, sosyal ağını yalnızca kendi görüşlerini yankılayan ve pekiştiren bir sosyal balon olarak tanımlarsa, onun aracılığıyla yayımlanan bilgi diğer topluluklarca zar zor daha geniş biçimde alınacaktır. Ağa yüksek maliyetle radikal bir iddiayı sokmayı başarmam, karşı tarafın itibarını değerlendirirken ona herhangi bir ağırlık vereceğim anlamına gelmez. Bazı iddiaları dikkate almam için topluluğum beni iter (faillere verilen cezalar ve kısıtlamalar); diğerleri tümüyle bana kalmıştır — belirli bir bilgiyi dahil etmenin ya da dışlamanın ekonomik değerine kendim karar veririm.

![THE VERIFIER — CHOSEN BY THE ALGORITHM](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
