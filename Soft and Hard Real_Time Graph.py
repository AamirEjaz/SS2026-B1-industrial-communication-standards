import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8, 5))

# Hard Real-Time (red solid)
x_hard = [0, 5, 5, 10]
y_hard = [5, 5, 0, 0]
ax.plot(x_hard, y_hard, color='red', linewidth=2, label='Hard real-time')

# Soft Real-Time (green dashed)
x_soft = [0, 5, 10]
y_soft = [5, 5, 5 - 0.6 * (10 - 5)]
ax.plot(x_soft, y_soft, color='green', linewidth=2,
        linestyle='--', dashes=(6, 4), label='Soft real-time')

# Deadline vertical dotted line 
ax.axvline(x=5, color='gray', linestyle=':', linewidth=1)

# Annotations 
ax.annotate('Deadline', xy=(5.1, 4.2), fontsize=9, color='gray')

# Axis labels
ax.set_xlabel('Time', fontsize=11)
ax.set_ylabel('Utility / Value', fontsize=11)

# X axis tick labels
ax.set_xticks([0, 5, 10])
ax.set_xticklabels(['Start', 'Deadline', 'Later'])

# Y axis tick labels
ax.set_yticks([0, 5])
ax.set_yticklabels(['0\n(no value)', 'High\nvalue'])

# Legend
ax.legend(loc='upper right', fontsize=9)

# Clean up borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('realtime_graph.png', dpi=300, bbox_inches='tight')
plt.show()