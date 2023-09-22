import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('metrics.csv')
print(df.head())

# Box plot
sns.boxplot(x=df['Affiliation'], y=df['H-index'])
plt.xlabel('University')
plt.ylabel('H-Index')
plt.title('H-Index Distribution by University')
plt.xticks(rotation=45)
plt.show()
