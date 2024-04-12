def f_cd(alpha_cc, f_ck_cyl, gamma_c=1.5):
    """
    Berechnung des Bemessungswertes der Betondruckfestigkeit nach DIN EN 1992-1-1, 3.1.6 (1)
    Examples:
        >>> f_cd(0.85, 30, 1.5)
        17.0

    
    Args:
    alpah_cc: Korrekturfaktor für langzeitige Einwirkungen
    f_ck_cyl: charakteristischer Zylinderdruckfestigkeitswert des Betons
    gamma_c: Teilsicherheitsbeiwert für Beton

    Returns: Bemessungswert der Betondruckfestigkeit f_cd
    """ 
    return alpha_cc * (f_ck_cyl/ gamma_c)


def hello():
    print("Hello from .py")
    return "Hello from .py"