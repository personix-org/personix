---
title: "Observer"
chapter: 3
part: "How Verification Works"
lang: en
version: v6
source: "merge of CZ 06-pozorovatel + the old standalone observer-trick"
---

# Người quan sát

Vai người quan sát loại bỏ động cơ bẻ cong quy tắc của người xác minh. Trong những tình huống mà người xác minh không ưa yêu cầu của bên phát hành hoặc của thẩm quyền, họ có thể đơn giản là im lặng — không phản hồi, và chặn chuỗi thuật toán. Người quan sát — hoặc một tập hợp những người quan sát — đặt cược danh tiếng của mình vào việc ghi lại tài liệu về cách người xác minh đã bị hỏi đến. Nếu người xác minh im lặng dù đã tuyên bố một chính sách nói ngược lại, họ có thể bị kết tội vi phạm giao thức.

![THE OBSERVER — KEEPS A RECORD OF THE VERIFIER](../../../Info%20Graphics/v5/v5-08g-role-observer.webp)

## Cơ chế: dấu thời gian và mã thách thức

Trước khi bạn gửi một tuyên bố tới người xác minh, bạn định tuyến nó qua những người quan sát — những người bạn tin, hoặc các nhà cung cấp dịch vụ quan sát chuyên biệt thu một khoản phí nhỏ. Mỗi người quan sát nhận phần gửi của bạn, đóng dấu thời gian lên nó, ký xác nhận rằng họ đã thấy nó đi ra, và tạo một mã thách thức — một hash mật mã của chữ ký họ. Các mã này được gắn thêm vào yêu cầu của bạn. Người xác minh nhìn thấy chúng nhưng không hề biết những người quan sát là ai, hay các mã đó có thật hay không. Do đó, những người quan sát đóng vai proxy giữa bên phát hành và người xác minh, giữ một bản ghi độc lập rằng tuyên bố đã được gửi và nó chứa những gì. Có thể có từ không đến N người trong số họ.

Khi người xác minh hành xử trung thực — chấp nhận hoặc từ chối đúng theo chính sách họ đã tuyên bố — các mã vẫn mờ đục. Không ai bị lộ.

Nhưng nếu người xác minh im lặng dù có một chính sách chiều theo, hoặc phản hồi theo cách mâu thuẫn với những gì họ đã công bố, thì bạn nắm giữ các chữ ký gốc của người quan sát. Bạn có thể công bố chúng như lời chứng gián tiếp rằng tuyên bố đã được gửi và người xác minh đã không tuân theo giao thức. Bất kỳ ai cũng có thể kiểm chứng rằng các chữ ký khớp với các mã thách thức.

## Điểm chốt: bạn không cần người quan sát thật

Và đây là phần thanh tao nhất: **bạn hoàn toàn không cần người quan sát thật.** Bạn có thể tạo ra những con số ngẫu nhiên trông y hệt các mã thách thức. Người xác minh không thể phân biệt được — họ buộc phải đổ xúc xắc xem có nên liều danh tiếng của mình hay không. Đằng sau mỗi yêu cầu họ nhận được có thể là một người quan sát được kính trọng đang dõi theo trong bóng tối — hoặc có thể chỉ là nhiễu thuần túy. Người xác minh không biết. Và chính sự bất định ấy là cơ chế.

Chi phí để duy trì áp lực trung thực: gần như bằng không (số ngẫu nhiên thì miễn phí). Chi phí tiềm tàng của sự bất lương đối với người xác minh: thảm khốc. Hành vi trung thực được khuyến khích ngay cả khi thực ra chẳng có ai đang theo dõi.

Hệ thống vận hành được vì ai cũng hơi hoang tưởng một chút. Sự bất định rẻ hơn sự giám sát.

![THE BLUFF THAT KEEPS THE VERIFIER HONEST](../../../Info%20Graphics/v5/v5-09-trik-s-pozorovateli.webp)

> [!note] Nhiều người xác minh trong một vòng lặp duy nhất
> Một quy tắc bổ trợ củng cố cho tính sẵn sàng của người xác minh có thể là một mở rộng thuật toán trả về, trong một vòng lặp duy nhất, một tập các ứng viên xác minh thay vì chỉ một.
