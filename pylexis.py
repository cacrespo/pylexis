import matplotlib.pyplot as plt


def pylexis(year_start, year_end, age_start, age_end):
       
       # plot
       fig, ax = plt.subplots()

       plt.xlabel("Year")
       plt.ylabel("Age")
       plt.title("Lexis Diagram")

       ax.set(xlim=(year_start, year_end), xticks=range(year_start, year_end+1),
              ylim=(age_start, age_end), yticks=range(age_start, age_end+1))

       plt.show()