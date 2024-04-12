def f_cd(alpha_cc, f_ck_cyl, gamma_c=1.5):
    """
    Berechnung des Bemessungswertes der Betondruckfestigkeit nach DIN EN 1992-1-1, 3.1.6
    :param f_ck_cyl: charakteristischer Zylinderdruckfestigkeitswert des Betons
    :param alpha_cc: Korrekturfaktor für langzeitige Einwirkungen
    :return: Bemessungswert der Betondruckfestigkeit
    """ 
    return alpha_cc * (f_ck_cyl/ gamma_c)


def hello():
    print("Hello from mats_beton.py")