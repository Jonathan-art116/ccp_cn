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

from itertools import combinations
from fastapi import APIRouter
from tools.salary import calculate_salary
from tools.loan import calculate_equal_installment_interest_loan, calculate_equal_installment_principal_loan
from tools.twenty_four import find_24

router = APIRouter(tags=['calc'])


@router.get("/calc/q1/tax/")
def get_net_income(monthly_salary: int):
    social_insurance, housing_fund, medical_insurance, unemployment_insurance, \
    injury_insurance, maternity_insurance, tax, net_income = calculate_salary(monthly_salary)
    result = {"社保": f"{social_insurance:.2f} 元",
              "公积金": f"{housing_fund:.2f} 元",
              "医疗保险": f"{medical_insurance:.2f} 元",
              "失业保险": f"{unemployment_insurance:.2f} 元",
              "工伤保险": f"{injury_insurance:.2f} 元",
              "生育保险": f"{maternity_insurance:.2f} 元",
              "个人所得税": f"{tax:.2f} 元",
              "实际到手收入": f"{net_income:.2f} 元"}
    return {"message": "OK", "code": "200", "data": result}


@router.get("/calc/q2/loan/")
def get_loan(loan_amount: int, annual_interest_rate: float, loan_years: int):
    #  等额本金还款方式
    equal_principal: list = []
    equal_principal_schedule = calculate_equal_installment_principal_loan(loan_amount, annual_interest_rate, loan_years)
    for month, monthly_payment, monthly_interest, remaining_principal in equal_principal_schedule:
        equal_principal.append(
            f"第{month}月，月供：{monthly_payment:.2f}元，利息：{monthly_interest:.2f}元，剩余本金：{remaining_principal:.2f}元")
    # 等额本息还款方式
    equal_installment: list = []
    equal_interest_schedule = calculate_equal_installment_interest_loan(loan_amount, annual_interest_rate, loan_years)
    for month, monthly_payment, monthly_interest, monthly_principal, remaining_principal in equal_interest_schedule:
        equal_installment.append(
            f"第{month}月，月供：{monthly_payment:.2f}元，利息：{monthly_interest:.2f}元，本金：{monthly_principal:.2f}元，剩余本金：{remaining_principal:.2f}元")
    result = {"等额本金还款方式": equal_principal, "等额本息还款方式": equal_installment}
    return {"message": "OK", "code": "200", "data": result}


@router.get("/calc/q3/find_24")
def get_find_24():
    arithmetic_expression: list = []
    numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for number in combinations(numbers, 3):
        result = find_24(list(number))
        if result:
            arithmetic_expression.append(result)
    return {"message": "OK", "code": "200", "data": arithmetic_expression}

