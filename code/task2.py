#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def circle(radius):
    return math.pi * radius**2

def cylinder():
    radius = float(input("Введите радиус цилиндра: "))
    height = float(input("Введите высоту цилиндра: "))

    choice = input("Хотите ли вы получить только площадь боковой поверхности цилиндра? (да/нет): ")

    lateral_area = 2 * math.pi * radius * height

    if choice.lower() == 'да':
        print(f"Площадь боковой поверхности цилиндра: {lateral_area}")
    else:
        full_area = lateral_area + 2 * circle(radius)
        print(f"Полная площадь цилиндра: {full_area}")

if __name__ == '__main__':
    cylinder()
