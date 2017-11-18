
import read
import datetime as dt
from dateutil.parser import parse

def parse_year(time_str) :    
    return parse(time_str).year

def parse_month(time_str) :    
    return parse(time_str).month

def parse_weekday(time_str) :    
    return parse(time_str).weekday()

def parse_hour(time_str) :    
    return parse(time_str).hour 

if __name__ == '__main__' :
    
    data = read.load_data()
    data['year'] = data['submission_time'].apply(parse_year)  
    data['month'] = data['submission_time'].apply(parse_month)
    data['weekday'] = data['submission_time'].apply(parse_weekday)
    data['hour'] = data['submission_time'].apply(parse_hour)
    
    print(data['year'].value_counts())
    print(data['month'].value_counts())
    print(data['weekday'].value_counts())
    print(data['hour'].value_counts())
    