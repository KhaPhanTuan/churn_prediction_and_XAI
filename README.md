📌 Tổng quan dự án:

Dự án tập trung vào việc xây dựng mô hình học máy (Machine Learning) để phát hiện sớm những khách hàng có nguy cơ rời bỏ dịch vụ tài chính (Customer Churn). Điểm nổi bật của dự án là việc tích hợp các phương pháp Explainable AI (XAI) như SHAP và LIME, giúp doanh nghiệp không chỉ biết ai sẽ rời đi mà còn hiểu rõ tại sao họ đưa ra quyết định đó.

🛠 Công nghệ sử dụng
- Ngôn ngữ: Python.
- Thư viện ML: Pandas, NumPy, Scikit-learn, XGBoost.
- Web Framework: Django.
- Cơ sở dữ liệu: MySQL.
- Giải thích mô hình (XAI): SHAP, LIME.
- Giao diện: HTML, CSS, Javascript (AJAX).

Huấn luyện mô hình và so sánh 3 thuật toán:
- Logistic Regression.
- Random Forest.
- Gradient Boosting (Best Model) với F1-score đạt 0.6193 và Recall đạt 0.7807.

Giải thích: Sử dụng SHAP để phân tích mức độ ảnh hưởng toàn cục và LIME để giải thích từng trường hợp dự đoán cụ thể.

💻 Tính năng chính trên Website local:
- Dự đoán trực tuyến (Machine Learning): Nhập thông tin khách hàng và nhận kết quả dự đoán cùng xác suất rời bỏ theo thời gian thực.
- Giải thích chi tiết (Explanation): Trực quan hóa lý do dự đoán bằng biểu đồ LIME cho từng khách hàng và biểu đồ SHAP cho toàn bộ mô hình.
- Khám phá dữ liệu (Statistics): Xem trực tiếp cấu trúc và hồ sơ dữ liệu từ database thông qua giao diện bảng trực quan.
- Huấn luyện lại (Retrain Model): Cho phép người dùng tải lên file .csv mới để cập nhật mô hình trực tiếp từ giao diện web.

📊 Kết quả: Thông qua mô hình SHAP, dự án đã tìm ra các yếu tố hàng đầu dẫn đến rủi ro rời bỏ:
- Loại hợp đồng: Hợp đồng theo tháng (Month-to-month) có nguy cơ rời bỏ cao nhất.
- Thời gian gắn bó (Tenure): Khách hàng mới có tỉ lệ rời đi cao hơn người gắn bó lâu dài.
- Chi phí hàng tháng: Mức phí cao thường đẩy khách hàng rời bỏ dịch vụ.

📂 Cấu trúc thư mục
- /core: Chứa logic nghiệp vụ và routing của Django.
- /templates: Giao diện HTML của hệ thống.
- /static: Các file CSS, Javascript và hình ảnh.
- /model: Lưu trữ các mô hình đã huấn luyện và script ML pipeline.
Dự án được thực hiện bởi nhóm sinh viên trường Đại học Kinh tế - Luật (UEL) dưới sự hướng dẫn của TS. Trần Duy Thanh.