import streamlit as st

st.title("ROBOT BACCARAT")
st.write("Dán kết quả vào đây để Robot gợi ý:")

# Ô nhập liệu
chuoi = st.text_input("Nhập chuỗi P B:", "")

if chuoi:
    st.write("Robot đang tính...")
    st.success("Gợi ý: Đánh BANKER")

