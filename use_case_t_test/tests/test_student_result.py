from use_case_t_test.data.student_result import StudentTestResult


def test_student_result_passes_when_pval_inf_alpha():
    p_val = 0.01
    alpha = 0.05

    result = StudentTestResult(
        p_value=p_val,
        alpha=alpha,
    )


    assert result.are_means_equals(), "The test should pass when p_value is lte alpha"


def test_student_result_passes_when_pval_sup_alpha():
    p_val = 0.05
    alpha = 0.01

    result = StudentTestResult(
        p_value=p_val,
        alpha=alpha,
    )


    assert not result.are_means_equals(), "The test should pass when p_value is lte alpha"
