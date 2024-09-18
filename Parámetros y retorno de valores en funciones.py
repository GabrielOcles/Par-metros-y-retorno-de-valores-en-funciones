# Definir la función que calcula el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento basado en el monto total y el porcentaje de descuento.
    :param monto_total: float - Monto total de la compra
    :param porcentaje_descuento: float - Porcentaje de descuento (por defecto es 10)
    :return: float - Monto del descuento
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Ejecutar el programa con valores definidos
if __name__ == "__main__":
    # Valores predeterminados
    monto_total_1 = 1500  # Monto total para la primera compra
    porcentaje_descuento_1 = 10  # Descuento del 10% por defecto

    monto_total_2 = 2500  # Monto total para la segunda compra
    porcentaje_descuento_2 = 20  # Descuento del 20%

    # Primera llamada con descuento predeterminado (10%)
    descuento_1 = calcular_descuento(monto_total_1, porcentaje_descuento_1)
    monto_final_1 = monto_total_1 - descuento_1
    print(f"Play Station 5 - Monto total: ${monto_total_1}, Descuento: ${descuento_1}, Monto final: ${monto_final_1}")

    # Segunda llamada con descuento del 20%
    descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
    monto_final_2 = monto_total_2 - descuento_2
    print(f"TV Grande - Monto total: ${monto_total_2}, Descuento: ${descuento_2}, Monto final: ${monto_final_2}")