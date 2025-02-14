import pytest
import time
import os
import torch
from copy import deepcopy

from ding.entry import serial_pipeline
from ding.entry.serial_entry_sqil import serial_pipeline_sqil
from dizoo.classic_control.cartpole.config.cartpole_sql_config import cartpole_sql_config, cartpole_sql_create_config
from dizoo.classic_control.cartpole.config.cartpole_sqil_config import cartpole_sqil_config, cartpole_sqil_create_config
from dizoo.classic_control.cartpole.config.cartpole_dqn_config import cartpole_dqn_config, cartpole_dqn_create_config
from dizoo.classic_control.cartpole.config.cartpole_ppo_config import cartpole_ppo_config, cartpole_ppo_create_config
from dizoo.classic_control.cartpole.config.cartpole_a2c_config import cartpole_a2c_config, cartpole_a2c_create_config
from dizoo.classic_control.cartpole.config.cartpole_impala_config import cartpole_impala_config, cartpole_impala_create_config  # noqa
from dizoo.classic_control.cartpole.config.cartpole_rainbow_config import cartpole_rainbow_config, cartpole_rainbow_create_config  # noqa
from dizoo.classic_control.cartpole.config.cartpole_iqn_config import cartpole_iqn_config, cartpole_iqn_create_config  # noqa
from dizoo.classic_control.cartpole.config.cartpole_c51_config import cartpole_c51_config, cartpole_c51_create_config  # noqa
from dizoo.classic_control.cartpole.config.cartpole_qrdqn_config import cartpole_qrdqn_config, cartpole_qrdqn_create_config  # noqa
from dizoo.classic_control.cartpole.config.cartpole_sqn_config import cartpole_sqn_config, cartpole_sqn_create_config  # noqa
from dizoo.classic_control.cartpole.config.cartpole_ppg_config import cartpole_ppg_config, cartpole_ppg_create_config  # noqa
from dizoo.classic_control.cartpole.config.cartpole_acer_config import cartpole_acer_config, cartpole_acer_create_config  # noqa
from dizoo.classic_control.cartpole.entry.cartpole_ppg_main import main as ppg_main
from dizoo.classic_control.cartpole.entry.cartpole_ppo_main import main as ppo_main
from dizoo.classic_control.cartpole.config.cartpole_r2d2_config import cartpole_r2d2_config, cartpole_r2d2_create_config  # noqa
from dizoo.classic_control.pendulum.config import pendulum_ddpg_config, pendulum_ddpg_create_config
from dizoo.classic_control.pendulum.config import pendulum_td3_config, pendulum_td3_create_config
from dizoo.classic_control.pendulum.config import pendulum_sac_config, pendulum_sac_create_config
from dizoo.classic_control.bitflip.config import bitflip_her_dqn_config, bitflip_her_dqn_create_config
from dizoo.classic_control.bitflip.entry.bitflip_dqn_main import main as bitflip_dqn_main
from dizoo.multiagent_particle.config import cooperative_navigation_qmix_config, cooperative_navigation_qmix_create_config  # noqa
from dizoo.multiagent_particle.config import cooperative_navigation_vdn_config, cooperative_navigation_vdn_create_config  # noqa
from dizoo.multiagent_particle.config import cooperative_navigation_coma_config, cooperative_navigation_coma_create_config  # noqa
from dizoo.multiagent_particle.config import cooperative_navigation_collaq_config, cooperative_navigation_collaq_create_config  # noqa
from dizoo.multiagent_particle.config import cooperative_navigation_atoc_config, cooperative_navigation_atoc_create_config  # noqa
from dizoo.league_demo.league_demo_ppo_config import league_demo_ppo_config
from dizoo.league_demo.selfplay_demo_ppo_main import main as selfplay_main
from dizoo.league_demo.league_demo_ppo_main import main as league_main

with open("./algo_record.log", "w+") as f:
    f.write("ALGO TEST STARTS\n")


