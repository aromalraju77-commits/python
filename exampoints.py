# present value

import numpy_financial as npf
rate = 0.10      # Discount rate per period (10%)
nper = 3         # Number of periods
fv = 1000        # Future Value
pv = npf.pv(rate, nper, pmt=200, fv=fv)  # pmt=0 because no periodic payments

print("Present Value:", round(pv, 2))

'''You are set to receive ₹200 at the end of each year for 5 years,
plus a lump sum of ₹1,000 at the end of year 5. Using a 10% discount rate,
the present value of all these future payments is calculated to be ₹1,592.74.
This means that all the money you will receive in the future is worth ₹1,592.74 in today’s terms,
because money available in the future is worth less than money today due to the time value of money.
In other words, receiving ₹1,592.74 today is equivalent to receiving those future payments over 5 years.'''



#  Future Value

import numpy_financial as npf
rate = 0.08       # annual interest rate
nper = 5          # number of periods
pv = -5000        # present value (investment today, negative for cash outflow)
pmt = -1000       # annual deposit (negative because it's money going out)
when = 'end'      # payments at the end of the period
fv_total = npf.fv(rate, nper, pmt, pv, when)
print("Total Future Value after 5 years:", round(fv_total, 2))

'''
You initially invest ₹5,000 today and then deposit ₹1,000 at the end of each year
for 5 years at an annual interest rate of 8%. After 5 years,
the total future value of your investment is ₹13,212.50. 
This means that the initial ₹5,000 grows to ₹7,346.50 due to compounding,
while the annual ₹1,000 contributions grow to ₹5,866 by the end of the period.
Together, your total contributions of ₹10,000 have increased to ₹13,212.50,
showing how regular investments and compound interest work together to grow your money over time.
'''

# Perpetuity Present Value

C = 1000   # cash flow per period
r = 0.05   # discount rate

PV = C / r
print("Present Value of the perpetuity is:", PV)

'''Receiving **₹1,000 every year forever is worth ₹20,000 today**
because if you invest ₹20,000 at 5% interest, you would earn ₹1,000 every year.
So, getting ₹1,000 every year forever is the same as having ₹20,000 now.
'''


# NPV - Net Present Value 

import numpy_financial as npf

cash_flows = [-10000, 3000, 3500, 4000, 4500]
rate = 0.10   # 10%

npv = npf.npv(rate, cash_flows)
npv
print("Net Present Value (NPV):", round(npv, 2))

'''The project requires an investment of ₹10,000 today and
is expected to generate cash inflows over the next four years.
After discounting these inflows at a 10% required return,
the Net Present Value (NPV) is ₹1,698.65, which is positive. 
This means the project is expected to generate ₹1,698.65 more than its cost in today’s value.
Since the NPV is positive, the project will add value to the company and is considered financially beneficial, 
so the company should accept the project.'''

# IRR - Internal Rate of Return

import numpy_financial as npf

cash_flows = [-12000, 4000, 5000, 6000, 7000]
rate = 0.10
irr = npf.irr(cash_flows)
print("Internal Rate of Return (IRR):", round(irr * 100, 2),"%")

''' The IRR of the project is about ≈ 25%.
This means the project is expected to generate a 25% annual return on the money invested.
Since this return is higher than the company’s required rate of return (10%),
 the project is financially attractive.
Therefore, the company should accept the project because it is
 expected to earn more than the minimum return required.'''


#profitability index

import numpy_financial as npf

cash_flows = [-20000, 7000, 8000, 9000]
rate = 0.10
npv = npf.npv(rate, cash_flows)
pi = (npv + abs(cash_flows[0])) / abs(cash_flows[0])
print("Profitability Index (PI):", round(pi, 2))

''' For this project, the profitability index (PI) is approximately 0.99.
This indicates that for every ₹1 invested, the project is expected to generate
only ₹0.99 in present-value terms. In other words, the present value
of future cash inflows is slightly lower than the initial cost of investment. 
Since the PI is less than 1, the project does not create additional value and 
fails to recover its full cost after accounting for the time value of money.
Therefore, the project is not financially viable, and the company should reject it.'''


#varience and standard deviation

import numpy as np

data = [10, 12, 15, 18, 20]

variance = np.var(data)      # population variance
std_dev = np.std(data)       # population standard deviation

print("Variance:", variance)
print("Standard Deviation:", round(std_dev,2))

'''This data shows that the values are moderately consistent,
with a variance of 13.6 and a standard deviation of 3.69.
In finance terms, if these numbers were asset returns,
the variance tells us the overall spread of returns from the mean,
while the standard deviation shows the typical deviation.
Together, they indicate a moderate level of risk—the returns usually fluctuate about 3–4 units
from the average, so the asset is not highly volatile but not perfectly stable either.'''

#to find the coverance and correlation

import numpy as np

x = [10, 12, 15, 18, 20]
y = [8, 11, 14, 17, 19]

# Covariance
cov_matrix = np.cov(x, y)        # covariance matrix
cov_xy = cov_matrix[0, 1]        # covariance between x and y

# Correlation
corr_matrix = np.corrcoef(x, y)  # correlation matrix
corr_xy = corr_matrix[0, 1]      # correlation coefficient

print("Covariance:", cov_xy)
print("Correlation:", corr_xy)
