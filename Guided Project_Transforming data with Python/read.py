
import pandas as pd

def load_data() :
    
    data = pd.read_csv('hn_stories.csv', header=None)
    data.columns = ['submission_time', 'upvotes', 'url', 'headline']
    
    return data

# for testing in read.py
if __name__ == '__main__' :
        
    data = load_data()    
    print(data.head(2))
    