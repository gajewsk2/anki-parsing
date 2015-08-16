from html_stripper import strip_tags
import os


def remove_file(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass



def main():
    input_file = 'JP101.com.txt'
    output = 'output/1.csv'
    remove_file(output)

    # i = open(input_file, 'r')
    list_i = [strip_tags(i) for i in open(input_file, encoding="utf8").readlines()]


    # clean_i = strip_tags(li)

    o = open(output, 'a+', encoding="utf8")
    for item in list_i:
        o.write("%s\n" % item)
    # o.write(li.encode('utf8'))
    o.close()



if __name__ == '__main__':
    main()
