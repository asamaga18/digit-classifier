# 🧠 MNIST Digit Recognizer Web App

A web-based handwritten digit recognition system using TensorFlow.js. Draw digits 0-9 on a canvas and watch AI predict them in real-time!

![Demo](https://img.shields.io/badge/Status-Working-brightgreen)
![TensorFlow](https://img.shields.io/badge/TensorFlow.js-4.11.0-orange)
![Python](https://img.shields.io/badge/Python-3.8+-blue)

## 📋 Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Model Architecture](#model-architecture)
- [Troubleshooting](#troubleshooting)
- [Future Improvements](#future-improvements)

## ✨ Features

- 🎨 **Interactive Canvas** - Draw digits with your mouse or touch screen
- 🤖 **Real-time Prediction** - Instant AI-powered digit recognition
- 📊 **Confidence Scores** - See probability distribution for all 10 digits
- 🎯 **99%+ Accuracy** - Trained on the MNIST dataset
- 📱 **Responsive Design** - Works on desktop and mobile devices
- 🌐 **No Backend Required** - Runs entirely in the browser

## 🎬 Demo

1. Draw a digit (0-9) on the black canvas
2. Click "Predict" to see the AI's prediction
3. View confidence scores for all digits
4. Click "Clear" to try another digit

## 📁 Project Structure

```
MNIST_Neural_Network_App/
├── models/
│   └── mnist_cnn.h5           # Trained Keras model
├── tfjs_model/
│   ├── model.json             # TensorFlow.js model architecture
│   └── group1-shard*.bin      # Model weights
├── train_model.py             # Python script to train the model
├── convert_model.py           # Script to convert model to TensorFlow.js
├── index.html                 # Web application
└── README.md                  # This file
```

## 🚀 Setup & Installation

### Prerequisites

- Python 3.8+
- pip (Python package manager)
- A modern web browser

### Step 1: Clone the Repository

```bash
git clone <your-repo-url>
cd MNIST_Neural_Network_App
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate it
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install tensorflow==2.15.1
pip install tensorflowjs==4.22.0
```

### Step 4: Train the Model

```bash
python train_model.py
```

This will:
- Download the MNIST dataset
- Train a neural network for 5-10 epochs
- Save the model to `./models/mnist_cnn.h5`
- Display test accuracy

### Step 5: Convert Model to TensorFlow.js

```bash
python convert_model.py
```

This creates the `tfjs_model/` directory with:
- `model.json` - Model architecture
- Weight files (`.bin`)

### Step 6: Run the Web App

```bash
# Option 1: Python HTTP server
python -m http.server 8000

# Option 2: Node.js http-server
npx http-server -p 8000

# Option 3: VS Code Live Server extension
# Right-click index.html > "Open with Live Server"
```

### Step 7: Open in Browser

Navigate to: `http://localhost:8000`

## 🎮 Usage

### Drawing Tips for Better Recognition

- **Draw Large**: Fill most of the canvas
- **Center Your Digit**: Keep it in the middle
- **Use Clear Strokes**: Smooth, confident lines work best
- **Close Loops**: Make sure circles are fully closed (0, 6, 8, 9)

### Common Digit Issues

| Digit | Common Issue | Solution |
|-------|--------------|----------|
| **3** | Confused with 7 | Draw two clear bumps on the right side |
| **0** | Confused with 6 or 8 | Make a complete, smooth circle |
| **7** | Confused with 1 | Draw clear horizontal top line |
| **5** | Confused with 6 | Emphasize top horizontal line |

## 🏗️ Model Architecture

### Current Model (Simple Fully-Connected Network)

```
Input (28x28) 
    ↓
Flatten (784)
    ↓
Dense (128, ReLU)
    ↓
Dropout (0.2)
    ↓
Dense (10)
```

**Note**: Model outputs logits (raw scores). Softmax is applied in the JavaScript code for probability conversion.

**Accuracy**: ~97-98%

**Training Details**:
- Optimizer: Adam
- Loss: Sparse Categorical Crossentropy (from_logits=True)
- Epochs: 5
- No data augmentation

### Why This Architecture?

This simple architecture was chosen for:
- Fast training time (~1-2 minutes)
- Small model size (~400KB)
- Easy to understand for learning purposes
- Good baseline performance

### Future: CNN Version

A Convolutional Neural Network (CNN) version is planned for better accuracy (99%+). This would include:
- Conv2D layers for feature extraction
- MaxPooling for dimensionality reduction
- More robust to variations in handwriting

## 🔧 Troubleshooting

### Model Won't Load

**Problem**: "Error loading model"

**Solutions**:
- Ensure `tfjs_model/model.json` exists
- Check that you're accessing via `http://` not `file://`
- Verify model files are in the same directory as `index.html`
- Check browser console for detailed error messages

### Prediction Errors

**Problem**: "Error making prediction"

**Solutions**:
- Check browser console for tensor shape mismatches
- Ensure model was converted correctly
- Verify TensorFlow.js is loaded (check network tab)

### Weird Percentages (>100% or negative)

**Problem**: Confidence scores don't make sense

**Solution**: Model output doesn't have softmax activation. Either:
1. Retrain model with `activation='softmax'` on final layer
2. JavaScript already applies softmax, so this should be fixed

### Dependencies Not Installing

**Problem**: `tensorflow_decision_forests` errors

**Solution**:
```bash
pip uninstall tensorflow-decision-forests -y
# Or use the workaround script provided
```

### Canvas Drawing Issues

**Problem**: Can't draw on mobile

**Solution**: Touch events are implemented. If still having issues:
- Try a different browser
- Check that JavaScript is enabled
- Clear browser cache

## 📈 Future Improvements

- [ ] Add data augmentation during training
- [ ] Implement model comparison (show multiple predictions)
- [ ] Add "undo" button for drawing
- [ ] Save/load drawings
- [ ] Add brush size control
- [ ] Export predictions to image
- [ ] Add more visual feedback (animations)
- [ ] Implement dark mode
- [ ] Add tutorial/onboarding
- [ ] Multi-digit recognition

## 🛠️ Technologies Used

- **TensorFlow/Keras** - Model training
- **TensorFlow.js** - Browser-based inference
- **HTML5 Canvas** - Drawing interface
- **JavaScript (ES6+)** - Application logic
- **CSS3** - Styling and animations

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| Training Accuracy | ~98% |
| Test Accuracy | ~97% |
| Inference Time | <100ms |
| Model Size | ~400KB |

## 📝 License

This project is open source and available under the MIT License.