import matplotlib.pyplot as plt
import matplotlib as mpl

# from pylexis.common import check_range_grid
from common import check_range_grid

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
            self.ax.axhspan(value, value + 1, alpha=alpha, color=color)

        if target == 'year':
            self.ax.axvspan(value, value + 1, alpha=alpha, color=color)

        if target == 'cohort':
            _range = self.year_end - value
            self.ax.fill_between((value, self.year_end),
                                 (self.age_start, _range),
                                 (self.age_start - 1, _range - 1),
                                 color=color, alpha=alpha)

    def add_births(self, year: int, value: int):
        """
        Draw number of births in a specific year.

        :param year: Year.
        :param value: Births.
        """

        check_range_grid(self.year_start, self.year_end, year)

        pad = ((9 - len(str(value))) / 9) / 2  # to center up to 9 digits
        plt.text(year + pad, 0, value, fontsize=self.fontsize)

    def __plot_by_coords(
        self,
        year: int,
        age: int,
        value: int,
        safe: bool = True,
        pad_year: str or float or function = "default",
        pad_age: str or float or function = "default"
    ):
        """
        Private method to plot a data point in the grid.

        :param year: Year.
        :param age: Age.
        :param value: Value to be added.
        :param safe: Check if the coordinates are within the grid.
        :param padding: Padding to center the value in the grid: "default" or float or some function on string.
        :param pad_age: Padding to center the value in the grid: "default" or float or some function on string.
        """

        # Check coordinates
        if safe:
            check_range_grid(self.year_start, self.year_end, year)
            check_range_grid(self.age_start, self.age_end, age)

        # Calculate padding
        # This equation is based on the number of digits in the value
        # and the font size to center the value in the grid.
        if pad_year == "default":
            xpad = (((4 - len(str(value))) / 4) / 2) * (self.fontsize / 12)
        elif callable(pad_year):
            xpad = pad_year(value)
        else:
            xpad = pad_year

        if pad_age == "default":
            ypad = 0.5
        elif callable(pad_age):
            ypad = pad_age(value)
        else:
            ypad = pad_age

        # Plot the value
        plt.text(
            year + xpad,
            age + ypad,
            value,
            fontsize=self.fontsize,
            fontweight=self.fontweight
        )

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

        if (year - cohort) - age == 1:
            self.__plot_by_coords(
                year,
                age,
                value,
                pad_year="default",
                pad_age=0.5
            )
        elif (year - cohort) - age == 0:
            self.__plot_by_coords(
                year,
                age,
                value,
                pad_year=0.5,
                pad_age=0.3
            )
        else:
            message = f"""Invalid Data:
            cohort: {cohort}
            year: {year}
            age: {age}"""
            raise ValueError(message)

    def add_text(self, year: int, age: int, value: any):
        """
        Add a text data point to the Lexis Diagram.

        :param year: Year.
        :param age: Age.
        :param value: Value to be added.
        """

        self.__plot_by_coords(year, age, value, pad_year=0.5, pad_age=0.5)

    def add_data(self, year: list[int], age: list[int], values: list[any]):
        """
        Add a list of data points to the Lexis Diagram.

        :param year: List of years.
        :param age: List of ages.
        :param values: List of values to be added.
        """

        for y, a, value in zip(year, age, values):
            self.__plot_by_coords(y, a, value, pad_year=0.5, pad_age="default")

    def add_data_unsafe(self, year: list[int], age: list[int], values: list[any]):
        """
        Add a list of data points to the Lexis Diagram. Skips the check for
        the range of the grid.

        :param year: List of years.
        :param age: List of ages.
        :param values: List of values to be added.
        """

        for y, a, value in zip(year, age, values):
            self.add_text(y, a, value)

    def load_data(self, data:list, xaxis: str, yaxis: str, value: str):
        """
        Load data from a list of dictionaries.

        :param data: List of dictionaries.
        :param xaxis: Name of the key for the x-axis.
        :param yaxis: Name of the key for the y-axis.
        """

        for row in data:
            try:
                self.add_text(year=int(row[xaxis]), age=int(row[yaxis]), value=row[value])
            except ValueError:
                raise ValueError("Invalid data cannot be casted to int.")

    def set_font(self, size: int = 12, weight: str = 'regular', update_axis: bool = True):
        """
        Set the font size and weight.
        Use this to update the font size before plotting.

        :param size: Font size in points (default 12, range[1-1000])
        :param weight: Font weight (default regular, options: regular, bold, heavy, light, book, medium)
        """

        # Gaurds
        if size < 1 or size > 1000:
            raise ValueError("Font size must be between 1 and 1000.")
        elif weight not in ['regular', 'bold', 'heavy', 'light', 'book', 'medium']:
            raise ValueError("Font weight must be one of the following: regular, bold, heavy, light, book, medium.")

        # Update value
        self.fontsize = size
        self.fontweight = weight

        # Axes font
        if update_axis:
            self.ax.tick_params(labelsize=self.fontsize)

    def set_font_retroactively(self, size: int = 12, weight: str = 'regular'):
        """
        Set the font to a retroactively.
        Use this to update the font size after plotting and standardize the graph.

        :param size: Font size in points (default 12, range[1-1000])
        :param weight: Font weight (default regular, options: regular, bold, heavy, light, book, medium)
        """

        # Throwable
        self.set_font(size, weight)

        # Update the text already rendered on the plot
        for text in self.ax.texts:
            text.set_fontsize(self.fontsize)
            text.set_fontweight(self.fontweight)

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

    def save_image(self, name: str):
        """
        Save the Lexis Diagram as an Image file.

        :param name: Name of the file.
        """

        plt.savefig(name)