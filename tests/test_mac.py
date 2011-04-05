from __future__ import division

import os
import hmac

from tomcrypt import mac
from tomcrypt import Error as TomCryptError

def test_single_digest():
    for i in range(1, 10):
        key = os.urandom(8 * i)
        x = hmac.new(key)
        y = mac.MAC('hmac', 'md5', key)
        for j in range(1, 10):
            v = os.urandom(j * 8)
            x.update(v)
            y.update(v)
        assert x.digest() == y.digest()

def test_mutiple_digests():
    i = j = -1
    try:
        for i in range(1, 10):
            j = -1
            key = os.urandom(8 * i)
            x = hmac.new(key)
            y = mac.MAC('hmac', 'md5', key)
            for j in range(1, 10):
                v = os.urandom(j * 8)
                x.update(v)
                y.update(v)
                assert x.digest() == y.digest()
    except (AssertionError, TomCryptError) as e:
        assert False, 'failed on %d-%d: %r' % (i, j, e)

def test_copy():
    i = j = -1
    try:
        for i in range(1, 10):
            j = -1
            key = os.urandom(8 * i)
            x = mac.MAC('hmac', 'md5', key)
            for j in range(1, 10):
                v = os.urandom(j * 8)
                y = x.copy()
                x.update(v)
                y.update(v)
                assert x.digest() == y.digest()
                d = x.digest()
                y = x.copy()
                y.update(v)
                assert y.digest() != d
                assert x.digest() == d
    except (AssertionError, TomCryptError) as e:
        assert False, 'failed on %d-%d: %r' % (i, j, e)


def test_api():
    assert 'hmac' in mac.names
    msg = 'hello, world'
    assert mac.hmac('sha256', msg).hexdigest() == 'bf9498672a3fc6c06a7b13f7b0a7c24d2c9aeb8f797dbfc00cb4e1a1ab5cb420'
         