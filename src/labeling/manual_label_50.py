import json

LABELS = ["PRODUCT", "PRICE", "LOCATION", "CONTACT", "O"]

def manual_bio_labeling(tokenized_data, limit=50):
    labeled_dataset = []

    for i, item in enumerate(tokenized_data):
        tokens = item["tokens"]
        print(f"\n--- MESSAGE {i + 1}/{limit} ---")
        print("🧾 Text:", " ".join(tokens))

        ner_tags = []
        prev_label = None

        for token in tokens:
            label = input(f"🔹 {token} → Label? (PRODUCT / PRICE / LOCATION / CONTACT / O): ").strip().upper()
            if label not in LABELS:
                print("⚠️ Invalid label. Using 'O'.")
                label = "O"

            if label == "O":
                ner_tags.append("O")
                prev_label = None
            else:
                if prev_label == label:
                    ner_tags.append(f"I-{label}")
                else:
                    ner_tags.append(f"B-{label}")
                    prev_label = label

        labeled_dataset.append({
            "tokens": tokens,
            "ner_tags": ner_tags
        })

        print(f"✅ Labeled sample {i + 1}\n")
        if i + 1 >= limit:
            break

    return labeled_dataset

if __name__ == "__main__":
    with open("data/processed/tokenized_messages.json", "r", encoding="utf-8") as f:
        tokenized_data = json.load(f)

    labeled_ner_data = manual_bio_labeling(tokenized_data)

    with open("data/processed/ner_dataset_50.json", "w", encoding="utf-8") as f:
        json.dump(labeled_ner_data, f, ensure_ascii=False, indent=2)

    print("🎉 Done! Saved 50 manually labeled samples to ner_dataset_50.json")
