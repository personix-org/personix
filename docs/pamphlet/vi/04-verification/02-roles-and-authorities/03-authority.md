---
title: "Authority"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
---

# Thẩm quyền

Thẩm quyền đóng một vai trò kép: nó có thể là một **kiểm toán viên** (xác minh chất lượng bằng chứng trước khi một tuyên bố được công bố) hoặc một **người bảo lãnh** (đặt cược danh tiếng của mình vào tính chân thực của một tuyên bố). Trong cả hai trường hợp, nó làm mạnh thêm tuyên bố của bên phát hành. Hai dịch vụ này có thể tách rời — một thẩm quyền có thể chào dịch vụ này, dịch vụ kia, hoặc cả hai cùng lúc. Giả định làm việc là hầu hết các dịch vụ do các thẩm quyền cung cấp đều có thể được cung ứng trên cơ sở thị trường tự do. Điều đó đúng ngay cả trong những lĩnh vực khó hình dung là có thể tư nhân hóa, chẳng hạn tư pháp, nơi các dịch vụ chuyên biệt — điều tra, đánh giá bằng chứng, cho đến cả những dịch vụ mà ngày nay do quân đội tập trung cung cấp (hoạch định chiến lược, huấn luyện chuẩn hóa, mua sắm và quản lý kho dự trữ, v.v.) — đều có thể được các tác nhân thị trường cung ứng một cách hiệu quả. Hầu như chẳng có gì mà sau khi tái cấu trúc lại không thể được làm cho hiệu quả hơn nhờ các động cơ của thị trường tự do.

> [!warning] Thẩm quyền, bên phát hành và người quan sát không bao giờ được là người xác minh cho chính vụ việc của mình.
> Việc chọn người xác minh theo thuật toán bảo đảm tính độc lập. Không ai có thể xác minh tuyên bố của chính mình, hay một tuyên bố mà mình có lợi ích trực tiếp trong đó. Đây là một trong những quy tắc cơ bản mà cả cộng đồng DID đều có lợi ích trong việc gìn giữ.

Các hình ảnh sau đây cho thấy những góc nhìn bổ sung cho nhau về bề rộng hoạt động mà các thẩm quyền bao trùm (thuật ngữ "thẩm quyền" có thể được đọc thay thế cho "nhà cung cấp dịch vụ").

![THE AUTHORITY — WHO STAKES THEIR NAME](../../../Info%20Graphics/v5/v5-08d-role-authority.webp)

![TWO FACES OF AUTHORITY](../../../Info%20Graphics/v5/v5-08a-autorita-auditor-garant.webp)

> [!note] Thẩm quyền với vai người quan sát ẩn danh
> Một thẩm quyền có danh tiếng — hãy nghĩ đến một công chứng viên mà công việc làm ăn hoàn toàn phụ thuộc vào hồ sơ thành tích của mình — có thể, bên cạnh các chức năng chính (kiểm toán viên / người bảo lãnh), chào thêm một chức năng thứ ba: vai người quan sát ẩn danh trong quá trình xác minh. Họ lưu một bản ghi có đóng dấu thời gian về tuyên bố đã gửi để người xác minh không thể lặng lẽ vứt bỏ nó. Cơ chế của vai người quan sát được mô tả kỹ hơn trong phần về vai trò Người quan sát.
