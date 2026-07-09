---
title: "Verifier"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Người xác minh

Bất kỳ DID nào cũng có thể đóng vai người xác minh, hoặc trực tiếp hoặc thông qua quyền xác minh được ủy cho một DID thứ ba. Để tôi — hoặc người được tôi ủy quyền — có thể xác minh, tôi cần có mặt trên mạng lưới (trực tuyến). Không phải ai cũng muốn cam kết điều đó, và vì thế một bản ghi DID có thể liệt kê, theo thứ tự ưu tiên, những người thay thế sẽ thực hiện chức năng này thay cho nó khi nó ngoại tuyến.

Mỗi DID đang hoạt động trong mạng lưới đều công khai tuyên bố chính sách của riêng mình. Thông qua các quy tắc được định nghĩa trong chính sách đó, trong quá trình xác minh nó đánh giá danh tiếng của đối tác cùng nội dung và hình thức của tuyên bố mà bên phát hành đã đánh dấu để công bố lên mạng lưới danh tiếng. Một phần của chính sách là công thức tính dùng để tính phí cho dịch vụ xác minh. Một khi điều đó đã sẵn sàng, thì trên một số lượng lớn về mặt thống kê các tuyên bố chảy qua mạng lưới, tôi chờ thuật toán của mạng lưới rút tôi ra ở phía bên phát hành và giao cho tôi, trong một vòng lặp nhất định, việc xác minh thông tin đang được phát hành. Bên phát hành có thể tính trước xem một người xác minh hành xử đúng đắn sẽ phản ứng thế nào, nhưng không thể tránh việc thực sự liên hệ với họ (hoặc những người thay thế của họ); vòng lặp với người xác minh được chọn phải được bên phát hành thực hiện ngay cả khi họ biết trước là sẽ không qua.

Làm sao chúng ta biết bên phát hành chạy thuật toán chọn người xác minh trên đúng tập các DID ứng viên xác minh? Cùng với chính sách được công khai tuyên bố của mình, mỗi DID cũng công bố danh sách hiện thời các định danh của mạng xã hội của nó bên trong mạng lưới danh tiếng. Nếu một bên phát hành định nghĩa mạng xã hội của mình như một bong bóng xã hội chỉ vọng lại và củng cố quan điểm của chính nó, thì thông tin được công bố qua nó sẽ khó lòng được các cộng đồng khác đón nhận rộng rãi hơn. Việc tôi xoay xở đẩy được, với chi phí cao, một tuyên bố cực đoan vào mạng lưới không hàm nghĩa rằng, khi đánh giá danh tiếng của đối tác, tôi sẽ dành cho nó bất kỳ sức nặng nào. Một số tuyên bố tôi bị cộng đồng ép phải tính đến (các bản án và hạn chế áp lên kẻ vi phạm); những tuyên bố khác thì hoàn toàn tùy ở tôi — tôi tự quyết định giá trị kinh tế của việc đưa vào hay loại ra một mẩu thông tin nhất định.

![THE VERIFIER — CHOSEN BY THE ALGORITHM](../../../Info%20Graphics/v5/v5-08e-role-verifier.webp)
