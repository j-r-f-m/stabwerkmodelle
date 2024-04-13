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
    Testfall für die Funktion b2_red im Modul teilflächenbelastung.

    Dieser Testfall überprüft, ob die Funktion b2_red den erwarteten Wert zurückgibt,
    wenn der Eingabewert 0.1 ist. Der erwartete Ausgabewert ist 0.3 und die Funktion soll das Ergebnis auf 2 Dezimalstellen runden.
    """
    assert round(teilflächenbelastung.b2(0.1), 2) == 0.3


def test_A_co():
    """
    Testfall für die Funktion A_co im Modul teilflächenbelastung.

    Dieser Testfall überprüft, ob die Funktion A_co den erwarteten Wert zurückgibt,
    wenn die Eingabewerte 0.2 und 0.1 sind. Der erwartete Ausgabewert ist 0.02 und die Funktion soll das Ergebnis auf 2 Dezimalstellen runden.
    """
    assert round(teilflächenbelastung.A_c0(0.2, 0.1), 2) == 0.02
