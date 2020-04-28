import sys, os, re
import numbers as nb


def fill_template(text, pattern, value_number):

    if value_number == 0:
        value = nb.revenue_change
    elif value_number == 1:
        value = nb.profit_change
    elif value_number == 2:
        value = nb.average_check
    text = text.replace(pattern, value)
    return text


def write_line_in_file(new_line):
    f = open("filled.txt", "w")
    f.write(new_line)
    f.close()


def main():
    if len(sys.argv) != 2:
        print("Please write a file name as an argument with extension '.template'\nexample: file.template")
        return
    file_name = str(sys.argv[1])
    name = re.search('.*.template', file_name)
    if name is None:
        print("Wrong file extension, must be: '.template'")
        return
    f = open(sys.argv[1])
    if not f:
        print('File doesn\'t exist')
        return
    try:
        nb.average_check, nb.profit_change, nb.revenue_change
    except AttributeError:
        print('Missing values in numbers.py')
        return
    text = f.read()
    for i in range(3):
        m = re.search('{.*?}', text)
        text = fill_template(text, m.group(0), i)
        write_line_in_file(text)
    print(text)


if __name__ == '__main__':
    main()
