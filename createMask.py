import sys
import itertools
import getopt
def createOutputString(list):
    out = ""
    for item in list:
        out += str(item)
    return out
def sortSecond(val):
    return val[1]


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "mo:l:")
    except getopt.GetoptError as err:
        print("error in argument parsing. Available Arguments: -o -l --increment-min")
        print(err)
        sys.exit(2)

    length = 0
    path = "generated.txt"
    minSize = 1
    for opt, arg in opts:
        print(opt+" / "+arg)
        if opt == '-o':
            path = arg
        elif opt == '-l':
            if int(arg) > 0:
                length = int(arg)
            else:
                print("Given length is lower than 0. The script is using 1 instead")
        elif opt == '-m':
            if int(arg) > 0:
                minSize = int(arg)
            else:
                print("Given --increment-min is lower than 0. The script is using 0 instead")

    possibleValues = ["?l", "?u", "?d", "?h", "?H", "?s", "?a", "?b"]
    priority = {}
    priority["?l"] = 26
    priority["?u"] = 26
    priority["?d"] = 10
    priority["?h"] = 16
    priority["?H"] = 16
    priority["?s"] = 33
    priority["?a"] = priority["?l"] + priority["?u"] + priority["?d"] + priority["?s"]
    priority["?b"] = 255
    erg = []
    print(str(range(minSize, length+1)))
    for i in range(minSize, length+1):
        if erg == []:
            erg = list(itertools.combinations_with_replacement(possibleValues, i))
        else:
            zerg = list(itertools.combinations_with_replacement(possibleValues, i))
            erg = erg + zerg
            print(str(len(zerg)))

    combinedErg = []
    for item in erg:
        prioSum = 1
        for val in item:
            prioSum *= priority[val]
        combinedErg.append([item, prioSum])
    combinedErg.sort(key=sortSecond)
    with open(path, 'w') as file_handler:
        for item in combinedErg:
            #file_handler.write(createOutputString(item[0]) + "     " +str(item[1])+"\n")
            file_handler.write(createOutputString(item[0])+"\n")

    print("%s Masks generated" % len(erg))


if __name__ == "__main__":
    print(str(sys.argv))
    main(sys.argv[1:])
