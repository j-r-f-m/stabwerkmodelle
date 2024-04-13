import sys

sys.path.append(
    "c:\\Users\\donut\\programming\\python_projects\\stabwerkmodelle\\src\\stabwerkmodelle"
)

import teilflächenbelastung


def test_b1_red():
    """
    Testfall für die Funktion b1_red im Modul teilflächenbelastung.

    Dieser Testfall überprüft, ob die Funktion b1_red den erwarteten Wert zurückgibt, 
    wenn die Eingabewerte 0.2 und 0.05 sind. Der erwartete Ausgabewert ist 0.1.
    """
    assert teilflächenbelastung.b1_red(0.2, 0.05) == 0.1

def test_b2_red():
    """
    Test case for the b2_red function in teilflächenbelastung module.
    
    This test checks if the b2_red function returns the expected value when given an input of 0.1.
    The expected output is 0.3, and the function is expected to round the result to 2 decimal places.
    """
    assert round(teilflächenbelastung.b2_red(0.1), 2) == 0.3

