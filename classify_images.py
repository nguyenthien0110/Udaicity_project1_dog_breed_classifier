import time
import argparse
from get_pet_labels import get_pet_labels
from check_images import load_model, classify_image, read_dognames, is_dog

def get_input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='pet_images/', help='Path to the folder of pet images')
    parser.add_argument('--arch', type=str, default='vgg', help='Model architecture')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help='File that contains dognames')
    return parser.parse_args()

if __name__ == "__main__":
    start_time = time.time()
    
    in_arg = get_input_args()
    pet_labels = get_pet_labels(in_arg.dir)
    
    model = load_model(in_arg.arch)
    dognames = read_dognames(in_arg.dogfile)

    for filename, label in pet_labels.items():
        image_path = in_arg.dir + filename
        predicted_label_index = classify_image(model, image_path)
        predicted_label = dognames[predicted_label_index] if predicted_label_index < len(dognames) else "Unknown"
        
        pet_label_is_dog = is_dog(label[0], dognames)
        predicted_label_is_dog = is_dog(predicted_label, dognames)
        
        if pet_label_is_dog and predicted_label_is_dog:
            print(f"Both labels are dogs: {filename} - {label}")
        elif not pet_label_is_dog and not predicted_label_is_dog:
            print(f"Both labels are not dogs: {filename} - {label}")
        else:
            print(f"Mismatch: {filename} - {label} vs {predicted_label}")

    end_time = time.time()
    print(f"Total execution time: {end_time - start_time} seconds")
