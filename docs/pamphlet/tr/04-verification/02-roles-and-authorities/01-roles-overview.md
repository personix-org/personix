---
title: "Rollere Genel Bakış"
chapter: 3
part: "Doğrulama Nasıl İşler"
lang: en
version: v6
---

# Rollere Genel Bakış

Bu rollerden bazılarına, ağ ve temel özellikleri hakkındaki bölümde kısaca değinmiştik. Şimdi onlara yeniden daha ayrıntılı bakma ve ağı daha sağlam kılmak için ihtiyaç duyduğumuz ek olanları ekleme zamanı. Her doğrulama işlemi birkaç rolü içerir — bunların nasıl davrandığına bakalım.

> [!note] Bir Doğrulama İşlemindeki Roller
> Her doğrulama, aşağıdaki tabloda özetlenen altı ayrı role kadar rolü içerir. Bunların hepsi merkeziyetsiz itibar ağında kendi DID'ine sahip olabilir.

| Rol | Açıklama |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **İhraççı** | Bilgiyi ağa yayımlayan kişi — bir şeyin olduğunu iddia eder (bir DID oluşturuldu, düzenlendi ya da feshedildi, bir iddia, belirli bir DID'in politikası vb.) |
| **Özne** | Bilginin hakkında olduğu kişi — iddianın muhatabı |
| **Otorite** | İddiayı soruşturarak ve sunulan kanıtı inceleyerek ya da onu etkin biçimde toplayarak iddianın niteliği üzerine adını koyan güvenilir varlık |
| **Gözlemci** | Doğrulayıcının iddiayı nasıl ele aldığına dair kayıt tutan bağımsız üçüncü taraf — doğrulayıcının ne sessiz kalmasını ne de ilan ettiği politikadan sapmamasını sağlar |
| **Doğrulayıcı** | İşlemi işleyen, algoritmik olarak seçilmiş katılımcı |
| **Vekil** | Başka bir katılımcı adına hareket eden kişi |
