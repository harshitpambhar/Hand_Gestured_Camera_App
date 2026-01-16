# 📸 Hand Gesture Camera App

<div align="center">

**A sophisticated Python-based camera application with AI-powered gesture controls, real-time filters, and professional video recording capabilities.**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Latest-orange.svg)](https://mediapipe.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Documentation](#-documentation)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Gesture Controls](#-gesture-controls)
- [Available Filters](#-available-filters)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

---

## 🌟 Overview

The **Hand Gesture Camera App** is an innovative computer vision application that combines traditional camera functionality with cutting-edge hand gesture recognition technology. Built with Python, OpenCV, and MediaPipe, this application enables users to control their camera experience entirely hands-free using intuitive pinch gestures.

### Key Highlights

- 🤚 **AI-Powered Gesture Recognition** - Utilizes Google's MediaPipe for accurate hand tracking
- 🎨 **Real-Time Filter Processing** - Apply professional filters with zero latency
- 📹 **HD Video Recording** - Record high-quality videos at 1280x720 resolution
- 🖱️ **Dual Control System** - Both gesture and mouse controls for maximum flexibility
- 🎯 **High Accuracy** - 70% confidence threshold for precise gesture detection

---

## ✨ Features

### 🎥 Camera Management
- **Live Preview**: Real-time camera feed with 1280x720 HD resolution
- **Camera Flip**: Toggle between front/back cameras or mirror the view
- **Frame Rate Optimization**: Smooth 30+ FPS performance

### 🤚 Gesture Controls
- **Pinch-to-Click**: Use thumb and index finger pinch gestures to interact
- **Visual Feedback**: Real-time hand landmark visualization
- **Smart Debouncing**: Prevents accidental multiple activations
- **Single Hand Detection**: Optimized for stable tracking with one hand

### 📸 Photo Capture
- **3-Second Countdown**: Automatic countdown timer before capture
- **Gesture or Click**: Trigger captures via gesture or button
- **Auto-Save**: Images automatically saved to `captures/` directory
- **Timestamped Files**: Organized naming with date and time

### 📹 Video Recording
- **Start/Stop Toggle**: Easy recording control via gesture or button
- **Visual Indicator**: On-screen recording status display
- **High-Quality Output**: AVI format with XVID codec
- **Real-Time Encoding**: No post-processing delays

### 🎨 Filter System
- **5 Professional Filters**:
  - 🌅 **Sepia**: Vintage warm tone effect
  - ⚫ **Grayscale**: Classic black and white
  - 🌫️ **Blur**: Gaussian blur with adjustable kernel
  - 🔲 **Edge Detection**: Canny edge algorithm
  - ✨ **None**: Original unfiltered view
- **Interactive Menu**: Easy filter selection interface
- **Real-Time Application**: Instant filter preview

### 🖥️ User Interface
- **Custom UI Components**: Professionally designed buttons and menus
- **Hover Effects**: Visual feedback for better UX
- **Lock Mechanism**: Prevents rapid fire actions
- **Responsive Design**: Adaptive to screen resolution

---

## 🎬 Demo

### Application in Action

```
┌─────────────────────────────────────────┐
│  [📷]  [🎥]  [🎨]           [🔄]  [❌]   │  ← UI Controls
│                                         │
│                                         │
│         👆 Pinch to Control            │
│                                         │
│           [Hand Tracking]               │
│                                         │
│                                         │
│  Current Filter: Sepia                  │
│  Status: Recording...                   │
└─────────────────────────────────────────┘
```

### Screenshots

*[Add your screenshots here]*

- Main interface with gesture controls
- Filter selection menu
- Capture countdown timer
- Video recording indicator

---

## 🔧 Prerequisites

Before installation, ensure you have the following:

### System Requirements
- **Operating System**: Windows 10/11, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Python**: Version 3.8 or higher
- **Webcam**: Built-in or USB camera
- **RAM**: Minimum 4GB (8GB recommended)
- **Processor**: Intel i5 or equivalent (for smooth gesture tracking)

### Software Dependencies
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

---

## 📦 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/Hand_Gestured_Camera_App.git
cd Hand_Gestured_Camera_App
```

### Step 2: Create Virtual Environment (Recommended)

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Verify Installation

```bash
python -c "import cv2, mediapipe; print('Installation successful!')"
```

### Core Dependencies

The application requires these key packages:
- **opencv-python (cv2)** - Computer vision and camera handling
- **mediapipe** - Hand tracking and gesture recognition
- **numpy** - Numerical operations and filter processing

---

## 🚀 Usage

### Starting the Application

```bash
python app.py
```

The application will:
1. Initialize the camera (default: 1280x720 resolution)
2. Open a window titled "Live Preview (PRESS 'q' to Quit)"
3. Start MediaPipe hand tracking
4. Display the UI control panel

### Basic Workflow

1. **Position Your Hand**: Hold your hand in front of the camera
2. **Make a Pinch Gesture**: Touch thumb and index finger together
3. **Interact**: Move your index finger to hover over buttons
4. **Click**: Pinch gesture acts as a click when over UI elements

---

## 🤚 Gesture Controls

### Hand Tracking Settings

```python
Detection Confidence: 0.7 (70%)
Tracking Confidence: 0.7 (70%)
Max Hands: 1 (optimized for stability)
```

### Pinch Gesture Detection

The pinch gesture is detected when:
- Distance between thumb tip and index finger tip < 0.05 (normalized)
- Works in any camera orientation
- Visual feedback: Red circles on finger tips

### Control Mapping

| Action | Gesture Control | Mouse Control | Result |
|--------|----------------|---------------|---------|
| Capture Photo | Pinch over 📷 button | Click 📷 button | 3-second countdown → Photo saved |
| Start/Stop Video | Pinch over 🎥 button | Click 🎥 button | Toggle recording |
| Open Filters | Pinch over 🎨 button | Click 🎨 button | Display filter menu |
| Select Filter | Pinch over filter name | Click filter name | Apply selected filter |
| Flip Camera | Pinch over 🔄 button | Click 🔄 button | Mirror video feed |
| Exit App | Press 'q' key | Click ❌ button | Close application |

### Tips for Best Gesture Recognition

- ✅ Ensure good lighting conditions
- ✅ Keep hand within camera frame
- ✅ Make deliberate, clear pinch gestures
- ✅ Wait for button hover state before pinching
- ❌ Avoid rapid hand movements
- ❌ Don't position hand too close to camera

---

## 🎨 Available Filters

### 1. **None (Original)**
- No processing applied
- Full-color original camera feed
- Best performance (no computational overhead)

### 2. **Grayscale**
```python
Converts: BGR → Grayscale → BGR
Algorithm: OpenCV cvtColor
Use Case: Classic black & white photography
```

### 3. **Sepia**
```python
Color Transform Matrix:
[0.272, 0.534, 0.131]
[0.349, 0.686, 0.168]
[0.393, 0.769, 0.189]
Use Case: Vintage, warm-toned aesthetic
```

### 4. **Blur**
```python
Method: Gaussian Blur
Kernel Size: 15x15
Use Case: Soft focus, background blur effect
```

### 5. **Edge Detection**
```python
Algorithm: Canny Edge Detection
Thresholds: 50 (min), 150 (max)
Use Case: Artistic outline effect, computer vision debugging
```

---

## 📁 Project Structure

```
Hand_Gestured_Camera_App/
│
├── 📄 app.py                          # Main application entry point
├── 📄 requirements.txt                # Python dependencies
├── 📄 README.md                       # Project documentation
│
├── 📁 actions/                        # Action handlers
│   ├── 📄 capture.py                  # Photo capture logic
│   └── 📄 record.py                   # Video recording logic
│
├── 📁 camera/                         # Camera management
│   ├── 📄 __init__.py
│   └── 📄 camera_feed.py              # Camera initialization & feed
│
├── 📁 filters/                        # Image processing filters
│   └── 📄 basic_filters.py            # Filter implementations
│
├── 📁 gestures/                       # Hand tracking & gesture detection
│   ├── 📄 __init__.py
│   ├── 📄 hand_tracker.py             # MediaPipe hand tracking
│   └── 📄 pinch.py                    # Pinch gesture detection
│
├── 📁 ui/                             # User interface components
│   ├── 📄 __init__.py
│   ├── 📄 capture_button.py           # Photo capture button
│   ├── 📄 video_button.py             # Video recording button
│   ├── 📄 filters_icon.py             # Filter button
│   ├── 📄 filters_menu.py             # Filter selection menu
│   ├── 📄 flip_camera.py              # Camera flip button
│   └── 📄 close_button.py             # Application close button
│
├── 📁 utils/                          # Utility functions
│   └── 📄 math_utils.py               # Mathematical calculations
│
├── 📁 captures/                       # Output directory (auto-generated)
│   ├── 📸 photo_*.jpg                 # Captured photos
│   └── 🎥 video_*.avi                 # Recorded videos
│
└── 📁 assets/                         # Application resources
    └── 📁 icons/                      # UI icons (optional)
```

### Module Descriptions

#### Core Modules

- **app.py**: Main event loop, coordinates all components
- **camera/camera_feed.py**: OpenCV camera initialization
- **gestures/hand_tracker.py**: MediaPipe Hands configuration

#### Action Modules

- **actions/capture.py**: Handles photo capture with countdown
- **actions/record.py**: Manages video recording state and file I/O

#### UI Modules

- **ui/*.py**: Individual button components with hover detection
- **ui/filters_menu.py**: Dynamic filter selection interface

#### Processing Modules

- **filters/basic_filters.py**: Image transformation algorithms
- **utils/math_utils.py**: Distance calculations for gesture detection

---

## ⚙️ Configuration

### Camera Settings

Edit in `app.py`:

```python
# Resolution (default: 1280x720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Frame rate (if supported by camera)
cap.set(cv2.CAP_PROP_FPS, 30)
```

### Gesture Sensitivity

Edit in `gestures/hand_tracker.py`:

```python
hands = mp_hands.Hands(
    min_detection_confidence=0.7,  # Lower = more sensitive
    min_tracking_confidence=0.7,   # Lower = more responsive
)
```

### Capture Delay

Edit in `app.py`:

```python
capture_delay = 3  # Seconds before photo capture
```

### Filter Parameters

Edit in `filters/basic_filters.py`:

```python
# Blur intensity
def apply_blur(frame, ksize=15):  # Increase for more blur

# Edge detection sensitivity
edges = cv2.Canny(gray, 50, 150)  # Adjust thresholds
```

---

## 🐛 Troubleshooting

### Common Issues

#### 1. **Camera Not Opening**

```
Error: "❌ Frame not received"
```

**Solutions:**
- Check if another application is using the camera
- Try changing camera index in `camera/camera_feed.py`:
  ```python
  cap = cv2.VideoCapture(0)  # Try 1, 2, etc.
  ```
- Verify camera permissions in system settings
- Test camera with: `python -c "import cv2; print(cv2.VideoCapture(0).read())"`

#### 2. **Hand Not Detected**

**Solutions:**
- Improve lighting conditions
- Position hand within 0.5-2 meters from camera
- Ensure hand is fully visible (all fingers in frame)
- Lower detection confidence in `hand_tracker.py`
- Check for MediaPipe installation: `pip install --upgrade mediapipe`

#### 3. **Gesture Not Responding**

**Solutions:**
- Make pinch gesture more deliberate (thumb and index finger clearly touching)
- Check if cursor circles appear on fingertips
- Adjust pinch threshold in `gestures/pinch.py`
- Ensure button hover state is activated before pinching

#### 4. **Low Frame Rate**

**Solutions:**
- Close other applications
- Disable filter when not needed (use "None")
- Reduce camera resolution in `app.py`
- Check CPU usage and system resources

#### 5. **Import Errors**

```
ModuleNotFoundError: No module named 'cv2'
```

**Solutions:**
```bash
pip install opencv-python mediapipe numpy
# Or reinstall all dependencies
pip install -r requirements.txt --force-reinstall
```

#### 6. **Captures Folder Missing**

**Solutions:**
- The folder is auto-created on first capture
- Manually create: `mkdir captures`
- Check write permissions in application directory

### Debug Mode

Enable detailed logging by adding to `app.py`:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Getting Help

If issues persist:
1. Check [existing issues](https://github.com/yourusername/Hand_Gestured_Camera_App/issues)
2. Create a new issue with:
   - Operating system and version
   - Python version (`python --version`)
   - Error messages/screenshots
   - Steps to reproduce

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

### How to Contribute

1. **Fork the Repository**
   ```bash
   git clone https://github.com/yourusername/Hand_Gestured_Camera_App.git
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **Make Your Changes**
   - Follow existing code style
   - Add comments for complex logic
   - Update documentation if needed

4. **Test Your Changes**
   - Ensure application runs without errors
   - Test all gesture controls
   - Verify filters work correctly

5. **Commit Your Changes**
   ```bash
   git commit -m "Add: Amazing new feature"
   ```

6. **Push to Branch**
   ```bash
   git push origin feature/AmazingFeature
   ```

7. **Open a Pull Request**
   - Describe your changes
   - Reference any related issues
   - Wait for review

### Code Style Guidelines

- Follow PEP 8 for Python code
- Use descriptive variable names
- Add docstrings to functions
- Keep functions focused and concise

### Feature Suggestions

We're particularly interested in:
- 🎯 Additional gesture types (swipe, wave, etc.)
- 🎨 More advanced filters (face beautification, AR effects)
- 📊 Performance optimizations
- 🌐 Multi-language support
- 📱 Mobile app version

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

[Full MIT License text...]
```

---

## 🙏 Acknowledgments

### Technologies Used

- **[OpenCV](https://opencv.org/)** - Computer vision library for camera handling and image processing
- **[MediaPipe](https://mediapipe.dev/)** - Google's ML framework for hand tracking and landmark detection
- **[NumPy](https://numpy.org/)** - Numerical computing for efficient array operations

### Inspiration

This project was inspired by:
- Touchless interface needs during the global pandemic
- Accessibility requirements for hands-free computing
- Modern gesture-based interaction paradigms

### Special Thanks

- Google MediaPipe team for excellent hand tracking models
- OpenCV community for comprehensive documentation
- All contributors and testers

---

## 📞 Contact

**Project Maintainer**: [Your Name]

- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)

**Project Link**: [https://github.com/yourusername/Hand_Gestured_Camera_App](https://github.com/yourusername/Hand_Gestured_Camera_App)

---

## 🗺️ Roadmap

### Version 1.0 (Current)
- ✅ Basic hand gesture recognition
- ✅ Photo capture with countdown
- ✅ Video recording
- ✅ 5 essential filters
- ✅ Interactive UI components

### Version 1.1 (Planned)
- ⏳ Multi-hand support
- ⏳ Custom filter creation
- ⏳ Settings configuration UI
- ⏳ Photo gallery viewer

### Version 2.0 (Future)
- 🔮 Face filters and effects
- 🔮 Cloud storage integration
- 🔮 Social media sharing
- 🔮 AI-powered photo enhancement
- 🔮 Voice commands integration

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star! ⭐**

Made with ❤️ and Python

[Report Bug](https://github.com/yourusername/Hand_Gestured_Camera_App/issues) • [Request Feature](https://github.com/yourusername/Hand_Gestured_Camera_App/issues) • [Documentation](https://github.com/yourusername/Hand_Gestured_Camera_App/wiki)

</div>
