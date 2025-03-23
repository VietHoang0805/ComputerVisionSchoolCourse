# KNN Visualization

Đây là dự án minh họa thuật toán K-Nearest Neighbors (KNN) thông qua các tệp mã nguồn, dữ liệu và video trực quan.

## 📁 Cấu trúc thư mục
```
KNN/
│── KNNOfficial/              # Thư mục chứa minh họa về KNN Image classification
|   |- datasets               # Thư mục chứa dataset   
|   |- images                 # Thư mục chứa ảnh để test
|   |- KNN.ipynb              # Notebook để thực thi code
|   |- knnpickle_file.pkl     # File chứa mô hình
│── KNNVisualize/             # Thư mục chứa mã nguồn trực quan hóa KNN
│   │── NotebookInteractive/  # Chứa các notebook tương tác
│   │   ├── KNN.ipynb         # Notebook minh họa KNN
│   │── Video/                # Chứa các video minh họa
│   │   ├── KNNVisualization.mp4  # Video trực quan KNN
│   │   ├── myvideo.mp4           # Video từ KNNGdal.py
│   │── dataframe/            # Chứa hình ảnh cắt ra từ myvideo.mp4
│   │── KNN.py                # Code sử dụng manim
│   │── KNNGdal.py            # Code sử GDAL
│   │── main.py               
```
🚀 Hướng dẫn sử dụng

1. Cài đặt thư viện cần thiết

Trước khi chạy mã, hãy cài đặt các thư viện cần thiết bằng lệnh:
```
pip install -r requirements.txt 
```

2. Chạy minh họa KNN

Chạy minh họa KNN sử dụng manim từ terminal bằng lệnh:
```
manim -pql KNN.py KNNVisualization
```
Chi tiết setup cài manim trên VSCode [Manim Setup](https://www.youtube.com/watch?v=ib-I3ayqFaw).

Chạy minh họa KNN sử dụng Gdal từ terminal bằng lệnh:
```
python KNNGdal.py

```
📺 Video minh họa
Dự án có các video trực quan hóa thuật toán KNN. Bạn có thể mở file KNNVisualization.mp4 và myvideo.mp4 trong thư mục Video để xem chi tiết.

3. Tương tác với biểu đồ

Mở file KNN.ipynb trong Jupyter Notebook để chạy từng bước.
Nếu như đã chạy xong hết thì sẽ hiện hình bên dưới có thể điều chỉnh giá trị k

![alt text](/KNN/KNNVisualize/NotebookInteractive/newplot.png "Title")

4. Image Classification với dữ liệu Dog,Cat,Panda

Chạy file KNN.ipynb bằng cách bấm Runall sẽ cho ra kết quả như hình bên dưới

![alt text](/KNN/KNNOfficial/output.png "Title")