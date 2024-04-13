import sys

sys.path.append(
    "c:\\Users\\donut\\programming\\python_projects\\stabwerkmodelle\\src\\stabwerkmodelle"
)

import mats_beton
import teilflächenbelastung
import pytest

def test_f_cd():
    """
    Testfunktion für mats_beton.f_cd.

    Sie verwendet die Funktion mats_beton.f_cd, um f_cd-Werte für eine Liste von f_ck-Werten zu berechnen.
    Die berechneten f_cd-Werte werden dann auf zwei Dezimalstellen gerundet.
    Schließlich wird überprüft, ob die gerundeten f_cd-Werte den erwarteten Werten entsprechen.

    Rückgabewert:
        None
    """
    arr_fck = [12, 16, 20, 25, 30, 35, 40, 45, 50, 55, 60, 70, 80, 90, 100]
    fcd = map(lambda x: mats_beton.f_cd(0.85, x, 1.5), arr_fck)
    round_fcd = list(map(lambda x: round(x, 2), fcd))
    # Erwartete Werte aus Wendehorst Zahlentafeln S.288
    assert round_fcd == [
        6.8,
        9.07,
        11.33,
        14.17,
        17.0,
        19.83,
        22.67,
        25.5,
        28.33,
        31.17,
        34.0,
        39.67,
        45.33,
        51.0,
        56.67,
    ]
