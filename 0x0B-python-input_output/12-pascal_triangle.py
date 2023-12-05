#!/usr/bin/python3
"""this is methid ti pint out pascal triangle"""


def pascal_triangle(n):
    """print out pascal triangle"""
    if n <= 0:
        return []
    else:
        triangle = []
        for i in range(n):
            if i == 0:
                row = [1]
            else:
                prevrow = triangle[i - 1]
                row = [1]
                for j in range(1, i):
                    row.append(prevrow[j - 1] + prevrow[j])
                row.append(1)
            triangle.append(row)
        return triangle
