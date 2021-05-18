"""Hacer un algoritmo que calcule el total a pagar por la compra de camisas. Si se compran
tres camisas o más se aplica un descuento del 20% sobre el total de la compra y si son
menos de tres camisas un descuento del 10%"""
def camisa():
    cantidadCamisa=int(input("Digite la cantidad de camisas que desea comprar: "))
    valorCamisa=int(input("Digite el valor de la camisa: "))
    if cantidadCamisa >= 3:
        total=valorCamisa*cantidadCamisa
        totalDescuento=total-(total*0.2)
        print(f"El valor total a pagar es de {totalDescuento}")
    else:
        total=valorCamisa*cantidadCamisa
        totalDescuento=total-(total*0.1)
        print(f"El valor total a pagar es de {totalDescuento}")

print(camisa())