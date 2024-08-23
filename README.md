# DA2_learning_and_testing_analysis

## I. CHALLENGES

Đánh giá là một mảng rất quan trọng trong các hoạt động giáo dục. Hoạt động đánh giá thường thấy nhất chính là các bài kiểm tra trong trường học, nhưng nghĩ rộng ra, mọi hoạt động giáo dục như các khoá học, bồi dưỡng cho người đi làm cũng rất cần đến hoạt động kiểm tra đánh giá. Nhưng vấn đề là hình như, chỉ những kỳ thi tuyển chọn và cấp bằng thì chất lượng câu hỏi mới thực sự được quan tâm. Điều này có thể thấy rõ ràng là trong các kì thi, việc biên soạn câu hỏi chặt chẽ và nghiêm ngặt hơn, các kết quả phân tích cũng được tiến hành rất chi tiết, dựa trên nhiều mô hình đánh giá lâu đời và đáng tin cậy (hai phương pháp tôi hay dùng nhất là Classical Test Theory và Item Response Theory - IRT). Như ở Việt Nam hiện nay thì thay vì chỉ dùng điểm thô như trước, các kì thi đánh giá năng lực đã ứng dụng thêm IRT để tính điểm năng lực của thí sinh, ví dụ như Đại Học Quốc Gia TP HCM ([link](https://vnuhcm.edu.vn/tin-tuc_32343364/cau-truc-bai-thi-danh-gia-nang-luc-dhqg-hcm/313832393364.html)). Chính vì vậy mà từ kết quả các bài thi, năng lực của thí sinh hay chất lượng đề thi được mô tả khá rõ ràng. Tôi tự hỏi, nếu trong suốt quá trình luyện tập, người học nhận được những đánh giá hữu ích, người dạy được phản hồi về chất lượng công cụ đánh giá qua những con số thì tốt biết bao. Mà tại sao không nhỉ? Công cụ sẵn đó, có dữ liệu là có kết quả, nhưng rào cản vẫn còn quá lớn.

-   **Rào cản #1:** Vì việc thu thập điểm số của người học trong suốt quá trình luyện tập, xong tiến hành phân tích kết quả (thủ công) là một sự quá tải với người dạy. Vì khi dạy học, người dạy thường có rất nhiều thứ cần chuẩn bị như soạn kế hoạch bài dạy và cũng dạy rất nhiều người học. Dẫn đến việc theo dõi từng người học là việc bất khả thi nếu không sử dụng các nền tảng học trực tuyến.

-   **Rào cản #2**: Mặc dù các nền tảng học trực tuyến đã sẵn sàng nhưng tính đáp ứng chưa cao, nền tảng cung cấp tài liệu thì bài tập tràn lan, không có thống kê sử dụng, hay những nền tảng là môi trường dạy - học thì lại không có ngữ liệu mà người dạy cần, muốn dùng được thì họ phải mất công số hoá tài liệu của mình. Đây trở thành một rào cản lớn khi người dạy đã có tuổi và không thông thạo công nghệ. Nhưng về cơ bản, giữa lựa chọn lưu trữ dạng text trong máy tính, có thể in ra bất cứ lúc nào, với việc mất công số hoá lên một nền tảng trực tuyến, xong còn phải trả phí và lo sợ một ngày nào đó nền tảng không còn, tài liệu cũng mất, thì càng khó để thuyết phục người dạy ứng dụng một nền tảng số để lưu trữ và sử dụng tài liệu. Câu hỏi lớn cho các nền tảng quản lí học liệu là làm thế nào để người dạy có thể số hoá học liệu một cách dễ dàng, ít tốn công mà vẫn chính xác?

Chính vì vậy, tôi nghĩ đến một giải pháp đánh giá cần ứng dụng được các công nghệ, phương pháp hiện đại như khoa học dữ liệu, các mô hình thống kê trong giáo dục, nhưng lại cần đảm bảo dễ hiểu (theo nhu cầu), ít thao tác và cần ít thiết bị.

## II. SOLUTION

Phần mềm T&A chính là giải pháp cho nhu cầu đánh giá công cụ và đối tượng thông qua phân tích thông tin một cách toàn diện.

### Selling points

1.  **Đối tượng sử dụng rộng:** vì không phụ thuộc vào một nền tảng học tập hay lưu trữ tài liệu nào, nên mọi người dùng có nhu cầu phân tích trong kiểm tra đánh giá thì đều có thể sử dụng được.

2.  **Yêu cầu thiết bị ở mức tối thiểu:** một chiếc smart phone có lẽ là đủ, nhưng khuyến nghị nên sử dụng laptop để quan sát biểu đồ dễ dàng hơn. Giảm mức phụ thuộc vào thiết bị sẽ hữu ích với học sinh (HS) tại các trường công lập hoặc vùng sâu vùng xa, HS nhỏ tuổi.

3.  **Phân tích toàn diện:** Với các mô hình thống kê có sẵn trong giáo dục, việc tự động hoá phân tích là hoàn toàn khả thi. Chỉ cần có những chỉ dẫn, giải thích chi tiết cho từng trường hợp, người dạy có thể dễ dàng hiểu được ý nghĩa của các chỉ số thống kê.

### Cách sử dụng

![](https://media.licdn.com/dms/image/v2/D5612AQHgQ-uLEpLN7Q/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1722266900802?e=1729728000&v=beta&t=xL-xU9V368o96Y9ZHVHkQYN35WHYdht5D9RY8eArXHA)

Người dùng sẽ chỉ cần thao tác một vài thao tác đơn giản là có thể phân tích kết quả. Đầu tiên người dùng đăng nhập vào app. Sau đó, người dùng cần nhập 2 bảng thông tin, bảng ma trận câu hỏi và đáp án lựa chọn của người học. Đây là toàn bộ thao tác của người dùng cần thực hiện.

-   **Nhập ma trận đặc tính của câu hỏi:** Về mặt lí thuyết, để thiết kế một đề kiểm tra thì luôn cần xây dựng ma trận câu hỏi trước, sau đó thiết kế câu hỏi từ ma trận. Nhưng trong thực tế, thường các bài kiểm tra quan trọng như giữa kì, cuối kì, thi chuyển cấp mới có ma trận chi tiết. Tuy nhiên, đây cũng không phải vấn đề lớn, phần mềm sẽ cung cấp phân tích theo lượng thông tin mà người dùng cung cấp, đề đơn giản, ít thông tin về câu hỏi thì sẽ phân tích ít hơn, và ngược lại. Người dùng sẽ cần nhập đặc tính của từng các câu hỏi và đáp án. Nhiệm vụ này khá đơn giản, số lượng câu hỏi thường dao động trong khoảng 20 đến 50 câu. Với những kì thi lớn, số lượng câu hỏi nhiều, thì việc nhập đặc tính của nhiều câu hỏi cũng không chiếm nhiều thời gian trong khâu chuẩn bị.

-   **Nhập kết quả bài làm của người học:** nhiệm vụ này khó khăn hơn vì số lượng người học có thể sẽ lớn. Nếu thí sinh dự thi làm bài qua các nền tảng trực tuyến (như google form hay microsoft form) thì việc ghi nhận dữ liệu số khá đơn giản. Nhưng hình thức này lại chỉ phù hợp với khi có thể cung cấp mỗi thí sinh một thiết bị, việc này thường bất khả thi ở phần lớn trường học. Còn nếu thí sinh làm bài trên giấy, app sẽ cần phải chuyển dạng được từ hình ảnh bài làm thành dữ liệu số dạng bảng. Vì đã nhập đáp án câu hỏi từ bước trước, app có thể chấm bài tự động. Thay vì phải chấm bài thủ công, việc chụp ảnh từng bài của thí sinh vẫn tiết kiệm thời gian hơn, quan trọng là thí sinh phải làm bài đúng quy cách để phần mềm nhận diện đủ và đúng bài làm.

Việc nhập điểm người học với các bài kiểm tra trắc nghiệm từ bài làm trên giấy lên phần mềm thì tôi thấy cũng có khá nhiều phần mềm có thể làm được, thí sinh làm bài trong answer sheet mẫu là được. Không rõ kĩ thuật sâu xa bên trong những phần mềm là gì nhưng mọi thứ có thể khá đơn giản nếu ứng dụng AI. Chưa kể nếu dùng AI, data có được sẽ được tải về và lưu trữ khá dễ dàng, giúp việc lưu trữ tiết kiệm và an toàn hơn. Giả sử tôi có bài làm mẫu như bên dưới, đây là kiểu làm mà các phần mềm khó nhận diện nhất, nếu làm đúng theo format như các phiếu trắc nghiệm, việc nhận diện sẽ dễ hơn nhiều. Nhưng kể cả với kiểu bài làm như thế này, vấn đề kĩ thuật cũng chẳng mấy phức tạp với các công cụ AI hiện tại.

![](https://media.licdn.com/dms/image/v2/D5612AQFO971m7YbEqg/article-inline_image-shrink_1000_1488/article-inline_image-shrink_1000_1488/0/1722298641580?e=1729728000&v=beta&t=AEgI4BlvamQj9YABCmTHA9fCA-Ve06y54vV0C_tRDgA)

Tôi có thể sử dụng ChatGPT để nhận diện toàn bộ câu trả lời của học sinh, chuyển dữ liệu về dạng .csv, và download về.

![](https://media.licdn.com/dms/image/v2/D5612AQEKizeirbobHA/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1722525853520?e=1729728000&v=beta&t=zaw6hGO-atagjHTD2_VewmhiKXtjSiW0rxU8aNd11HY)

## III. METHODOLOGY FOR DATA ANALYSIS

**Đặc tính của Dataset:**

Thực ra data để có thể hiện thực hoá ý tưởng phân tích khá đơn giản, nhìn chung chỉ có 2 loại chính, đó là data tương tác của thí sinh với từng câu hỏi và data thông tin của từng câu hỏi.

![](https://media.licdn.com/dms/image/v2/D5612AQGPZ3fJxy8lQw/article-inline_image-shrink_1500_2232/article-inline_image-shrink_1500_2232/0/1722531616285?e=1729728000&v=beta&t=9nIONs9YWjEvhTTy454mVP5sI_riabZL3fjXM4Y-GKQ)

Tuy nhiên, đây là data khi đã được tổng hợp cho đúng mục đích phân tích của ứng dụng (tức là được thiết kế chuẩn xác với những đánh giá mà tôi tiến hành). Tôi muốn tìm một bộ data thực với dữ liệu tương tác thực, nên việc xử lí sẽ phức tạp hơn. Sau các bước xử lí dữ liệu, tôi mới có được thông tin ở dạng mong muốn để mô tả cho phần mềm. Nếu data từ đầu được thiết kế đúng format thì việc phân tích sẽ dễ dàng hơn nhiều.

Data sử dụng trong bài này được lấy từ một nền tảng học tập trực tuyến tên là [Eedi](https://eedi.com/us), nền tảng này khá thú vị, họ publish một phần data tương tác thực của học sinh cho một cuộc thi phân tích data trong giáo dục, việc này giúp họ thu thập được những nghiên cứu quý giá cho ứng dụng của mình. Data sử dụng trong phân tích của tôi được lấy từ public data của Eedi, tuy nhiên, tôi chỉ sử dụng một phần. Do phân tich với một vài mô hình khảo thí, nên tôi trích xuất dữ liệu sao để đảm bảo tất cả học sinh tương tác với tất cả câu hỏi trong bộ data của mình.

1.  **"question_metadata.csv":** Tên chủ đề của câu hỏi qua 3 cấp độ, được mã hoá

2.  **"subject_metadata.csv":** Chính là phần giải thích tên của các chủ đề với mọi cấp độ, giống như phần giúp giải mã chủ đề được mã hoá ở data trên.

3.  **"my_sample_data.csv":** là data tôi trích xuất cho minh hoạ của mình. Dù có thể làm cho kết quả trở nên bias, nhưng phần phân tích không phải hướng đến đánh giá khắt khe các đối tượng (học sinh và câu hỏi) trong thực tế, mà chỉ mang tính chất minh hoạ cho phân tích dữ liệu (việc phân tích đảm bảo chính xác).

4.  **"item_IRT_2P.csv"**: là data kết quả của phân tích IRT 2 tham số. Phần này đúng ra có thể làm bằng python và không cần xuất ra file sẵn, nhưng tôi thấy R vẫn cho kết quả ước lượng IRT hợp lí hơn (các thư viện IRT của python có vẻ không ổn lắm). Nên đành dùng R để xuất dữ liệu IRT cho mô phỏng này.

Sơ lược nhanh về phần mềm sẽ được giới thiệu qua video bên dưới.

<https://youtu.be/r1ce-HAayxA>
