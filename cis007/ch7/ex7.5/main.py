# Ch5 ex 7.5
# main function
# Macky Ruiz
# CIS 007

from RegularPolygon import RegularPolygon

def main():
    polygon1 = RegularPolygon()
    polygon2 = RegularPolygon(6, 4)
    polygon3 = RegularPolygon(10, 4, 5.6, 7.8)

    print("Polygon1's Perimeter is: ", format(polygon1.getPerimeter(), ".2f"), " and Area is ", format(polygon1.getArea(), ".2f"))
    print("Polygon2's Perimeter is: ", format(polygon2.getPerimeter(), ".2f"), " and Area is ", format(polygon2.getArea(), ".2f"))
    print("Polygon3's Perimeter is: ", format(polygon3.getPerimeter(), ".2f"), " and Area is ", format(polygon3.getArea(), ".2f"))

main()
