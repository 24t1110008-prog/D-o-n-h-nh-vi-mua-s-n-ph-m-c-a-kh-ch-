import streamlit as st
import pandas as pd
import time

# ==========================================
# 1. SETUP CONFIG (PHẢI ĐẶT ĐẦU TIÊN)
# ==========================================
st.set_page_config(
    page_title="Customer AI Prediction",
    page_icon="🛒",
    layout="wide"
)

# ==========================================
# 2. ĐỌC FILE CSS NGOÀI (Mã hóa UTF-8 chống lỗi)
# ==========================================
with open("style.css", encoding="utf-8") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# ==========================================
# 3. TIÊU ĐỀ CHÍNH (Hòa quyện vào nền tối)
# ==========================================
st.markdown(
    """
    <div class='main-header'>
        <h1>🛒 Customer Purchase Prediction</h1>
        <p class='subtitle'>Hệ thống AI phân tích và dự đoán tỷ lệ chuyển đổi hành vi mua hàng theo thời gian real-time</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ==========================================
# 4. THANH SIDEBAR NHẬP LIỆU
# ==========================================
st.sidebar.markdown("### 📋 Thông Tin Khách Hàng")
st.sidebar.markdown("---")

age = st.sidebar.slider("🎂 Tuổi (Age)", 18, 60, 25)
income = st.sidebar.slider("💰 Thu nhập (Income - Triệu/Tháng)", 5, 50, 15)
online_time = st.sidebar.slider("⏱️ Thời gian Online (Giờ/Ngày)", 1.0, 8.0, 2.0, step=0.5)
product_views = st.sidebar.slider("👀 Lượt xem sản phẩm (Views)", 1, 20, 5)
gender = st.sidebar.selectbox("⚧️ Giới tính (Gender)", ["Female", "Male"])

# ==========================================
# 5. HIỂN THỊ THÔNG SỐ (METRIC CARDS)
# ==========================================
st.markdown("### 📊 Tổng quan đối tượng mục tiêu")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(f"<div class='metric-card'><p class='metric-label'>🎂 Tuổi</p><p class='metric-value'>{age}</p></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='metric-card'><p class='metric-label'>💰 Thu nhập</p><p class='metric-value'>{income}M</p></div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div class='metric-card'><p class='metric-label'>⏱️ Online</p><p class='metric-value'>{online_time}h</p></div>", unsafe_allow_html=True)
with col4:
    st.markdown(f"<div class='metric-card'><p class='metric-label'>👀 Lượt xem</p><p class='metric-value'>{product_views}</p></div>", unsafe_allow_html=True)
with col5:
    st.markdown(f"<div class='metric-card'><p class='metric-label'>⚧️ Giới tính</p><p class='metric-value'>{gender}</p></div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# 6. KHỐI XỬ LÝ NÚT DỰ ĐOÁN & LOGIC KẾT QUẢ
# ==========================================
left_co, cent_co, last_co = st.columns([1, 2, 1])
with cent_co:
    predict_btn = st.button("🚀 PHÂN TÍCH VÀ DỰ ĐOÁN", use_container_width=True)

if predict_btn:
    with st.spinner('🤖 AI đang phân tích dữ liệu hành vi...'):
        time.sleep(0.6)
        
        # Công thức tính điểm hành vi giả lập
        score = (income * 0.3 + online_time * 2 + product_views * 0.8)
        
        st.markdown("---")
        st.markdown("### 🤖 Kết Quả Dự Đoán Từ Hệ Thống")
        
        if score >= 18:
            st.markdown(
                f"""
                <div class='result-card success-card'>
                    <h2>✅ KHÁCH HÀNG SẼ MUA HÀNG (WILL BUY)</h2>
                    <p>Dựa trên thuật toán phân tích chuyên sâu, khách hàng này có tiềm năng chốt đơn rất cao. Nên đẩy mạnh chiến dịch tiếp thị bám đuôi (Retargeting).</p>
                    <div class='result-meta'>🎯 Chỉ số điểm hành vi: {score:.2f} / Ngưỡng: 18.0</div>
                </div>
                """, 
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div class='result-card danger-card'>
                    <h2>❌ KHÁCH HÀNG KHÔNG MUA HÀNG (WILL NOT BUY)</h2>
                    <p>Khả năng chốt đơn thấp. Hệ thống đề xuất kích hoạt thêm chương trình tặng voucher giảm giá để cải thiện tỷ lệ chuyển đổi.</p>
                    <div class='result-meta'>🎯 Chỉ số điểm hành vi: {score:.2f} / Ngưỡng: 18.0</div>
                </div>
                """, 
                unsafe_allow_html=True
            )

# ==========================================
# 7. CHÂN TRANG (FOOTER)
# ==========================================
st.markdown("<div class='footer'>⚡ Designed with Premium UI Elements • Machine Learning Core Engine v2.0</div>", unsafe_allow_html=True)