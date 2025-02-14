import pytest
import torch
from ding.rl_utils import gae_data, gae


@pytest.mark.unittest
def test_gae():
    T, B = 32, 4
    value = torch.randn(T, B)
    next_value = torch.randn(T, B)
    reward = torch.randn(T, B)
    done = torch.zeros((T, B))
    data = gae_data(value, next_value, reward, done)
    adv = gae(data)
    assert adv.shape == (T, B)
