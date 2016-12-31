# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Even though both are a sequence of values, lists are mutable while tuples are immutable.
Since a key in a dictionary must be immutable, tuples can be used as a key.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Sets, like lists are collections, and like all collections it has membership testing and length. The key difference
is sets do not keep a record of the element position or order of insertion. There must also be no duplicate
elements in sets. How a set can be more advantageous than lists is that it support common
set operations in math such as union, intersection and difference.

**list**
```python
>>> a = [3, 2, 1]
>>> a.append(4)
>>> 3 in a
True
>>> print a[4]
4
```
**set**
```python
>>> a = Set([3, 2, 1])
>>> a.add(4)
>>> 3 in a
True
>>> print a
Set([3, 2, 1, 4])
```

In regards to finding an element, sets are a lot faster than lists because it performs
lookup by computing a hash of the element. On the other hand, list's implementation is
usually an array and while it's good to find the element of a certain index, it has to
go through the array to see if the element exists in the list.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

`lambda` is a function without a name. It doesn't require a name because it is usually small, and is just needed where they've been created. It allows functions to be assigned to a variable and be returned from another function. It is used a lot in list comprehension by using filter, map and reduce.

```Python
>>> sorted([1, 2, 3, 4], key=lambda x: math.pow((2 - x), 2))
[2, 1, 3, 4]
```
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

List comprehension is an alternative way to filter, map and reduce lists. It can completely substitute those functions and syntax is preferable to some people.

```python
# filter
>>> l1 = [1, 2, 3, 4]
>>> l1_even = [x for x in l1 if x % 2 == 0]
>>> l1
[2, 4]
# map
>>> l2 = ['cat', 'dog', 'fish']
>>> l2_capitalized = [x.capitalize() for x in l2]
>>> l2_capitalized
['Cat', 'Dog', 'Fish']
# set comprehensions
>>> a = set(['ab', 'ac', 'bc'])
>>> b = {x for x in a if 'a' in x}
{'ac', 'ab'}
# dict comprehension
>>> d = {'one' : 'uno', 'two' : 'dos', 'three' : 'tres'}
>>> {v:k for k,v in d.items()}
{'dos': 'two', 'uno': 'one', 'tres': 'three'}

```
From the examples above, we can see that set comprehension is similar with list comprehension using curly braces instead of square brackets.

Similarly, make the dictionary iterable and map two values, the key and value, for dictionary comprehension.

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

7850

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
