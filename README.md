# 📦 3D Model Viewer Platform

> **Online platform voor architecten, ontwerpers en studenten om 3D-modellen te uploaden, bekijken en delen**

Een eenvoudig web-platform gebouwd als Minimum Viable Product (MVP) dat de kernfunctionaliteit demonstreert voor het uploaden, visualiseren en delen van 3D-modellen rechtstreeks in de browser.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![Three.js](https://img.shields.io/badge/three.js-0.160-orange.svg)](https://threejs.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📖 Inhoudsopgave

- [Features](#-features)
- [Snelstart](#-snelstart)
- [Hoe het werkt](#-hoe-het-werkt)
- [Projectstructuur](#-projectstructuur)
- [Technische Details](#-technische-details)
- [Gebruikersflow](#-gebruikersflow)
- [Toekomstige Verbeteringen](#-toekomstige-verbeteringen)
- [Bijdragen](#-bijdragen)
- [Licentie](#-licentie)

## ✨ Features

### Kernfunctionaliteit
- **📤 3D Model Upload**: Upload .glb en .gltf bestanden tot 50MB
- **🎨 Interactieve 3D Viewer**: Bekijk modellen in je browser met Three.js
- **🔗 Eenvoudig Delen**: Deel modellen via een unieke link
- **📱 Responsive Design**: Werkt op desktop en mobiele apparaten
- **💾 Lokale Opslag**: Veilige bestandsopslag met SQLite database

### Gebruikerservaring
- **🖱️ Intuïtieve Besturing**: Draaien, zoomen en pannen met muis
- **⚡ Snel Visualiseren**: Direct bekijken na upload
- **🌐 Geen Login Vereist**: Simpel en toegankelijk
- **📚 Model Bibliotheek**: Bekijk alle geüploade modellen

### Technische Eigenschappen
- **🔒 Bestandsvalidatie**: Alleen toegestane 3D-formaten
- **🚀 Lichtgewicht**: Minimale dependencies
- **📊 Database Tracking**: Metadata opslag in SQLite
- **🎯 Clean Architecture**: Modulaire code organisatie

## 🚀 Snelstart

### Vereisten

- **Python 3.8+** (Controleer met `python3 --version`)
- **pip** (Python package installer)
- **10 MB** vrije schijfruimte

### Installatie

#### Optie 1: Handmatige Setup

```bash
# 1. Clone de repository
git clone https://github.com/SilFopma4h2/fake-news-checker.git
cd fake-news-checker

# 2. Installeer dependencies
pip install -r requirements.txt

# 3. Start de applicatie
python3 app.py
```

#### Optie 2: Automated Setup

```bash
# Clone en start met één commando
git clone https://github.com/SilFopma4h2/fake-news-checker.git
cd fake-news-checker
chmod +x run.sh
./run.sh
```

### Toegang tot de Applicatie

Open je browser en navigeer naar:
```
http://localhost:5001
```

### 🎮 Hoe te gebruiken

1. **Upload** een 3D-model (.glb of .gltf bestand)
2. **Bekijk** het model direct in de interactieve 3D-viewer
3. **Deel** het model via de gegenereerde link
4. **Beheer** je modellen in de bibliotheek

## 🧠 Hoe het werkt

### Technische Flow

```
┌─────────────┐
│   Browser   │
└──────┬──────┘
       │ 1. Upload 3D Model
       ▼
┌─────────────┐
│    Flask    │
│  Backend    │
└──────┬──────┘
       │ 2. Valideer & Opslaan
       ▼
┌─────────────┐    ┌─────────────┐
│   Lokale    │◄───│   SQLite    │
│   Opslag    │    │  Database   │
└──────┬──────┘    └─────────────┘
       │ 3. Genereer Link
       ▼
┌─────────────┐
│  Three.js   │
│   Viewer    │
└─────────────┘
```

### 1. Upload Process
- Gebruiker selecteert een 3D-model bestand
- Flask backend valideert bestandstype en grootte
- Bestand wordt opgeslagen met unieke filename
- Metadata wordt toegevoegd aan SQLite database
- Unieke view URL wordt gegenereerd

### 2. View Process
- Gebruiker opent view URL
- Three.js laadt het 3D-model
- Interactieve controls worden geïnitialiseerd
- Model wordt gecentreerd en geschaald voor optimale weergave

### 3. Share Process
- Gebruiker kopieert de share link
- Link kan direct gedeeld worden
- Geen authenticatie nodig om model te bekijken

## 📁 Projectstructuur

```
fake-news-checker/
├── 📄 app.py                   # Flask applicatie (main entry point)
├── 📄 database.py              # SQLite database module
├── 📋 requirements.txt         # Python dependencies
├── 📁 templates/
│   ├── 🎨 index.html          # Upload pagina
│   ├── 🎨 viewer.html         # 3D Model viewer (Three.js)
│   └── 🎨 models.html         # Model bibliotheek
├── 📁 uploads/                 # Geüploade 3D-modellen (lokaal)
├── 💾 models.db               # SQLite database
├── 📖 README.md               # Deze file
└── 📘 LICENSE                 # MIT License
```

## 🔧 Technische Details

### Tech Stack

| Component | Technologie | Details |
|-----------|-----------|---------|
| **Backend** | Flask 3.0 | Python web framework |
| **Database** | SQLite | Lightweight database |
| **Frontend** | HTML5/CSS3 | Modern web standards |
| **3D Engine** | Three.js 0.160 | WebGL 3D library |
| **File Storage** | Lokaal | Upload folder management |

### Database Schema

```sql
CREATE TABLE models (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT NOT NULL,
    original_filename TEXT NOT NULL,
    file_path TEXT NOT NULL,
    upload_date TEXT NOT NULL,
    user_id TEXT DEFAULT NULL
);
```

### API Endpoints

| Endpoint | Method | Beschrijving |
|----------|--------|-------------|
| `/` | GET | Upload pagina |
| `/upload` | POST | Upload 3D model |
| `/view/<id>` | GET | Bekijk 3D model |
| `/models` | GET | Model bibliotheek |
| `/models/<id>` | GET | Model info (API) |
| `/uploads/<filename>` | GET | Serve model files |

### Ondersteunde Formaten

- **GLB** (GL Transmission Format Binary) - Aanbevolen
- **GLTF** (GL Transmission Format)

Maximum bestandsgrootte: **50MB**

## 🎯 Gebruikersflow in de MVP

### Standaard Workflow

1. Gebruiker opent de site (`/`)
2. Drukt op "Upload 3D model" of sleept bestand
3. Selecteert bijvoorbeeld `house.glb`
4. Flask ontvangt bestand → slaat op → maakt link (`/view/12`)
5. Gebruiker kan direct bekijken, draaien, delen

**Geen login, geen profiel, geen complexiteit - alleen de kern: "upload → bekijk → deel"**

### 3D Viewer Controls

| Actie | Besturing |
|-------|-----------|
| **Draaien** | Linker muisknop + slepen |
| **Zoomen** | Scrollwiel |
| **Pannen** | Rechter muisknop + slepen |

## 🔮 Toekomstige Verbeteringen

### Na MVP (Post-Launch)

#### Hoge Prioriteit
- [ ] **Gebruikersaccounts**: Login en persoonlijke dashboards
- [ ] **Cloud Opslag**: AWS S3 of Azure Blob Storage integratie
- [ ] **Model Thumbnails**: Automatische preview generatie
- [ ] **Zoek Functionaliteit**: Filter en zoek door modellen

#### Medium Prioriteit
- [ ] **AI Features**: Auto-textureren, lichtoptimalisatie
- [ ] **Real-time Samenwerking**: Meerdere gebruikers tegelijk
- [ ] **Annotaties**: Comments en markup op modellen
- [ ] **Export Opties**: Download in verschillende formaten

#### Nice to Have
- [ ] **VR/AR Support**: WebXR integratie
- [ ] **Model Vergelijking**: Side-by-side viewer
- [ ] **Projectmappen**: Organisatie met tags en mappen
- [ ] **API voor Integratie**: RESTful API voor third-party apps
- [ ] **Analytics Dashboard**: Usage statistics
- [ ] **Social Features**: Likes, comments, followers

### Technische Verbeteringen
- [ ] **Docker Support**: Containerized deployment
- [ ] **CI/CD Pipeline**: Automated testing en deployment
- [ ] **CDN**: Snellere model laadtijden
- [ ] **Caching**: Redis voor performance
- [ ] **Rate Limiting**: API bescherming
- [ ] **Logging**: Monitoring en error tracking

## 🤝 Bijdragen

Bijdragen zijn welkom! Zo kun je helpen:

### Manieren om bij te dragen

#### 🐛 Bug Reports
Gevonden een bug? [Open een issue](https://github.com/SilFopma4h2/fake-news-checker/issues) met:
- Duidelijke beschrijving van het probleem
- Stappen om te reproduceren
- Verwacht vs actueel gedrag
- Screenshots indien van toepassing

#### ✨ Feature Requests
Heb je een idee? [Dien een feature request in](https://github.com/SilFopma4h2/fake-news-checker/issues) met:
- Use case beschrijving
- Voorgestelde oplossing
- Alternatieve benaderingen

#### 🔧 Code Contributions

1. Fork de repository
2. Maak een feature branch (`git checkout -b feature/geweldige-feature`)
3. Commit je wijzigingen (`git commit -m 'Voeg geweldige feature toe'`)
4. Push naar branch (`git push origin feature/geweldige-feature`)
5. Open een Pull Request

### Focus Gebieden

- 🎨 **UI/UX**: Design verbeteringen, accessibility
- 🔧 **Backend**: Performance, security
- 📱 **Frontend**: Three.js features, animations
- 📖 **Documentatie**: Betere voorbeelden, vertalingen
- 🧪 **Testing**: Uitbreiden van test coverage
- 🐛 **Bug Fixes**: Bekende issues oplossen

## 📝 Licentie

MIT License - Zie [LICENSE](LICENSE) bestand voor details.

Copyright (c) 2024 SilFopma4h2

## 🙏 Acknowledgments

- **Three.js**: Voor de krachtige 3D engine
- **Flask**: Voor het lichtgewicht web framework
- **Open Source Community**: Voor inspiratie en resources

## 📞 Contact & Support

- **Author**: SilFopma4h2
- **Repository**: [github.com/SilFopma4h2/fake-news-checker](https://github.com/SilFopma4h2/fake-news-checker)
- **Issues**: [Report bugs of request features](https://github.com/SilFopma4h2/fake-news-checker/issues)

---

## 🚨 Troubleshooting

### Veelvoorkomende Problemen

#### Probleem: Port Already in Use

```
OSError: [Errno 48] Address already in use
```

**Oplossing:**
```bash
# Vind proces op poort 5001
lsof -i :5001
# Stop het proces
kill -9 <PID>

# Of wijzig de poort in app.py
app.run(debug=True, host='0.0.0.0', port=5002)
```

#### Probleem: Upload Fails

**Mogelijke oorzaken:**
- Bestand is te groot (>50MB)
- Ongeldig bestandsformaat
- Geen schrijfrechten voor uploads folder

**Oplossing:**
```bash
# Controleer permissions
chmod 755 uploads/

# Vergroot limiet in app.py indien nodig
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB
```

#### Probleem: Model Not Loading

**Oplossing:**
- Controleer of het bestand een geldig GLB/GLTF formaat is
- Test het model in een andere GLTF viewer
- Check browser console voor errors

---

<div align="center">

**⭐ Star deze repository als je het nuttig vindt!**

Gemaakt voor architecten, ontwerpers en 3D enthusiasts

[Report Bug](https://github.com/SilFopma4h2/fake-news-checker/issues) · [Request Feature](https://github.com/SilFopma4h2/fake-news-checker/issues)

</div>
