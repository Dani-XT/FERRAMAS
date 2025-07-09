from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

# Funciones
# -------------------------------------------------------
# TODO: Calculos subsidios
# -------------------------------------------------------
def calcular_percentil(ingreso, personas, arriendo):
    ingreso_ajustado = Decimal((ingreso - arriendo)/personas)
    subsidios = []
    rango = [
        {"max": 69518, "percentil": 10},
        {"max": 109984, "percentil": 20},
        {"max": 145631, "percentil": 30},
        {"max": 181532, "percentil": 40},
        {"max": 221249, "percentil": 50},
        {"max": 278403, "percentil": 60},
        {"max": 353729, "percentil": 70},
        {"max": 476523, "percentil": 80},
        {"max": 774525, "percentil": 90},
        {"max": float('inf'), "percentil": 100},
    ]

    for r in rango:
        if ingreso_ajustado < r["max"]:
            percentil = r["percentil"]

    if percentil <= 40:
        subsidios.append({
            "nombre": "Subsidio DS49",
            "descripcion": "Para el 40% más vulnerable.",
            "link": "../pages/percentile/ds49.html"
        })

    if percentil <= 60:
        subsidios.append({
            "nombre": "Subsidio DS1 Tramo 1",
            "descripcion": "Compra de viviendas hasta 1.100 UF (hasta 60% de vulnerabilidad).",
            "link": "../pages/percentile/ds1t1.html"
        })

    if percentil <= 70:
        subsidios.append({
            "nombre": "Subsidio DS1 Tramo 2",
            "descripcion": "Compra de viviendas hasta 1.600 UF (hasta 70% de vulnerabilidad).",
            "link": "../pages/percentile/ds1t2.html"
        })

    if percentil <= 100:
        subsidios.append({
            "nombre": "Subsidio DS1 Tramo 3",
            "descripcion": "Compra de viviendas hasta 2.200 UF (solo requiere RHS).",
            "link": "../pages/percentile/ds1t3.html"
        })

    return {
        "ingreso_ajustado": Decimal(ingreso_ajustado),
        "percentil": percentil,
        "subsidios": subsidios
    }
    