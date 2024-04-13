"""
Modul zur Berechnung der Teilfächenbelastung
"""

#  Reduktion der Belastungsfläche bei ausmittiger Lasteintragung


def b1_red(b1, e):
    """
    Berechnet den reduzierten Wert von b1_red, bei ausmittiger Lasteintragung.
    Nach EC 2 - 2012, 6.7, S.98

    Parameter:
    b1 (float): Seitenlänge b1 der Lasteintragsfläche (z. Bsp. Die Seite b eines Elastomerlagers).
    e (float): Der Wert der Exentrizität.

    Returns:
    float: Der reduzierte Wert von b1.
    """
    return b1 - 2 * e


def b2(b1):
    """
    Berechnet die Seitenlänge b2 der Verteilungsfläche Ac1.
    Nach EC 2 - 2012, 6.7, S.98

    Parameter:
    b1 (float): Seitenlänge d1 der Lasteintragsfläche Ac0.

    Returns:
    float: Der berechnete Wert von b2.
    """
    return 3 * b1

def d2(d1):
    """
    Berechnet die Seitenlänge d2 der Verteilungsfläche Ac1.
    Nach EC 2 - 2012, 6.7, S.98

    Parameter:
    d1 (float): Seitenlänge d1 der Lasteintragsfläche Ac0.
    Returns:
    float: Der berechnete Wert von d2.
    """
    return 3 * d1


def A_c0(b_1, d_1):
    """
    Berechnet die Belastungsfläche A_c0 
    nach EC 2 - 2012, 6.7, S. 98.

    Parameter:
    b_1 (float): Die Länge der Basis des Rechtecks.
    d_1 (float): Die Höhe des Rechtecks.

    Returns:
    float: Die Fläche des Rechtecks.
    """
    return b_1 * d_1
