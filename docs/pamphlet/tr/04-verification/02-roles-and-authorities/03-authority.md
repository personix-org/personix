---
title: "Otorite"
chapter: 3
part: "Doğrulama Nasıl İşler"
lang: en
version: v6
---

# Otorite

Otorite ikili bir rol oynar: bir **denetçi** (bir iddia yayımlanmadan önce kanıtın niteliğini doğrular) ya da bir **kefil** (bir iddianın doğruluğu üzerine itibarını ortaya koyar) olabilir. Her iki durumda da ihraççının iddiasını güçlendirir. Bu iki hizmet ayrılabilir — bir otorite birini, ötekini ya da ikisini birden sunabilir. Çalışma varsayımı, otoritelerce sağlanan hizmetlerin çoğunun serbest piyasa temelinde sunulabileceğidir. Bu, adalet gibi özelleştirilmesi zor hayal edilen alanlarda bile geçerlidir; burada uzmanlaşmış hizmetler — soruşturma, kanıt değerlendirmesi, hatta bugün merkezî ordularca sağlanan hizmetlere (stratejik planlama, standartlaştırılmış eğitim, tedarik ve stok yönetimi vb.) kadar — piyasa aktörlerince verimli biçimde sunulabilir. Yeniden yapılandırıldıktan sonra serbest piyasa teşvikleriyle daha verimli kılınamayacak neredeyse hiçbir şey yoktur.

> [!warning] Otorite, ihraççı ve gözlemci asla kendi olgularının doğrulayıcısı olamaz.
> Doğrulayıcının algoritmik seçimi bağımsızlığı güvence altına alır. Hiç kimse kendi iddiasını ya da doğrudan çıkarı olan bir iddiayı doğrulayamaz. Bu, tüm DID topluluğunun savunmakta çıkarı olduğu temel kurallardan biridir.

Aşağıdaki grafikler, otoritelerin kapsadığı etkinlik genişliğine dair tamamlayıcı görünümler sunar (“otorite” terimi “hizmet sağlayıcı” ile birbirinin yerine okunabilir).

![THE AUTHORITY — WHO STAKES THEIR NAME](../../../Info%20Graphics/v5/v5-08d-role-authority.webp)

![TWO FACES OF AUTHORITY](../../../Info%20Graphics/v5/v5-08a-autorita-auditor-garant.webp)

> [!note] Kimliğini Gizleyen Gözlemci Olarak Otorite
> Saygın bir otorite — işi yalnızca geçmiş kaydına bağlı bir noterı düşünün — ana işlevlerin (denetçi / kefil) yanında bir üçüncüsünü de sunabilir: doğrulama sırasında kimliğini gizleyen gözlemci rolü. Sunulan iddianın zaman damgalı bir kaydını tutarlar; böylece doğrulayıcı onu sessizce düşüremez. Gözlemci rolünün mekanizması, Gözlemci rolüne ilişkin bölümde daha ayrıntılı anlatılır.
