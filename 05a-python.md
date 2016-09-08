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

>> `lambda` functions are essentially temporary functions. It is generally used for situations where an operation requires another intermediate operation that would normally require defining an additional function that won't necessarily be used again (thus taking up memory). In this case, it would be better to use a temporary `lambda` function.

>> Below are some examples of using lambda in conjunction with built-in functions:

>> ```python
>> # 1) using lambda with sorted
>> 
>> # example: sort list by order of each element's last letter
>> peanuts = ['snoopy', 'woodstock', 'charlie']
>> print sorted(peanuts, key = lambda name: name[-1]) # ['charlie', 'woodstock', 'snoopy']
>> 
>> # 2) using lambda with filter
>> 
>> # example: use filter to subset words that are palindromes
>> word_list = ['noon', 'morn', 'civic', 'center', 'radar', 'racecar']
>> filter(lambda word: word == word[::-1], word_list) # python 2
>> list(filter(lambda word: word == word[::-1], word_list)) # must convert to list in python 3
>> 
>> # example: use filter to subset even numbers
>> num_range = range(1, 11) # list(range(1, 11)) in python 3
>> print(num_range) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>> odds = filter(lambda num: num % 2 != 0, num_range)
>> # odds = list(filter(lambda num: num % 2 != 0, num_range)) # python 3
>> print(odds) # [1, 3, 5, 7, 9]
>> 
>> # 3) using lambda with map
>>
>> # example: return a list of ending letters
>> peanuts = ['snoopy', 'woodstock', 'charlie']
>> ends = map(lambda name: name[-1], peanuts)
>> # ends = list(map(lambda name: name[-1], peanuts)) # python 3
>> print(ends) # ['y', 'k', 'e']
>> ```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a more concise way of constructing lists based on conditions, compared to using a for loop. List comprehensions can do the same things that map and filter can do, without having to use lambda functions.

>> Below is a comparison of list comprehensions vs. map and filter for the same examples above.

>> ```python 
>> # using list comprehension (vs. filter) to subset even numbers
>> num_range = list(range(1, 11))
>> odds = [num for num in num_range if num % 2 != 0]
>> print(odds) # [1, 3, 5, 7, 9]
>>
>> # using list comprehension (vs. map) to return a list of ending letters
>> peanuts = ['snoopy', 'woodstock', 'charlie']
>> ends = [name[-1] for name in peanuts]
>> print(ends) # ['y', 'k', 'e']
>> ```

>> Below is an example of set comprehension. It's just like a list comprehension, except that it uses {}.

>> ```python
>> # construct a set of odd numbers from num_range
>> num_range = list(range(1, 11))
>> oddset = {num for num in num_range if num % 2 != 0}
>> print(oddset) # {1, 3, 5, 9, 7}
>> ```

>> Below are some examples of dictionary comprehension. It also uses {}, but uses pairs.
>>
>> ```python
>> # construct a dictionary from two lists
>> car_model = ['model x', 'model s']
>> low_price = [75200, 67200]
>> price_table = {car:price for (car, price) in zip(car_model, low_price)}
>> print(price_table) # {'model x': 75200, 'model s': 67200}
>> 
>> # construct a dictionary of integers as keys and their squares as values
>> num_range = list(range(1,11))
>> square_table = {num:num**2 for num in num_range}
>> print(square_table) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
>> ```

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> There are 937 days between `01-02-2013` and `07-28-2015`.

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> There are 513 days between `12312013` and `05282015`.

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> There are 7850 days between `15-Jan-1994` and `14-Jul-2015`. 

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

