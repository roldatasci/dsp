# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> **Similarities:** both lists and tuples are **ordered** collections of elements, both are **iterable** (can operate on each of its elements), and both can contain **elements of different types** (i.e. their elements can be a mixture of str, int, float, etc.).

>> **Differences:** the most significant difference between lists and tuples is that **lists are mutable** (meaning they can be changed, added to, etc.), whilst **tuples are IMmutable** (they CANNOT be changed).

>> Because tuples are immutable, they are better as keys to a dictionary, because you don't want the key to be changed (otherwise, you can't find values that were previously associated with a key that has been changed).

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> **Similarities:** both lists and sets are **iterable**, **mutable**, and can contain **elements of different types**.

>> **Differences:** lists are **ordered**, whilst sets are **UNordered**. As well, sets contain only _unique_ elements, whilst lists can contain the same element/value multiple times.

>> The uniqueness of elements in sets makes it perform better for finding an element (i.e. checking membership) because it behaves like a dictionary in terms of lookups (it doesn't traverse every single element like a list does), and is sometimes described as a dictionary with only keys (no corresponding values). However, if the operation requires iteration, anyway, lists are probably better by design.

>> As an example, suppose we have two lists and we are trying to determine whether one list is contained in the other (i.e. one is a _subset_ of the other). Since set operations in python are designed to work like mathematical set operations, it would be faster to use sets in this problem.

>> ```python
>> a = [1,2,2,3,4,5,6,7,4,5,6,7,3,4,5,6]
>> b = [1,2,3,5]
>> 
>> # solution using lists
>> counter = 0
>> for elem in b:
>>     if elem in a:
>>         counter += 1
>> print(counter == len(b)) # True
>> 
>> # solution using sets
>> set(b).issubset(a) # True
>> ```

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `lambda` functions are essentially temporary functions. It is generally used for situations where a larger operation requires smaller operations that would otherwise require defining yet another function that won't necessarily be used again (thus taking up memory). In this case, it would be better to use a temporary `lambda` function.

>> Suppose

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





