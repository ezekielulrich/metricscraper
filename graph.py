import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def graph():
    df = pd.read_csv('metrics.csv')
    print(df.head())

    # by default, outliers are not included. This helps pretty the plot
    sns.boxplot(x=df['Affiliation'], y=df['H-index'], showfliers=False) 
    plt.xlabel('University')
    plt.ylabel('H-Index')
    plt.title('H-Index Distribution by University')
    plt.xticks(rotation=45)
    plt.savefig('H-Index Distribution by University.png')
    plt.show()

if __name__ == "__main__":
    graph()