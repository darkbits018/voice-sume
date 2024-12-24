import os
import random

data_dir = 'resume-corpus'  # Replace with the actual path to your data
normalized_file = os.path.join(data_dir, 'normlized_classes.txt')
skills_file = os.path.join(data_dir, 'skills_it.txt')

# Output file paths
train_file = 'resume-corpus/train.txt'
val_file = 'resume-corpus/val.txt'
test_file = 'resume-corpus/test.txt'
train_label_file = 'resume-corpus/train.lab'
val_label_file = 'resume-corpus/val.lab'
test_label_file = 'resume-corpus/test.lab'

# Read the data
with open(normalized_file, 'r') as nf, open(skills_file, 'r') as sf:
    resume_texts = nf.readlines()
    skills_labels = sf.readlines()

# Split the data into training, validation, and test sets
data = list(zip(resume_texts, skills_labels))
random.shuffle(data)

train_size = int(0.8 * len(data))  # 80% for training
val_size = int(0.1 * len(data))  # 10% for validation
test_size = len(data) - train_size - val_size

train_data = data[:train_size]
val_data = data[train_size:train_size + val_size]
test_data = data[train_size + val_size:]

# Write the splits to files
with open(train_file, 'w') as tf, open(train_label_file, 'w') as tlf:
    for text, label in train_data:
        tf.write(text + '\n')
        tlf.write(label + '\n')

with open(val_file, 'w') as vf, open(val_label_file, 'w') as vlf:
    for text, label in val_data:
        vf.write(text + '\n')
        vlf.write(label + '\n')

with open(test_file, 'w') as tf, open(test_label_file, 'w') as tlf:
    for text, label in test_data:
        tf.write(text + '\n')
        tlf.write(label + '\n')

print("Data split into train, val, and test files.")
