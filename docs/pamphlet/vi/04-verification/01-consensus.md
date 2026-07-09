---
title: "Consensus and the Verification Process"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: v1
---

# Đồng thuận và quy trình xác minh

Để xây dựng đồng thuận về những quy tắc mà một xã hội, trung bình, nên gìn giữ và thực thi, cơ chế sau đây có thể giúp ích. Với tư cách một người tham gia DID, tôi tuyên bố những quy tắc mà tôi đăng ký và sẽ sống theo, và tôi công bố chúng. (Hãy hình dung đó như điều lệ và quy chế mà theo tôi làm nên thế giới lý tưởng của mình — một thế giới nơi tôi không cảm thấy bị bó buộc, mà an toàn.)

Tôi có thể ước lượng trước xem các mối liên hệ DID của mình sẽ phản ứng thế nào — và đánh giá tôi sẽ bị chế tài mạnh đến đâu, và bởi ai, trong các tương tác xã hội hoặc kinh doanh thông thường, nếu chúng giả định có xảy ra.

Việc đánh giá dứt khoát diễn ra khi bạn yêu cầu thông tin từ một DID khác, hoặc yêu cầu họ xác minh một tuyên bố (hoặc yêu cầu một thẩm quyền cung cấp dịch vụ, v.v.) mà bạn muốn công bố lên mạng lưới danh tiếng. Kết quả lẽ ra phải giống hệt như khi bạn tự chạy đánh giá, chạy thử, đối chiếu với chính sách mà đối tác đã tuyên bố — và nếu không giống, thì có gì đó không ổn ở phía đối tác: họ đang cố chơi một ván không trung thực.

Kết cục hoặc là chấp nhận, kèm theo một mức giá được báo cho việc xác minh (trong trường hợp dịch vụ của người xác minh hoặc thẩm quyền), hoặc là từ chối. Cả các chế tài lẫn các phần thưởng cho việc lệch khỏi chính sách của người đánh giá đều được gộp vào mức giá báo. Người yêu cầu khi đó quyết định có chấp nhận điều khoản hay không, hoặc chuyển sang vòng xác minh tiếp theo trong thuật toán phân bổ — lặp lại quy trình cho đến khi hài lòng, hoặc cho đến khi bài toán kinh tế khiến việc tiếp tục trở nên vô nghĩa.

> [!note] Đồ thị xã hội
> Mạng lưới danh tiếng, trước hết và trên hết, là một mạng xã hội. Bạn thêm các liên hệ — những người đồng ý kết nối. Họ có các liên hệ, và các liên hệ đó lại có các liên hệ. Thuật toán tìm kiếm những người xác minh trong một độ sâu có thể cấu hình (ví dụ, ba tầng: các liên hệ trực tiếp của bạn, các liên hệ của họ, và một tầng xa hơn nữa). Không cần một blockchain toàn cầu — mạng lưới tự nhiên hình thành các cộng đồng có phần chồng lấn sang các cộng đồng khác.
>
> Thuật toán là phi tất định: nó băm tài liệu tuyên bố của bạn, ánh xạ hash tới một vị trí trên một vòng các danh tính đã biết trong vòng tròn này, và chọn danh tính gần nhất làm ứng viên xác minh. Bạn không thể dự đoán hay tác động đến việc ai sẽ xác minh tuyên bố của mình.

Mỗi lần từ chối của một người xác minh làm tài liệu của bạn phình to ra và tăng chi phí xử lý nó — đó là kênh chi phí thứ nhất (sự lớn lên của tài liệu). Mỗi người xác minh mới tính phí dựa trên khối lượng dữ liệu, danh tiếng của bạn, và mức độ nội dung tuyên bố của bạn lệch khỏi chính sách xác minh mà họ đã tuyên bố — đó là kênh chi phí thứ hai (khoản phụ phí rủi ro). Và mỗi vòng lặp tốn thời gian và năng lượng — kênh chi phí thứ ba.

