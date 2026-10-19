"""예시 문제의 제공 검사. 학생이 이 파일을 수정할 필요 없음."""

from practice import total_price


def test_total_for_four_items():
    assert total_price(1500.0, 4) == 6000.0


def test_total_for_three_items():
    assert total_price(2500.0, 3) == 7500.0


def test_zero_quantity():
    assert total_price(2500.0, 0) == 0.0
