[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> Using the variable `totalwgt_lb`, investigate whether first babies are lighter
>> or heavier than others. Compute Cohen's d to quantify the difference between
>> the groups. How does it compare to the difference in pregnancy weight?

```python
import math
import nsfg # make sure to run nsfg.py so that data is clean

preg = nsfg.ReadFemPreg() # read in full df
# create a smaller df by subsetting observations for which 'outcomes' = 1
# preg.outcomes == 1 is a boolean Series used for masking
live = preg[preg.outcome == 1] # smaller df restricted to live birth observations

# split df 'live' into df for first babies ('firsts') and for 'others'
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

# define function for Cohen's d

def CohenEffectSize(group1, group2):
	'''
	inputs: single variable for group1 and group2
	output: Cohen's d = ratio of between group difference to
	within-group variability (pooled standard deviation)
	interpretation: d is the difference in means (in standard deviations)'''
	diff = group1.mean() - group2.mean()
	var1, var2 = group1.var(), group2.var()
	n1, n2 = len(group1), len(group2)
	pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
	d = diff / math.sqrt(pooled_var)
	return d

# isolate the variables 'totalwgt_lb' and 'prglngth' from each df
# and pass it to the function below
if __name__ == '__main__':
	print(CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)) # -0.089
	print(CohenEffectSize(firsts.prglngth, others.prglngth)) # 0.029
```

>> Interpretation:

>> The Cohen's d computed (-0.089) for total weight in lbs shows that first babies 
>> tend to weight LESS than other babies. However, the effect size, while larger
>> than that for pregnancy length, is essentially negligible.

>> The author (Downey) interprets the 'd' value as the difference in means
>> in standard deviations. In this case, we would say that the difference
>> in means for total weights between first babies and other babies is only 0.089
>> standard deviations.

>> In comparison, the difference in means for pregnancy length between first babies
>> and other babies is even smaller, at only 0.029 standard deviations.   
