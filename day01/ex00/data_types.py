def data_type(int ,str, float, bool, list, dict, tuple, set):
    datas = [(int),str,float,bool,list,dict,tuple,set]
    j = 0
    spisok = [0,1,2,3,4,5,6,7]
    for i in datas:
        spisok[j] = type(i).__name__
        j += 1
    print('[', end = "")
    print(*spisok, sep = ", ", end="]")

if __name__ == '__main__':
    data_type(2,"hello",2.5,True,[1,2,3],{'dict': 1, 'dictionary': 2},(1,2),{'a','b'})
