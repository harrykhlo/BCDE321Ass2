import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('classes_trial.png')

fig = plt.imshow(img)
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
plt.show()