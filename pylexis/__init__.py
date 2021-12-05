import matplotlib.pyplot as plt


def create(year_start, year_end, age_start, age_end):
    """ Plot a basic Lexis Diagram """

    # plot
    fig, ax = plt.subplots()

    plt.xlabel("Year")
    plt.ylabel("Age")
    plt.title("Lexis Diagram")

    ax.set(xlim=(year_start, year_end), xticks=range(year_start, year_end+1),
    ylim=(age_start, age_end), yticks=range(age_start, age_end+1))

    # grid
    plt.grid()

    for i in range(year_start, year_end):
        plt.axline( (i, age_start), (i + 1  , age_start + 1 ), linewidth=0.3, color='gray')
        plt.axline( (year_start, i - year_start), (year_start + 1, i - year_start + 1), linewidth=0.3, color='gray')


    plt.show()
