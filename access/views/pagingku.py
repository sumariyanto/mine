
def pagingku(limit,offset,mdl):
    if limit:
        if offset:
            if int(offset) > 0:
                mdl =mdl[int(offset):int(limit)+int(offset)]
            else:
                mdl =mdl[int(offset):int(limit)]
        else:
            mdl =mdl[0:int(limit)]
    else:
        mdl =mdl[0:10]
    
    return mdl

def listpageku(offset,total):
    if offset !='':
        offset = int(offset)
    if offset =='':
        offset = 0
        
    list_page = []
    if offset >=1:
        list_page.append(1)
    if offset+3 < total:
        for i in range(offset,offset+4):
            list_page.append(i)
    else:
        for i in range(offset,total):
            list_page.append(i)
    list_page.append(offset-1)

    if int(total)-3 > 0:
        for i in range(total-3,total+1):
            list_page.append(i)
    else:
        for i in range(1,total+1):
            list_page.append(i)
    list_page =list(set(list_page))
    if 0 in list_page:
        list_page.remove(0)
    list_page.sort()

    return list_page