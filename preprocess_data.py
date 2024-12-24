import logging
import os
import torch
from transformers import AutoTokenizer, BertTokenizer, BertForSequenceClassification
from torch.utils.data import Dataset


class ResumeDataset(Dataset):
    def __init__(self, text_file, label_file, tokenizer, max_len=512):
        self.texts = []
        self.labels = []
        self.tokenizer = tokenizer
        self.max_len = max_len

        with open(text_file, 'r') as f:
            self.texts = f.read().splitlines()

        with open(label_file, 'r') as f:
            self.labels = f.read().splitlines()

        # Debugging: Print number of lines in text and label files
        print(f"Number of text lines: {len(self.texts)}")
        print(f"Number of label lines: {len(self.labels)}")

        assert len(self.texts) == len(self.labels), "Mismatch in number of text and label lines"

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        labels = self.labels[idx].split(':::')  # Split based on delimiter if necessary

        encoding = self.tokenizer(
            text,
            padding='max_length',
            truncation=True,
            max_length=self.max_len,
            return_tensors="pt"
        )

        # Convert labels to integers while ignoring the extra parts (if applicable)
        label_list = []
        for label in labels:
            try:
                label_list.append(int(label))
            except ValueError:
                pass  # Skip non-integer labels if necessary

        return {
            'input_ids': encoding['input_ids'].squeeze(),
            'attention_mask': encoding['attention_mask'].squeeze(),
            'labels': torch.tensor(label_list)  # Use list of parsed integers
        }


if __name__ == "__main__":
    data_dir = 'resume-corpus'  # Directory where .txt and .lab files are located
    train_file = 'train.txt'
    train_label_file = 'train.lab'
    val_file = 'val.txt'
    val_label_file = 'val.lab'

    tokenizer = BertTokenizer.from_pretrained('allenai/scibert_scivocab_uncased')
    model = BertForSequenceClassification.from_pretrained('allenai/scibert_scivocab_uncased')

    train_dataset = ResumeDataset(os.path.join(data_dir, train_file), os.path.join(data_dir, train_label_file),
                                  tokenizer)
    val_dataset = ResumeDataset(os.path.join(data_dir, val_file), os.path.join(data_dir, val_label_file), tokenizer)

    # Save only the tensors
    torch.save({
        'train_input_ids': [train_dataset[idx]['input_ids'] for idx in range(len(train_dataset))],
        'train_attention_mask': [train_dataset[idx]['attention_mask'] for idx in range(len(train_dataset))],
        'train_labels': [train_dataset[idx]['labels'] for idx in range(len(train_dataset))],
    }, 'train_dataset.pt')

    torch.save({
        'val_input_ids': [val_dataset[idx]['input_ids'] for idx in range(len(val_dataset))],
        'val_attention_mask': [val_dataset[idx]['attention_mask'] for idx in range(len(val_dataset))],
        'val_labels': [val_dataset[idx]['labels'] for idx in range(len(val_dataset))],
    }, 'val_dataset.pt')

    print("Datasets saved as tensors.")
