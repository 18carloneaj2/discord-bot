def calculate(eqn: str):
    '''

    :param eqn:
    :return:
    '''
    eqn = eqn.split()
    del eqn[0]

    eqn[0] = float(eqn[0])
    eqn[2] = float(eqn[2])

    if eqn[1] == '+':
        return eqn[0] + eqn[2]
    elif eqn[1] == '-':
        return eqn[0] - eqn[2]
    elif eqn[1] == '*' or eqn[1] == 'x':
        return eqn[0] * eqn[2]
    elif eqn[1] == '/':
        return eqn[0] / eqn[2]
    else:
        return 'Invalid equation'