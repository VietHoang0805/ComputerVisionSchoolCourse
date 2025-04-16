# 🧠 Transfer Learning & Pretrained Model - Image Classification

📁 Đây là bài tập trong khóa học **Computer Vision**, tập trung vào việc xây dựng mô hình phân loại ảnh bằng hai phương pháp:

1. **Pretrained Model** (sử dụng trực tiếp mô hình huấn luyện sẵn)
2. **Transfer Learning** (tùy biến lại mô hình pretrained theo bài toán mới)

---

## 📂 Cấu trúc thư mục
``` bash
TransferLearning/ 
├── PretrainedModelImageClassification/📘 Sử dụng mô hình VGG16,Mobilenet,Inception,Resnet50 đã huấn luyện sẵn để phân loại ảnh trực tiếp │ 
├── TransferLearningImageClassification/ 📗 Tinh chỉnh mô hình ResNet bằng dữ liệu mới (20 lớp từ CIFAR-100)
```

## 1️⃣ PretrainedModelImageClassification

- Sử dụng mô hình VGG16,Mobilenet,Inception,Resnet50 đã được huấn luyện trên **ImageNet** để phân loại ảnh mà **không thực hiện huấn luyện lại**.
- Mục tiêu:
  - Hiểu cách sử dụng các mô hình pretrained như một extractor đặc trưng (feature extractor).
- Các bước chính:
  - Nạp ảnh đầu vào
  - Dùng VGG16,Mobilenet,Inception,Resnet50 để dự đoán trực tiếp
- Phù hợp cho các ứng dụng cần inference nhanh mà không có đủ dữ liệu để huấn luyện.

---

## 2️⃣ TransferLearningImageClassification

- Dùng **Transfer Learning** để huấn luyện mô hình ResNet dựa trên **tập con CIFAR-100 (20 lớp)**.
- Quy trình:
  - Chia tập dữ liệu thành `train/` và `test/`
  - Tăng cường dữ liệu (Image Augmentation)
  - Tải mô hình ResNet pretrained và **đóng băng các tầng đầu**
  - Tùy biến các tầng cuối cho bài toán phân loại ảnh 20 lớp
  - Sử dụng:
    - `Categorical Crossentropy`
    - `Adam` optimizer
    - `ReduceLROnPlateau`
  - Trực quan hóa quá trình huấn luyện (biểu đồ Accuracy & Loss)
- **Kết quả đạt được:**
  - Accuracy train: 97.51%
  - Accuracy Validation: 86.98%