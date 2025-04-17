from tensorflow.keras.datasets import mnist  # 從keras導入mnist數據集
from tensorflow import keras
from tensorflow.keras import layers

(train_data, train_labels), (test_data, test_labels) = mnist.load_data()

train_data = train_data.reshape((60000, 28 * 28))
train_data = train_data.astype("float32") / 255

test_data = test_data.reshape((10000, 28 * 28))
test_data = test_data.astype("float32") / 255

model = keras.Sequential([
    layers.Dense(512, activation='relu'),
    layers.Dense(10, activation='softmax'),
])

model.compile(optimizer='rmsprop',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_data, train_labels, epochs=5, batch_size=128)

predictions = model.predict(test_data)
print(predictions[0])
print(predictions[0].argmax())  # 找出機率最大值的索引

test_loss, test_acc = model.evaluate(test_data, test_labels)
print('test_acc:', test_acc)
print('test_loss:', test_loss)