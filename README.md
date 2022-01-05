# PyLexis

`PyLexis` is a tool to easily plot Lexis Diagrams within Python. It is based on [`matplotlib`](https://matplotlib.org/) and inspirated in 
[LexisPlotR](https://github.com/ottlngr/LexisPlotR).

### What is a Lexis Diagram?

> In demography a Lexis diagram (named after economist and social scientist Wilhelm Lexis) is a two dimensional diagram that is used to represent events 
(such as births or deaths) that occur to individuals belonging to different cohorts. Calendar time is usually represented on the horizontal axis, while 
age is represented on the vertical axis. (<https://en.wikipedia.org/wiki/Lexis_diagram>)

### Installation

### Using PyLexis

First import the package and create a **Diagram** object with the following arguments:
- initial year
- final year
- first age
- last age

``` py
import pylexis
diagram = pylexis.Diagram(1910, 1920, 0, 10)
```
![](docs/images/basic_grid.png)

Then you have a few methods to interact with the graph:

``` py
Diagram.lexis_fill(target, value, color)
```
        Highlight a certain age, year or cohort in the grid.

        Parameters
        ----------
        target: {'age', 'year' or 'cohort'}
        value : int with the value of the target selected.
        color: str with the colour to fill.

``` py
Diagram.titles(x_label, y_label, title)
```
``` py
Diagram.add_births(year, value)
```
``` py
Diagram.add_deaths(year, value)
```

### FAQ

Just ask me what you need!
