"""
Modul zur Berechnung der Teilfächenbelastung
"""

#  Reduktion der Belastungsfläche bei ausmittiger Lasteintragung

def b1_red(b1, e):
    """
    Berechnet den reduzierten Wert von b1_red, bei ausmittiger Lasteintragung.

    Parameter:
    b1 (float): Breite der Lasteintragsfläche (z. Bsp. Die Seite b eines Elastomerlagers).
    e (float): Der Wert der Exentrizität.

    Returns:
    float: Der reduzierte Wert von b1.
    """
    return b1 - 2 * e


def b2_red(b1_red):
    """
    Berechnet den Wert von b2_red basierend auf dem gegebenen Wert von b1_red.

    Parameter:
    b1_red (float): Der Wert von b1_red.

    Returns:
    float: Der berechnete Wert von b2_red.
    """
    return 3 * b1_red
