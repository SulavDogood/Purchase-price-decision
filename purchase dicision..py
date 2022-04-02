# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 13:49:20 2022

@author: Sulav
"""


import pandas as pd
import numpy as np

# Read in the `clicks.csv` file as `abdata`
abdata = pd.read_csv('clicks.csv')
print(abdata.head())

# Find if one group is more likely to make a purchase than another.
table = pd.crosstab(abdata.group, abdata.is_purchase)
print(table)
# running contingenncy test to find whether being in one group makes purchases significantly more likely.
# Null Hypothesis: Being in a certain group makes purchases more likely.
# Alternative Hypothesis: Being in a certain group doesn't make purchases more likely.
from scipy.stats import chi2_contingency
chi2, pval, dof, expected = chi2_contingency(table)
print(pval)
#since pval is less than the significance threshold of 0.0 so we can say that being in a certain group doesn't make purchases mor likely and reject the null hypothesis.

# number of visitors in a typical week:
num_visits = len(abdata)
print(num_visits)
# num of sales at $0.99 to make $1000 each week:
num_sales_needed_099 = 1000/0.99
# percentage of weekly visitors who need to make a sale to reach sales goal at $0.99.
p_sales_needed_099 = num_sales_needed_099/num_visits
print(p_sales_needed_099)
# num of sales at $1.99 to make $1000 each week:
num_sales_needed_199 = 1000/1.99
# percentage of weekly visitors who need to make a sale to reach sales goal at $1.99.
p_sales_needed_199 = num_sales_needed_199/num_visits
# num of sales at $4.99 to make $1000 each week:
num_sales_needed_499 = 1000/4.99
# percentage of weekly visitors who need to make a sale to reach sales goal at $4.99.
p_sales_needed_499 = num_sales_needed_499/num_visits
# since group A was offered sale at price point at $0.99, we want to test if their purchase is significantly greater than the percentage of sale needed at $0.99 to fulfill the revenue goal of $1000.
samp_size_099 = np.sum(abdata.group == "A")
print(samp_size_099)
sales_099 = np.sum((abdata.group == "A") & (abdata.is_purchase == "Yes"))
print(sales_099)
# since group B was offered sale at price point at $1.99, we want to test if their purchase is significantly greater than the percentage of sale needed at $1.99 to fulfill the revenue goal of $1000.
samp_size_199 = np.sum(abdata.group == "B")
print(samp_size_199)
sales_199 = np.sum((abdata.group == "B") & (abdata.is_purchase == "Yes"))
print(sales_199)

# since group C was offered sale at price point at $4.99, we want to test if their purchase is significantly greater than the percentage of sale needed at $4.99 to fulfill the revenue goal of $1000.
samp_size_499 = np.sum(abdata.group == "C")
print(samp_size_499)
sales_499 = np.sum((abdata.group == "C") & (abdata.is_purchase == "Yes"))
print(sales_499)

# Hypohesis testing:
#Null: The observed purchase is significantly greater than percentage of sales needed at $0.99 at group A.
# Alternative: The observed purchase isn't significantly greater than percentage of sales needed at $0.99 at group A.
from scipy.stats import binom_test
pvalueA = binom_test(sales_099, samp_size_099,p_sales_needed_099)
print(pvalueA)
# since pvalueA is 0.211 which is gretter than significance threshold of 0.05 we accept our alternative hypothesis.

# Hypohesis testing:
#Null: The observed purchase is significantly greater than percentage of sales needed at $1.99 at group B.
# Alternative: The observed purchase isn't significantly greater than percentage of sales needed at $1.99 at group B.

pvalueB = binom_test(sales_199, samp_size_199,p_sales_needed_199)
print(pvalueB)
# since pvalueB is 0.06 which is gretter than significance threshold of 0.05 we accept our alternative hypothesis.

# Hypohesis testing:
#Null: The observed purchase is significantly greater than percentage of sales needed at $4.99 at group C.
# Alternative: The observed purchase isn't significantly greater than percentage of sales needed at $4.99 at group C.

pvalueC = binom_test(sales_499, samp_size_499,p_sales_needed_499)
print(pvalueC)
# since pvalueA is 0.046 which is less than significance threshold of 0.05 we accept our null hypothesis.

# From the p_value tests for all groups at different price range, we found that percentage of sales was significantly higher in group C. Therefore, it would be a good decision to charge a price of $4.99.
