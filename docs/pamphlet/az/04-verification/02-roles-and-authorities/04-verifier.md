---
title: "Doğrulayıcı"
chapter: 3
part: "Doğrulama Necə İşləyir"
lang: en
version: v6
---

# Doğrulayıcı

İstənilən DID doğrulayıcı kimi çıxış edə bilər, ya birbaşa, ya da üçüncü bir DID-ə səlahiyyət kimi verilmiş doğrulama hüquqları vasitəsilə. Mənim — ya da səlahiyyətlimin — doğrulaya bilməsi üçün şəbəkədə əlçatan (onlayn) olmalıyam. Hər kəs buna öhdəlik götürmək istəməyəcək, məhz buna görə də DID qeydi, offlayn olduğu müddətdə funksiyanı onun adından yerinə yetirəcək əvəzediciləri prioritet sırası ilə sadalaya bilər.

Şəbəkədə aktiv olan hər DID öz siyasətini açıq şəkildə bəyan edir. Həmin siyasətdə müəyyən edilmiş qaydalar vasitəsilə o, doğrulama prosesi zamanı qarşı tərəfin reputasiyasını və naşirin reputasiya şəbəkəsinə dərc üçün işarələdiyi iddianın məzmununu və formasını mühakimə edir. Siyasətin bir hissəsi doğrulama xidmətləri üçün ödənişləri hesablamaqda istifadə olunan hesablama düsturudur. Bu, yerində olduqdan sonra, şəbəkədən axan statistik olaraq çoxlu sayda iddia arasında mən şəbəkənin alqoritminin məni naşirin tərəfinə çəkməsini və verilmiş iterasiyada verilən məlumatı doğrulamaq üçün mənə tapşırmasını gözləyirəm. Naşir düzgün davranan bir doğrulayıcının necə reaksiya verəcəyini əvvəlcədən hesablaya bilər, amma onlarla (ya da onların əvəzediciləri ilə) faktiki əlaqə saxlamaqdan qaça bilməz; seçilmiş doğrulayıcı ilə iterasiya, hətta əvvəlcədən keçməyəcəyini bildikləri halda belə, naşir tərəfindən yerinə yetirilməlidir.

Naşirin doğrulayıcı-seçim alqoritmini düzgün namizəd doğrulayıcı DID-lər dəsti üzərində işlətdiyini haradan bilirik? Hər DID öz açıq şəkildə bəyan etdiyi siyasəti ilə birlikdə reputasiya şəbəkəsi daxilində öz sosial şəbəkəsinin identifikatorlarının cari siyahısını da dərc edir. Əgər naşir öz sosial şəbəkəsini sadəcə öz baxışlarını əks etdirən və gücləndirən bir sosial qabarcıq kimi müəyyən edirsə, onun vasitəsilə dərc olunan məlumat digər icmalar tərəfindən çətinliklə daha geniş qəbul ediləcək. Mənim böyük xərclə radikal bir iddianı şəbəkəyə itələməyi bacarmam qarşı tərəfin reputasiyasını mühakimə edərkən ona hər hansı çəki verəcəyim mənasına gəlmir. Bəzi iddiaları nəzərə almağa icmam tərəfindən itələnirəm (təqsirkarlara verilən hökmlər və məhdudiyyətlər); başqaları isə tamamilə mənim ixtiyarımdadır — verilmiş məlumat parçasını daxil etməyin ya da xaric etməyin iqtisadi dəyərinə özüm qərar verirəm.

![DOĞRULAYICI — ALQORİTM TƏRƏFİNDƏN SEÇİLƏN](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
