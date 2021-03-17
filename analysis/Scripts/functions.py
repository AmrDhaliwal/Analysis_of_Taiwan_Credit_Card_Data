import pandas as pd

# Method chain wrapped in a function
# Has renamned columns and dropped Nan values and duplicates
def load_and_process(_):
    #Method 1 load csv file and drop for Nan values
    df1 = (
        pd.read_csv(r"C:\Users\Amrit\Desktop\School\data301\course-project-solo_119\data\data.raw\default of credit card clients.csv")
        .dropna()
    )
    # Method 2 rename all columns in Dataframe
    df2 = (
        df1
        .rename(columns={'Unnamed: 0': 'ID', 'X1': 'Limit_BAL', 'X2': 'SEX', 'X3': 'EDUCATION',
                           'X4': 'MARRIAGE', 'X5': 'AGE', 'X6': 'PAY_APR', 'X7': 'PAY_MAY',
                           'X8': 'PAY_JUN', 'X9': 'PAY_JUL', 'X10': 'PAY_AUG', 'X11': 'PAY_SEPT',
                           'X12': 'BILL_AMT_APR', 'X13': 'BILL_AMT_MAY', 'X14': 'BILL_AMT_JUN',
                           'X15': 'BILL_AMT_JUL', 'X16': 'BILL_AMT_AUG', 'X17': 'BILL_AMT_SEPT',
                           'X18': 'PAY_AMT_APR', 'X19': 'PAY_AMT_MAY', 'X20': 'PAY_AMT_JUN',
                           'X21': 'PAY_AMT_JUL', 'X22': 'PAY_AMT_AUG', 'X23': 'PAY_AMT_SEPT',
                           'Y': 'PAY_NEXT_MONTH'})
    )
    # Method 3 use .drop to remove duplicate names from Dataframe
    # Change floats to int
    df3 = (
        df2
        .drop(df2.index[0])
        .astype(int)
    )
    
    return df3    
    