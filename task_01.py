#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Wk 12 Synth Task 1"""


class BaseError(Exception):
    """A Basic Exception Class"""
    pass


class StringError(BaseError, TypeError):
    """Exception for Strings"""
    pass


class NumberError(BaseError, TypeError):
    """Exception for Numbers"""
    pass


class NonZeroError(NumberError):
    """Exception for NonZeros"""
    pass
