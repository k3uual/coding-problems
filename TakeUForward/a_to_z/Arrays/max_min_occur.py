
def max_min_occur(a):
    dict = {}
    for num in a:
        if(dict.get(num)) is None:
            dict[num] = 1
        else: 
            dict[num] += 1
            
    print(max(dict, key=dict.get))
    print(min(dict, key=dict.get))

if __name__ == '__main__':
    max_min_occur([10,5,10,15,10,5])        