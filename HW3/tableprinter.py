#Assignment3
#WEIWEI SU
#U17420699
#Last Modify: 9-20-2017
#Filename: tableprinter.py

#given data here
tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['alice', 'bob', 'carol', 'david'],
            ['dogs', 'cats', 'moose', 'goose']]

def printtable(L):
    #check maximum width of word in a list
    colWidth = [0] * len(L) #One number on the list represent a maximum word length in the given list col
    for c in range(len(L)):
        for i in L[c]:
            if len(i) > colWidth[c]:
                colWidth[c] = len(i)

    #inverse each inner list form column format to row.
    columns = []
    for i in range(len(L[0])):
        for c in range(len(L)):
            try:
                columns[i].append(L[c][i])
            except:
                columns.append([L[c][i]])

    #then print it out with rjust order
    for r in columns:
        lists = ''
        for i in range(len(r)):
            lists += r[i].rjust(colWidth[i] + 1)
        print(lists)

printtable(tableData)
