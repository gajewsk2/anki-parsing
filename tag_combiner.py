import os


def remove_file(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass



def main():
    input_file = 'deck1.txt'
    output = 'output/2.csv'
    remove_file(output)

    # i = open(input_file, 'r')
    new_file = {}
    for i in open(input_file, encoding="utf8").readlines():
        split_i = i.split('\t', 4)
        exp = split_i[0]
        tags = split_i[4]
        try:
            n = new_file[exp].split('\t', 4)
            set(tags).union(t)
            new_file[exp] = new_file[exp].replace('\n', str(n[4]) + '\n')
        except KeyError:
            new_file[exp] = i
        #
        #     split_n = n.split('\t', 4)
        #     exp_n = split_n[0]
        #     tag_n = split_n[4]
        #     if exp_n == exp:
        #         original = new_file[new_file.index(n)]
        #         new_file[new_file.index(n)] = original + tag_n
        #         added = True
        #         break
        # if not added:
        #     new_file.append()




    # clean_i = strip_tags(li)

    o = open(output, 'a+', encoding="utf8")
    for key in new_file:
        o.write("%s" % new_file[key])
    # o.write(li.encode('utf8'))
    o.close()



if __name__ == '__main__':
    main()
