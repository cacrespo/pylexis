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

    def lexis_fill(self, target: str, value: int, color: str):
        """
        Highlight a certain age, year or cohort in the grid.

        :param target: Set "age", "year" or "cohort".
        :param value: This is the value of the *target* selected.
        :param color: Color to fill.
        """

        if target == 'age':
            self.ax.axhspan(value, value + 1, alpha=0.5, color=color)

        if target == 'year':
            self.ax.axvspan(value, value + 1, alpha=0.5, color=color)

        if target == 'cohort':
            _range = self.year_end - value
            self.ax.fill_between((value, self.year_end),
                                 (self.age_start, _range),
                                 (self.age_start - 1, _range - 1),
                                 color=color, alpha=0.2)

    def add_births(self, year: int, value: int):
        """
        Draw number of births in a specific year.

        :param year: Year.
        :param value: Births.
        """

        check_range_grid(self.year_start, self.year_end, year)

        pad = ((9 - len(str(value))) / 9) / 2  # to center up to 9 digits
        plt.text(year + pad, 0, value)

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
                     fontsize=12)

        elif (year - cohort) - age == 0:
            plt.text(year + 0.5,
                     age + 0.3,
                     value,
                     fontsize=12)
        else:
            message = f"""Invalid Data:
            cohort: {cohort}
            year: {year}
            age: {age}"""
            raise ValueError(message)

    # def load_data(self, data:list):
