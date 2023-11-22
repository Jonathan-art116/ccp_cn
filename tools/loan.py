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


import math


def calculate_equal_installment_principal_loan(principal, annual_interest_rate, years):
    # 等额本金计算方式
    monthly_interest_rate = annual_interest_rate / 12 / 100
    total_payments = years * 12
    monthly_principal = principal / total_payments

    monthly_payment_schedule = []
    remaining_principal = principal

    for month in range(1, total_payments + 1):
        monthly_interest = remaining_principal * monthly_interest_rate
        monthly_payment = monthly_principal + monthly_interest
        remaining_principal -= monthly_principal
        monthly_payment_schedule.append((month, monthly_payment, monthly_interest, remaining_principal))

    return monthly_payment_schedule


def calculate_equal_installment_interest_loan(principal, annual_interest_rate, years):
    # 等额本息计算方式
    monthly_interest_rate = annual_interest_rate / 12 / 100
    total_payments = years * 12

    monthly_payment = (principal * monthly_interest_rate * math.pow(1 + monthly_interest_rate, total_payments)) / \
                      (math.pow(1 + monthly_interest_rate, total_payments) - 1)

    monthly_payment_schedule = []
    remaining_principal = principal

    for month in range(1, total_payments + 1):
        monthly_interest = remaining_principal * monthly_interest_rate
        monthly_principal = monthly_payment - monthly_interest
        remaining_principal -= monthly_principal
        monthly_payment_schedule.append(
            (month, monthly_payment, monthly_interest, monthly_principal, remaining_principal))

    return monthly_payment_schedule
