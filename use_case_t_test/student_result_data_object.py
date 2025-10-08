from dataclasses import dataclass


@dataclass
class StudentTestResult:
    """
    Class to hold the result of a student test.
    We consider that it passes if the two samples are equal.
    (i.e the p_val is <= alpha)
    """

    alpha: float = 0.05
    p_value: float = 0.05

    def does_test_pass(self) -> bool:
        return self.p_value <= self.alpha
