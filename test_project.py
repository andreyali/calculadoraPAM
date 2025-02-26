import pytest
from project import calcular_pam, interpretar_pam, validar_presion

def test_calcular_pam():
    assert calcular_pam(120, 80) == pytest.approx(93.33, 0.01)
    assert calcular_pam(100, 70) == pytest.approx(80.00, 0.01)
    with pytest.raises(TypeError):
        calcular_pam("120", 80)
    with pytest.raises(ValueError):
        calcular_pam(-10, 80)
    with pytest.raises(ValueError):
        calcular_pam(120, 150)

def test_interpretar_pam():
    assert interpretar_pam(50) == "PAM baja (puede indicar hipotensión)"
    assert interpretar_pam(65) == "PAM ligeramente baja"
    assert interpretar_pam(85) == "PAM normal"
    assert interpretar_pam(110) == "PAM alta (puede indicar hipertensión)"

def test_validar_presion():
    assert validar_presion(120, 80) == "Presión arterial normal"
    assert validar_presion(80, 50) == "Presión arterial baja"
    assert validar_presion(150, 100) == "Presión arterial alta"