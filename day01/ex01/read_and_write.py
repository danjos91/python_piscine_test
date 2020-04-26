def transform_line(line):
    return(line.replace(',','\t'))

def write_line_in_file(new_line):
    f = open("ds.tsv", "a+")
    f.write(new_line)
    f.close()

def main():
    file = open('d01_ds.csv')
    while True:
        line = file.readline()
        line = transform_line(line)
        write_line_in_file(line)
        if not line: 
            break
    
if __name__ == '__main__':
    main()


