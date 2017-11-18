
import read
import collections as cl

if __name__ == '__main__' :
    
    data = read.load_data()
    headlines = data['headline'].tolist()    
    # print(headlines[0:5])
    
    all_lines = ' '.join(str(h).lower() for h in headlines)
    words = all_lines.split(' ')
    # print(words[0:10])
    
    word_count = cl.Counter(words)
    print(word_count.most_common(100))
    