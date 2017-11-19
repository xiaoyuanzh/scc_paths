"""
    Copyright: Gerd Gruenert, 2017
    All rights reserved.
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# Create a figure of size 8x6 inches, 80 dots per inch
import scipy.special
from matplotlib.gridspec import GridSpec
from matplotlib.patches import Circle

from traject.scc.turnparams import TurnParams
from traject.scc.turn import Turn


# Create a new subplot from a grid of 3x3
gs = GridSpec(3, 3)
fig = plt.figure(figsize=(8, 14))
ax0 = fig.add_subplot(gs[:, :])
ax0.set_label("x-y")


tparam = TurnParams(1.0, 1.0)
# DELTA = math.pi/8
DELTA = tparam.delta_min*0.9

turn = Turn(tparam, DELTA)

# plot outer circle:
omega = tparam.omega
ax0.add_patch(Circle(omega, tparam.outer_rad, facecolor='none', edgecolor='black'))
# plot inner circle center point:
ax0.add_patch(Circle(omega, tparam.inner_rad))
ax0.plot(omega[0], omega[1], "x", color='black')

# plot whole line
XT = np.linspace(0, turn.len, 128, endpoint=True)
tra1 = turn.state(XT)
ax0.plot(tra1.x, tra1.y, color="yellow", linewidth=5.0, linestyle="-")

# plot arc segment 1
X = np.linspace(0, turn._len_clothoid_part_smalldelta, 128, endpoint=True)
tra2 = turn._state_clothoid_smalldelta_first(X)
ax0.plot(tra2.x, tra2.y, color="red", linewidth=1.0, linestyle="-")

# plot arc segment 2
X = np.linspace(turn._len_clothoid_part_smalldelta, 2*turn._len_clothoid_part_smalldelta, 128, endpoint=True)
tra3 = turn._state_clothoid_smalldelta_second(X)
ax0.plot(tra3.x, tra3.y, color="green", linewidth=1.0, linestyle="-")


# plot qg point:
ax0.plot(turn.state_qg.x, turn.state_qg.y, "bo")

# plot qi point:
ax0.plot(turn.state_qi.x, turn.state_qi.y, "bo")


# Set x limits, ticks, etc.
ax0.set_xlim(-4.0, 4.0)
ax0.set_xticks(np.linspace(-4, 4, 9, endpoint=True))
ax0.set_ylim(-4.0, 4.0)
ax0.set_yticks(np.linspace(-4, 4, 9, endpoint=True))



# Show result on screen
plt.show()
