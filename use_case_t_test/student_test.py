from numpy import ndarray
from scipy.stats import ttest_ind

from use_case_t_test.data.student_result import StudentTestResult


def student_test(sample_1: ndarray, sample_2: ndarray, alpha: float = 0.05) -> StudentTestResult:
    """
    bla bla bla
    """
    _, p_value = ttest_ind(sample_1, sample_2)

    return StudentTestResult(
        alpha=alpha,
        p_value=p_value
    )