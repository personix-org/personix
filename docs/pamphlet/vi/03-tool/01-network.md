---
title: "Reputation-Based Social Network"
chapter: 2
part: "The Tool"
lang: en
version: v6
source: v1
---

# Mạng xã hội dựa trên danh tiếng

Để tạo ra thay đổi, chúng ta cần một công cụ được thiết kế cẩn thận. Trước hết ta sẽ phác họa nó vắn tắt; trong các chương sau ta sẽ xem xét từng mảnh chi tiết hơn và bổ sung thêm. Hãy hình dung một mạng xã hội phi tập trung, toàn cầu, không thể kiểm duyệt, nơi bạn có thể an toàn tạo ra và quản lý danh tính đại diện của mình — một cái gọi là Danh tính Phi tập trung (DID). DID là một danh tính số mà bạn tự tạo và tự kiểm soát, không phụ thuộc vào bất kỳ thẩm quyền trung tâm nào. Không ai có thể lấy đi hay làm giả nó, bởi nó được ký bằng mật mã với khóa riêng của bạn (hoặc nhiều khóa, qua multisig).

> [!note] Ghi chú
> Một hệ quả là một danh tính như vậy có thể dần thay thế các giấy tờ tùy thân do nhà nước cấp — nhưng chi tiết hơn sẽ ở chương về chuyển tiếp.

![YOUR IDENTITY, YOUR KEYS, YOUR RULES](../../Info%20Graphics/v5/v5-01b-co-je-did.webp)

Trong một mạng lưới như vậy, qua danh tính của mình, bạn có thể báo rằng ai đó đã gây thiệt hại cho bạn (và về sau, có thể, rằng họ đã khắc phục nó hoặc bị buộc phải khắc phục). Để phản hồi này — nhắm vào kẻ đã gây ra thiệt hại — có giá trị như một nguồn thông tin đáng tin, việc đưa thông tin vào mạng lưới phải tốn thời gian, năng lượng và tiền bạc — và trên hết, phải tạo ra bằng chứng có thể kiểm chứng cho những người khác rằng đây không phải chuyện tầm phào.

Đọc thông tin thì dễ và tương đối rẻ, nhưng tạo ra một bản ghi riêng lẻ thì tốn kém và đòi hỏi công sức. Việc ghi sẽ tuân theo một giao thức rõ ràng, trong đó phép tính theo thuật toán đã chọn xác định một cách nghiêm ngặt phải hỏi DID nào để xác minh thông tin đã gửi và tiến hành thế nào để người tham gia được chọn xử lý thông tin thay cho bạn, công bố nó, và trở thành người xác minh của nó.

> [!note] Thuật toán so với chủ nghĩa cực đoan
> Việc chọn người xác minh theo thuật toán bảo đảm rằng những người công bố thông tin không cực đoan, theo thời gian, sẽ duy trì được một cán cân gần như trung tính giữa chi phí của thông tin được công bố và phần thưởng cho việc xác minh.

![PUBLISHING COSTS TIME, ENERGY, AND MONEY](../../Info%20Graphics/v5/v5-02g-cena-publikace.webp)

Hãy xem thuật toán chọn người xác minh thế nào.

> [!note] Thuật toán
> Việc chọn theo thuật toán chọn ra một cách phi tất định một người xác minh khác nhau (hoặc một tập hợp những người xác minh khả dĩ) cho những mẩu thông tin khác nhau. Một hash (một hàm toán học một chiều tạo ra một “dấu vân tay” duy nhất từ bất kỳ đầu vào nào — như dấu vân tay của một tài liệu) của toàn bộ tài liệu DID xác định vị trí trên một vòng hash nhất quán và chọn ra các ứng viên xác minh.
>
> $$
> \text{verifier\_DID} = \text{hash}(\text{DID\_document})
> $$
>
> Nói nôm na: thuật toán lấy toàn bộ tài liệu DID của bạn, tính một dấu vân tay từ đó, và dấu vân tay ấy xác định người xác minh của bạn.

![HOW THE ALGORITHM SELECTS YOUR VERIFIER](../../Info%20Graphics/v5/v5-02e-hash-ring.webp)

