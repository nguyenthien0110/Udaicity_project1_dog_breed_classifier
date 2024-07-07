from os import listdir

def get_pet_labels(image_dir):
    pet_labels = {}
    filenames = listdir(image_dir)
    
    for filename in filenames:
        if filename[0] != ".":
            label = ' '.join([word.lower() for word in filename.split('_') if word.isalpha()])
            pet_labels[filename] = [label]
    
    return pet_labels
