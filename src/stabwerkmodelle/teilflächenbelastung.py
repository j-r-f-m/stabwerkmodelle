"""
Modul zur Berechnung der Teilfächenbelastung
"""

from math import sqrt

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

def d1_red(d1, e):
    """
    Berechnet den reduzierten Wert von d1_red, bei ausmittiger Lasteintragung.
    Nach EC 2 - 2012, 6.7, S.98

    Parameter:
    d1 (float): Seitenlänge d1 der Lasteintragsfläche (z. Bsp. Die Seite d eines Elastomerlagers).
    e (float): Der Wert der Exentrizität.

    Returns:
    float: Der reduzierte Wert von d1.
    """
    return d1 - 2 * e

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
    b_1 (float): Seitenlänge b_1 der Lastausbreitungsfläche.
    d_1 (float): Seitenlänge d_1 der Lastausbreitungsfläche.

    Returns:
    float: Die Fläche des Rechtecks.
    """
    return b_1 * d_1

def A_c1(d2, b2 ):
    """
    Berechnet die Lastausbreitungsfläche A_c1 
    nach EC 2 - 2012, 6.7, S. 98.

    Parameter:
    b_2 (float): Seitenlänge b_2 der Lastausbreitungsfläche.
    d_2 (float): Seitenlänge d_2 der Lastausbreitungsfläche.

    Returns:
    float: Die Fläche des Rechtecks.
    """
    return d2 * b2

def F_Rdu(Ac0, Ac1, f_cd):
    """
    Berechnet vom Beton aufnehmbare Druckkraft F_Rd,u

    Parameters:
    Ac0 (float): Lasteinleitungsfläche 
    Ac1 (float): Lastausbreitungsfläche
    fcd (float): Bemessungswert der Betpndruckfestigkeit [N/mm^2]

    Returns:
    float: Design value of the partial load [N]
    """
    term_1 = Ac0 * f_cd * sqrt(Ac1 / Ac0)
    term_2 = 3 * f_cd * Ac0
    if term_1 <= term_2:
        return term_1
    else:
        return term_2

def NachweisAuswertung(Fed,Fed_einheit, F_Rdu, F_Rdu_einheit):

    if Fed <= F_Rdu:
        return f"Nachweis erfüllt: {Fed} {Fed_einheit} <= {F_Rdu} {F_Rdu_einheit}"
    else:
        return f"Nachweis nicht erfüllt: {Fed} {Fed_einheit} > {F_Rdu} {F_Rdu_einheit}"
    
    
