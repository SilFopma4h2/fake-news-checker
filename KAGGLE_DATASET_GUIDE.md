# 📊 Using Kaggle Datasets with Fake News Checker

This guide shows you how to use CSV datasets from Kaggle or other sources with the Fake News Checker.

## 🎯 Quick Start

### Step 1: Download a Dataset

Popular fake news datasets:

1. **[Kaggle Fake News Dataset](https://www.kaggle.com/c/fake-news/data)** (20,000+ articles)
   - Download `train.csv`
   - Contains: `id`, `title`, `author`, `text`, `label`

2. **[LIAR Dataset](https://www.cs.ucsb.edu/~william/data/liar_dataset.zip)** (12,000+ statements)
   - Download and extract
   - Contains labeled fact-checked statements

3. **[FakeNewsNet](https://github.com/KaiDMML/FakeNewsNet)** (Multi-source)
   - Clone the repository
   - Use provided CSV files

### Step 2: Train with Your Dataset

**Basic usage (auto-detect columns):**
```bash
python train_model.py --csv path/to/your/dataset.csv
```

**Specify column names:**
```bash
python train_model.py --csv train.csv --text-column title --label-column label
```

**View all options:**
```bash
python train_model.py --help
```

## 📋 CSV Format Requirements

### Required Columns

Your CSV must have at least **2 columns**:

1. **Text column**: Contains the news article or statement
2. **Label column**: Binary classification (real vs fake)

### Auto-Detected Column Names

The script automatically detects these common column names:

**Text columns:**
- `text`
- `title`
- `article`
- `content`
- `news`
- `statement`
- `claim`

**Label columns:**
- `label`
- `target`
- `class`
- `category`
- `is_fake`
- `fake`

### Supported Label Formats

The script handles various label formats:

| Format | Example Values | Auto-Converted |
|--------|---------------|----------------|
| Binary numbers | `0`, `1` | ✅ (0=real, 1=fake) |
| Text labels | `real`, `fake` | ✅ Mapped to 0, 1 |
| Boolean | `true`, `false` | ✅ Mapped to 0, 1 |
| Custom text | `REAL`, `FAKE` | ✅ Mapped to 0, 1 |

## 📝 Example CSV Formats

### Example 1: Standard Format
```csv
text,label
"Scientists publish peer-reviewed climate study",0
"Aliens built pyramids, government confirms",1
"Stock market shows steady growth in Q3",0
"Miracle cure discovered by single doctor",1
```

### Example 2: Kaggle Format
```csv
id,title,author,text,label
1,"Breaking: New discovery","John Doe","Scientists have made...",0
2,"Shocking truth revealed","Jane Smith","Government hiding...",1
```

### Example 3: Custom Labels
```csv
article,category
"Economic report shows growth","REAL"
"Conspiracy theory about aliens","FAKE"
```

## 🚀 Complete Examples

### Example 1: Kaggle Fake News Dataset

```bash
# Download from https://www.kaggle.com/c/fake-news/data
# Then train with it:
python train_model.py --csv train.csv --text-column text --label-column label
```

### Example 2: Custom Dataset with Title

```bash
# If your CSV uses 'title' instead of 'text':
python train_model.py --csv news_data.csv --text-column title --label-column is_fake
```

### Example 3: Auto-Detection

```bash
# Let the script detect columns automatically:
python train_model.py --csv my_dataset.csv
```

Output:
```
Loading dataset from my_dataset.csv...
CSV loaded. Shape: (20000, 5)
Columns: ['id', 'title', 'text', 'label', 'source']
Auto-detected text column: 'text'
Auto-detected label column: 'label'
Dataset loaded successfully. 19998 rows after removing NaN values.
```

## ⚠️ Common Issues & Solutions

### Issue: "Could not auto-detect text column"

**Solution:** Specify the column name explicitly:
```bash
python train_model.py --csv dataset.csv --text-column your_text_column_name
```

### Issue: "Expected 2 unique labels, found 3"

**Cause:** Your dataset has more than 2 classes (e.g., `real`, `fake`, `unknown`)

**Solution:** Clean your CSV to only include two classes before training

### Issue: Missing values in dataset

**Handled automatically:** The script removes rows with NaN/missing values

Output:
```
Dataset loaded successfully. 19998 rows after removing NaN values.
```

### Issue: Large CSV file takes too long

**Expected:** Training with large datasets (20,000+ articles) may take several minutes

**Tip:** Start with a subset for testing:
```bash
# Create subset in Python
import pandas as pd
df = pd.read_csv('large_dataset.csv')
df.head(1000).to_csv('subset.csv', index=False)
```

## 📊 Expected Performance

| Dataset Size | Training Time | Expected Accuracy |
|-------------|---------------|-------------------|
| 100 articles | ~5 seconds | ~75-80% |
| 1,000 articles | ~10 seconds | ~85-88% |
| 10,000 articles | ~30 seconds | ~90-92% |
| 20,000+ articles | ~1-2 minutes | ~93-95% |

## 🔍 Verifying Your Training

After training, check the output:

```
Dataset size: 20000 articles
Fake news: 10413, Real news: 9587

Preprocessing text...
Training set: 16000, Test set: 4000

Creating TF-IDF vectorizer...
Training Logistic Regression model...

Accuracy: 92.34%

Classification Report:
              precision    recall  f1-score   support

        Real       0.91      0.93      0.92      1920
        Fake       0.94      0.92      0.93      2080

    accuracy                           0.92      4000
```

## 🎓 Tips for Best Results

1. **Use balanced datasets**: Similar number of real and fake examples
2. **Clean your data**: Remove duplicates and invalid entries
3. **Larger is better**: More training data = better accuracy
4. **Quality matters**: Use professionally labeled datasets
5. **Test with different articles**: After training, test with various news sources

## 🔗 Recommended Datasets

1. **For beginners**: Start with 1,000-5,000 articles
2. **For production**: Use 20,000+ professionally labeled articles
3. **For research**: Try multiple datasets and compare results

---

**Need help?** Check the main [README.md](README.md) or [QUICKSTART.md](QUICKSTART.md)
