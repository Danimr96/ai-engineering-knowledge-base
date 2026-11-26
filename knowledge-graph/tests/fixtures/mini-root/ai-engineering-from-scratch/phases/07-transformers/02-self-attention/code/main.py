# see docs/en.md
import math
import numpy as np
import torch
from dataclasses import dataclass


def softmax(x):
    return np.exp(x) / np.exp(x).sum()


class SelfAttention:
    pass


print("hi")
