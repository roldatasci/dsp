[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> In the BRFSS (see Section 5.4), the distribution of heights is roughly normal,
>> with parameters mu = 178 (cm) and sigma = 7.7 (cm) for men, and
>> mu = 163 (cm) and sigma = 7.3 (cm) for women.

>> In order to join the Blue Man Group, you have to be male between 5'10' and 6'1"
>> (see http://bluemancasting.com). What percentage of the U.S. male population
>> is in this range?

>> Hint: use scipy.stats.norm.cdf.

```python

# convert height range to inches, then to cm (1 in = 2.54 cm)
lo_cm = ((5 * 12) + 10) * 2.54
hi_cm = ((6 * 12) + 1) * 2.54
print(lo_cm, hi_cm) # (177.8, 185.42)
 
from scipy.stats import norm
mu, sigma = 178, 7.7
cdf_lo_cm = norm.cdf(lo_cm, loc = mu, scale = sigma)
cdf_hi_cm = norm.cdf(hi_cm, loc = mu, scale = sigma)
print(cdf_lo_cm) # 0.489639027865
print(cdf_hi_cm) # 0.832385865496
print(cdf_hi_cm - cdf_lo_cm) # 0.342746837631
```

>> With the assumption that heights are normally distributed for men in the U.S.,
>> with mu = 178 (cm) and sigma = 7.7 (cm), about 34% of the U.S. male population
>> have heights in the range of 5'10" and 6'1".
