from numpy import ndarray

from use_case_t_test.student_result_data_object import StudentTestResult


def func(x: ndarray, y: ndarray, alpha: float = 0.05) -> StudentTestResult:
    ...