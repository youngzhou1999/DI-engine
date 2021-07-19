import pytest
import numpy as np
from dizoo.minigrid.envs import MiniGridEnv


@pytest.mark.unittest
class TestMiniGridEnv:

    def test_naive(self):
        env = MiniGridEnv(MiniGridEnv.default_config())
        env.seed(314)
        assert env._seed == 314
        obs = env.reset()
        act_val = env.info().act_space.value
        min_val, max_val = act_val['min'], act_val['max']
        for i in range(10):
            random_action = np.random.randint(min_val, max_val, size=(1, ))
            timestep = env.step(random_action)
            print(timestep)
            assert isinstance(timestep.obs, np.ndarray)
            assert isinstance(timestep.done, bool)
            assert timestep.obs.shape == (2739, )
            assert timestep.reward.shape == (1, )
            assert timestep.reward >= env.info().rew_space.value['min']
            assert timestep.reward <= env.info().rew_space.value['max']
        print(env.info())
        env.close()
