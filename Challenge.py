import pandas as pd
import matplotlib.pyplot as plt
data_loans = pd.read_csv('data.csv')
purposes = data_loans.groupby('purpose')
avg_interest = purposes['int_rate'].mean()
avg_interest2 = avg_interest.to_frame()
avg_interest2.columns = ['avg_interest_rate']
avg_interest2.reset_index(inplace=True)
print(avg_interest2.head())
avg_interest2.to_csv('result.csv', header = True, index=False)
ax = avg_interest2.plot.bar(x = 'purpose',y = 'avg_interest_rate')
ax.set_xlabel('purpose')
ax.set_ylabel('avg_interest_rate')
ax.get_legend().remove()
plt.savefig('chart.png',bbox_inches = 'tight')
plt.tight_layout()
plt.show()
