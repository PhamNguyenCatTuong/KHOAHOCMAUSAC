import streamlit as st
import numpy as np
import colour

st.title('🎨 Tính toán ΔE (CIE 2000)')

# Tạo 2 cột để nhập liệu
col1, col2 = st.columns(2)

with col1:
    st.header("Màu tham chiếu")
    L1 = st.number_input('Nhập L1:', 0.0, 100.0, 50.0, key="L1")
    a1 = st.number_input('Nhập a1:', -128.0, 128.0, 0.0, key="a1")
    b1 = st.number_input('Nhập b1:', -128.0, 128.0, 0.0, key="b1")

with col2:
    st.header("Màu mẫu (Sample)")
    L2 = st.number_input('Nhập L2:', 0.0, 100.0, 50.0, key="L2")
    a2 = st.number_input('Nhập a2:', -128.0, 128.0, 0.0, key="a2")
    b2 = st.number_input('Nhập b2:', -128.0, 128.0, 0.0, key="b2")

# Nút tính toán
if st.button("Tính ΔE (CIE 2000)"):
    Lab1 = np.array([L1, a1, b1])
    Lab2 = np.array([L2, a2, b2])
    
    delta_E = colour.delta_E(Lab1, Lab2, method='CIE 2000')
    
    # Đánh giá
    if delta_E < 1:
        assessment = "✅ Không thể phân biệt bằng mắt thường"
    elif delta_E < 2:
        assessment = "🔍 Rất nhỏ - chỉ phát hiện bởi chuyên gia"
    elif delta_E < 3:
        assessment = "👍 Nhỏ - chấp nhận được trong in chất lượng cao"
    elif delta_E < 6:
        assessment = "⚠️ Vừa - chấp nhận được trong in thông thường"
    elif delta_E < 12:
        assessment = "❌ Lớn - không đạt yêu cầu in chuyên nghiệp"
    else:
        assessment = "🚫 Rất lớn - khác biệt rõ ràng"
    
    # Hiển thị kết quả
    st.success(f"""
    ### Kết quả:
    **ΔE (CIE 2000):** {delta_E:.4f}  
    **Đánh giá:** {assessment}
    """)