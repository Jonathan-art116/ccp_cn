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

def calculate_income_tax(taxable_income):
    # 税率表
    tax_rate = [(3000, 0.03), (12000, 0.1), (25000, 0.2), (35000, 0.25), (55000, 0.3), (80000, 0.35),
                (float('inf'), 0.45)]

    # 计算个人所得税
    tax = 0
    for threshold, rate in tax_rate:
        if taxable_income <= 0:
            break
        if taxable_income > threshold:
            tax += (threshold * rate)
            taxable_income -= threshold
        else:
            tax += (taxable_income * rate)
            break

    return tax


def calculate_insurance(gross_salary, social_insurance_rate=0.08, housing_fund_rate=0.07,
                        medical_insurance_rate=0.02, unemployment_insurance_rate=0.005,
                        injury_insurance_rate=0.01, maternity_insurance_rate=0.005):
    # 计算各项保险
    social_insurance = gross_salary * social_insurance_rate
    housing_fund = gross_salary * housing_fund_rate
    medical_insurance = gross_salary * medical_insurance_rate
    unemployment_insurance = gross_salary * unemployment_insurance_rate
    injury_insurance = gross_salary * injury_insurance_rate
    maternity_insurance = gross_salary * maternity_insurance_rate

    return social_insurance, housing_fund, medical_insurance, unemployment_insurance, injury_insurance, maternity_insurance


def calculate_salary(gross_salary):
    # 计算保险
    social_insurance, housing_fund, medical_insurance, unemployment_insurance, injury_insurance, maternity_insurance = \
        calculate_insurance(gross_salary)

    # 计算应纳税所得额
    taxable_income = gross_salary - social_insurance - housing_fund - medical_insurance - unemployment_insurance - 5000

    # 计算个人所得税
    tax = calculate_income_tax(taxable_income)

    # 计算实际到手收入
    net_income = gross_salary - social_insurance - housing_fund - medical_insurance - \
                 unemployment_insurance - injury_insurance - maternity_insurance - tax

    return social_insurance, housing_fund, medical_insurance, unemployment_insurance, \
           injury_insurance, maternity_insurance, tax, net_income

