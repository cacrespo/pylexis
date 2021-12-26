import matplotlib.pyplot as plt


class diagram():
    """ Basic Lexis Diagram """

    def __init__(self, year_start: int, year_end: int, age_start: int, age_end: int):

        self.year_end = year_end
        self.age_start = age_start

        self.fig, self.ax = plt.subplots()
        self.ax.set(xlim=(year_start, year_end), xticks=range(year_start, year_end+1),
                    ylim=(age_start, age_end), yticks=range(age_start, age_end+1))

        # grid
        plt.grid()

        for i in range(year_start, year_end):
            plt.axline( (i, age_start), (i + 1, age_start + 1), linewidth=0.3, color='gray')
            plt.axline( (year_start, i - year_start), (year_start + 1, i - year_start + 1), linewidth=0.3, color='gray')

        self.titles()

    def titles(self, x_label="Year", y_label="Age", title="Lexis Diagram"):
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)

    def lexis_fill(self, target:str, value:int, color:str):
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

    # def load_data(self, data:list):
        # pass #TODO
