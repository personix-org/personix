---
title: "Reputasiyaya Əsaslanan Sosial Şəbəkə"
chapter: 2
part: "Alət"
lang: en
version: v6
source: v1
---

# Reputasiyaya Əsaslanan Sosial Şəbəkə

Dəyişikliyi həyata keçirmək üçün diqqətlə hazırlanmış bir alətə ehtiyacımız var. Əvvəlcə onu qısaca eskiz edəcəyik; sonrakı fəsillərdə hər hissəni daha ətraflı nəzərdən keçirəcək və yenilərini əlavə edəcəyik. Təsəvvür edin, senzura edilə bilməyən, qlobal, mərkəzsizləşdirilmiş bir sosial şəbəkə, harada öz vəkil kimliyinizi — sözdə Mərkəzsizləşdirilmiş Kimliyi (DID) — təhlükəsiz şəkildə yarada və idarə edə bilərsiniz. DID özünüzün yaratdığınız və idarə etdiyiniz rəqəmsal kimlikdir, heç bir mərkəzi avtoritetdən asılı olmadan. Onu heç kim əlinizdən ala və ya saxtalaşdıra bilməz, çünki o, sizin özəl açarınızla (ya da açarlarınızla, multisig vasitəsilə) kriptoqrafik olaraq imzalanır.

> [!note] Qeyd
> Bir nəticə odur ki, belə bir kimlik tədricən dövlətin verdiyi kimlik sənədlərini əvəz edə bilər — amma bu barədə keçid fəslində daha ətraflı.

