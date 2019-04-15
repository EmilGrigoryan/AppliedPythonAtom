#!/usr/bin/env python
# coding: utf-8


import numpy as np


def mse(y_true, y_hat, derivative=False):
    """
    Mean squared error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    y_true = np.array(y_true)
    y_hat = np.array(y_hat)
    if len(np.array(y_true)) == len(np.array(y_hat)):
        return np.mean((y_true - y_hat)**2)


def mae(y_true, y_hat):
    """
    Mean absolute error regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    y_true = np.array(y_true)
    y_hat = np.array(y_hat)
    if len(np.array(y_true)) == len(np.array(y_hat)):
        return np.mean(np.abs(y_true - y_hat))


def r2_score(y_true, y_hat):
    """
    R^2 regression loss
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated target values
    :return: loss
    """
    y_true = np.array(y_true)
    y_hat = np.array(y_hat)
    if len(np.array(y_true)) == len(np.array(y_hat)):
        return 1 - (np.sum((y_true - y_hat)**2) /
                    np.sum((y_true - np.mean(y_true)))**2)
