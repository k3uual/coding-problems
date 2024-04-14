
def occurence(a):
    dict = {}
    for num in a:
        if(dict.get(num)) is None:
            dict[num] = 1
        else:    
            dict[num] += 1
    for num in dict:
        print(num,dict[num])  
        
if __name__ == '__main__':
    occurence([10,5,10,15,10,5])        