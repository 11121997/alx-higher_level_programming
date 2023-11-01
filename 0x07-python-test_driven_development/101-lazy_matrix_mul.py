#!/usr/bin/python3
"""Lazy matrix mul module"""
import numpy

def lazy_matrix_mul(m_a, m_b):
    """
    function that multiplies 2 matrices
    Args:
        m_a: first matrix
        m_b: second matrix
        Return: m_a * m_b
    """
    
    return numpy.matmul(m_a, m_b)