> [!note] Người xác minh kiểm tra những gì, theo thứ tự nào
> Một khi được chọn, người xác minh đánh giá một tuyên bố theo khoảng bốn bước có thứ tự — các bộ lọc rẻ nhất trước, các kiểm tra nội dung tốn kém sau cùng:
>
> 1. **Kiểm soát chính sách.** Loại tuyên bố này có nằm trong phạm vi những gì người xác minh công khai xác minh hay không? Nếu không, yêu cầu bị từ chối thẳng.
> 2. **Lòng tin vào thẩm quyền.** Thẩm quyền đã bảo chứng cho tuyên bố có đủ đáng tin theo chính sách mà người xác minh tự tuyên bố hay không? Một thẩm quyền dưới ngưỡng tin cậy của người xác minh là căn cứ để từ chối bất kể nội dung của tuyên bố.
> 3. **Danh tiếng của bên phát hành.** Bên phát hành có đạt các ngưỡng danh tiếng mà người xác minh đã tuyên bố cho loại tuyên bố này hay không? Danh tiếng thấp có thể hoặc làm tăng phí hoặc kích hoạt việc từ chối.
> 4. **Kiểm tra nội dung.** Chỉ khi ba cổng đầu đã qua thì người xác minh mới đánh giá bản thân tuyên bố — chữ ký, tính nhất quán nội tại, tính đúng đắn về hình thức, và mức độ nó lệch khỏi chính sách của người xác minh. Phí tính cho bước cuối này phản ánh rủi ro thực sự phải gánh.
>
> Người xác minh công bố chính sách chi phối từng cổng này, nên các bước không nằm ở sự tùy tiện của họ — họ bị ràng buộc bởi những gì họ đã tuyên bố. Việc lệch khỏi chính sách đã công bố tự nó là một tuyên bố có thể công bố chống lại họ, và họ trả cho nó bằng danh tiếng của mình.

Kết quả: công bố một tuyên bố đáng tin và hữu ích thì gần như chẳng tốn gì. Công bố một tuyên bố cực đoan thì tốn hơn. Công bố một lời dối trá thì trở nên đắt đến mức cấm cản — bạn phải lặp qua hết người xác minh này đến người xác minh khác, và ai từ chối bạn cũng đều làm tăng chi phí. Thị trường định giá tuyên bố của bạn, và cái giá cho bạn biết bạn đang đứng ở đâu trong tương quan với những cộng đồng mà bạn qua lại.

Tuyên bố rằng mình tuân thủ một quy tắc trong khi thực tế thì không, là chưa đủ. Trong trường hợp đó, DID của bạn có nguy cơ bị công bố một bản ghi tiêu cực phơi bày thói đạo đức giả — điều biến bạn thành một rủi ro cho mọi người khác. Kết cục lẽ ra phải là ít quy tắc hơn nhưng được tuân theo nhất quán hơn, và việc dọn sạch khu rừng luật lệ và quy định mà đến cả giới luật gia chuyên nghiệp cũng khó lòng lần được đường.

![HYPOCRISY IS THE MOST EXPENSIVE BEHAVIOR](../../Info%20Graphics/v5/v5-07c-pokrytectvi.webp)

> [!note] Đồng thuận so với trách nhiệm giải trình
> Để mạng lưới phục vụ như một nguồn thông tin có giá trị, một DID không nên quá cực đoan — nếu không những người khác sẽ từ chối nó. Áp lực xã hội sẽ tìm kiếm điểm cân bằng, và những nỗ lực gây bất ổn nó nhiều khả năng sẽ bị trừng phạt.

![DECLARE YOUR RULES, PAY THE PRICE](../../Info%20Graphics/v5/v5-07-deklarace-a-cena.webp)

> [!warning] Số phiếu bầu không đồng nghĩa với sức nặng của tiếng nói
> Juraj Karpiš nói rằng "tiền là ký ức về những việc tốt." Tôi xin thêm rằng danh tiếng là ký ức về những việc xấu.
>
> Từ đó suy ra, theo lối trọng dụng nhân tài, ai đóng góp nhiều hơn mà không có danh tiếng xấu thì xứng đáng có sức nặng tiếng nói lớn hơn trong cộng đồng. Nhìn qua lăng kính các quan hệ song phương: khi tôi cân nhắc phải chiều theo những áp lực đồng thuận nào, sức nặng lớn nhất thuộc về những quan hệ mà từ đó tôi thu được lợi ích kinh tế lớn nhất. Mười người mà tôi không có giao thương gì sẽ ảnh hưởng đến tôi ít hơn nhiều so với một đối tác kinh doanh thường xuyên. Mô thức này không giới hạn ở thương mại — nó mở rộng sang các quan hệ xã hội, chính trị và các quan hệ khác.
