---
title: "Roles Overview"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Tổng quan các vai trò

Chúng ta đã chạm sơ qua một số vai trò này trong chương về mạng lưới và các thuộc tính cơ bản của nó. Giờ là lúc nhìn lại chúng chi tiết hơn và bổ sung những vai trò khác cần thiết để làm cho mạng lưới vững chắc hơn. Mỗi giao dịch xác minh liên quan đến vài vai trò — hãy xem chúng hành xử thế nào.

> [!note] Các vai trò trong một giao dịch xác minh
> Mỗi lần xác minh liên quan đến tối đa sáu vai trò riêng biệt, được tóm tắt trong bảng dưới đây. Tất cả đều có thể có DID riêng của mình trong mạng lưới danh tiếng phi tập trung.

| Vai trò | Mô tả |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Issuer** (bên phát hành) | Người công bố thông tin lên mạng lưới — tuyên bố rằng điều gì đó đã xảy ra (một DID được tạo, chỉnh sửa hay giải thể, một tuyên bố, chính sách của một DID nhất định, v.v.) |
| **Subject** (chủ thể) | Người mà thông tin nói về — người nhận của tuyên bố |
| **Authority** (thẩm quyền) | Một thực thể đáng tin đặt cược danh dự của mình vào chất lượng của tuyên bố bằng cách điều tra nó và hoặc xem xét bằng chứng được trình ra hoặc chủ động thu thập nó |
| **Observer** (người quan sát) | Một bên thứ ba độc lập lưu lại bản ghi về cách người xác minh xử lý tuyên bố — bảo đảm rằng người xác minh không im lặng cũng không lệch khỏi chính sách họ đã tuyên bố |
| **Verifier** (người xác minh) | Một người tham gia được chọn theo thuật toán để xử lý giao dịch |
| **Delegate** (người được ủy quyền) | Một người hành động thay mặt cho một người tham gia khác |