Với người xác minh đầu tiên mà thuật toán chọn ra, bạn với tư cách người công bố có thể không thành công — danh tiếng hoặc các thiết đặt bạn tuyên bố có thể không đáp ứng yêu cầu của họ. Bạn sẽ tiếp tục tìm kiếm người kế tiếp theo thuật toán bằng cách thực hiện một vòng lặp đệ quy khác, gán cho bạn một người xác minh xa hơn. Với mỗi bước, “khoảng cách” tới người xác minh đích tăng lên, và siêu dữ liệu đi kèm phải công bố cũng vậy. Khi dữ liệu lớn lên, chi phí tự nhiên tăng theo (không chỉ vì kích thước ban đầu của tuyên bố, mà còn vì siêu dữ liệu tích lũy sau mỗi lần bị từ chối). Thông tin đáng tin đi qua dễ dàng hơn nhiều so với những ý thích vô lý. Mỗi người tự quyết định họ sẵn lòng chịu cái giá cao đến đâu và bản ghi ấy quan trọng với họ đến mức nào — chủ nghĩa cực đoan chắc chắn sẽ trở nên đắt đỏ.

![HOW THE VERIFIER ANSWERS](../../Info%20Graphics/v5/v5-02e2-odpoved-verifikatora.webp)

Dù người xác minh quyết định thế nào trước yêu cầu xác minh của bạn, quả bóng lại quay về sân của người công bố: họ có thể chấp nhận đề nghị dịch vụ xác minh của người xác minh, gộp câu trả lời vào dòng thời gian và thử lại (với giá cao hơn), hoặc bỏ đi và nuốt trọn khoản chi phí đã mất.

