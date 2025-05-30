
import streamlit as st

# 세션을 활용하여 상태를 기억하는 방법 소개
st.title("🔁 튜토리얼 6: 세션 상태 관리")


# 세션 상태에 count가 없으면 초기값 설정
if "count" not in st.session_state:
    st.session_state.count = 0


# 버튼 클릭 시 count 값 증가
if st.button("카운트 증가"):
    st.session_state.count += 1


# 현재 상태 값 출력
st.write("현재 카운트:", st.session_state.count)
