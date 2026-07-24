# 🎯 숫자 맞추기 게임

Streamlit으로 만든 간단한 웹 기반 숫자 맞추기 게임입니다.  
1부터 100까지의 랜덤 숫자를 맞추며, 힌트와 시도 기록을 통해 게임을 즐길 수 있습니다.

## 프로젝트 소개

컴퓨터가 1~100 사이의 숫자를 무작위로 선택하고, 사용자는 최대 10번의 기회 안에 정답을 맞추는 게임입니다.

### 주요 기능

- **힌트 제공**: 입력한 숫자가 정답보다 크거나 작은지 안내
- **시도 횟수 표시**: 현재까지 시도한 횟수와 남은 기회 확인
- **시도 기록**: 이전 입력과 힌트를 목록으로 표시
- **게임 재시작**: 정답을 맞추거나 기회를 모두 사용한 뒤 새 게임 시작

## 개발 환경

| 항목 | 내용 |
|------|------|
| 운영체제 | Windows 10 / 11 |
| 언어 | Python 3.11 (**64-bit 필수**) |
| 프레임워크 | Streamlit 1.32+ |
| 에디터 | Cursor IDE |
| 패키지 관리 | pip |

> **중요:** Streamlit은 32-bit Python을 지원하지 않습니다.  
> [python.org](https://www.python.org/downloads/)에서 **Windows installer (64-bit)** 를 설치해 주세요.

## 프로젝트 구조

```
vibe_first_project/
├── app.py              # Streamlit 게임 애플리케이션
├── requirements.txt    # Python 의존성 목록
└── README.md           # 프로젝트 설명 문서
```

## 설치 방법

### 1. 저장소 클론

```bash
git clone https://github.com/chj8839/vibe_first_project.git
cd vibe_first_project
```

### 2. Python 가상 환경 생성 (권장)

**Windows (PowerShell)**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Python 버전 확인

64-bit Python이 설치되어 있는지 확인합니다.

```powershell
python -c "import struct; print(struct.calcsize('P') * 8, 'bit')"
```

출력이 `64 bit`이어야 합니다. `32 bit`이면 64-bit Python을 새로 설치한 뒤 터미널을 다시 열어 주세요.

### 4. 의존성 설치

```powershell
python -m pip install -r requirements.txt
```

## 실행 방법

```powershell
python -m streamlit run app.py
```

`streamlit` 명령을 찾을 수 없다는 오류가 나면 위처럼 `python -m streamlit` 형식으로 실행하세요.

실행 후 브라우저에서 아래 주소로 접속합니다.

```
http://localhost:8501
```

## 게임 방법

1. 1~100 사이의 숫자를 입력합니다.
2. **확인** 버튼을 누르면 더 큰 숫자인지, 더 작은 숫자인지 힌트가 표시됩니다.
3. 최대 10번 안에 정답을 맞추면 승리합니다.
4. 기회를 모두 사용하거나 정답을 맞추면 **다시 하기** 버튼으로 새 게임을 시작할 수 있습니다.

## 문제 해결

### `streamlit` 명령을 찾을 수 없음

Streamlit이 설치되지 않았거나 PATH에 등록되지 않은 경우입니다.

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

### `pip install` 중 pandas / pyarrow 설치 실패

현재 **32-bit Python**을 사용 중일 가능성이 큽니다. Streamlit 의존성(pandas, pyarrow 등)은 64-bit 환경에서만 정상 설치됩니다.

1. [Python 3.11 64-bit](https://www.python.org/downloads/) 설치
2. 설치 시 **Add python.exe to PATH** 옵션 체크
3. 터미널을 새로 연 뒤 아래 명령으로 확인

```powershell
py -0p
python -c "import struct; print(struct.calcsize('P') * 8, 'bit')"
```

4. 프로젝트 폴더에서 다시 설치 및 실행

```powershell
cd C:\project\vibe_first_project
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## 기술 스택

- [Python](https://www.python.org/) — 프로그래밍 언어
- [Streamlit](https://streamlit.io/) — 웹 UI 프레임워크

## 라이선스

이 프로젝트는 [MIT License](LICENSE) 하에 배포됩니다.
