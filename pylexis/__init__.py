import matplotlib.pyplot as plt


class diagram():
    """ Basic Lexis Diagram """

#TODO inicalizar con el gráfico base y que cada función añada lo necesario. plot que simplemente muestre.
    def __init__(self, year_start: int, year_end: int, age_start: int, age_end: int):
        self.year_start = year_start
        self.year_end = year_end
        self.age_start = age_start
        self.age_end = age_end

        self.titles()

    def titles(self, x_label="Year", y_label="Age", title="Lexis Diagram"):
        self.xlabel = x_label
        self.ylabel = y_label
        self.title = title

    def lexis_age(self, age:int, colour:str):
        """ Highlight a certain age in the grid """
        self.fill_age = age
        self.colour_a = colour

    def lexis_year(self, year:int, colour:str):
        """ Highlight a certain year in the grid """
        self.fill_year = year
        self.colour_y = colour

    def lexis_cohort(self, cohort:int, colour:str):
        """ Highlight a certain cohort in the grid """
        self.fill_cohort = cohort
        self.colour_c =  colour

    def load_data(self, data:list):
        pass #TODO

    def plot(self):
        fig, ax = plt.subplots()

        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)

        ax.set(xlim=(self.year_start, self.year_end), xticks=range(self.year_start, self.year_end+1),
        ylim=(self.age_start, self.age_end), yticks=range(self.age_start, self.age_end+1))

        # grid
        plt.grid()

        for i in range(self.year_start, self.year_end):
            plt.axline( (i, self.age_start), (i + 1  , self.age_start + 1 ), linewidth=0.3, color='gray')
            plt.axline( (self.year_start, i - self.year_start), (self.year_start + 1, i - self.year_start + 1), linewidth=0.3, color='gray')

        # fill age, year, cohort
        ax.axhspan(self.fill_age, self.fill_age + 1, alpha=0.5, color=self.colour_a)
        ax.axvspan(self.fill_year, self.fill_year + 1, alpha=0.5, color=self.colour_y)

        _range = self.year_end - self.fill_cohort
        ax.fill_between((self.fill_cohort, self.year_end),
                        (self.age_start, _range),
                        (self.age_start - 1, _range - 1),
                        color=self.colour_c, alpha=0.2)


        plt.show()
