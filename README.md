# Dog Daycare Monitor

A computer vision project to monitor dog daycare locations by collecting and analyzing camera feed screenshots at regular intervals.

## Overview

This project automatically captures screenshots from dog daycare webcam feeds and processes them to detect and track dogs and humans. The system is currently deployed on a **Raspberry Pi 5** with a **10-minute cron job** for continuous monitoring.

## Features

### Current Functionality

- **Automated Screenshot Collection** (`capture/`): Downloads images at regular intervals from multiple dog daycare camera feeds
- **Object Detection** (`process/`): Uses YOLOv8 model to detect and draw bounding boxes around:
  - Dogs
  - Humans
  - Displays confidence scores for each detection

### Future Goals

- Identify individual dogs (your specific dog)
- Detect dog stances and behaviors
- Track the ratio of dogs to people over time
- Generate analytics and alerts based on activity patterns

## Project Structure

```
dog-daycare/
├── capture/
│   └── download-data.py    # Script to download screenshots from camera feeds
├── process/
│   └── process-image.py    # Script to detect dogs and humans in images
└── data/                   # Storage for captured images (gitignored)
```

## Usage

### Capturing Screenshots

The capture script downloads images from configured camera feeds:

```bash
python capture/download-data.py
```

Images are saved to `data/<camera_name>/<timestamp>.jpg`

### Processing Images

Analyze an image to detect dogs and humans:

```bash
python process/process-image.py <path_to_image>
```

This will display the image with bounding boxes around detected dogs and people.

## Deployment

Currently running on a Raspberry Pi 5 with a cron job that executes every 10 minutes to collect screenshots automatically.

## Technologies

- **Python**: Core programming language
- **YOLOv8**: State-of-the-art object detection model (via Ultralytics)
- **OpenCV**: Image processing and visualization
- **Requests**: HTTP client for downloading images

## Requirements

- Python 3.x
- ultralytics
- opencv-python
- requests
