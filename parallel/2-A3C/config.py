import torch

env_name = 'CartPole-v1'
gamma = 0.99
lr = 0.0001
goal_score = 200
log_interval = 10
n_step = 10
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
max_episode = 10
