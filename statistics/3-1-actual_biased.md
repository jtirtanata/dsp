[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> Mean of actual pmf: 1.825644949715785  
Mean of biased pmf: 2.418477935452966
**Plot of Actual vs Biased PMF**
![Actual vs. Biased](actualvsbias.png)
The mean of a biased pmf is higher because there are more children who are in bigger families. Therefore if one were to survey a group of children and ask how many children are in their family, you would get this biased pmf because the distribution is observed by the children, and there are more children in a larger family because larger families have more children.  

Python code:

```python
import nsfg
import pandas
import thinkplot
import thinkstats2

def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
    new_pmf.Normalize()
    return new_pmf

df = nsfg.ReadFemPreg()
df = pandas.DataFrame(df)
pmf = thinkstats2.Pmf(df['birthord'])
biased_pmf = BiasPmf(pmf, label='biased pmf')
actual_pmf = pmf.Copy(label='actual pmf')
thinkplot.PrePlot(2)
thinkplot.Pmfs([actual_pmf, biased_pmf])
thinkplot.Show(xlabel='number of children', ylabel='PMF')
```
