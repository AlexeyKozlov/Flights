

def percents(x,y):
    '''what percent x is y'''
    one_perc=x/100
    result = y/one_perc
    return result


def print_result(x,y):
    print(str(y) +' is '+ str(percents(x,y))+' % of ' +str(x))



percents(200,50)