def root(number: float, root_value: float) -> float:
    assert isinstance(number, (float, int)),\
        'Argument \'number\' is not float or int'
    assert isinstance(root_value, (float, int)), \
        'Argument \'root_value\' is not float or int'
    assert root_value != 0, \
        'Argument \'root_value\' must be non zero'
    return number ** (1 / root_value)


def pover(number: float, pover: float) -> float:
    assert isinstance(number, (float, int)),\
        'Argument \'number\' is not float or int'
    assert isinstance(pover, (float, int)), \
        'Argument \'pover\' is not float or int'
    return number**pover
