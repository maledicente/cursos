from matplotlib import pyplot as plt

mentions = [500, 505]
years = [2013, 2014]
plt.bar([2012.6, 2013.6], mentions, 0.8)
plt.xticks(years)
plt.ylabel("# de vezes que ouvimos alguém dizer 'data science'")

plt.ticklabel_format(useOffset=False)


plt.axis([2012.5,2014.5,499,506])
plt.title("Olhe o Grande Aumento!")
plt.show()