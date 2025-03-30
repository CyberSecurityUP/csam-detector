# CSAM Detector 🔍🛡️

A lightweight AI-powered prototype for detecting potential Child Sexual Abuse Material (CSAM) in images, with perceptual hashing, encrypted logging, and a secure web interface.

## 🚀 Features

- ✅ NSFW image detection using ResNet-50 (Yahoo Open NSFW model)
- 🔐 Perceptual hash generation and matching (pHash)
- 🧠 Fast classification via OpenCV's DNN module
- 🧾 AES-256 encrypted SQLite logging
- 🔍 Blurred image preview for analyst safety
- 📦 Ready for local testing and educational use

## 🧰 Tech Stack

- Python 3.10+
- Flask (Web Framework)
- OpenCV (`cv2.dnn`)
- Pillow + ImageHash
- Cryptography (Fernet AES encryption)

## 📁 Project Structure

```
csam-detector/
├── app/
│   ├── routes.py, ai_model.py, hashing.py, database.py
├── static/
├── templates/
├── model/               # Contains .caffemodel and prototxt
├── hash_db/             # Simulated hash list
├── secure_logs/         # Encrypted logs
├── uploads/             # Uploaded images (blurred view only)
└── run.py
```

## ⚙️ Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py
```

Then open your browser at:  
`http://127.0.0.1:5000`

## ⚠️ Ethical Use

This tool is intended **strictly for research, educational, and forensic training purposes**. It **does not store any real CSAM** and uses only public NSFW datasets and simulated hashes.

Please use responsibly and in compliance with local laws.

## 📚 Related Work

- [Yahoo Open NSFW Model](https://github.com/yahoo/open_nsfw)
- [NuDetective (Brazilian Forensic Tool)](https://blog.ipog.edu.br/tecnologia/nudetective-ferramenta-pedofilia/)
- [CSAM Detection via Perceptual Hashing](https://www.microsoft.com/en-us/photodna)

## 🔗 Author

Developed by [Joas Antonio dos Santos](https://github.com/CyberSecurityUP)  
Repo: [https://github.com/CyberSecurityUP/csam-detector](https://github.com/CyberSecurityUP/csam-detector)
