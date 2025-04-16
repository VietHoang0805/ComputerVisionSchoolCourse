# 🖼️ Image-Classification-using-Transfer-learning
Phân loại hình ảnh trên một tập dữ liệu nhỏ với độ chính xác cao (>80%) bằng cách sử dụng **Transfer Learning** với mô hình **ResNet**.

## 📌 Mục tiêu
Xây dựng mô hình học sâu có khả năng phân loại ảnh chính xác dù tập dữ liệu huấn luyện nhỏ, bằng cách tận dụng sức mạnh của mô hình học sẵn (pretrained) **ResNet**.

---

## 🧠 Kiến thức áp dụng

- Transfer Learning
- Image Augmentation
- ResNet (pretrained on ImageNet)
- Categorical Crossentropy
- Optimizer: Adam
- Learning Rate Scheduling (ReduceLROnPlateau)

---

## 📁 Dataset

- **Nguồn:** CIFAR-100
- **Đặc điểm:**
  - Gốc có 100 lớp
  - Sử dụng **20 lớp** được chọn lọc để huấn luyện
- **Kích thước ảnh:** 256x256 (resized)

---

## 🧪 Chuẩn bị dữ liệu

- Dữ liệu ban đầu được chia thành `train` và `test` sử dụng notebook [`Split-Folder.ipynb`](<Split folders.ipynb>)
- Thư viện `os` được dùng để duyệt toàn bộ hình ảnh và chia chúng vào 2 thư mục:
  - `train/`
  - `test/`

---

## 🔄 Augmentation

- Vì dữ liệu ban đầu rất nhỏ, sử dụng `ImageDataGenerator` để thực hiện augmentation:
  - Xoay ảnh
  - Dịch trái/phải, trên/dưới
  - Zoom
  - Lật ngang/dọc
- Augmentation giúp tăng kích thước và tính đa dạng của tập dữ liệu.

---

## ⚙️ Mô hình

- Sử dụng mô hình **ResNet pretrained** (huấn luyện trước trên ImageNet)
- Các lớp đầu của ResNet được giữ lại, phần đuôi được tùy biến để phân loại 20 lớp của CIFAR-100 (subset)
- Hàm loss: `CategoricalCrossentropy`
- Optimizer: `Adam`
- Sử dụng `ReduceLROnPlateau` để giảm tốc độ học khi model không còn cải thiện.

---

## 🏋️ Huấn luyện

- Huấn luyện mô hình trên tập `train` và đánh giá trên tập `validation`
- Trực quan hóa quá trình huấn luyện qua:
  - Biểu đồ Accuracy (Train vs Validation)
  - Biểu đồ Loss (Train vs Validation)

---

## 📈 Kết quả

| Loại | Giá trị |
|------|---------|
| Accuracy (Train) | **97.51%** |
| Accuracy (Validation) | **86.98%** |

---
