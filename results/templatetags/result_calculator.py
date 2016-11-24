from django import template

register = template.Library()

@register.filter(name='grade')
def grade_calculator(marks):
    if marks >=80:
        grade = 'A+'
    elif marks >= 75 <= 79:
        grade = 'A'
    elif marks >= 70 <= 74:
        grade = 'A-'
    elif marks >= 65 <= 69:
        grade = 'B+'
    elif marks >= 60 <= 64:
        grade = 'B'
    elif marks >= 55 <= 59:
        grade = 'B-'
    elif marks >= 50 <= 54:
        grade = 'C+'
    elif marks >= 45 <= 49:
        grade = 'C'
    elif marks >= 40 <= 44:
        grade = 'D'
    elif marks <= 39:
        grade = 'F'
    return grade


@register.filter(name='gpa')
def gpa_calculator(marks):
    if marks >=80:
        gpa = 4
    elif marks >= 75 <= 79:
        gpa = 3.75
    elif marks >= 70 <= 74:
        gpa = 3.50
    elif marks >= 65 <= 69:
        gpa = 3.25
    elif marks >= 60 <= 64:
        gpa = 3.00
    elif marks >= 55 <= 59:
        gpa = 2.75
    elif marks >= 50 <= 54:
        gpa = 2.50
    elif marks >= 45 <= 49:
        gpa = 2.25
    elif marks >= 40 <= 44:
        gpa = 2.00
    elif marks <= 39:
        gpa = 0.00
    return gpa
