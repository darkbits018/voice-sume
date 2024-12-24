from transformers import AutoModelForTokenClassification, AutoTokenizer
import torch

if __name__ == "__main__":
    model = AutoModelForTokenClassification.from_pretrained("./fine_tuned_sciBERT")
    tokenizer = AutoTokenizer.from_pretrained('dbmdz/scibert-base')

    test_text = "John Doe, Software Engineer, XYZ Company, Python, Java, B.Tech, 2018"
    inputs = tokenizer(test_text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)

    predictions = torch.argmax(outputs.logits, dim=-1)
    predicted_labels = [model.config.id2label[label.item()] for label in predictions[0]]
    print(predicted_labels)
