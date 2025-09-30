# 🚀 Fake News Checker - Quick Start Guide

## 🎯 What Is This?

An **AI-powered web application** that analyzes news articles and predicts whether they contain misinformation or are credible. Perfect for educational projects and learning about machine learning!

### Key Features
- ✅ Real-time analysis of news articles
- 🤖 Machine learning-powered detection
- 📊 Confidence scoring (0-100%)
- 🌐 Easy-to-use web interface
- ⚡ Fast results in seconds

## 🚀 Quick Setup (3 Steps!)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

**What this does:** Installs Flask, scikit-learn, and other required Python packages.

### Step 2: Train the AI Model
```bash
python train_model.py
```

**What this does:** 
- Creates a sample dataset (30 articles: 15 fake + 15 real)
- Trains a Logistic Regression classifier
- Generates a TF-IDF vectorizer
- Saves model files to `model/` directory
- Takes about 5 seconds to complete

### Step 3: Start the Application
```bash
python app.py
```

**Or use the automated script:**
```bash
./run.sh
```

### Step 4: Open Your Browser
Navigate to: **http://localhost:5001**

🎉 **You're ready to go!**

## 🎮 How to Use

### Simple 3-Step Process

1. **Paste** a news article into the text area
2. **Click** "📊 Analyseren" (Analyze button)
3. **Review** the results:
   - ✅ **Real News** = Article appears authentic (green background)
   - ❌ **Fake News** = Article likely contains misinformation (red background)
   - **Confidence**: Percentage showing how certain the model is

### Pro Tips
- 💡 Use articles with at least 50+ words for best results
- ⌨️ Press **Ctrl+Enter** to quickly analyze
- 🔄 Click "Wissen" (Clear) to start fresh

## 📊 Example Articles

### Fake News Example
```
Scientists confirm aliens built pyramids using secret technology 
that was hidden from the public. Government officials refuse to 
comment on the shocking discovery that proves everything we know 
about ancient history is completely wrong.
```
**Expected Result:** ❌ Fake News (~60-70% confidence)

**Why it's fake:** Sensational claims, conspiracy language, no credible sources

### Real News Example
```
Scientists publish peer-reviewed study on climate change impacts. 
The research team from the university presented their findings 
at an international conference. The study analyzed data collected 
over ten years and shows trends in temperature patterns.
```
**Expected Result:** ✅ Real News (~60-70% confidence)

**Why it's real:** Verifiable sources, measured language, peer-reviewed research

## 🔧 Technical Overview

### AI Model Architecture

| Component | Details |
|-----------|---------|
| **Algorithm** | Logistic Regression |
| **Vectorization** | TF-IDF (Term Frequency-Inverse Document Frequency) |
| **Features** | Up to 5,000 features (unigrams + bigrams) |
| **Accuracy** | ~83% on sample dataset |

### Text Processing Steps

The model processes text through these stages:

1. **Lowercase Conversion** - "BREAKING NEWS" → "breaking news"
2. **URL Removal** - Remove http:// links  
3. **Email Removal** - Remove email addresses
4. **Special Character Filtering** - Keep only letters and spaces
5. **Whitespace Normalization** - Clean up extra spaces
6. **TF-IDF Vectorization** - Convert to numerical features

### Technology Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Flask 3.0 (Python web framework) |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Styling** | Modern gradient design, responsive |
| **API** | JSON-based RESTful endpoints |

## 📚 Project Structure

```
OS/
├── app.py                  # 🌐 Flask web application (main entry point)
├── train_model.py          # 🤖 Model training script
├── text_processor.py       # 🔧 Text preprocessing utilities
├── test_components.py      # 🧪 Unit tests for components
├── requirements.txt        # 📋 Python dependencies
├── run.sh                  # 🚀 Automated startup script
├── templates/
│   └── index.html         # 🎨 Web interface (HTML/CSS/JS)
├── model/                 # 💾 Trained models (generated after training)
│   ├── fake_news_model.pkl    # Logistic Regression model
│   └── vectorizer.pkl         # TF-IDF vectorizer
├── README.md              # 📖 Full documentation
└── QUICKSTART.md          # 🚀 This quick reference guide
```

## ⚙️ Improving Model Performance

### Option 1: Use a Real Dataset

For production-level accuracy, train with professional datasets:

