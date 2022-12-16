
def add_from_file(a,x1,x2,x3,x4,x5,x6):
    f = open(a)
    data = f.readlines()
    f.close()
    for i in range(len(data)):
        d = data[i].split()
        if d != []:
            x1.append(d[0])
            x2.append(d[1])
            x3.append(d[2])
            x4.append(d[3])
            x5.append(d[4])
            x6.append(d[5])
        
def generate_data(x1,x2,x3,x4,x5,x6):
    return list(zip(x1,x2,x3,x4,x5,x6))

def formation_str(a):
    data_str = ''
    for i in range(len(a)):
        for j in range(len(a[i])):
            data_str += a[i][j] + ' '
        data_str += '\n'
    return data_str

def align_list(a):
    m = len(a[0])
    for i in range(len(a)):
        if len(a[i])> m:
            m = len(a[i])
    for j in range(len(a)):
        k = m-len(a[j])
        a[j] += ' '*k
    return a

def write_to_file(a,b,c):
    f = open(a, b)
    f.write(c)
    f.write('\n')
    f.close()

def find_in_list(a, x):
    lst = []
    for i in range(len(x)):
        ind = x[i].find(a)
        if ind != -1:
            lst.append(i)
    return lst

def find_data(a,x1,x2,x3,x4,x5,x6):
    a = a.split() 
    lst = [x1,x2,x3,x4,x5,x6]
    lst_indx = []
    for i in a:
        for x in lst:
            lst1 = find_in_list(i,x)
            if lst1 != []:
                lst_indx.append(lst1)
    if lst_indx != []:
        lst_indx = min(lst_indx)
    return lst_indx

def select_data(a,x):
    select_data = []
    for i in a:
        select_data.append(x[i])
    return select_data

def formation_data(x1,x2,x3,x4,x5,x6):
    lst = [x1,x2,x3,x4,x5,x6]
    for i in lst:
        i = align_list(i)

def reset_data(x):
    x = []
    return x
    

