from transformers import AutoModelForTokenClassification, TrainingArguments, Trainer
import torch

from preprocess_data import ResumeDataset

# Load datasets
train_data = torch.load('train_dataset.pt')
val_data = torch.load('val_dataset.pt')

# Define training arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=5e-5,
    per_device_train_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
    save_total_limit=1,
    logging_dir="./logs",
    logging_steps=10,
    save_steps=100
)

# Instantiate the Trainer
trainer = Trainer(
    model=AutoModelForTokenClassification.from_pretrained('allenai/scibert_scivocab_uncased', num_labels=4),
    args=training_args,
    train_dataset=ResumeDataset(train_data['input_ids'], train_data['attention_mask'], train_data['labels']),
    eval_dataset=ResumeDataset(val_data['input_ids'], val_data['attention_mask'], val_data['labels'])
)

# Start training
trainer.train()
trainer.save_model("./fine_tuned_sciBERT")
