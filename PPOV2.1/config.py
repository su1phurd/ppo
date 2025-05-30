# config.py

# ======================
# 超参数配置
# ======================
GRID_SIZE = 500
MAX_STEPS = 1000
CONC_PEAK = 100.0
TURBULENCE_INTENSITY = 3.0

# 高斯场参数配置（仅用于数据记录和LSTM训练，不影响PPO主流程）
GAUSSIAN_RADIUS = 15.0      # 初始高斯半径σ
PEAK_CONCENTRATION = 100.0  # 源头峰值浓度

# PPO参数
GAMMA = 0.99
LAMBDA = 0.95
CLIP_EPSILON = 0.2
ENTROPY_BETA = 0.01
LEARNING_RATE = 3e-5
BATCH_SIZE = 256
EPOCHS = 5

# 探索参数
EXPLORE_BONUS = 0.6
DECAY_FACTOR = 0.999
GRID_DIVISIONS = 10
EXPLORE_DECAY_ALPHA = 0.002

# 课程学习
INITIAL_RADIUS = 50.0
MIN_RADIUS = 5.0
RADIUS_DECAY = 0.9
SUCCESS_THRESHOLD = 0.6
WINDOW_SIZE = 120

# 奖励参数
CONC_REWARD_COEF = 2.0
TKE_PENALTY_FACTOR = 0.4
BOUNDARY_PENALTY = 0.1
BOUNDARY_DECAY_START = 0.15

# 训练参数
TRAINING_SIZE = 10 # 训练集大小
