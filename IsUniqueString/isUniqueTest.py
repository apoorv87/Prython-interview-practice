import pytest
from isUnique import isUniqueASCII

def test_is_unique():
    str = ''
    assert (isUniqueASCII(str) == True)
    str = 'abc'
    assert (isUniqueASCII(str) == True)
    str = 'abca'
    assert (isUniqueASCII(str) == False)



