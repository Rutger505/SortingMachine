# Sorting Machine Color Detection


## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate`
4. Install the requirements: `pip install -r requirements.txt`

## Usage

### Train

1. Enter Robotrain api key in `src/training/main.py`
2. Run `python src/training/main.py`

### Inference

1. Make sure user is in the dialout group: `sudo usermod -aG dialout $USER`
2. Run `python src/inference/main.py`
