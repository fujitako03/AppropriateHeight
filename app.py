import math

import streamlit as st

st.title("適正身長診断アプリ")


def calc_appropriate_height(weight: float) -> int:
    """体重から適正身長を計算する

    Args:
        weitht (float): 体重

    Returns:
        float: 適正身長
    """
    height = math.sqrt(weight / 22) * 100

    return round(height)

def handle_change():
    """スライダーが更新されるたびに体重と適正身長を更新
    """
    st.session_state.weight = st.session_state.weight_slider 
    st.session_state.height = calc_appropriate_height(st.session_state.weight)


# 初期化
if 'weight' not in st.session_state:
    st.session_state.weight = 0

if 'height' not in st.session_state:
    st.session_state.height = 0

# 身長
st.markdown(
    f"<h1 style='text-align: center; color: red;'> \
    あなたの適正身長は\
    </h1>", unsafe_allow_html=True)
# 身長
st.markdown(
    f"<h1 style='text-align: center; color: red; font-size: 7em; margin-bottom: -100;'> \
    {st.session_state.height}\
    </h1>", unsafe_allow_html=True)
st.markdown(
    f"<h1 style='text-align: center; color: red;'> \
    cm\
    </h1>", unsafe_allow_html=True)


# 体重
st.slider(
    '体重を入力してね', 
    min_value=0, 
    max_value=150,
    on_change=handle_change,
    key="weight_slider")
# st.write("あなたの適正身長は", calc_appropriate_height(w), "cm")


#
st.subheader("参考")
st.markdown("- [日本医師会](https://www.med.or.jp/forest/health/eat/11.html)")
