import json
import re

def simple_tokenize(text):
    return re.findall(r'[\u1200-\u137F\w@]+', text)

def tokenize_all_messages(json_data):
    tokenized = []
    for item in json_data:
        text = item.get("text", "")
        tokens = simple_tokenize(text)
        if tokens:
            tokenized.append({"tokens": tokens})
    return tokenized

if __name__ == "__main__":
    with open("messages.json", "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    tokenized_data = tokenize_all_messages(raw_data)

    with open("tokenized_messages.json", "w", encoding="utf-8") as f:
        json.dump(tokenized_data, f, ensure_ascii=False, indent=2)

    print("✅ Tokenized all messages and saved to tokenized_messages.json")
