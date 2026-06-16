import streamlit as st
import base64
import datetime

st.title("推し紹介カード")

if "cards" not in st.session_state:
    st.session_state.cards = []

image = st.file_uploader(
    "推しの写真を選択",
    type = ["jpg", "jpeg", "png"]
)

with st.expander("推し情報を入力"):
    name = st.text_input("推しの名前")
    group = st.text_input("グループ名")
    age = st.slider("年齢", 0, 100, 1)
    birthday = st.date_input("誕生日", value=datetime.date(2000, 1, 1))
    color = st.text_input("メンバーカラー")
    color1 = st.color_picker(
        "メンバーカラー",
        "#FFFFFF"
    )
    song = st.text_input("好きな曲")
    point = st.text_input("好きなところ")
    level = st.slider("推し度", 0, 100, 10)
    card_color = st.color_picker(
        "カードの色",
        "#FFFFFF"
    )
    create = st.button("カード作成")

if create:
    card = {
        "name": name,
        "group": group,
        "age": age,
        "birthday": birthday.strftime("%Y/%m/%d"),
        "color": color,
        "color1": color1,
        "song": song,
        "point": point,
        "level": level,
        "card_color": card_color,
        "image": image.read() if image is not None else None
    }
    st.session_state.cards.append(card)

    st.markdown("---")
    st.subheader("推し紹介カード")

    img_html = ""
    if card["image"]:
        b64_img = base64.b64encode(card["image"]).decode()
        img_html = f'<img src="data:image/png;base64,{b64_img}" style="width: 200px; border-radius: 10px; margin-bottom: 10px; display: block;">'

    st.markdown(
        f"""
        <div style="background-color: {card_color}80; padding: 20px; border-radius: 15px; border: 1px solid #ddd; color: black; margin-bottom: 10px;">
            {img_html}
            <h3 style="margin-top: 0; color: black;">{name}</h3>
            <p style="margin-bottom: 5px;"><b>グループ:</b> {group} | <b>年齢:</b> {age}歳</p>
            <p style="margin-bottom: 5px;"><b>誕生日:</b> {birthday.strftime("%Y/%m/%d")}</p>
            <p style="margin-bottom: 5px;"><b>メンバーカラー:</b> {color}</p>
            <div style="width:100px; height:20px; background-color:{color1}; border:1px solid black; margin-bottom:10px;"></div>
            <p style="margin-bottom: 5px;"><b>好きな曲:</b> {song}</p>
            <p style="margin-bottom: 5px;"><b>好きなところ:</b> {point}</p>
            <div style="margin-top: 10px;">
                <p style="margin-bottom: 2px; font-size: 0.8em;"><b>推し度:</b> {level}%</p>
                <div style="background-color: rgba(0,0,0,0.1); border-radius: 5px; height: 10px; width: 100%;">
                    <div style="background-color: #4caf50; width: {level}%; height: 10px; border-radius: 5px;"></div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")
st.subheader("カード一覧")

for i, card in enumerate(st.session_state.cards):
    img_html_list = ""
    if card["image"]:
        b64_img_list = base64.b64encode(card["image"]).decode()
        img_html_list = f'<img src="data:image/png;base64,{b64_img_list}" style="width: 100px; border-radius: 10px; margin-bottom: 10px; display: block;">'

    st.markdown(
        f"""
        <div style="background-color: {card['card_color']}80; padding: 20px; border-radius: 15px; border: 1px solid #ddd; color: black; margin-bottom: 10px;">
            {img_html_list}
            <h3 style="margin-top: 0; color: black;">{card['name']}</h3>
            <p style="margin-bottom: 5px;"><b>グループ:</b> {card['group']} | <b>年齢:</b> {card['age']}歳</p>
            <p style="margin-bottom: 5px;"><b>誕生日:</b> {card['birthday']}</p>
            <p style="margin-bottom: 5px;"><b>メンバーカラー:</b> {card['color']}</p>
            <div style="width:100px; height:20px; background-color:{card['color1']}; border:1px solid black; margin-bottom:10px;"></div>
            <p style="margin-bottom: 5px;"><b>好きな曲:</b> {card['song']}</p>
            <p style="margin-bottom: 5px;"><b>好きなところ:</b> {card['point']}</p>
            <div style="margin-top: 10px;">
                <p style="margin-bottom: 2px; font-size: 0.8em;"><b>推し度:</b> {card['level']}%</p>
                <div style="background-color: rgba(0,0,0,0.1); border-radius: 5px; height: 10px; width: 100%;">
                    <div style="background-color: #4caf50; width: {card['level']}%; height: 10px; border-radius: 5px;"></div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("このカードを削除", key=f"delete_{i}"):
        st.session_state.cards.pop(i)
        st.rerun()
    st.markdown("---")

if st.button("保存したカードをすべて削除"):
    st.session_state.cards = []
    st.rerun()