"""
숫자 맞추기 게임 - Streamlit 웹 애플리케이션

컴퓨터가 1~100 사이의 숫자를 무작위로 선택하고,
사용자가 힌트를 참고해 최대 10번 안에 정답을 맞추는 게임입니다.
"""

import random

import streamlit as st

# 게임 규칙 상수
MIN_NUMBER = 1          # 맞출 수 있는 최소 숫자
MAX_NUMBER = 100        # 맞출 수 있는 최대 숫자
MAX_ATTEMPTS = 10       # 게임당 최대 시도 횟수
DEFAULT_GUESS = 50      # 숫자 입력란 기본값

# Streamlit 페이지 기본 설정 (브라우저 탭 제목, 아이콘, 레이아웃)
st.set_page_config(page_title="숫자 맞추기", page_icon="🎯", layout="centered")

# 화면 상단 제목 및 안내 문구
st.title("🎯 숫자 맞추기 게임")
st.caption("1부터 100까지의 숫자 중 하나를 맞춰보세요!")


def init_game():
    """게임 상태를 초기화하고 새로운 정답 숫자를 생성합니다."""
    # session_state: Streamlit이 사용자 세션마다 유지하는 상태 저장소
    st.session_state.target = random.randint(MIN_NUMBER, MAX_NUMBER)  # target: 정답 숫자
    st.session_state.attempts = 0       # attempts: 현재까지 시도한 횟수
    st.session_state.history = []       # history: 시도 기록 목록 (입력값, 힌트)
    st.session_state.won = False        # won: 정답을 맞췄는지 여부


# 최초 실행 시 또는 세션에 게임 상태가 없으면 새 게임 시작
if "target" not in st.session_state:
    init_game()

# 상단 지표 영역: 시도 횟수와 남은 기회를 2열로 표시
col1, col2 = st.columns(2)  # col1, col2: 좌·우 컬럼 레이아웃

with col1:
    st.metric("시도 횟수", st.session_state.attempts)

with col2:
    remaining = max(0, MAX_ATTEMPTS - st.session_state.attempts)  # remaining: 남은 시도 횟수
    st.metric("남은 기회", remaining if not st.session_state.won else "—")

# 게임 결과에 따라 화면 분기 처리
if st.session_state.won:
    # 정답을 맞춘 경우: 축하 메시지와 다시 하기 버튼 표시
    st.success(
        f"🎉 정답입니다! **{st.session_state.target}** — "
        f"{st.session_state.attempts}번 만에 맞췄어요!"
    )
    if st.button("다시 하기", type="primary"):
        init_game()   # 게임 상태 초기화
        st.rerun()    # rerun: 화면을 새로고침하여 변경된 상태 반영

elif st.session_state.attempts >= MAX_ATTEMPTS:
    # 시도 횟수를 모두 사용한 경우: 정답 공개 및 다시 하기 버튼 표시
    st.error(f"😢 기회를 모두 사용했습니다. 정답은 **{st.session_state.target}** 이었어요.")
    if st.button("다시 하기", type="primary"):
        init_game()
        st.rerun()

else:
    # 게임 진행 중: 숫자 입력 및 확인 버튼 표시
    guess = st.number_input(
        "숫자를 입력하세요",
        min_value=MIN_NUMBER,
        max_value=MAX_NUMBER,
        value=DEFAULT_GUESS,
        step=1,
        key="guess_input",  # key: 위젯을 구분하는 고유 식별자
    )

    if st.button("확인", type="primary"):
        st.session_state.attempts += 1  # 시도 횟수 1 증가

        # 입력값과 정답을 비교해 힌트 메시지 결정
        if guess < st.session_state.target:
            hint = "⬆️ 더 큰 숫자입니다."   # hint: 사용자에게 보여줄 힌트 문구
        elif guess > st.session_state.target:
            hint = "⬇️ 더 작은 숫자입니다."
        else:
            hint = "🎉 정답!"
            st.session_state.won = True     # 정답이면 승리 상태로 변경

        # 이번 시도 결과를 기록에 추가
        st.session_state.history.append({"guess": guess, "hint": hint})
        st.rerun()

# 시도 기록이 있으면 하단에 목록으로 표시
if st.session_state.history:
    st.divider()
    st.subheader("시도 기록")

    # reversed: 최신 시도가 위에 오도록 역순 순회
    for i, entry in enumerate(reversed(st.session_state.history), start=1):
        # entry: 한 번의 시도 정보 (guess=입력값, hint=힌트)
        # i: 역순 목록에서의 순번 (표시용 번호 계산에 사용)
        attempt_number = len(st.session_state.history) - i + 1
        st.write(f"**{attempt_number}번째** — {entry['guess']}: {entry['hint']}")
