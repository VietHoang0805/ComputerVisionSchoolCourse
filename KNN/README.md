# KNN Visualization

Đây là dự án minh họa thuật toán `K-Nearest Neighbors (KNN)` thông qua các tệp mã nguồn, dữ liệu và video trực quan.

## :file_folder: Cấu trúc thư mục

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

### :rocket: Hướng dẫn sử dụng

### :computer: Thiết lập môi trường ảo (`venv`) (Optional)
Sử dụng môi trường ảo giúp cô lập các thư viện Python của dự án với hệ thống. Làm theo các bước sau:

#### **Tạo môi trường ảo**
Trong thư mục chứa dự án, chạy lệnh sau để tạo môi trường ảo (`venv`):

```bash
python -m venv myenv
```

Sau khi tạo môi trường ảo active lên bằng lệnh
```bash
myenv\Scripts\activate
```

:one: Cài đặt thư viện cần thiết

Trước khi chạy mã, hãy cài đặt các thư viện cần thiết bằng lệnh:

```bash
pip install -r requirements.txt 
```

:two: Chạy minh họa `KNN`

Chạy minh họa KNN sử dụng manim từ terminal bằng lệnh:
```
manim -pql KNN.py KNNVisualization
```

Chi tiết setup cài `manim` trên VSCode [Manim Setup](https://www.youtube.com/watch?v=ib-I3ayqFaw).

**Sau khi chạy sẽ hiện ra video như bên dưới**

<video controls src="KNNVisualize/Video/KNNVisualization.mp4" title="Title"></video>

Chạy minh họa `KNN` sử dụng `Gdal` từ terminal bằng lệnh:

```bash
python KNNGdal.py
```

**Sau khi chạy sẽ hiện ra video như bên dưới**

<video controls src="KNNVisualize/Video/myvideo.mp4" title="Title"></video>

:tv: Video minh họa

Dự án có các video trực quan hóa thuật toán `KNN`. Bạn có thể mở file [KNNVisualization.mp4](/KNN/KNNVisualize/Video/KNNVisualization.mp4) và [myvideo.mp4](/KNN/KNNVisualize/Video/myvideo.mp4) trong thư mục Video để xem chi tiết.

:three: Tương tác với biểu đồ

Mở file [KNN.ipynb](/KNN/KNNVisualize/NotebookInteractive/KNN.ipynb) trong Jupyter Notebook để chạy từng bước.

Nếu như đã chạy xong hết thì sẽ hiện hình bên dưới có thể điều chỉnh giá trị k

![alt text](/KNN/KNNVisualize/NotebookInteractive/newplot.png "Title")

:four: Image Classification với dữ liệu Dog,Cat,Panda

Chạy file [KNN.ipynb](/KNN/KNNOfficial/KNN.ipynb) bằng cách bấm Runall sẽ cho ra kết quả như hình bên dưới

![alt text](/KNN/KNNOfficial/output.png "Title")