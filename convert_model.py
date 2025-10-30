import sys
import os

# Create a dummy module to satisfy the import
class DummyModule:
    def __getattr__(self, name):
        return DummyModule()
    
    def __call__(self, *args, **kwargs):
        return DummyModule()

# Inject the dummy module BEFORE any imports
sys.modules['tensorflow_decision_forests'] = DummyModule()

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Now import tensorflowjs
import tensorflowjs as tfjs
from tensorflow import keras

try:
    # Load your Keras model
    print("Loading model...")
    model = keras.models.load_model('./models/mnist_cnn.h5')
    print("Model loaded successfully!")
    
    # Convert and save to tfjs format
    print("Converting to TensorFlow.js format...")
    tfjs.converters.save_keras_model(model, './tfjs_model')
    print("✓ Model converted successfully to ./tfjs_model")
    print("\nFiles created:")
    print("  - model.json")
    print("  - group1-shard1of*.bin")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()