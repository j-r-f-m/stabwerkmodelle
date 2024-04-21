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


def test_d1_red():
    """
    Testfall für die Funktion d1_red im Modul teilflächenbelastung.

    Dieser Testfall überprüft, ob die Funktion d1_red den erwarteten Wert zurückgibt,
    wenn die Eingabewerte 0.2 und 0.05 sind. Der erwartete Ausgabewert ist 0.1.
    """
    assert teilflächenbelastung.d1_red(0.2, 0.05) == 0.1

def test_b2():
    """
    Testfall für die Funktion b2_red im Modul teilflächenbelastung.

    Dieser Testfall überprüft, ob die Funktion b2_red den erwarteten Wert zurückgibt,
    wenn der Eingabewert 0.1 ist. Der erwartete Ausgabewert ist 0.3 und die Funktion soll das Ergebnis auf 2 Dezimalstellen runden.
    """
    assert round(teilflächenbelastung.b2(0.1), 2) == 0.3

def test_d2():
    """
    Testfall für die Funktion d2_red im Modul teilflächenbelastung.

    Dieser Testfall überprüft, ob die Funktion d2_red den erwarteten Wert zurückgibt,
    wenn der Eingabewert 0.1 ist. Der erwartete Ausgabewert ist 0.3 und die Funktion soll das Ergebnis auf 2 Dezimalstellen runden.
    """
    assert round(teilflächenbelastung.d2(0.1), 2) == 0.3

def test_A_co():
    """
    Testfall für die Funktion A_co im Modul teilflächenbelastung.

    Dieser Testfall überprüft, ob die Funktion A_co den erwarteten Wert zurückgibt,
    wenn die Eingabewerte 0.2 und 0.1 sind. Der erwartete Ausgabewert ist 0.02 und die Funktion soll das Ergebnis auf 2 Dezimalstellen runden.
    """
    assert round(teilflächenbelastung.A_c0(0.2, 0.1), 2) == 0.02

def test_A_c1():
    """
    Test case for the A_c1 function in the teilflächenbelastung module.
    
    This test case checks if the A_c1 function returns the expected result when given specific input values.
    It asserts that the rounded result of A_c1(0.3, 0.6) is equal to 0.18.
    """
    assert round(teilflächenbelastung.A_c1(0.3, 0.6), 2) == 0.18

def test_F_Rdu():
    """
    Test case for the F_Rdu function in the teilflächenbelastung module.
    
    This test case checks if the F_Rdu function returns the expected result
    when given specific input values. It asserts that the rounded result
    of F_Rdu(0.02, 0.18, 17.0) is equal to 1.02.
    """
    assert round(teilflächenbelastung.F_Rdu(0.02, 0.18, 17.0), 2) == 1.02
    
def test_Nachweis_Auswertung():
    assert(teilflächenbelastung.NachweisAuswertung(1, "MN",1.02, "MN")) == "Nachweis erfüllt: 1 MN <= 1.02 MN"