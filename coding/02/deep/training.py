model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)), # 1차원 배열로
  tf.keras.layers.Dense(128, activation='relu'), # 커널 개수 128
  tf.keras.layers.Dropout(0.2), # 일부 노드 끄기. 20% 노드 끄기
  tf.keras.layers.Dense(10, activation='softmax') 
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test,  y_test)
