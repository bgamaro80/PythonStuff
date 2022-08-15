from gym.envs.registration import register

register(
    id='tresraya-v0',
    entry_point='tresraya.envs.tresraya:TresrayaEnv',
)
