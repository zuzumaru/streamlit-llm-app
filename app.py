from dotenv import load_dotenv

load_dotenv()

# 画面に入力フォームを1つ用意し、
# 入力フォームから送信したテキストをLangChainを使ってLLMにプロンプトとして渡し、
# 回答結果が画面上に表示されるようにしてください。
# また、入力フォームの内容に応じて、LLMに渡すプロンプトの内容を変更してください。
#　LLMにわたすプロンプトのシステムメッセージも変更する。

#　ｓtreamlitを使った画面の作成
import streamlit as st

st.title("サンプルアプリ: 2種類の専門家を用意したLLMアプリ")

st.write("##### 専門家モード1: 筋トレの専門家")
st.write("筋トレの専門家として回答します")
st.write("##### 専門家モード2: 栄養の専門家")
st.write("栄養の専門家として回答します")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["筋トレの専門家モード", "栄養の専門家モード"]
)

st.divider()

input_message = st.text_input(label="質問内容を入力してください。")


from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

if st.button("実行"):
    st.divider()
    if input_message:
        if selected_item == "筋トレの専門家モード":
            system_msg = "あなたは筋トレの専門家です。ユーザーの質問に専門的かつ分かりやすく答えてください。"
            user_msg = f"筋トレについて質問です: {input_message}"
        else:
            system_msg = "あなたは栄養の専門家です。ユーザーの質問に専門的かつ分かりやすく答えてください。"
            user_msg = f"栄養について質問です: {input_message}"
        messages = [
            SystemMessage(content=system_msg),
            HumanMessage(content=user_msg)
        ]
        result = llm(messages)
        st.write(f"LLM回答: {result.content}")
    else:
        st.error("質問内容を入力してから「実行」ボタンを押してください。")