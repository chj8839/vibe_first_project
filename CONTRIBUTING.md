# 기여 가이드

숫자 맞추기 게임 프로젝트에 기여해 주셔서 감사합니다!

## 기여 방법

1. [저장소](https://github.com/chj8839/vibe_first_project)를 Fork합니다.
2. 새 브랜치를 만듭니다.

   ```bash
   git checkout -b feature/my-feature
   ```

3. 변경 사항을 적용하고 커밋합니다.

   ```bash
   git commit -m "feat: 기능 설명"
   ```

4. Fork한 저장소에 Push합니다.

   ```bash
   git push origin feature/my-feature
   ```

5. Pull Request를 생성합니다.

## 개발 환경 설정

```powershell
git clone https://github.com/chj8839/vibe_first_project.git
cd vibe_first_project
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

> Python **64-bit** 환경이 필요합니다. 자세한 내용은 [README.md](README.md)를 참고하세요.

## 커밋 메시지 가이드

- `feat:` 새 기능
- `fix:` 버그 수정
- `docs:` 문서 변경
- `refactor:` 코드 리팩터링
- `chore:` 빌드·설정 등 기타 변경

## Pull Request 체크리스트

- [ ] 변경 목적이 PR 설명에 명확히 적혀 있습니다.
- [ ] 로컬에서 `python -m streamlit run app.py`로 동작을 확인했습니다.
- [ ] README 등 관련 문서를 함께 수정했습니다 (필요한 경우).

## 행동 강령

기여 시 [행동 강령](CODE_OF_CONDUCT.md)을 준수해 주세요.

## 문의

버그 제보는 [Issues](https://github.com/chj8839/vibe_first_project/issues)를 이용해 주세요.
