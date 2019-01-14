class DocpyError(Exception):
    pass

def file_to_dicc(route, splitBy=',', nameKey=[], hasTop=False, idxKey=[], groupBy={}): 
    #groupBy = {'asd' : {'key':"name",'data':[]}}
    if route[-3] == "txt" or route[-3] == 'csv':
        raise DocpyError('file_to_dicc is only able to read .txt files or csv')
    with open(route) as f:
        dicc = {}
        top = []
        ids = []
        if hasTop == True:
            top = f.readline().strip().split(splitBy)
            if len(idxKey) == 0 and len(nameKey) != 0 and hasTop == True:
                for name in nameKey:
                    ids.append(top.index(name))
                if len(groupBy.keys()) != 0:
                    for key in groupBy.keys():
                        if len(groupBy[key].keys()) == 0:
                            raise DocpyError("Created a Group but didnt gave any key or name to work with.")
                        if groupBy[key]['key'] == 'idx':
                            ids.append([key,groupBy[key]['data']])
                        elif groupBy[key]['key'] == 'name':
                            temp = [key]
                            i = 0
                            for name in groupBy[key]['data']:
                                temp.append(top.index(name))
                            ids.append(temp)
                        else:
                            raise DocpyError("The type of key given in the " + key + " group is not defined, use \'name\' or \'idx\'")
            else:
                ids = idxKey
        elif hasTop == False and len(idxKey) == 0:
            raise DocpyError("Impossible to classify without a idxKey or a nameKey")
        for line in f:
            line = line.strip().split(splitBy)
            if len(groupBy.keys()) == 0:
                for i in range(len(ids)):
                    if i != 0:
                        if line[ids[0]] in dicc:
                            dicc[line[ids[0]]].update({top[ids[i]]:line[ids[i]]})
                        else: 
                            dicc[line[ids[0]]] = {top[ids[i]]:line[ids[i]]}
            else:
                for i in range(len(ids)):
                    if type(ids[i]) != list and i != 0:
                        if line[ids[0]] in dicc:
                            dicc[line[ids[0]]].update({top[ids[i]]:line[ids[i]]})
                        else:
                            dicc[line[ids[0]]] = ({top[ids[i]]:line[ids[i]]})
                    elif type(ids[i]) == list:
                        temp = []
                        for j in ids[i][1:]:
                            temp.append(line[j])
                        dicc[line[ids[0]]].update({ids[i][0]:temp})
    return dicc

def arrayPrinter(array,TopText = [],SideText = [], divider = '',offset = 2):
    firstSpacer = len(max(SideText,key = len))
    spacer = []
    line = ' '*firstSpacer + ' '*offset + divider + ' '*offset
    for j in range(len(TopText)):
        temp = array[:,j].tolist()
        indent = len(max(temp,key=len))
        spacer.append(indent)
        line = line + TopText[j] + ' '*(indent - len(TopText[j])) + ' '*offset + divider + ' '*offset
    print(line)
    for i in range(len(SideText)):
        line = SideText[i] + " "*(firstSpacer - len(SideText[i])) + ' '*offset + divider + ' '*offset
        for j in range(len(TopText)):
            data = data[i,j]
            line = line + data + ' '*(spacer[j]-len(data)) + ' '*offset + divider + ' '*offset
        print(line)

def dataVerifier(data,restrains = {},needsToHave = {}):
    #restrains = {'type':str,'maxLen': 10, 'minVal' : 0, 'maxVal' : 10,'minLen': 0}
    #needsToHave = {'@gmail.com' : {'Quantity':1,'FixedPosition':'Bottom'}}
    #End, Begin,Middle
    msg = ''
    valid = True
    try:
        if restrains['type'] == int:
            data = int(data)
            valid = True
        elif restrains['type'] == float:
            data = float(data)
            valid = True
        elif restrains['type'] == complex:
            data = complex(data)
            valid = True
        elif restrains['type'] == str:
            data = str(data)
            valid = True
        elif restrains['type'] == bool:
            data = str(data)
            valid = True
        
        if 'minLen' in restrains.keys() and restrains['type'] != bool:
            if len(data) < restrains['minLen']:
                msg += data + ' can be converted to '+ restrains['type'] +' but doesnt have the minimun Lenght (' +restrains['minLen']+')' + '\n'
                valid = False
        if 'maxLen' in restrains.keys() and restrains['type'] != bool:
            if len(data) > restrains['maxLen']:
                msg += data + ' can be converted to '+ restrains['type'] +' but doesnt have the maximun Lenght (' +restrains['maxLen']+')' + '\n'
                valid = False
        if 'minVal' in restrains.keys() and restrains['type'] != bool and restrains['type'] != str:
            if data < restrains['minVal']:
                valid = False
                msg += data + ' has a lower value than ' + restrains['minVal'] + '\n'
        if 'maxVal' in restrains.keys() and restrains['type'] != bool and restrains['type'] != str:
            if data < restrains['maxVal']:
                valid = False
                msg += data + ' has a greater value than ' + restrains['maxVal'] + '\n'
        
        if len(needsToHave.keys()) != 0:
            for key in needsToHave.keys():
                this = needsToHave[key]
                if len(this.keys()) != 0:
                    if 'Quantity' in this:
                        if str(data).count(key) != this['Quantity']:
                            msg += data + ' doesnt have ' + key + ' repeated ' + this['Quantity'] + ' times\n'
                            valid = False
                    elif 'Quantity' not in this:
                        raise DocpyError('Needs to define the quantity for ' + key)
                    if 'FixedPosition' in this:
                        if this['FixedPosition'] == 'Begin':
                            if data[:len(key)] != key:
                                msg += ' is not at the position requested\n'
                                valid = False
                        if this['FixedPosition'] == 'End':
                            if data[-len(key)] != key:
                                valid = False
                                msg += ' is not at the position requested\n'
                        if this['FixedPosition'] == 'Middle':
                            if data[len(data)/2:len(key)] != key:
                                valid = False
                                msg += ' is not at the position requested\n'
        return data,msg,valid

    except ValueError:
        valid = False
        msg = data + ' cant be converted to ' + restrains['type']
        return data,msg,valid

