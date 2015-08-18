import os


def remove_file(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass



def main():
    input_file = 'backup.txt'
    output = 'output/2.csv'
    remove_file(output)

    # i = open(input_file, 'r')
    new_file = {}
    for i in open(input_file, encoding="utf8").readlines():
        split_i = i.split('\t', 4)
        exp = split_i[0]
        tags = split_i[4].split(' ')
        tags = [x.replace('\n', '') for x in tags]
        try:
            for t in tags:
                new_file[exp].add(t)
        except KeyError:
            new_file[exp] = set(tags)

    print(len(new_file.keys()))
    added = {}
    o = open(output, 'a+', encoding="utf8")
    for i in open(input_file, encoding="utf8").readlines():
        split_i = i.split('\t', 4)
        exp = split_i[0]
        try:
            if added[exp]:
                pass
        except:
            added[exp] = True
            first = '\t'.join([split_i[0],split_i[1],split_i[2],split_i[3]])
            line = first + ' ' + ' '.join(new_file[exp])
            o.write("%s\n" % line)
    o.close()



if __name__ == '__main__':
    main()
