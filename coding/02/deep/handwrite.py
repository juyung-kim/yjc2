from os import path
from google.colab import auth
auth.authenticate_user()

from google.colab import drive
drive.mount('/content/gdrive/')

from PIL import Image
im = Image.open('./gdrive/My Drive/aaa/number.png')

plt.imshow(im)
print("사이즈 : ", im.size)
im = np.array(im)
a = model.predict(np.reshape(im, (1, 28, 28)))
print("결과", a)
print("예측율 : ",max(a[0]))
print("숫자 : ",list(a[0]).index(max(a[0])))
