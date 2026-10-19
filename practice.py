"""환경 점검용 예시 문제. 실제 시험 문제와 무관함."""


def total_price(unit_price, quantity):
    # 할 일: 단가(unit_price)와 수량(quantity)을 곱한 값을 result에 저장.
    # 입력: 단가는 0 이상의 실수, 수량은 0 이상의 정수.
    # 수정 위치: 아래 BEGIN/END 사이 한 줄. 함수 이름과 return은 유지.
    # 수량이 0이면 결과도 0.0이어야 함. 입력값 검사는 작성하지 않음.
    # ----- BEGIN PRACTICE_1 -----
    result = 0.0
    # ----- END PRACTICE_1 -----
    return result


if __name__ == "__main__":
    for unit_price, quantity in [(1500.0, 4), (2500.0, 3)]:
        print(f"{unit_price:.1f} x {quantity} = {total_price(unit_price, quantity):.1f}")
