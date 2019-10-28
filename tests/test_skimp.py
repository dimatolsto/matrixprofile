#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

range = getattr(__builtins__, 'xrange', range)
# end of py2 compatability boilerplate

import os

import pytest

import numpy as np

from matrixprofile.algorithms import skimp


def test_binary_split_1():
    desired = [0]
    actual = skimp.binary_split(1)

    np.testing.assert_equal(actual, desired)


def test_binary_split_many():
    desired = [0, 5, 2, 7, 1, 3, 6, 8, 4, 9]
    actual = skimp.binary_split(10)

    np.testing.assert_equal(actual, desired)


def test_maximum_subsequence_128():
    np.random.seed(9999)
    ts = np.random.uniform(size=2**10)
    w = 2**5
    subq = ts[0:w]
    ts[0:w] = subq
    ts[w+100:w+100+w] = subq

    upper = skimp.maximum_subsequence(ts, 0.98)

    assert(upper == 128)


def test_maximum_subsequence_256():
    np.random.seed(9999)
    ts = np.random.uniform(size=2**10)
    w = 2**6
    subq = ts[0:w]
    ts[0:w] = subq
    ts[w+100:w+100+w] = subq

    upper = skimp.maximum_subsequence(ts, 0.98)

    assert(upper == 256)