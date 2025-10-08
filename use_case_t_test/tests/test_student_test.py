import numpy as np

from use_case_t_test.student_test import student_test


def test_equal_samples():
    x = np.random.normal(0, 1, 1000)
    y = np.random.normal(0, 1, 1000)
    alpha = 0.2

    result = student_test(sample_1=x, sample_2=y, alpha=alpha)

    assert result.are_means_equals(), "Means are equals and test should confirm"


def test_different_samples():
    x = np.random.normal(0, 1, 1000)
    y = np.random.normal(100, 1, 1000)
    alpha = 0.2

    result = student_test(sample_1=x, sample_2=y, alpha=alpha)

    assert result.are_means_equals(), "Means are different and test should confirm"