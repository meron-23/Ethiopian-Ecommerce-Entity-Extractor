import json

with open("data/processed/ner_dataset_50.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Deduplicate based on "tokens" list
unique = []
seen = set()

for item in data:
    tok_str = " ".join(item["tokens"])
    if tok_str not in seen:
        seen.add(tok_str)
        unique.append(item)

print(f"✅ Cleaned dataset: {len(data)} → {len(unique)} unique samples")

with open("data/processed/ner_dataset_50_cleaned.json", "w", encoding="utf-8") as f:
    json.dump(unique, f, ensure_ascii=False, indent=2)
