import pandas as pd
import re
import json
import os

def normalize_amharic_text(text):
    if not isinstance(text, str) or text.strip() == "":
        return ""
    
    # Remove non-informative emojis and clutter
    text = re.sub(r'[^\u1200-\u137Fa-zA-Z0-9@፩-፻ብርቢ።፡ቁ\s:/,.-]', '', text)
    text = re.sub(r'\s+', ' ', text)  # collapse whitespace
    return text.strip()

def preprocess_csv(csv_path, output_path='data/processed/messages.json'):
    df = pd.read_csv(csv_path)

    df['Cleaned_Message'] = df['Message'].apply(normalize_amharic_text)

    all_entries = []

    for _, row in df.iterrows():
        entry = {
            "channel": row['Channel Title'],
            "username": row['Channel Username'],
            "msg_id": int(row['ID']),
            "timestamp": row['Date'],
            "text": row['Cleaned_Message'],
            "image_path": row['Media Path'] if pd.notna(row['Media Path']) else None
        }
        all_entries.append(entry)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_entries, f, ensure_ascii=False, indent=2)

    print(f"✅ Preprocessed {len(all_entries)} messages and saved to {output_path}")

if __name__ == "__main__":
    preprocess_csv("telegram_data.csv")
