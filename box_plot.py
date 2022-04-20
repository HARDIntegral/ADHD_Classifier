import matplotlib.pyplot as plt

RBF = [50,54,50,54,50,50,50,50,54,50,50,50,50,50,50,50,50,50,50,54,50,54,50,54,50,50,50,50,50,50,50,50,54,54,50,50,54,54,54,50,54,50,50,50,50,54,54,50,54,50]
CUSTOM = [50,54,58,54,58,54,62,54,62,54,54,38,67,50,54,54,50,58,54,62,50,46,62,62,67,42,50,58,62,54,58,67,67,54,58,58,38,58,58,67,50,46,42,54,50,50,58,46,67,58,]
data = [RBF, CUSTOM]

fig = plt.figure(figsize=(8,5))
ax = fig.add_subplot(111)

bp = ax.boxplot(data, patch_artist = True, vert=1)
colors = ['#993333', '#333399']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
for median in bp['medians']:
    median.set(linewidth=3)

ax.set_xticklabels(['RBF', 'Custom'])
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

plt.xlabel('Kernel Type')
plt.ylabel('Accuracy (%)')
plt.title('Distribution of Accuracy of an SVM Model Trained With the RBF Kernel vs the Custom Kernel')

plt.show()