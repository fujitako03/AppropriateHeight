import math

import streamlit as st


def calc_appropriate_height(weight: float) -> int:
    """体重から適正身長を計算する

    Args:
        weitht (float): 体重

    Returns:
        float: 適正身長
    """
    height = math.sqrt(weight / 22) * 100

    return round(height)

def get_advice(now_height: int, best_height: int) -> str:
    diff = best_height - now_height
    base_text = f"あと{diff}cm!"

    if diff >= 5:
        return base_text + "今すぐ骨延長手術を受けてください。"
    elif 1 <= diff <= 4:
        return base_text + "あとちょっとです。牛乳たくさん飲んで、立つことを控えましょう"
    elif diff == 0:
        return "素晴らしい！今後身長を伸ばさないように心がけましょう"
    elif diff <= -1:
        return base_text + "身長が高すぎます。常にダンベルを持ち運ぶことを心がけましょう"

def weight_slider_change():
    """体重スライダーが更新されるたびに体重と適正身長を更新
    """
    st.session_state.weight = st.session_state.weight_slider 
    st.session_state.best_height = calc_appropriate_height(st.session_state.weight)

def height_slider_change():
    """身長が更新されるたびに体重と適正身長を更新
    """
    st.session_state.now_height = st.session_state.height_slider 

# 初期化
if 'weight' not in st.session_state:
    st.session_state.weight = 0

if 'best_height' not in st.session_state:
    st.session_state.best_height = 0

if 'now_height' not in st.session_state:
    st.session_state.now_height = None

# 身長
st.markdown(
    f"<h1 style='text-align: center; color: #809C51;'> \
    あなたの適正身長は\
    </h1>", unsafe_allow_html=True)
# 身長
st.markdown(
    f"<h1 style='text-align: center; color: #528540; font-size: 7em; margin-bottom: -100;'> \
    {st.session_state.best_height}\
    </h1>", unsafe_allow_html=True)
st.markdown(
    f"<h1 style='text-align: center; color: #809C51;'> \
    cm\
    </h1>", unsafe_allow_html=True)


# 体重
st.slider(
    '体重を入力してね', 
    min_value=0, 
    max_value=150,
    on_change=weight_slider_change,
    key="weight_slider")

# アドバイス
if st.session_state.now_height:
    advice_text = get_advice(
        now_height=st.session_state.now_height,
        best_height=st.session_state.best_height)
    st.text(advice_text)
    st.image("./eiyoshi.png", width=100)


# option
with st.expander("オプション"):
    st.slider(
        '現在の身長を入力してね', 
        min_value=50, 
        max_value=220,
        on_change=height_slider_change,
        key="height_slider")

    # 性別
    gender = st.radio("性別", ("未回答", "男性", "女性"))
    st.text("※性別は適正体重と無関係です")

    # 干支
    gender = st.radio("干支", ("未回答", "子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥", "女性"))
    st.text("※干支は適正体重と無関係です")

# 参考
st.markdown("作者： [@fujitako](https://twitter.com/fujitako03)")
st.markdown("参考： [日本医師会](https://www.med.or.jp/forest/health/eat/11.html)")
