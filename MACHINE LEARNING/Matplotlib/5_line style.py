import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,6])
ypoints=np.array([0,10])

plt.plot(ypoints,linestyle="dashed",color="red")
plt.show()

plt.plot(ypoints,linestyle="dashed",linewidth=55,color="#ffce00")
plt.show()

plt.plot(ypoints,ls="dashed",lw=10)
plt.show()

plt.plot(ypoints,ls="solid")
plt.show()




