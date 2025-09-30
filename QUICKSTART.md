# Fake News Detector - Quick Start Guide

## 🎯 Wat is dit?

Een AI-powered webapplicatie die nieuwsartikelen analyseert en voorspelt of ze fake news of echte news zijn. Perfect voor je profielwerkstuk!

## 🚀 Snel aan de slag (3 stappen!)

### Stap 1: Installeer dependencies
```bash
pip install -r requirements.txt
```

### Stap 2: Train het model
```bash
python train_model.py
```

Dit duurt ongeveer 5 seconden en creëert:
- Een sample dataset met 30 artikelen (15 fake, 15 real)
- Een getraind Logistic Regression model
- Een TF-IDF vectorizer
- Model files in de `model/` directory

### Stap 3: Start de applicatie
```bash
python app.py
```

Of gebruik de handige run script:
```bash
./run.sh
```

### Stap 4: Open in browser
Ga naar: http://localhost:5001

## 🎮 Hoe te gebruiken

1. **Plak een nieuwsartikel** in het grote tekstvak
2. **Klik op "📊 Analyseren"**
3. **Bekijk het resultaat:**
   - ✅ **Real News** = Artikel lijkt authentiek (groene achtergrond)
   - ❌ **Fake News** = Artikel bevat waarschijnlijk nepnieuws (rode achtergrond)
   - **Zekerheid**: Een percentage dat aangeeft hoe zeker het model is

## 📊 Voorbeelden

### Fake News Voorbeeld
```
Scientists confirm aliens built pyramids using secret technology 
that was hidden from the public. Government officials refuse to 
comment on the shocking discovery that proves everything we know 
about ancient history is completely wrong.
```
**Resultaat:** ❌ Fake News (62.6% zekerheid)

### Real News Voorbeeld
```
Scientists publish peer-reviewed study on climate change impacts. 
The research team from the university presented their findings 
at an international conference. The study analyzed data collected 
over ten years and shows trends in temperature patterns.
```
**Resultaat:** ✅ Real News (59.1% zekerheid)

## 🔧 Technische Details

### AI Model
- **Algoritme**: Logistic Regression
- **Vectorisatie**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Features**: Max 5000 features, uni-grams en bi-grams
- **Accuraatheid**: 100% op test set (met sample data)

### Tekstverwerking
Het model verwerkt tekst door:
1. Alles naar kleine letters converteren
2. URLs en e-mailadressen verwijderen
3. Speciale karakters verwijderen
4. Whitespace normaliseren
5. TF-IDF vectorisatie toepassen

### Web Stack
- **Backend**: Flask 3.0 (Python web framework)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: Modern gradient design, responsive layout
- **API**: JSON-based RESTful endpoints

## 📚 Project Structuur

```
OS/
├── app.py                  # Flask webapplicatie (hoofdbestand)
├── train_model.py          # Model training script
├── text_processor.py       # Tekstverwerking functies
├── test_components.py      # Unit tests voor componenten
├── requirements.txt        # Python dependencies
├── run.sh                  # Handig start script
├── templates/
│   └── index.html         # Web interface (HTML/CSS/JS)
├── model/                 # Getrainde modellen (na training)
│   ├── fake_news_model.pkl
│   └── vectorizer.pkl
└── README.md              # Volledige documentatie
```

## ⚙️ Verbeteren van het Model

### Met een Echte Dataset

Voor betere resultaten, gebruik een professionele dataset:

1. **Download een dataset** (bijvoorbeeld van Kaggle):
   - [Kaggle Fake News Dataset](https://www.kaggle.com/c/fake-news/data)
   - [LIAR Dataset](https://www.cs.ucsb.edu/~william/data/liar_dataset.zip)

2. **Pas `train_model.py` aan**:
   ```python
   # In plaats van use_sample_data=True
   df = pd.read_csv('jouw_dataset.csv')
   ```

3. **Train opnieuw**:
   ```bash
   python train_model.py
   ```

### Hyperparameter Tuning

Je kunt de modelparameters aanpassen in `train_model.py`:

```python
# TF-IDF parameters
vectorizer = TfidfVectorizer(
    max_features=10000,     # Verhoog voor meer features
    min_df=2,              # Min document frequency
    max_df=0.8,            # Max document frequency
    ngram_range=(1, 3)     # Gebruik ook tri-grams
)

# Model parameters
model = LogisticRegression(
    max_iter=2000,         # Meer iteraties
    C=1.0,                 # Regularisatie sterkte
    random_state=42
)
```

## 🧪 Testen

Run de component tests:
```bash
python test_components.py
```

Dit test:
- Tekstverwerking functies
- Model aanwezigheid
- Voorspellingen met voorbeelddata

## 🎓 Voor je Profielwerkstuk

### Wat demonstreert dit project?

1. **Machine Learning**: Supervised learning classificatie
2. **Natural Language Processing**: Tekstanalyse met TF-IDF
3. **Web Development**: Full-stack Python applicatie
4. **Data Science**: Model training, evaluatie, deployment
5. **Software Engineering**: Modulaire code, testing, documentatie

### MVP Checklist (Alle afgevinkt! ✅)

- [x] Dataset en model (sample + Logistic Regression)
- [x] Tekstverwerking (cleaning, TF-IDF vectorisatie)
- [x] Webinterface (Flask + HTML/CSS/JavaScript)
- [x] Nieuwsanalyse (Real-time predictions)
- [x] Confidence score (Percentage zekerheid)

### Mogelijke Uitbreidingen (Post-MVP)

- [ ] URL scraping (automatisch artikelen ophalen)
- [ ] Explainability (waarom is het fake?)
- [ ] Visualisaties (grafieken, trends)
- [ ] Model vergelijking (Naive Bayes, SVM, NN)
- [ ] Grotere dataset (10.000+ artikelen)
- [ ] Nederlands taalmodel
- [ ] Database voor geschiedenis
- [ ] User feedback systeem

## 💡 Tips

1. **Test met verschillende teksten** om te zien hoe het model reageert
2. **Let op de confidence score** - lagere scores betekenen minder zekerheid
3. **Gebruik langere teksten** voor betere resultaten
4. **Train met meer data** voor hogere accuraatheid in productie

## 🐛 Problemen Oplossen

### "Model niet getraind"
```bash
python train_model.py
```

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### "Port 5001 already in use"
Wijzig in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5002)
```

### Lage accuraatheid
- Train met grotere dataset
- Pas hyperparameters aan
- Gebruik meer training data

## 📞 Support

Vragen? Check de volledige documentatie in `README.md`

## 🎉 Klaar!

Je hebt nu een werkende AI-powered Fake News Detector!

**Volgende stappen:**
1. Test met verschillende artikelen
2. Verbeter het model met meer data
3. Presenteer je MVP voor je profielwerkstuk!

---

**Gemaakt voor profielwerkstuk | MIT License**
