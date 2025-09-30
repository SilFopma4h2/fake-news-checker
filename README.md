# 🔍 Fake News Checker

> **AI-Powered News Verification Tool**

An intelligent web application that analyzes news articles using machine learning to determine their credibility. Built as a Minimum Viable Product (MVP) for educational purposes, this tool demonstrates the practical application of Natural Language Processing and supervised learning in combating misinformation.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📖 Table of Contents

- [Features](#-features)
- [Quick Start](#-quick-start)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Technical Details](#-technical-details)
- [Model Performance](#-model-performance)
- [Educational Value](#-educational-value)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [Troubleshooting](#-troubleshooting)
- [License](#-license)

## ✨ Features

### Core Capabilities
- **🤖 AI-Powered Analysis**: Utilizes Logistic Regression for sophisticated text classification
- **📊 TF-IDF Vectorization**: Advanced natural language processing for feature extraction
- **🎯 Confidence Scoring**: Displays prediction certainty as a percentage (0-100%)
- **⚡ Real-time Results**: Instant feedback on submitted articles
- **🧹 Smart Text Processing**: Automatic cleaning, normalization, and preprocessing

### User Experience
- **🌐 Modern Web Interface**: Clean, intuitive, and responsive design
- **📱 Mobile-Friendly**: Works seamlessly on desktop and mobile devices
- **🎨 Visual Feedback**: Color-coded results (green for real, red for fake)
- **⌨️ Keyboard Shortcuts**: Press Ctrl+Enter to analyze quickly

### Technical Excellence
- **🔒 Error Handling**: Comprehensive validation and error messages
- **🚀 Easy Deployment**: Simple setup with one-command scripts
- **📦 Minimal Dependencies**: Lightweight and easy to maintain
- **🧪 Tested Components**: Includes unit tests for core functionality

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** (Check with `python3 --version`)
- **pip** (Python package installer)
- **10 MB** free disk space

### Installation

#### Option 1: Automatic Setup (Recommended)

```bash
# Clone the repository
git clone https://github.com/SilFopma4h2/OS.git
cd OS

# Run the automated setup script
chmod +x run.sh
./run.sh
```

The script will automatically:
✅ Check Python installation  
✅ Install required dependencies  
✅ Train the ML model  
✅ Start the web application  

#### Option 2: Manual Setup

```bash
# 1. Clone the repository
git clone https://github.com/SilFopma4h2/OS.git
cd OS

# 2. Install dependencies
pip install -r requirements.txt

# 3. Train the model
python train_model.py

# 4. Start the application
python app.py
```

### Access the Application

Once running, open your browser and navigate to:
```
http://localhost:5001
```

### 🎮 How to Use

1. **Paste** a news article into the text area
2. **Click** "📊 Analyseren" (Analyze)
3. **Review** the results:
   - ✅ **Real News**: Article appears authentic (green background)
   - ❌ **Fake News**: Article likely contains misinformation (red background)
   - **Confidence Score**: Model's certainty level (0-100%)

#### Example Articles

**Fake News Example:**
```
Scientists confirm aliens built pyramids using secret technology 
that was hidden from the public. Government officials refuse to 
comment on the shocking discovery that proves everything we know 
about ancient history is completely wrong.
```

**Real News Example:**
```
Scientists publish peer-reviewed study on climate change impacts. 
The research team from the university presented their findings 
at an international conference. The study analyzed data collected 
over ten years and shows trends in temperature patterns.
```

## 🧠 How It Works

The Fake News Checker uses a multi-stage pipeline to analyze text:

### 1. Text Preprocessing
- **Normalization**: Converts text to lowercase
- **Cleaning**: Removes URLs, email addresses, and special characters
- **Tokenization**: Breaks text into meaningful units
- **Whitespace Handling**: Normalizes spacing

### 2. Feature Extraction
- **TF-IDF Vectorization**: Transforms text into numerical features
  - **TF** (Term Frequency): How often words appear
  - **IDF** (Inverse Document Frequency): How unique words are
- **N-grams**: Captures both single words (unigrams) and word pairs (bigrams)
- **Feature Limit**: Up to 5,000 most informative features

### 3. Classification
- **Algorithm**: Logistic Regression with L2 regularization
- **Training**: 80/20 train-test split with stratification
- **Output**: Binary classification (Real/Fake) with probability scores

### 4. Result Presentation
- **Visual Feedback**: Color-coded results for quick understanding
- **Confidence Score**: Transparent probability metrics
- **User-Friendly**: Clear, actionable information

## 📁 Project Structure

```
OS/
├── 📄 app.py                   # Flask web application (main entry point)
├── 🤖 train_model.py           # Model training script
├── 🔧 text_processor.py        # Text preprocessing utilities
├── 🧪 test_components.py       # Unit tests for components
├── 📋 requirements.txt         # Python dependencies
├── 🚀 run.sh                   # Automated startup script
├── 📁 templates/
│   └── 🎨 index.html          # Web interface (HTML/CSS/JavaScript)
├── 📁 model/                   # Trained models (generated after training)
│   ├── fake_news_model.pkl    # Logistic Regression model
│   └── vectorizer.pkl         # TF-IDF vectorizer
├── 📖 README.md               # This file
└── 📘 QUICKSTART.md           # Quick reference guide
```

## 🔧 Technical Details

### AI/ML Stack

| Component | Technology | Details |
|-----------|-----------|---------|
| **Algorithm** | Logistic Regression | Efficient, interpretable binary classifier |
| **Vectorization** | TF-IDF | Converts text to numerical features |
| **Features** | Up to 5,000 | Unigrams and bigrams |
| **Training** | 80/20 Split | Stratified sampling for balanced classes |
| **Library** | scikit-learn | Industry-standard ML library |

### Text Processing Pipeline

```python
# Preprocessing Steps
1. Lowercase conversion          # "BREAKING NEWS" → "breaking news"
2. URL removal                   # Remove http:// links
3. Email removal                 # Remove email addresses
4. Special character filtering   # Keep only letters and spaces
5. Whitespace normalization     # Clean up extra spaces
6. TF-IDF vectorization         # Convert to numerical features
```

### Web Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend** | Flask 3.0 | Python web framework |
| **Frontend** | HTML5/CSS3 | Modern web standards |
| **JavaScript** | Vanilla JS | Client-side interactivity |
| **API** | JSON/REST | Data exchange format |
| **Styling** | CSS Grid/Flexbox | Responsive layout |

### Architecture

```
┌─────────────┐
│   Browser   │
└──────┬──────┘
       │ HTTP Request (POST /predict)
       ▼
┌─────────────┐
│    Flask    │
│  Web Server │
└──────┬──────┘
       │ Process Text
       ▼
┌─────────────┐
│    Text     │
│  Processor  │
└──────┬──────┘
       │ Vectorize
       ▼
┌─────────────┐
│   TF-IDF    │
│ Vectorizer  │
└──────┬──────┘
       │ Predict
       ▼
┌─────────────┐
│  Logistic   │
│ Regression  │
└──────┬──────┘
       │ Return Result
       ▼
┌─────────────┐
│   Browser   │
│  (Display)  │
└─────────────┘
```

## 📊 Model Performance

### Sample Dataset Metrics

| Metric | Value | Details |
|--------|-------|---------|
| **Training Set** | 24 articles | 12 fake + 12 real |
| **Test Set** | 6 articles | 3 fake + 3 real |
| **Accuracy** | ~83% | Varies with random state |
| **Training Time** | <5 seconds | On standard hardware |

### Performance Characteristics

- **Precision**: High for identifying fake news patterns
- **Recall**: Balanced detection across both classes
- **F1-Score**: Good overall performance
- **Confidence Calibration**: Probability scores reflect true uncertainty

> **⚠️ Important Note**: The sample dataset is intentionally small for MVP demonstration. For production use, train with larger, professionally curated datasets:
> - [Kaggle Fake News Dataset](https://www.kaggle.com/c/fake-news/data) (20,000+ articles)
> - [LIAR Dataset](https://www.cs.ucsb.edu/~william/data/liar_dataset.zip) (12,000+ labeled statements)
> - [FakeNewsNet](https://github.com/KaiDMML/FakeNewsNet) (Multi-source verification)

### Improving Model Accuracy

To achieve production-level performance:

1. **Larger Training Data**: Use 10,000+ articles
2. **Better Features**: Add source credibility, metadata
3. **Advanced Models**: Try ensemble methods, transformers
4. **Cross-Validation**: Use k-fold validation
5. **Hyperparameter Tuning**: Optimize model parameters

## 🎓 Educational Value

This project serves as an excellent learning resource for understanding:

### Core Concepts Demonstrated

#### 1. Machine Learning
- **Supervised Learning**: Training with labeled data
- **Classification**: Binary decision making
- **Model Evaluation**: Accuracy, precision, recall
- **Overfitting Prevention**: Train-test split methodology

#### 2. Natural Language Processing
- **Text Preprocessing**: Cleaning and normalization
- **Feature Engineering**: TF-IDF vectorization
- **Tokenization**: Breaking text into units
- **N-gram Analysis**: Capturing context with word sequences

#### 3. Web Development
- **Backend**: Flask routing, API design
- **Frontend**: HTML5, CSS3, JavaScript
- **Client-Server**: HTTP requests, JSON responses
- **UX Design**: User feedback, loading states

#### 4. Software Engineering
- **Code Organization**: Modular architecture
- **Error Handling**: Validation and exceptions
- **Documentation**: README, docstrings, comments
- **Testing**: Unit tests for components

#### 5. Data Science Workflow
- **Data Collection**: Dataset creation
- **Model Training**: Fitting and optimization
- **Evaluation**: Performance metrics
- **Deployment**: Production-ready web app

### Learning Outcomes

After exploring this project, you'll understand:

✅ How machine learning can solve real-world problems  
✅ The basics of text classification and NLP  
✅ Full-stack web development with Python  
✅ The complete ML pipeline from data to deployment  
✅ Best practices in code organization and documentation  

### Perfect For

- 📚 **Students**: School projects, portfolios
- 🎓 **Learners**: Understanding ML fundamentals
- 👨‍💻 **Developers**: Quick ML integration reference
- 🧑‍🏫 **Teachers**: Educational demonstrations

## 🔮 Future Improvements

### Planned Enhancements (Post-MVP)

#### High Priority
- [ ] **URL Scraping**: Automatically fetch articles from news websites
- [ ] **Explainability**: Show which words/phrases triggered fake detection
- [ ] **Multi-language Support**: Add Dutch, German, French language models
- [ ] **Larger Dataset**: Train with 10,000+ professionally labeled articles

#### Medium Priority
- [ ] **Advanced Models**: Implement Naive Bayes, SVM, Neural Networks
- [ ] **Model Comparison**: A/B testing dashboard for different algorithms
- [ ] **Visualizations**: Charts, graphs, and trend analysis
- [ ] **Source Analysis**: Verify publisher credibility

#### Nice to Have
- [ ] **RESTful API**: Endpoints for third-party integration
- [ ] **Database**: Store analyses and user feedback
- [ ] **User Accounts**: Save history, preferences
- [ ] **Browser Extension**: Check news while browsing
- [ ] **Fact-Checking**: Integration with fact-checking databases
- [ ] **Social Media**: Analyze tweets and posts

### Technical Improvements
- [ ] **Docker Support**: Containerized deployment
- [ ] **CI/CD Pipeline**: Automated testing and deployment
- [ ] **Performance**: Caching, async processing
- [ ] **Security**: Rate limiting, input sanitization
- [ ] **Monitoring**: Logging, analytics, error tracking

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Ways to Contribute

#### 🐛 Bug Reports
Found a bug? [Open an issue](https://github.com/SilFopma4h2/OS/issues) with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable

#### ✨ Feature Requests
Have an idea? [Submit a feature request](https://github.com/SilFopma4h2/OS/issues) with:
- Use case description
- Proposed solution
- Alternative approaches

#### 🔧 Code Contributions
Want to contribute code?

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add/update tests
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Focus Areas

Priority areas for contributions:
- 🤖 **ML Model**: Improve accuracy, try new algorithms
- 📊 **Datasets**: Add more training data
- 🎨 **UI/UX**: Design improvements, accessibility
- 📖 **Documentation**: Better examples, translations
- 🧪 **Testing**: Increase test coverage
- 🐛 **Bug Fixes**: Address known issues

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add docstrings to functions
- Write clear commit messages
- Include tests for new features

## 📝 License

MIT License - See [LICENSE](LICENSE) file for details.

Copyright (c) 2024 SilFopma4h2

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

## 🙏 Acknowledgments

- **scikit-learn**: For the excellent machine learning library
- **Flask**: For the lightweight and powerful web framework
- **Open Source Community**: For inspiration and resources

## 📞 Contact & Support

- **Author**: SilFopma4h2
- **Repository**: [github.com/SilFopma4h2/OS](https://github.com/SilFopma4h2/OS)
- **Issues**: [Report bugs or request features](https://github.com/SilFopma4h2/OS/issues)

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ for educational purposes

[Report Bug](https://github.com/SilFopma4h2/OS/issues) · [Request Feature](https://github.com/SilFopma4h2/OS/issues) · [Documentation](https://github.com/SilFopma4h2/OS/wiki)

</div>

---

## 🚨 Troubleshooting

### Common Issues and Solutions

#### Problem: Model Not Found Error

```
Error: Model nog niet getraind. Run eerst train_model.py
```

**Solution:**
```bash
python train_model.py
```

This trains the model and saves it to the `model/` directory.

---

#### Problem: Module Not Found

```
ModuleNotFoundError: No module named 'flask'
```

**Solution:**
```bash
pip install -r requirements.txt
```

If still not working, try:
```bash
pip3 install -r requirements.txt
# or
python -m pip install -r requirements.txt
```

---

#### Problem: Port Already in Use

```
OSError: [Errno 48] Address already in use
```

**Solution:**

Option 1 - Stop the conflicting process:
```bash
# Find process using port 5001
lsof -i :5001
# Kill the process
kill -9 <PID>
```

Option 2 - Change the port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5002)  # Changed from 5001
```

---

#### Problem: Low Model Accuracy

**Solutions:**
1. Train with a larger dataset (recommended)
2. Adjust hyperparameters in `train_model.py`
3. Try different algorithms (see Future Improvements)

Example hyperparameter tuning:
```python
# In train_model.py
vectorizer = TfidfVectorizer(
    max_features=10000,  # Increase from 5000
    ngram_range=(1, 3)   # Add trigrams
)

model = LogisticRegression(
    max_iter=2000,       # More iterations
    C=0.5                # Adjust regularization
)
```

---

#### Problem: Application Crashes

**Diagnostic Steps:**
1. Check Python version: `python3 --version` (need 3.8+)
2. Verify dependencies: `pip list | grep -E 'flask|scikit|joblib'`
3. Check disk space: `df -h`
4. Review error logs in terminal

---

#### Problem: Predictions Don't Make Sense

**Possible Causes:**
- Sample dataset is too small (only 30 articles)
- Text is too short (< 50 words)
- Language mismatch (model trained on English)

**Solutions:**
- Use longer, more detailed articles
- Train with a professional dataset
- Ensure text is in English

---

### Getting Help

Still having issues?

1. 📖 Check the [QUICKSTART.md](QUICKSTART.md) guide
2. 🔍 Search [existing issues](https://github.com/SilFopma4h2/OS/issues)
3. 💬 [Open a new issue](https://github.com/SilFopma4h2/OS/issues/new) with details
4. 📧 Contact: Include error messages and steps to reproduce

### Debug Mode

Run in debug mode for more information:
```bash
# In app.py, ensure debug=True
app.run(debug=True, host='0.0.0.0', port=5001)
```
