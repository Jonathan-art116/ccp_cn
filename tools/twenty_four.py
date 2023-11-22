# This program is free software: 
# you can redistribute it and/or modify it under the terms of the GNU General Public License as published 
# by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with this program. 
# If not, see <https://www.gnu.org/licenses/>.
from itertools import permutations


def evaluate_expression(a: int, b: int, operator: str):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b


def find_24(numbers: list):
    operators: list = ['+', '-', '*', '/']
    for perm in permutations(numbers):
        for op1 in operators:
            for op2 in operators:
                expr1 = f"({perm[0]} {op1} {perm[1]}) {op2} {perm[2]}"
                expr2 = f"{perm[0]} {op1} ({perm[1]} {op2} {perm[2]})"
                expr3 = f"({perm[0]} {op1} {perm[1]}) {op2} ({perm[2]})"
                expr4 = f"{perm[0]} {op1} ({perm[1]} {op2} {perm[2]})"
                expr5 = f"({perm[1]} {op1} {perm[2]}) {op2} {perm[0]}"
                expr6 = f"{perm[1]} {op1} ({perm[2]} {op2} {perm[0]})"
                expr7 = f"({perm[1]} {op1} {perm[2]}) {op2} ({perm[0]})"
                expr8 = f"{perm[1]} {op1} ({perm[2]} {op2} {perm[0]})"

                expressions = [expr1, expr2, expr3, expr4, expr5, expr6, expr7, expr8]

                for expr in expressions:
                    try:
                        if abs(eval(expr) - 24) < 1e-6:
                            return f"表达式：{expr}"
                    except ZeroDivisionError:
                        pass

