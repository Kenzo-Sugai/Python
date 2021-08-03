def classdata(st=""):
    datalist = []
    arquivo = open(st, "r")
    for x in arquivo.readlines():
        datalist.append(x.strip())
    arquivo.close()

    classlist = []
    for x in datalist[0].split(","):
        classlist.append(x)

    for x in range(len(datalist)):
        if x != 0:
            for y in datalist[x].split(","):
                if y == "ball":
                    frase = datalist[x].split(",")
                    frasefinal =  ""
                    for y in frase:
                        if y == "640" or y == "360":
                            pass
                        else:
                            frasefinal+y
                            frasefinal+=","
                    frasefinal2 = ""
                    for x in range(len(frasefinal)-1):
                        frasefinal2+=frasefinal[x]
                    frasefinal2+='\n'
                    print(frasefinal2)