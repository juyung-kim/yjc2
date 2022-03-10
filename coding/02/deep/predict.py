import numpy as np
import matplotlib.pyplot as plt
num = 100
plt.imshow(x_test[num])
plt.show()
result = model.predict(x_test[num:num+1])
print('label:', y_test[num:num+1])
print('predict:', np.argmax(result))
