[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> 34.27% of US men are in the allowable range for Blue Man Group.

```Python
import scipy
from scipy import stats
height_lower_bound = 177.8
height_upper_bound = 185.42

probability_below_upper_bound = stats.norm.cdf(185.42, loc = 178, scale = 7.7)
probability_below_lower_bound = stats.norm.cdf(177.8, loc = 178, scale = 7.7)

probability_range = probability_below_upper_bound - probability_below_lower_bound
print(probability_range)
```