**Step 1:** Download a dataset
- [Kaggle Fake News Dataset](https://www.kaggle.com/c/fake-news/data) (20,000+ articles)
- [LIAR Dataset](https://www.cs.ucsb.edu/~william/data/liar_dataset.zip) (12,000+ statements)
- [FakeNewsNet](https://github.com/KaiDMML/FakeNewsNet) (Multi-source)

**Step 2:** Modify `train_model.py`
```python
# Replace the sample data section with:
df = pd.read_csv('your_dataset.csv')
# Ensure columns: 'text' and 'label' (0=real, 1=fake)
```

**Step 3:** Retrain
```bash
python train_model.py
```

### Option 2: Hyperparameter Tuning

Fine-tune model parameters in `train_model.py`:

```python
# TF-IDF Vectorizer Settings
vectorizer = TfidfVectorizer(
    max_features=10000,     # More features (default: 5000)
    min_df=2,              # Min document frequency
    max_df=0.8,            # Max document frequency
    ngram_range=(1, 3)     # Add trigrams (default: 1,2)
)

# Logistic Regression Settings
model = LogisticRegression(
    max_iter=2000,         # More iterations (default: 1000)
    C=1.0,                 # Regularization strength
    solver='lbfgs',        # Optimization algorithm
    random_state=42        # For reproducibility
)
```

### Performance Expectations

| Dataset Size | Expected Accuracy |
|--------------|-------------------|
| 30 articles (sample) | ~83% |
| 1,000 articles | ~88% |
| 10,000 articles | ~92% |
| 20,000+ articles | ~95% |

## 🧪 Testing

Run the component tests to verify everything works:

```bash
python test_components.py
```

**What gets tested:**
- ✅ Text processing functions
- ✅ Model file existence
- ✅ Predictions with sample data
- ✅ Confidence score calculation

**Expected output:**
```
Testing text processor...
✓ Text cleaned successfully
Testing model loading...
✓ Model loaded successfully
Testing predictions...
✓ Predictions working
All tests passed! ✅
```

## 🎓 Educational Value

### What You'll Learn

This project teaches:

1. **Machine Learning Fundamentals**
   - Supervised learning classification
   - Train-test split methodology
   - Model evaluation metrics

2. **Natural Language Processing**
   - Text preprocessing techniques
   - TF-IDF vectorization
   - Feature engineering

3. **Web Development**
   - Backend: Flask routing, APIs
   - Frontend: HTML, CSS, JavaScript
   - Client-server communication

4. **Software Engineering**
   - Code organization and modularity
   - Error handling and validation
   - Testing and documentation

5. **Data Science Pipeline**
   - Data preparation
   - Model training and evaluation
   - Deployment to production

### MVP Checklist ✅

- [x] Dataset creation (sample articles)
- [x] ML model (Logistic Regression)
- [x] Text preprocessing (cleaning, TF-IDF)
- [x] Web interface (Flask + HTML/CSS/JS)
- [x] Real-time predictions
- [x] Confidence scoring
- [x] Error handling
- [x] Documentation

### Future Enhancements (Post-MVP)

Ideas for expanding the project:

- [ ] **URL Scraping** - Automatically fetch articles from websites
- [ ] **Explainability** - Show which words triggered fake detection  
- [ ] **Visualizations** - Charts, graphs, trend analysis
- [ ] **Model Comparison** - Naive Bayes, SVM, Neural Networks
- [ ] **Larger Dataset** - Train with 10,000+ articles
- [ ] **Multi-language** - Support Dutch, German, French
- [ ] **Database** - Store analysis history
- [ ] **User Feedback** - Improve model with user corrections
- [ ] **Browser Extension** - Check news while browsing
- [ ] **API Endpoints** - RESTful API for integrations

## 💡 Usage Tips

1. **Article Length** - Use articles with 50+ words for best accuracy
2. **Confidence Scores** - Lower scores mean the model is less certain
3. **Language** - Model works best with English text
4. **Testing** - Try various article types to see how the model responds
5. **Training Data** - More training data = better accuracy

## 🐛 Troubleshooting

### "Model not trained" error
```bash
python train_model.py
```

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### "Port 5001 already in use"
Edit `app.py` and change:
```python
app.run(debug=True, host='0.0.0.0', port=5002)  # Changed port
```

### Low accuracy predictions
- Train with a larger dataset (recommended)
- Adjust hyperparameters (see section above)
- Use longer, more detailed articles
- Ensure articles are in English

### Can't access the application
1. Check if Flask is running (look for "Running on http://...")
2. Verify firewall isn't blocking port 5001
3. Try accessing `http://127.0.0.1:5001` instead
4. Check terminal for error messages

## 📞 Support

Need help? Here's what to do:

1. 📖 Read the full [README.md](README.md) for detailed information
2. 🔍 Check the [Troubleshooting](#-troubleshooting) section above
3. 💬 Search [existing issues](https://github.com/SilFopma4h2/OS/issues)
4. 🐛 [Open a new issue](https://github.com/SilFopma4h2/OS/issues/new) with details

## 🎉 Ready to Go!

You now have a working AI-powered Fake News Checker!

### Next Steps

1. ✅ Test with different articles
2. 📊 Check model accuracy on various texts
3. 🔧 Improve the model with more data
4. 🎓 Present your project!

---

<div align="center">

**Made for educational purposes | MIT License**

⭐ **Star this repo if you find it helpful!**

[Report Bug](https://github.com/SilFopma4h2/OS/issues) · [Request Feature](https://github.com/SilFopma4h2/OS/issues) · [Full Documentation](README.md)

</div>
