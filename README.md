# Week 8 환경 준비 · 1분반

**환경 준비와 간단한 예제 연습용 자료임. 실제 시험 문제와 답안은 포함되지 않음.**

1. 본인 GitHub 계정 확인
2. 바탕화면 학번 폴더 만들기와 clone
3. Conda 환경과 필수 패키지 설치
4. 예제 문제 작성·실행
5. 검사·계정 정리

모든 명령은 **Anaconda Prompt**에서 실행한다. VS Code는 편집·저장에만 사용한다.
GitHub 웹의 README에서 명령을 한 블록씩 복사한다.

- **지금:** 본인 분반 저장소를 직접 clone한다. **Use this template을 누르거나 개인 시험 저장소를 만들지 않는다.**
- **시험 당일:** 같은 분반 저장소에 게시된 시험 코드로 본인 Private 저장소를 만든 뒤 새로 clone한다. 지금 준비한 Conda 환경을 그대로 사용한다.
- 이번 연습에는 GitHub push, LMS 제출, 스크린샷 제출이 필요 없음.

[수업 화면 안내 PDF](environment_practice.pdf)는 설치 안내 다음에 실제 시험지 첫 쪽의 문제·그림을 비운 예시와 간단한 연습 문제를 보여준다. 이어서 검사와 계정 정리를 진행한다. 첫 쪽 예시의 제출 안내는 실제 시험에만 적용됨.

## 1. 본인 GitHub 계정 확인

- GitHub 웹에서 본인 계정으로 로그인한다. 다른 사람 계정이 보이면 교수자에게 알린다.
- 교수자가 초대를 보냈다고 안내하면 수락하고 **본인 분반** 저장소가 열리는지 확인한다. 초대가 없거나 저장소가 열리지 않으면 교수자에게 알린다.
- 저장소 주소: https://github.com/engineering-programming-course/applied-programming-2026-midterm-section01
- 이 초대는 분반 배포 저장소를 읽는 권한임. 시험 당일에도 같은 분반 주소를 사용한다.
- 안내 화면의 `SSUMechE`는 교수자 계정 예시임. 학생은 본인 계정으로 로그인한다.

clone 전에 Git에 저장된 계정을 확인한다. 웹 로그인과 Git 인증은 별개임.

```bat
git credential-manager github list --no-ui
```

저장된 계정이 없거나 본인 계정만 보여야 한다. 다른 사람의 계정이 보이거나 명령을 찾을 수 없으면 교수자에게 알린다. 다른 사람의 인증정보를 직접 삭제하지 않는다.

**인증창이 뜨지 않고 clone이 인증 오류로 실패할 때만** 아래 로그인 명령을 사용한다.
**YOUR_GITHUB_ID**를 본인 GitHub ID로 바꾼다. 예: **hong2026**.

```bat
git credential-manager github login --username YOUR_GITHUB_ID ^
  --device --no-ui --force
```

표시된 주소에서 **본인 웹 계정**인지 확인한 뒤, 본인 터미널에 표시된 코드를 입력하여 승인한다. 로그인이 끝나면 실패했던 clone 명령을 다시 실행한다. 다른 사람의 인증 코드를 승인하거나 본인 코드를 공유하지 않는다.

## 2. 바탕화면 학번 폴더 만들기와 clone

1. 탐색기에서 **바탕화면 → 새 폴더**를 선택하고 이름을 **본인 학번**으로 지정한다. 예: **20261234**.
2. 그 폴더를 열고 주소 표시줄의 **전체 경로**를 복사한다.
3. Windows 시작 메뉴에서 **Anaconda Prompt**를 연다.
4. 아래 예시 경로를 **방금 복사한 경로**로 바꾸어 실행한다. 따옴표는 유지한다.

```bat
cd /d "C:\Users\Student\Desktop\20261234"
```

명령 입력줄의 현재 위치가 본인 학번 폴더인지 확인한다. 폴더 이동이 실패하면 진행하지 않는다. 기존 파일이나 `prep` 폴더가 있으면 덮어쓰거나 삭제하지 말고 교수자에게 알린다.

```bat
git clone https://github.com/engineering-programming-course/applied-programming-2026-midterm-section01.git prep
cd prep
git remote -v
```

clone 명령이 `prep` 폴더를 만듦. `origin`은 위 **본인 분반 배포 저장소** 주소여야 한다. 인증창이 뜨면 본인 GitHub 계정으로 인증한다. URL에 암호나 토큰을 넣지 않는다.

## 3. Conda 환경과 필수 패키지 설치

현재 위치는 `바탕화면\본인학번\prep`임.
아래 명령의 **20261234**를 **본인 학번**으로 바꾼다. 환경은 처음 한 번만 생성한다. 이미 본인 환경이 있으면 생성 명령은 건너뛰고 활성화부터 진행한다.

```bat
conda --no-plugins env create --solver classic ^
  --file environment.yml --name ap-w08-20261234
```

환경 생성이 성공한 다음 활성화한다.

```bat
conda activate ap-w08-20261234
python -c "import sys; print(sys.executable)"
```

Python 경로에 `envs\ap-w08-본인학번\python.exe`가 포함되어야 한다. `base`나 다른 학생의 환경이면 설치를 진행하지 말고 교수자에게 알린다.

실제 시험에 필요한 NumPy, pytest와 로컬 설치용 setuptools까지 지금 설치한다.

```bat
python -m pip install -r requirements.txt
python --version
python -c "import numpy; print(numpy.__version__)"
python -c "import pytest; print(pytest.__version__)"
python -c "from importlib.metadata import version; print(version('setuptools'))"
python -m pip check
```

