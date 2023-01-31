import matplotlib.pyplot as plt

from pylexis.common import check_range_grid

__doc__ = """
PyLexis - A tool to easily plot Lexis Diagrams within Python.
=====================================================================

In demography a Lexis diagram (named after economist and social
scientist Wilhelm Lexis) is a two dimensional diagram that is used to
represent events (such as births or deaths) that occur to individuals
belonging to different cohorts.
"""


__version__ = "0.1.2"


class Diagram():
    """ Basic Lexis Diagram """

    def __init__(self,
                 year_start: int, year_end: int,
                 age_start: int, age_end: int):

        self.fontsize = 12
        self.fontweight = 100

        self.year_start = year_start
        self.year_end = year_end
        self.age_end = age_end
        self.age_start = age_start

        self.fig, self.ax = plt.subplots(figsize=(year_end - year_start,
                                                  age_end - age_start))
        self.ax.set(xlim=(year_start, year_end),
                    xticks=range(year_start, year_end+1),
                    ylim=(age_start, age_end),
                    yticks=range(age_start, age_end+1))

        plt.grid()

        for i in range(year_start - age_end, year_end):
            plt.axline((i, age_start),
                       (i + 1, age_start + 1),
                       linewidth=0.3, color='gray')

        self.titles()

    def titles(self, x_label="Year", y_label="Age", title="Lexis Diagram"):
        """
        Add title and x, y axis labels
        """

        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)

    def __random_color(self):
        from random import randint
        r = lambda: randint(0,255)
        return '#%02X%02X%02X' % (r(),r(),r())

    def lexis_fill(self, target: str, value: int, color: str, alpha: float = 0.5):
        """
        Highlight a certain age, year or cohort in the grid.

        :param target: Set "age", "year" or "cohort".
        :param value: This is the value of the *target* selected.
        :param color: Color to fill.
        """

        if not color or color == 'random':
            color = self.__random_color()

        if target == 'age':
            self.ax.axhspan(value, value + 1, alpha=alpha if alpha else 0.5, color=color)

        if target == 'year':
            self.ax.axvspan(value, value + 1, alpha=alpha if alpha else 0.5, color=color)

        if target == 'cohort':
            _range = self.year_end - value
            self.ax.fill_between((value, self.year_end),
                                 (self.age_start, _range),
                                 (self.age_start - 1, _range - 1),
                                 color=color, alpha=alpha if alpha else 0.2)

    def add_births(self, year: int, value: int):
        """
        Draw number of births in a specific year.

        :param year: Year.
        :param value: Births.
        """

        check_range_grid(self.year_start, self.year_end, year)

        pad = ((9 - len(str(value))) / 9) / 2  # to center up to 9 digits
        plt.text(year + pad, 0, value, fontsize=self.fontsize)

    def add_deaths(self, cohort: int, year: int, age: int, value: int):
        """
        Draw number of deaths in a specific year for a specific cohort.
        If the data is not consistent (for example, year of deaths < cohort
        year), it returns an error.

        :param cohort: Year of the cohort.
        :param year: Year of deaths.
        :param age: Age at the time of deaths. Deaths can be before or after
        birthdays.
        :param value: Deaths.
        """
        check_range_grid(self.year_start, self.year_end, year)

        pad = ((4 - len(str(value))) / 4) / 2
        if (year - cohort) - age == 1:
            plt.text(year + pad,
                     age + 0.5,
                     value,
                     fontsize=self.fontsize)

        elif (year - cohort) - age == 0:
            plt.text(year + 0.5,
                     age + 0.3,
                     value,
                     fontsize=self.fontsize)
        else:
            message = f"""Invalid Data:
            cohort: {cohort}
            year: {year}
            age: {age}"""
            raise ValueError(message)

    def add_data_point(self, year: int, age: int, value: any):
        """
        Add a data point to the Lexis Diagram.

        :param year: Year.
        :param age: Age.
        :param value: Value to be added.
        """

        check_range_grid(self.year_start, self.year_end, year)
        check_range_grid(self.age_start, self.age_end, age)

        plt.text(
            year + 0.5,
            age + 0.5,
            value,
            fontsize=self.fontsize,
            fontweight=self.fontweight
        )

    def add_data(self, year: list[int], age: list[int], values: list[any]):
        """
        Add a list of data points to the Lexis Diagram.

        :param year: List of years.
        :param age: List of ages.
        :param values: List of values to be added.
        """

        for y, a, value in zip(year, age, values):
            self.add_data_point(year=y, age=a, value=value)

    def add_data_unsafe(self, year: list[int], age: list[int], values: list[any]):
        """
        Add a list of data points to the Lexis Diagram. Skips the check for
        the range of the grid.

        :param year: List of years.
        :param age: List of ages.
        :param values: List of values to be added.
        """

        for y, a, value in zip(year, age, values):
            plt.text(
                y + 0.5,
                a + 0.5,
                value,
                fontsize=self.fontsize,
                fontweight=self.fontweight
            )

    def load_data(self, data:list, xaxis: str, yaxis: str, value: str):
        """
        Load data from a list of dictionaries.

        :param data: List of dictionaries.
        :param xaxis: Name of the key for the x-axis.
        :param yaxis: Name of the key for the y-axis.
        """

        for row in data:
            try:
                self.add_data_point(year=int(row[xaxis]), age=int(row[yaxis]), value=row[value])
            except ValueError:
                raise ValueError("Invalid data cannot be casted to int.")

    def set_font(self, size: int = 12, weight: str = 'regular'):
        """
        Set the font size and weight.

        :param size: Font size.
        :param weight: Font weight.
        """

        self.fontsize = size
        self.fontweight = weight

    def set_aspect(self, aspect: float or str = 'auto'):
        """
        Set the aspect ratio of the grid.

        :param aspect: Aspect ratio.
        """
        if aspect == 'auto':
            self.ax.set_aspect(aspect)
        elif aspect == 'equal':
            self.ax.set_aspect(aspect)
        elif aspect == 'square':
            self.set_aspect(1.0)
        elif type(aspect) == float or type(aspect) == int:
            x_range = self.year_end - self.year_start
            y_range = self.age_end - self.age_start
            ratio = x_range / y_range
            self.ax.set_aspect(aspect * ratio)
        else:
            raise ValueError("Invalid aspect ratio.")

    def save(self, name: str):
        """
        Save the Lexis Diagram to a file.

        :param name: Name of the file.
        """

        plt.savefig(name)