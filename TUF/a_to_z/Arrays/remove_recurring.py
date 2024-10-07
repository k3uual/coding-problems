
def rm_reccur(lst):
    z = zip(lst,[None]*len(lst))
    d = dict(z)
    lst = list(d.keys())
    print(lst)
    
rm_reccur([10,5,10,15,10,5])  