@pytest.mark.algotest
def test_dqn():
    config = [deepcopy(cartpole_dqn_config), deepcopy(cartpole_dqn_create_config)]
    try:
        serial_pipeline(config, seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("1. dqn\n")


@pytest.mark.algotest
def test_ddpg():
    config = [deepcopy(pendulum_ddpg_config), deepcopy(pendulum_ddpg_create_config)]
    try:
        serial_pipeline(config, seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("2. ddpg\n")


@pytest.mark.algotest
def test_td3():
    config = [deepcopy(pendulum_td3_config), deepcopy(pendulum_td3_create_config)]
    try:
        serial_pipeline(config, seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("3. td3\n")


@pytest.mark.algotest
def test_a2c():
    config = [deepcopy(cartpole_a2c_config), deepcopy(cartpole_a2c_create_config)]
    try:
        serial_pipeline(config, seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("4. a2c\n")


@pytest.mark.algotest
def test_rainbow():
    config = [deepcopy(cartpole_rainbow_config), deepcopy(cartpole_rainbow_create_config)]
    try:
        serial_pipeline(config, seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("5. rainbow\n")


@pytest.mark.algotest
def test_ppo():
    config = [deepcopy(cartpole_ppo_config), deepcopy(cartpole_ppo_create_config)]
    try:
        ppo_main(config[0], seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("6. ppo\n")


# @pytest.mark.algotest
def test_collaq():
    config = [deepcopy(cooperative_navigation_collaq_config), deepcopy(cooperative_navigation_collaq_create_config)]
    try:
        serial_pipeline(config, seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("7. collaq\n")


# @pytest.mark.algotest
def test_coma():
    config = [deepcopy(cooperative_navigation_coma_config), deepcopy(cooperative_navigation_coma_create_config)]
    try:
        serial_pipeline(config, seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("8. coma\n")


@pytest.mark.algotest
def test_sac():
    config = [deepcopy(pendulum_sac_config), deepcopy(pendulum_sac_create_config)]
    try:
        serial_pipeline(config, seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("9. sac\n")


@pytest.mark.algotest
def test_c51():
    config = [deepcopy(cartpole_c51_config), deepcopy(cartpole_c51_create_config)]
    try:
        serial_pipeline(config, seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("10. c51\n")


# @pytest.mark.algotest
def test_r2d2():
    config = [deepcopy(cartpole_r2d2_config), deepcopy(cartpole_r2d2_create_config)]
    try:
        serial_pipeline(config, seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("11. r2d2\n")


@pytest.mark.algotest
def test_a2c_with_nstep_return():
    config = [deepcopy(cartpole_a2c_config), deepcopy(cartpole_a2c_create_config)]
    config[0].policy.learn.nstep_return = config[0].policy.collect.nstep_return = True
    config[0].policy.collect.discount_factor = 0.9
    config[0].policy.collect.nstep = 3
    try:
        serial_pipeline(config, seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("12. a2c with nstep return\n")


# @pytest.mark.algotest
def test_atoc():
    config = [deepcopy(cooperative_navigation_atoc_config), deepcopy(cooperative_navigation_atoc_create_config)]
    try:
        serial_pipeline(config, seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("13. atoc\n")


# @pytest.mark.algotest
def test_vdn():
    config = [deepcopy(cooperative_navigation_vdn_config), deepcopy(cooperative_navigation_vdn_create_config)]
    try:
        serial_pipeline(config, seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("14. vdn\n")


# @pytest.mark.algotest
def test_qmix():
    config = [deepcopy(cooperative_navigation_qmix_config), deepcopy(cooperative_navigation_qmix_create_config)]
    try:
        serial_pipeline(config, seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("15. qmix\n")


@pytest.mark.algotest
def test_impala():
    config = [deepcopy(cartpole_impala_config), deepcopy(cartpole_impala_create_config)]
    try:
        serial_pipeline(config, seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("16. impala\n")


@pytest.mark.algotest
def test_iqn():
    config = [deepcopy(cartpole_iqn_config), deepcopy(cartpole_iqn_create_config)]
    try:
        serial_pipeline(config, seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("17. iqn\n")


@pytest.mark.algotest
def test_her_dqn():
    try:
        bitflip_dqn_main(bitflip_her_dqn_config, seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("18. her dqn\n")


@pytest.mark.algotest
def test_ppg():
    try:
        ppg_main(cartpole_ppg_config, seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("19. ppg\n")


@pytest.mark.algotest
def test_sqn():
    config = [deepcopy(cartpole_sqn_config), deepcopy(cartpole_sqn_create_config)]
    try:
        serial_pipeline(config, seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("20. sqn\n")


@pytest.mark.algotest
def test_qrdqn():
    config = [deepcopy(cartpole_qrdqn_config), deepcopy(cartpole_qrdqn_create_config)]
    try:
        serial_pipeline(config, seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("21. qrdqn\n")


@pytest.mark.algotest
def test_acer():
    config = [deepcopy(cartpole_acer_config), deepcopy(cartpole_acer_create_config)]
    try:
        serial_pipeline(config, seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("22. acer\n")


@pytest.mark.algotest
def test_selfplay():
    try:
        selfplay_main(deepcopy(league_demo_ppo_config), seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("23. selfplay\n")


@pytest.mark.algotest
def test_league():
    try:
        league_main(deepcopy(league_demo_ppo_config), seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("24. league\n")


@pytest.mark.algotest
def test_sqil():
    expert_policy_state_dict_path = './expert_policy.pth'
    config = [deepcopy(cartpole_sql_config), deepcopy(cartpole_sql_create_config)]
    expert_policy = serial_pipeline(config, seed=0)
    torch.save(expert_policy.collect_mode.state_dict(), expert_policy_state_dict_path)

    config = [deepcopy(cartpole_sqil_config), deepcopy(cartpole_sqil_create_config)]
    config[0].policy.collect.demonstration_info_path = expert_policy_state_dict_path
    try:
        serial_pipeline_sqil(config, seed=0)
    except Exception:
        assert False, "pipeline fail"
    with open("./algo_record.log", "a+") as f:
        f.write("25. sqil\n")