![KİMLİYİN SƏNİN, AÇARLARIN SƏNİN, QAYDALARIN SƏNİN](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

Belə bir şəbəkədə öz kimliyiniz vasitəsilə kiminsə sizə zərər vurduğunu (və sonradan, ehtimalən, onu düzəltdiyini ya da düzəltməyə məcbur edildiyini) bildirə bilərsiniz. Zərərin törədicisinə ünvanlanan bu geribildirimin əhəmiyyətli bir mənbə kimi dəyəri olması üçün məlumatı şəbəkəyə daxil etmək vaxt, enerji və pula başa gəlməlidir — üstəlik, bunun boş söz-söhbət olmadığına dair başqaları üçün doğrulana bilən sübut ortaya qoyulmalıdır.

Məlumatı oxumaq asan və nisbətən ucuz olardı, amma fərdi bir qeydi yaratmaq baha və çətin olardı. Yazmaq aydın bir protokola tabe olardı ki, orada seçilmiş alqoritmə görə hesablama, təqdim edilən məlumatın doğrulanması üçün hansı DID-dən soruşulacağını və seçilmiş iştirakçının məlumatı sizin adınıza necə emal edəcəyini, dərc edəcəyini və onun doğrulayıcısına çevriləcəyini ciddi şəkildə müəyyən edir.

> [!note] Alqoritm vs radikalizm
> Doğrulayıcıların alqoritmik seçimi təmin edir ki, radikal olmayan məlumat naşirləri zaman keçdikcə dərc olunan məlumatın xərcləri ilə doğrulama üçün mükafatlar arasında demək olar ki, neytral balansı saxlasınlar.

![DƏRC ETMƏK VAXT, ENERJİ VƏ PULA BAŞA GƏLİR](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Gəlin alqoritmin doğrulayıcını necə seçdiyinə baxaq.

> [!note] Alqoritm
> Alqoritmik seçim müxtəlif məlumat parçaları üçün qeyri-deterministik şəkildə fərqli bir doğrulayıcı (ya da mümkün doğrulayıcılar dəstini) seçir. Tam DID sənədinin heşi (istənilən girişdən unikal “barmaq izi” yaradan birtərəfli riyazi funksiya — sənədin barmaq izi kimi) ardıcıl heş halqasında mövqeyi müəyyən edir və doğrulayıcı namizədlərini seçir.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> Sadə dildə: alqoritm bütün DID sənədinizi götürür, ondan bir barmaq izi hesablayır və həmin barmaq izi sizin doğrulayıcınızı müəyyən edir.

![ALQORİTM DOĞRULAYICINIZI NECƏ SEÇİR](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Alqoritmin seçdiyi ilk doğrulayıcı ilə siz naşir kimi uğur qazanmaya bilərsiniz — reputasiyanız ya da bəyan etdiyiniz parametrlər onun tələblərinə cavab verməyə bilər. Növbətisini alqoritmik olaraq axtarmağa davam edərdiniz, bunun üçün başqa bir rekursiv iterasiya edərək, sizə daha bir doğrulayıcı təyin edərdiniz. Hər addımda hədəf doğrulayıcıya olan “məsafə” artır, onunla birlikdə dərc olunmalı müşayiətedici metadata da artır. Məlumat böyüdükcə xərclər təbii şəkildə qalxır (yalnız iddianın ilkin ölçüsünə görə deyil, həm də hər rəddedilmə ilə yığılan metadataya görə). Etibarlı məlumat mənasız qərəzlərdən çox daha asan keçir. Nə qədər yüksək qiymət ödəməyə hazır olduğu və qeydin onun üçün nə qədər əhəmiyyət daşıdığı hər kəsin öz işidir — radikalizm zəmanətlə bahalaşacaq.

![DOĞRULAYICI NECƏ CAVAB VERİR](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Doğrulayıcı sizin doğrulama sorğunuza cavab olaraq nə qərara alsa da, top yenidən naşirin meydanındadır: o, doğrulayıcının doğrulama xidmətləri təklifini qəbul edə bilər, cavabı xronologiyaya qatıb yenidən (daha baha) cəhd edə bilər, ya da uzaqlaşıb batmış xərci udmağı seçə bilər.

![NAŞİRİN SEÇİMİ](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Məlumatınıza daha çox çəki və doğrulayıcılar yanında qəbul edilmək üçün daha yaxşı şans vermək məqsədilə — dərc olunan məlumatda payı olan naşir kimi — **etibarlı bir avtoritetin** xidmətlərindən istifadə edə bilərsiniz. Avtoritet ya təqdim edilən məlumatı rədd edir, ya da onu qəbul edib öz yaxşı adını (reputasiyasını) ona qoyur. Avtoritet adətən real dünya sübutlarını tələb edir, onları yoxlayır və təsnif edir. Nəticə onun verilmiş halı verilmiş vaxtda qiymətləndirməsinin protokoludur. Avtoriteti həm real, həm rəqəmsal dünyada müəyyən növ xidmət üzrə mütəxəssis kimi düşünün — məsələn, müstəntiq, auditor, sığortaçı, müəyyən sinif malların təchizatçısı (mahiyyət etibarilə bazardakı istənilən iqtisadi aktor).

![ŞƏBƏKƏDƏ QEYD NECƏ YARANIR](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Siz məlumatı şəbəkəyə dərc etməyə çalışdığınız vaxta qədər o, çox güman ki, artıq öz aktorları haqqında məlumat daxil edəcək — bunlar reputasiya siqnallarıdır. Reputasiya siqnallarını necə oxumaqda — onların müxtəlif vəziyyətlərdə sizin üçün nə demək olduğu və hansı riskləri daşıdığı — istiqamət tapmaq mümkün ki, o qədər də sadə deyil. Hər iştirakçı reputasiya qeydlərinə öz DID-i vasitəsilə fərqli baxa bilər, qarşı tərəflə bağlı həll etdiyi vəziyyətdən asılı olaraq. Qarşı tərəf etibarlı bir ödəyicidir, yoxsa biznes əməliyyatı üçün pulu qabaqcadan tələb etməliyəm? Təklif olunan məhsulun gizli dələduzluq ya da qüsurlar haqqında rəyləri varmı? Nəsə səhv gedəndə müqavilə məsuliyyətindən sıyrılmağa çalışırlarmı? Bəzən qarşı tərəfin ümumi ardıcıllığına daha kompleks baxış lazım olur — bu, kimin icmalı tələb etdiyinin seçimlərindən asılıdır. Bazar reputasiyanın verilmiş vəziyyət kontekstində oxunmasını sadələşdirən, emal edən və aydınlaşdıran məhsul və xidmətlər təklif edə bilər. Müxtəlif avtoritetlər və onların təklif etdikləri xidmətlər də bu məqsədə xidmət edə bilər.

![REPUTASİYA NECƏ OXUNUR](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Nümunələr
> Naşirlər üçün maraqlı — və başqaları üçün dəyərli — tipik məlumat real ya da virtual dünyada adi şəxslərarası ünsiyyətdən kənar hadisələrə aiddir.
>
> Mənfi nümunələr:
> - cinayət əməllərinin sübutu (məsələn, etibarlı bir istintaq orqanı tərəfindən audit edilmiş)
> - dolayı sübutlar (təkbaşına zəif, amma statistik olaraq yığılan) — məsələn, qısa müddət ərzində bir neçə oğurluğun yaxınlığında təkrarən mövcud olmaq → yenə də təsadüf?
> - müqavilənin pozulması
>
> Müsbət nümunələr:
> - düzəldilmiş zərər (könüllü ya da icmanın cəza kimi təzyiqi altında)
> - X avtoriteti tərəfindən təklif edilmiş cəzanın qəbul edilməsi və çəkilməsi
> - X avtoriteti müəyyən dərəcədə təqsirkarın mülkiyyət hüquqlarının tanınmasını ləğv etdi
>
> Qarşı tərəf haqqında mövcud məlumatı toplamaq və riskləri öz seçimlərinə görə qiymətləndirmək hər kəsin öz işidir.

![ŞƏBƏKƏDƏ NƏ QEYD EDƏ BİLƏRSİNİZ?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Sizin haqqınızda məlumatın şəbəkədə görünüb-görünməməsi yalnız sizin öz davranışınızdan asılıdır.
> Belə bir şəbəkəyə heç vaxt qoşulmaq məcburiyyətində deyilsiniz, yenə də sizin haqqınızda məlumat orada görünə bilər. Bu, yalnız sizin hərəkətlərinizdən və onların başqalarına təsirindən asılıdır.

![İCMA SİZİN ÜÇÜN BİRİNİ AÇA BİLƏR](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

İndicə qısaca eskiz etdiyim şey Mərkəzsizləşdirilmiş Kimlikdən (DID) ilham alan bir sosial şəbəkənin necə işləyə biləcəyidir. DID konsepsiyalarının əsas məqsədi izləyəcəyim və yaşayacağım qaydalara üzv olmaq prinsipi vasitəsilə məxfiliyi və azadlığı gücləndirmək — istifadəçilərə hansı məlumatı hansı şərtlərlə paylaşacağını qərara alma imkanı verməkdir.

Mən DID-ləri əlavə olaraq bir ünsiyyət şəbəkəsində birləşdirməyi təklif edirəm ki, orada onların sahibləri kiməsə nəsə baş verdiyi və icmanın ya da fərdin reaksiya verməsi lazım olduğu vəziyyətlərdən kənarda belə geribildirim mübadiləsi etsinlər. Üzv olduğumuz qaydaların belə preventiv müqayisəsi — qarşı tərəfin necə fəaliyyət göstərməli olduğu ilə bağlı gözləntilərdəki qarşılıqlı sapmaların iqtisadi və digər nəticələrini hesablamaq imkanı ilə — konsensus tapmaq üçün motivasiya sayıla bilər. Azadlıq əvəzinə belə bir sistem real dünyadakı davranışa görə məsuliyyətlə birləşmiş könüllü qərar qəbulunu vurğulayardı.

Fərd sistemi təkbaşına sındıra bilməz — bir qrup insanın daha çox şansı var, çox məsələdə birlikdə çəkmək üçün razılaşdırılmış konsensusu və motivasiyaları olan bir qrup insanın isə avtoritar meyllərə müqavimət göstərmək üçün daha da çox şansı var. Birinci fəsildəki təşkilatlanma ön şərti iki şərt ödəndikdə yerinə yetiriləcək: DID reputasiya şəbəkəsi icmaları kifayət qədər təmsilçi şəkildə əhatə edir ki, onun istifadəsi ekzotik olmaqdan çıxsın. Və eyni zamanda bu icma seqmenti cəmiyyətin qalan hissəsi ilə iddialı şəkildə danışıqlar apara bilən iqtisadi baxımdan əhəmiyyətli azlığa çevrilsin.

> [!note] Könüllülük vs azadlıq
> Azadlıq — müsbət mənada — iki amili tarazlaşdırmağın ikinci dərəcəli təsiri olardı: könüllülük və ətrafın məsuliyyətə doğru təzyiqi.

> [!note] Süni İntellekt Erası və Reputasiyanın Dəyəri
> Süni intellekt erasında koqnitiv təfəkkürlə bağlı hər şey avtomatlaşdırılır — və bu, daha da irəli gedə bilər. Bəs onda insan fəaliyyətində rəqabət üstünlüyü kimi nə qalır? Cavab çətindir və mütləq nəsə tapılacaq, amma bir şeyi əminliklə deyə bilərik: reputasiya qərar verəcək. Davranışınızın, öhdəliklərinizin və onların yerinə yetirilməsinin doğrulana bilən tarixçəsi — bu, süni intellektin sizin üçün qurmayacağı bir şeydir.

![SÜNİ İNTELLEKT REPUTASİYANIZI QURA BİLMƏZ — YALNIZ SİZ](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![HƏQİQƏTİN İQTİSADİYYATI](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
