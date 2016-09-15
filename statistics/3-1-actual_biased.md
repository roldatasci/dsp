[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> Exercise 3.1

>> Something like the class size paradox appears if you survey children and ask
>> how many children are in their family. Families with many children are more
>> likely to appear in your sample, and families with no children have no chance
>> to be in the sample.

>> Use the NSFG respondent variable NUMKDHH to construct the actual distribution
>> for the number of children under 18 in the household.

```python
# read in the female respondent data
import chap01soln # to use ReadFemResp() function to read the data in
resp = chap01soln.ReadFemResp()

# actual distribution
import thinkstats2 # to use Pmf() function
pmf = thinkstats2.Pmf(resp.numkdhh, label = 'actual')
```

>> Now compute the biased distribution we would see if we surveyed the children
>> and asked them how many children under 18 (including themselves) are in their
>> household.

```python
# Biased PMF (as defined on pg. 34 of Think Stats 2)
# - probability associated with each class size is 'biased' by number of students
# in the class (biased through multiplication)

def BiasPmf(pmf, label):
	# generate copy to leave original intact
	# label here is for 'observed'
	# (i.e. 'biased' or 'as observed by students')
	new_pmf = pmf.Copy(label = label)

	for x, p in pmf.Items():
		new_pmf.Mult(x, x) # multiply prob associated with x by x (pr(x) * x) 

	new_pmf.Normalize()
	return new_pmf # new Pmf object representing the biased distribution

biased_pmf = BiasPmf(pmf, label = 'biased')
```

>> Plot the actual and biased distributions, and compute their means.
>> As a starting place, you can use `chap03ex.ipynb`.

```python
import thinkplot # Think Stats 2 module
thinkplot.PrePlot(2) # to generate 2 different colours
thinkplot.Pmfs([pmf, biased_pmf]) # plot PMF step functions
# modify plot labels and show the plot
thinkplot.Show(xlabel = 'no. of children under 18 in household', ylabel = 'PMF')
```

![actual_bias](https://github.com/roldatasci/dsp/blob/master/statistics/3-1-plot.png)

```python
# means for actual vs biased distributions
print(pmf.Mean()) # mean for actual distribution = 1.02
print(biased_pmf.Mean()) # mean for biased distribution = 2.4
```

>> The plots show that the actual distribution has a much longer right tail, 
>> whilst the biased distribution seems slightly more normal (but still 
>> right-skewed). The computed means of the two distributions show that 
>> the actual distribution has a mean of around 1.02 (children under 18), whilst
>> the biased distribution has a mean of around 2.4, more than double the actual
>> distribution.

>> This is a significant difference, biased towards larger families and their
>> higher tendency to report. Naturally, families with no children do not have
>> any children responding to a survey about the number of children in their
>> household.
