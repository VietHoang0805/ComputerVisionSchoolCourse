from manim import *
import numpy as np
import random

class KNNVisualization(Scene):
    def construct(self):
        # Tạo danh sách các điểm dữ liệu
        k = 5  # số lượng láng giềng cần xét
        points_class1 = [np.array([random.uniform(-4, -1), random.uniform(-2, 2), 0]) for _ in range(7)]
        points_class2 = [np.array([random.uniform(1, 4), random.uniform(-2, 2), 0]) for _ in range(7)]
        test_point = np.array([0, 0, 0])  # Điểm cần phân loại
        
        # Vẽ các điểm dữ liệu
        dots_class1 = [Dot(point, color=BLUE).scale(1.2) for point in points_class1]
        dots_class2 = [Triangle(color=RED, fill_opacity=1).scale(0.3).move_to(point) for point in points_class2]
        test_dot = Dot(test_point, color=WHITE).scale(1.5)
        
        self.play(*[Create(dot) for dot in dots_class1 + dots_class2], Create(test_dot))
        self.wait(1)
        
        # Tính khoảng cách từ test_point đến các điểm khác
        all_points = points_class1 + points_class2
        all_dots = dots_class1 + dots_class2
        distances = [(np.linalg.norm(test_point - p), dot) for p, dot in zip(all_points, all_dots)]
        distances.sort(key=lambda x: x[0])  # Sắp xếp theo khoảng cách tăng dần
        
        # Vẽ đường kết nối đến k điểm gần nhất
        nearest_neighbors = distances[:k]
        lines = [Line(test_point, neighbor[1].get_center(), color=YELLOW) for neighbor in nearest_neighbors]
        self.play(*[Create(line) for line in lines])
        
        # Đếm số lượng nhãn
        class1_count = sum(1 for _, dot in nearest_neighbors if isinstance(dot, Dot))
        class2_count = k - class1_count
        
        # Quyết định nhãn và đổi màu test_point
        if class1_count > class2_count:
            final_color = BLUE
        else:
            final_color = RED
        
        self.play(test_dot.animate.set_color(final_color))
        self.wait(2)