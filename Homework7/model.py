import storage as st

def add_from_file(a,x1,x2,x3,x4):
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
        
def generate_data(x1,x2,x3,x4):
    return list(zip(x1,x2,x3,x4))

def formation_str(a):
    data_str = ''
    for i in range(len(a)):
        for j in range(len(a[i])):
            data_str += a[i][j] + ' '
        data_str += '\n'
    return data_str

def write_to_file(a,b,c):
    f = open(a, b)
    f.write(c)
    f.write('\n')
    f.close()

def assemble_line(a, b, c, d):
    return a + ' '+ b +  ' '+ c + ' ' + d  

def read_file(a):
    f = open(a)
    data = f.readlines()
    f.close()
    data_str = ''
    for i in range(len(data)):
        data_str += data[i]
    return data_str
