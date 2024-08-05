import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import tree
import pandas as pd

def loanStatus_barchart(data_path):
    df = pd.read_csv(data_path)
    df['Loan_Status'].value_counts().plot.bar()
    plt.title('Loan Status Distribution')
    plt.xlabel('Loan Status')
    plt.ylabel('Count')
    plt.show()
    
    
    
    
    
    