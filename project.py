import json

def calcular_pam(sistolica, diastolica):
    """Calcula la presión arterial media (PAM)."""
    if not isinstance(sistolica, (int, float)) or not isinstance(diastolica, (int, float)):
        raise TypeError("La presión sistólica y diastólica deben ser números.")
    if sistolica < 0 or diastolica < 0:
        raise ValueError("La presión sistólica y diastólica no pueden ser negativas.")
    if diastolica > sistolica:
        raise ValueError("La presión diastólica no puede ser mayor que la presión sistólica.")

    pam = (sistolica + 2 * diastolica) / 3
    return pam

def interpretar_pam(pam):
    """Interpreta el valor de la PAM."""
    if pam < 60:
        return "PAM baja (puede indicar hipotensión)"
    elif pam < 70:
        return "PAM ligeramente baja"
    elif pam < 100:
        return "PAM normal"
    else:
        return "PAM alta (puede indicar hipertensión)"

def validar_presion(sistolica, diastolica):
    """Valida si la presión arterial está dentro de rangos normales."""
    if sistolica < 90 or diastolica < 60:
        return "Presión arterial baja"
    elif sistolica > 140 or diastolica > 90:
        return "Presión arterial alta"
    else:
        return "Presión arterial normal"

def main():
    """Función principal del programa."""
    try:
        sistolica = float(input("Ingrese la presión sistólica (mmHg): "))
        diastolica = float(input("Ingrese la presión diastólica (mmHg): "))
        pam = calcular_pam(sistolica, diastolica)
        interpretacion = interpretar_pam(pam)
        validacion = validar_presion(sistolica, diastolica)

        print(f"La presión arterial media (PAM) es: {pam:.2f} mmHg")
        print(f"Interpretación de la PAM: {interpretacion}")
        print(f"Validación de la presión arterial: {validacion}")

    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
