import tensorflow as tf


#importing a premade dataset built into tensorflow
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()


#normalize data by dividng by max pixel range
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])

# To look at the logits, you can do:
# predictions = model(x_train[:1]).numpy()
# You need to always use batch data, so use [:n], and then convert to numpy() for a regular array
# For the probablities, use the softmax function:
# tf.nn.softmax(predictions).numpy()

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer="adam",
              loss = loss_fn,
              metrics=["accuracy"]

)

model.fit(x_train, y_train, epochs = 5, verbose = 1)

print("Test Data: ")
model.evaluate(x_test, y_test, verbose = 2)