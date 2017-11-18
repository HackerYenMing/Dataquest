
import read
import pandas as pd

def remove_sub(url) :    
    words = str(url).split('.')
    Len = len(words)
    
    if Len <= 2 :
        return url
    return ''.join([words[Len-2], '.', words[Len-1]])    

if __name__ == '__main__' :
    
    data = read.load_data()       
    data['domain'] = data['url'].apply(remove_sub)

    urls = data['url'].value_counts()
    
    for name, count in urls.items() :
        if count < 100 : 
            break       
        print('url :', "{0}: {1}".format(name, count))

    domains = data['domain'].value_counts()

    for name, count in domains.items() :
        if count < 100 : 
            break       
        print('domain :', "{0}: {1}".format(name, count))
               