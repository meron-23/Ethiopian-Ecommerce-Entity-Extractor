# Ethiopian-Ecommerce-Entity-Extractor

A machine learning pipeline for extracting product names, prices, and locations from Amharic-language Telegram e-commerce channels using Named Entity Recognition (NER).

## Features
- Telegram message scraping
- Amharic text cleaning and tokenization
- CoNLL-style NER labeling
- Fine-tuning multilingual LLMs (XLM-R, mBERT)
- OCR for text embedded in images
- SHAP and LIME for model explainability

## Directory Structure
- `data/`: Raw and processed text/images
- `src/`: All training, preprocessing, scraping logic
- `notebooks/`: Training and analysis experiments

## Setup
```bash
git clone https://github.com/meron-23/Ethiopian-Ecommerce-Entity-Extractor.git
cd Ethiopian-Ecommerce-Entity-Extractor
pip install -r requirements.txt
