#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 17/11/7 下午4:35
# Author  : Shi Bo
# Email   : pkushibo@pku.edu.cn
# File    : utils.py

import numpy as np
from datetime import datetime

def load_dataset(data_path, max_seq_len=2048, pad_len=2048):
    """ utils: load the dataset
    :param data_path: the path of the dataset
    :param max_seq_len: the max length of a sequence
    :param pad_len: the padded length of the returned matrix
    :return: X_malware, malware_length, X_benign, benign_length
             X_malware and X_benign are the matrix of malware and benign.
                shape: [num instances, max_seq_len + pad_len]
             malware_length and benign_length are the length of the matrix, which should be smaller than max_seq_len
                shape: [num instances]
    """
    X_malware = []
    malware_length = []
    X_benign = []
    benign_length = []
    for line in open(data_path):
        elements = line.strip().split(';')
        Xi = []
        for element in elements[2:-1]:
            if len(element) <= 0:
                continue
            for digit in element.split(','):
                Xi.append(int(digit))
        Xi = Xi[:max_seq_len]
        if elements[1] is '0':
            benign_length.append(len(Xi))
            X_benign.append(np.array(Xi + [0] * (max_seq_len + pad_len - len(Xi)), dtype=np.int32))
        else:
            malware_length.append(len(Xi))
            X_malware.append(np.array(Xi + [0] * (max_seq_len + pad_len - len(Xi)), dtype=np.int32))
    return np.vstack(X_malware), np.array(malware_length), np.vstack(X_benign), np.array(benign_length)

def log_writer(log_filepath='log.txt', log_message=str(datetime.now())):
    """
    write log message to log file at log_filepath
    :param log_filepath: filepath to write log to
    :param log_message: log messages to write
    :return: None
    """
    with open(log_filepath, 'a') as f:
        f.write(log_message + '\n')
























