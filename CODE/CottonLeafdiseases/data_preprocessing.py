import os
from sklearn.model_selection import train_test_split
from shutil import copyfile

# Set the path to your original dataset
original_data_dir = r'E:\Sai\2024 workspace\Major projects Codes-2024\74.Cotton_Leaf_Disease_Detection_using_Convolutional_Neural_Networks_CNN\Cotton_Leaf_Disease_Detection_using_Convolutional_Neural_Networks_CNN\CODE\CottonLeafdiseases\dataset'

# Set the path to create new directories for training and validation sets
base_dir = r'E:\Sai\2024 workspace\Major projects Codes-2024\74.Cotton_Leaf_Disease_Detection_using_Convolutional_Neural_Networks_CNN\Cotton_Leaf_Disease_Detection_using_Convolutional_Neural_Networks_CNN\CODE\CottonLeafdiseases\data'
os.makedirs(base_dir, exist_ok=True)

# Create directories for training and validation sets
train_dir = os.path.join(base_dir, 'train')
os.makedirs(train_dir, exist_ok=True)

val_dir = os.path.join(base_dir, 'validation')
os.makedirs(val_dir, exist_ok=True)

# List all classes (subdirectories) in the original dataset
class_names = os.listdir(original_data_dir)

# Set the proportion for validation data (e.g., 20%)
validation_split = 0.2

# Iterate over each class and split the data
for class_name in class_names:
    class_path = os.path.join(original_data_dir, class_name)
    train_class_dir = os.path.join(train_dir, class_name)
    val_class_dir = os.path.join(val_dir, class_name)
    
    os.makedirs(train_class_dir, exist_ok=True)
    os.makedirs(val_class_dir, exist_ok=True)
    
    # List all files in the class directory
    files = os.listdir(class_path)
    
    # Split the files into training and validation sets
    train_files, val_files = train_test_split(files, test_size=validation_split, random_state=42)
    
    # Copy files to the respective directories
    for file in train_files:
        src_path = os.path.join(class_path, file)
        dst_path = os.path.join(train_class_dir, file)
        copyfile(src_path, dst_path)
    
    for file in val_files:
        src_path = os.path.join(class_path, file)
        dst_path = os.path.join(val_class_dir, file)
        copyfile(src_path, dst_path)

# Now, 'train_dir' contains the training set, and 'val_dir' contains the validation set