![THE ISSUER'S CHOICE](../../Info%20Graphics/v5/v5-02e3-rozhodnuti-issuera.webp)

Để thông tin của bạn có sức nặng hơn và cơ hội được các người xác minh chấp nhận tốt hơn, bạn — với tư cách người công bố có lợi ích trong việc thông tin được phát hành — có thể dùng dịch vụ của một **thẩm quyền đáng tin cậy**. Thẩm quyền hoặc từ chối thông tin đã gửi, hoặc chấp nhận nó và đặt cược danh tiếng (danh dự) của mình vào đó. Thẩm quyền thường yêu cầu bằng chứng ở thế giới thực, kiểm chứng và phân loại nó. Đầu ra là một biên bản đánh giá vụ việc đã cho tại thời điểm đã cho. Hãy nghĩ về một thẩm quyền như một chuyên gia trong một loại dịch vụ nhất định ở cả thế giới thực lẫn thế giới số — chẳng hạn một điều tra viên, một kiểm toán viên, một hãng bảo hiểm, một nhà cung cấp một loại hàng hóa nhất định (về bản chất, bất kỳ tác nhân kinh tế nào trên thị trường).

![HOW A RECORD IS CREATED IN THE NETWORK](../../Info%20Graphics/v5/v5-02a-jak-vznika-zaznam.webp)

Đến lúc bạn thử công bố thông tin vào mạng lưới, có lẽ nó đã chứa sẵn thông tin về các tác nhân của nó — đó là những tín hiệu danh tiếng. Việc điều hướng cách đọc các tín hiệu danh tiếng — chúng có ý nghĩa gì với bạn trong những tình huống khác nhau và chúng mang những rủi ro gì — có thể không hề đơn giản. Mỗi người tham gia có thể nhìn các bản ghi danh tiếng khác nhau qua DID của mình, tùy vào tình huống họ đang xử lý với đối tác. Đối tác có phải người trả tiền đáng tin, hay tôi cần đòi tiền trước cho một giao dịch kinh doanh? Sản phẩm được chào có mang những đánh giá về gian lận hay khiếm khuyết ẩn giấu không? Họ có đang cố lẩn tránh trách nhiệm hợp đồng khi có chuyện xảy ra không? Đôi khi một cái nhìn phức tạp hơn về tính nhất quán tổng thể của đối tác lại hữu ích — điều đó tùy vào sở thích của người yêu cầu bản tổng quan. Thị trường có thể cung cấp các sản phẩm và dịch vụ giúp đơn giản hóa, xử lý và làm rõ việc đọc danh tiếng trong bối cảnh của tình huống trước mắt. Các thẩm quyền khác nhau và dịch vụ họ chào cũng có thể phục vụ mục đích này.

![HOW TO READ REPUTATION](../../Info%20Graphics/v5/v5-02b-jak-se-cte-reputace.webp)

> [!example] Ví dụ
> Những thông tin điển hình mà người công bố quan tâm — và có giá trị với người khác — liên quan đến những sự kiện vượt ra ngoài giao tiếp thông thường giữa người với người trong thế giới thực hoặc ảo.
>
> Ví dụ tiêu cực:
> - bằng chứng về hành vi phạm tội (ví dụ được một cơ quan điều tra đáng tin kiểm định)
> - bằng chứng gián tiếp (yếu khi đứng một mình, nhưng tích lũy về mặt thống kê) — ví dụ nhiều lần có mặt gần nhiều vụ trộm trong thời gian ngắn → vẫn là trùng hợp chăng?
> - vi phạm hợp đồng
>
> Ví dụ tích cực:
> - thiệt hại đã được khắc phục (tự nguyện hoặc dưới áp lực của cộng đồng như một hình phạt)
> - chấp nhận và thi hành một hình phạt do thẩm quyền X đề xuất
> - thẩm quyền X đã thu hồi việc công nhận quyền tài sản của kẻ vi phạm ở một mức độ nhất định
>
> Mỗi người tự thu thập thông tin sẵn có về đối tác và đánh giá rủi ro theo sở thích của mình.

![WHAT CAN YOU RECORD IN THE NETWORK?](../../Info%20Graphics/v5/v5-02d-priklady-zaznamu.webp)

> [!note] Việc thông tin về bạn có xuất hiện trong mạng lưới hay không chỉ phụ thuộc vào hành vi của chính bạn.
> Bạn không bao giờ buộc phải tham gia một mạng lưới như vậy, thế nhưng thông tin về bạn vẫn có thể xuất hiện trong đó. Điều đó chỉ phụ thuộc vào hành động của bạn và tác động chúng gây ra cho người khác.

![THE COMMUNITY CAN OPEN ONE FOR YOU](../../Info%20Graphics/v5/v5-01b2-komunitni-did.webp)

Những gì tôi vừa phác họa vắn tắt là cách một mạng xã hội lấy cảm hứng từ Danh tính Phi tập trung (DID) có thể vận hành. Mục đích chính của các khái niệm DID là củng cố quyền riêng tư và tự do thông qua nguyên tắc đăng ký các quy tắc mà tôi sẽ tuân theo và sống theo — trao cho người dùng khả năng quyết định chia sẻ thông tin gì và với điều kiện nào.

Tôi đề xuất kết nối các DID hơn nữa thành một mạng lưới giao tiếp, nơi những người nắm giữ chúng trao đổi phản hồi ngay cả ngoài những tình huống mà điều gì đó đã xảy đến với ai đó và cộng đồng hoặc một cá nhân cần phản ứng. Sự so sánh mang tính phòng ngừa như vậy giữa các quy tắc mà chúng ta đã đăng ký — với tùy chọn tính toán hệ quả kinh tế và các hệ quả khác của những chênh lệch lẫn nhau trong kỳ vọng về cách bên kia lẽ ra phải vận hành — có thể được coi là một động cơ để tìm kiếm đồng thuận. Thay vì tự do, một hệ thống như vậy sẽ nhấn mạnh việc ra quyết định tự nguyện kết hợp với trách nhiệm cho hành vi ở thế giới thực.

Một cá nhân không thể tự mình phá vỡ hệ thống — một nhóm người có cơ hội lớn hơn, và một nhóm người có đồng thuận đã thương lượng cùng những động cơ để cùng nhau kéo về một hướng trên nhiều vấn đề thì có cơ hội chống lại những xu hướng độc tài còn lớn hơn nữa. Điều kiện tiên quyết về sự tổ chức ở chương đầu sẽ được thỏa mãn khi hai điều kiện được đáp ứng: mạng lưới danh tiếng DID phủ được các cộng đồng đủ mang tính đại diện đến mức việc sử dụng nó không còn là chuyện lạ lẫm nữa. Và đồng thời, phân khúc cộng đồng này trở thành một thiểu số có ý nghĩa kinh tế, có thể thương lượng một cách quyết đoán với phần còn lại của xã hội.

> [!note] Tự nguyện so với tự do
> Tự do — theo nghĩa tích cực — sẽ là một hiệu ứng thứ cấp của việc cân bằng hai yếu tố: tính tự nguyện và áp lực của môi trường xung quanh hướng tới trách nhiệm.

> [!note] Kỷ nguyên AI và giá trị của danh tiếng
> Trong kỷ nguyên trí tuệ nhân tạo, mọi thứ liên quan đến tư duy nhận thức đang được tự động hóa — và có thể còn đi xa hơn. Vậy điều gì còn lại trong hoạt động của con người như một lợi thế cạnh tranh? Câu trả lời không dễ, và chắc chắn sẽ tìm ra được điều gì đó, nhưng có một điều ta có thể nói chắc chắn: danh tiếng sẽ quyết định. Một lịch sử có thể kiểm chứng về hành vi của bạn, về những cam kết của bạn và việc bạn thực hiện chúng — đó là thứ mà AI sẽ không xây dựng thay cho bạn.

![AI CANNOT BUILD YOUR REPUTATION — ONLY YOU CAN](../../Info%20Graphics/v5/v5-02f-ai-era-reputace.webp)

![THE ECONOMICS OF TRUTH](../../Info%20Graphics/v5/v5-02c-ekonomika-pravdy.webp)
