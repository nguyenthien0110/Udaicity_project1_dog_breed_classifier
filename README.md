# Dog Breed Classifier

This project utilizes a pre-trained image classifier to identify dog breeds from images. It includes scripts for processing images, classifying them using a selected model architecture, and verifying the classification results against expected dog breed labels.

## Getting Started

### Prerequisites

- Python 3.8.0
- PyTorch (for image classification)
- torchvision (for image transformation and model loading)

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/nguyenthien0110Udaicity_project1_dog_breed_classifier.git
   cd dog-breed-classifier
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Usage

1. Place your pet images in the `pet_images/` directory.
2. Update `dognames.txt` with the list of dog breeds you want to recognize.
3. Run the classifier script:
   ```
   python classify_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
   ```

### Command Line Arguments

- `--dir`: Path to the folder containing pet images (default: `pet_images/`)
- `--arch`: Model architecture to use for classification (default: `vgg`)
- `--dogfile`: File containing names of dog breeds for verification (default: `dognames.txt`)

### Example Output

The script will output the classification results for each image, indicating whether the predicted label matches the expected dog breed label.