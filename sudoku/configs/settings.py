# System imports.
import os
from datetime import datetime


# env config
render_train     = False
render_test      = False
overwrite_render = True
record           = True
high             = 9 # 255.

# output config
timestamp = datetime.now().strftime("%Y-%m-%d %HH%M")
output_path = os.path.join("results", f"13-actions {timestamp}")
model_output = os.path.join(output_path, "model.weights")
log_path = os.path.join(output_path, "log.txt")
plot_output = os.path.join(output_path, "scores.png")
summarize_output = os.path.join(output_path, "summarize.png")
record_path = os.path.join(output_path, "records")

# model and training config
num_episodes_test = 20
grad_clip         = True
clip_val          = 10
saving_freq       = 50000
log_freq          = 500
eval_freq         = 50000
record_freq       = 50000
soft_epsilon      = 0.05

# hyper params
nsteps_train       = 3000000
batch_size         = 256
buffer_size        = 300000
target_update_freq = 500
gamma              = 0.99
learning_freq      = 4
state_history      = 4
lr_begin           = 0.00005
lr_end             = 0.0000005
lr_nsteps          = 2750000
eps_begin          = 1
eps_end            = 0.01
eps_nsteps         = 2500000
learning_start     = 300000


# Environment settings
MAX_STEPS = 10000

N_ACTIONS = 9 + 4
OBS_SHAPE = (9, 9, 2)

DIM_DENSE_1 = 64
DIM_DENSE_2 = 64


try:
    from .local_settings import *
except:
    # No local settings - use previous ones
    pass