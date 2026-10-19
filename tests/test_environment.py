"""제공된 간단한 검사. 학생 답안이나 시험 코드를 불러오지 않음."""

import sys

import numpy as np


def test_python_and_numpy():
    assert sys.version_info[:2] == (3, 12)
    values = np.array([10.0, 20.0, 30.0])
    assert (values * 2.0).tolist() == [20.0, 40.0, 60.0]
    assert values.tolist() == [10.0, 20.0, 30.0]
