import random

import streamlit as st

st.set_page_config(page_title="숫자 맞추기", page_icon="🎯", layout="centered")

st.title("🎯 숫자 맞추기 게임")
st.caption("1부터 100까지의 숫자 중 하나를 맞춰보세요!")


def init_game():
    st.session_state.target = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.history = []
    st.session_state.won = False


if "target" not in st.session_state:
    init_game()

col1, col2 = st.columns(2)
with col1:
    st.metric("시도 횟수", st.session_state.attempts)
with col2:
    remaining = max(0, 10 - st.session_state.attempts)
    st.metric("남은 기회", remaining if not st.session_state.won else "—")

if st.session_state.won:
    st.success(
        f"🎉 정답입니다! **{st.session_state.target}** — "
        f"{st.session_state.attempts}번 만에 맞췄어요!"
    )
    if st.button("다시 하기", type="primary"):
        init_game()
        st.rerun()
elif st.session_state.attempts >= 10:
    st.error(f"😢 기회를 모두 사용했습니다. 정답은 **{st.session_state.target}** 이었어요.")
    if st.button("다시 하기", type="primary"):
        init_game()
        st.rerun()
else:
    guess = st.number_input(
        "숫자를 입력하세요",
        min_value=1,
        max_value=100,
        value=50,
        step=1,
        key="guess_input",
    )

    if st.button("확인", type="primary"):
        st.session_state.attempts += 1

        if guess < st.session_state.target:
            hint = "⬆️ 더 큰 숫자입니다."
        elif guess > st.session_state.target:
            hint = "⬇️ 더 작은 숫자입니다."
        else:
            hint = "🎉 정답!"
            st.session_state.won = True

        st.session_state.history.append({"guess": guess, "hint": hint})
        st.rerun()

if st.session_state.history:
    st.divider()
    st.subheader("시도 기록")
    for i, entry in enumerate(reversed(st.session_state.history), start=1):
        st.write(f"**{len(st.session_state.history) - i + 1}번째** — {entry['guess']}: {entry['hint']}")
