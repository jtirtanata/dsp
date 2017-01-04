[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> The effect size is: -0.0887 lb(3 s.f)  
This means the mean difference between first babies and non-first babies is
very small. First babies are not heavier, but there's not enough proof that it is

```python
import nsfg
import math
import numpy as np

def calculateCohenD(group1, group2):
    group1_mean = group1.totalwgt_lb.mean()
    group1_var = group1.totalwgt_lb.var()
    group2_mean = group2.totalwgt_lb.mean()
    group2_var = group2.totalwgt_lb.var()

    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * group1_var + n2 * group2_var) / (n1 + n2)
    diff = group1_mean - group2_mean
    d = diff / math.sqrt(pooled_var)
    return d


df = nsfg.ReadFemPreg()
nsfg.CleanFemPreg(df)

live = df[df.outcome == 1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

print("The Cohen's d is: {}".format(calculateCohenD(firsts, others)))
```
