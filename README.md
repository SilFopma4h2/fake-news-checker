# Fake News Detector - MVP

Een AI-powered webapplicatie die nieuwsartikelen analyseert en voorspelt of ze fake news of echte news zijn. Dit project is ontwikkeld als MVP (Minimum Viable Product) voor een profielwerkstuk.

## ✨ Features

- **🤖 AI-Model**: Gebruikt Logistic Regression voor tekstanalyse
- **📊 TF-IDF Vectorisatie**: Geavanceerde tekstverwerking
- **🎯 Confidence Score**: Toont zekerheid van voorspelling (0-100%)
- **🌐 Webinterface**: Simpele, gebruiksvriendelijke interface
- **⚡ Real-time Analyse**: Directe feedback op ingevoerde artikelen
- **🧹 Tekstverwerking**: Automatische reiniging en preprocessing

## 🚀 Quick Start

### Vereisten

- Python 3.8 of hoger
- pip (Python package manager)

### Installatie

1. **Clone de repository**
```bash
git clone https://github.com/SilFopma4h2/OS.git
cd OS
```

2. **Installeer dependencies**
```bash
pip install -r requirements.txt
```

3. **Train het model**
```bash
python train_model.py
```

Dit zal:
- Een sample dataset creëren (15 fake + 15 real artikelen)
- Het model trainen met TF-IDF vectorisatie
- Het model evalueren en accuraatheid tonen
- Het model opslaan in de `model/` directory

4. **Start de webapplicatie**
```bash
python app.py
```

5. **Open je browser**
```
http://localhost:5000
```

### 🎮 Gebruik

1. Plak een nieuwsartikel in het tekstvak
2. Klik op "📊 Analyseren"
3. Bekijk het resultaat:
   - ✅ **Real News**: Artikel lijkt authentiek
   - ❌ **Fake News**: Artikel bevat waarschijnlijk nepnieuws
   - **Confidence Score**: Hoe zeker het model is (0-100%)

## 📁 Project Structure

```
.
├── app.py                  # Flask webapplicatie
├── train_model.py          # Model training script
├── text_processor.py       # Tekstverwerking module
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html         # Web interface
├── model/                 # Getrainde modellen (gegenereerd)
│   ├── fake_news_model.pkl
│   └── vectorizer.pkl
└── README.md              # Deze file
```

## 🔧 Technische Details

### AI/ML Stack
- **Model**: Logistic Regression (scikit-learn)
- **Vectorisatie**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Features**: Tot 5000 features, uni-grams en bi-grams
- **Training**: 80/20 train-test split met stratificatie

### Tekstverwerking
- Hoofdletters naar kleine letters
- Verwijdering van URLs en e-mailadressen
- Verwijdering van speciale karakters en cijfers
- Normalisatie van whitespace

### Web Framework
- **Backend**: Flask 3.0
- **Frontend**: Vanilla JavaScript met moderne CSS
- **API**: RESTful JSON endpoints

## 📊 Model Performance

Met de sample dataset:
- **Training set**: 24 artikelen
- **Test set**: 6 artikelen
- **Accuraatheid**: ~83% (afhankelijk van random state)

> **Note**: Voor productie gebruik, train het model met een grotere, gebalanceerde dataset zoals:
> - [Kaggle Fake News Dataset](https://www.kaggle.com/c/fake-news/data)
> - [LIAR Dataset](https://www.cs.ucsb.edu/~william/data/liar_dataset.zip)

## 🎓 Educational Value

Dit project demonstreert:
- **Machine Learning**: Supervised learning met classificatie
- **Natural Language Processing**: Tekstanalyse en feature extraction
- **Web Development**: Full-stack Python webapplicatie
- **Software Engineering**: Modulaire code structuur
- **Data Science**: Model training, evaluatie en deployment

## 🔮 Toekomstige Verbeteringen (Post-MVP)

- [ ] URL scraping: Automatisch artikelen ophalen van websites
- [ ] Explainability: Toon waarom een artikel als fake werd gezien
- [ ] Visualisaties: Grafieken en trends in nepnieuws
- [ ] Model vergelijking: Naive Bayes, SVM, Neural Networks
- [ ] Grotere dataset: Train met 10.000+ artikelen
- [ ] Nederlands taalmodel: Specifiek voor Nederlandse teksten
- [ ] API endpoints: RESTful API voor integratie
- [ ] Database: Opslaan van analyses en feedback

## 🤝 Contributing

Bijdragen zijn welkom! Focus gebieden:
- Verbetering van het ML-model
- Toevoegen van meer datasets
- UI/UX verbeteringen
- Documentatie updates
- Bug fixes

## 📝 License

MIT License - See LICENSE file for details.

## 🙏 Credits

Project ontwikkeld voor profielwerkstuk door SilFopma4h2.

---

## 🚨 Troubleshooting

### Model niet gevonden
**Probleem**: `Model nog niet getraind` error  
**Oplossing**: Run eerst `python train_model.py`

### Import errors
**Probleem**: `ModuleNotFoundError`  
**Oplossing**: Installeer dependencies: `pip install -r requirements.txt`

### Port already in use
**Probleem**: Port 5000 is al in gebruik  
**Oplossing**: 
- Stop andere applicaties op poort 5000
- Of wijzig de poort in `app.py`: `app.run(port=5001)`

### Low accuracy
**Probleem**: Model heeft lage accuraatheid  
**Oplossing**: 
- Train met een grotere dataset
- Download een professionele fake news dataset
- Pas hyperparameters aan in `train_model.py`
