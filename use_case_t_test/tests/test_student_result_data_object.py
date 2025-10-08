from use_case_t_test.student_result_data_object import StudentTestResult


def test_student_result_passes_when_pval_inf_alpha():
    p_val = 0.01
    alpha = 0.05

    result = StudentTestResult(
        p_value=p_val,
        alpha=alpha,
    )


    assert result.does_test_pass(), "The test should pass when p_value is lte alpha"


def test_student_result_passes_when_pval_sup_alpha():
    p_val = 0.05
    alpha = 0.01

    result = StudentTestResult(
        p_value=p_val,
        alpha=alpha,
    )


    assert not result.does_test_pass(), "The test should pass when p_value is lte alpha"
