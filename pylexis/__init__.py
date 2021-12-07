import matplotlib.pyplot as plt


class diagram():
    """ Basic Lexis Diagram """

    def __init__(self, year_start, year_end, age_start, age_end):
        self.year_start = year_start
        self.year_end = year_end
        self.age_start = age_start
        self.age_end = age_end

    def titles(self, x_label="Year", y_label="Age", title="Lexis Diagram"):
        self.xlabel = x_label
        self.ylabel = y_label
        self.title = title

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


        plt.show()