예상 결과:

```text
Python 3.12.13
2.4.6
9.1.1
80.9.0
No broken requirements found.
```

예제 문제를 풀기 전에 환경 검사만 실행한다. 미완성 예제 함수는 이 검사에서 호출하지 않는다.

```bat
python -m pytest -q tests\test_environment.py
```

결과는 **`1 passed`**임. 실행 시간은 PC마다 다름.
설치나 검사가 실패하면 오류를 교수자에게 보여준다. 다른 환경에 설치하거나 버전을 임의로 바꾸지 않는다.

## 4. 예제 문제 작성·실행

### Calculate the total price

단가와 수량을 곱한 총액을 반환하도록 `total_price`를 완성하시오.
실제 시험과 다른 간단한 연습 문제임.

1. VS Code의 **File > Open Folder**에서 `바탕화면\본인학번\prep`을 연다.
2. `practice.py`의 `total_price(unit_price, quantity)`를 찾는다.
3. **`PRACTICE_1`의 BEGIN/END 사이만 수정**하여 총액을 `result`에 저장한다. 함수 이름, 인수와 제공된 `return result`는 유지한다.
4. **Ctrl+S**로 저장하고, 본인 환경이 활성화된 Anaconda Prompt에서 아래 Run 명령을 실행한다.

`unit_price`는 0 이상의 단가이고 `quantity`는 0 이상의 정수 수량임. 입력 검사는 작성하지 않음. 함수의 세부 조건은 작성 구간 바로 위 주석에 있음.

수정 위치 — `practice.py`

```python
def total_price(unit_price, quantity):
    # ----- BEGIN PRACTICE_1 -----
    result = 0.0
    # ----- END PRACTICE_1 -----
    return result
```

**Run and expected output**

입력값은 코드에 미리 지정되어 있으므로 별도로 입력할 필요 없음.

```bat
python practice.py
```

```text
1500.0 x 4 = 6000.0
2500.0 x 3 = 7500.0
```

수정 전에는 총액이 두 경우 모두 `0.0`으로 표시됨. 작성 구간의 임시 값이며 환경 설치 오류가 아님. 수정 후에도 총액이 `0.0`이면 저장 여부와 현재 터미널 폴더를 확인한다.

## 5. 검사·계정 정리

작성한 함수를 제공 검사로 확인한다. 검사 파일은 수정하지 않는다.

```bat
python -m pytest -q tests\test_practice.py
```

결과는 **`3 passed`**임. 실행 시간은 PC마다 다름.
`failed`가 표시되면 출력된 입력값과 비교 결과를 확인하고 `practice.py`만 수정하여 다시 검사한다.

지금 만든 **`ap-w08-본인학번` 환경은 삭제하지 않는다.** 공용 PC를 떠날 때 다음 순서로 정리한다.

1. 아래 **YOUR_GITHUB_ID**를 본인 GitHub ID로 바꾸어 Git에서 로그아웃한다.

```bat
git credential-manager github logout ^
  YOUR_GITHUB_ID --no-ui
```

2. 목록에서 본인 ID가 사라졌는지 확인한다.

```bat
git credential-manager github list --no-ui
```

3. GitHub 웹 오른쪽 위 프로필 메뉴에서 **Sign out**을 선택한다.
4. VS Code의 연습 폴더·파일과 Anaconda Prompt를 닫는다. LMS에 로그인했다면 로그아웃한다.

웹 로그아웃과 Git 인증정보 정리는 서로 다른 작업임. 다른 사람의 인증정보를 일괄 삭제하거나 공용 Git 설정을 바꾸지 않는다. 이번 연습에는 push가 없으므로 Git 이름·이메일 설정은 필요 없음. 실제 시험 종료 후 파일 삭제는 시험 종료 안내를 따른다.

## 시험 당일 — 지금 실행하지 않음

시험 코드는 **같은 분반 저장소 주소**에 게시된다. **2분반 → 1분반** 순서로 진행하며 본인 분반의 게시 안내를 따른다.

1. 교수자가 코드 게시를 안내하면 분반 저장소 페이지를 새로고침한다.
2. **Use this template > Create a new repository**로 **본인 계정의 Private 저장소**를 만든다.
3. 개인 저장소를 바탕화면 학번 폴더 안 `exam`에 **새로 clone**한다. 현재 `prep`은 사용하지 않는다.
4. 지금 준비한 `ap-w08-본인학번` 환경을 활성화한다. `origin`은 본인 개인 저장소 주소여야 한다.
5. 시험 코드의 `README.md`와 `pyproject.toml`이 있는 `exam` 폴더에서 아래 명령을 실행한다. 준비한 의존성을 사용하여 새 시험 코드를 현재 환경에 연결하는 단계임.

```bat
python -m pip install -e . --no-deps ^
  --no-build-isolation --no-index --no-cache-dir
```

이후 실제 시험 README의 실행·검사·제출 안내를 따른다. 현재 환경 연습에는 `pyproject.toml`이 없으므로 위 명령을 실행하지 않는다. 개인 복사본과 `prep` 폴더는 분반 원본이 바뀌어도 자동으로 갱신되지 않음.

## 설치 오류가 생길 때만

Conda 명령에서 **`cp949` 또는 `UnicodeDecodeError`**가 표시되면, 같은 Anaconda Prompt에서 아래 명령을 실행한 뒤 실패한 명령을 다시 실행한다.

```bat
set PYTHONUTF8=1
```

오류가 없으면 이 설정은 필요 없음. 다른 오류이거나 재시도에도 실패하면 오류 화면을 교수자에게 보여준다.
