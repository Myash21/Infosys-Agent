# Infosys-Agent

# Link to complete documentation
https://docs.google.com/document/d/1wQUdKAW8PF4VrwFMdFf9-6bU7FsrFmO8EbYfTwn0W9E/edit?usp=sharing

## 🛠 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/infosys-competitor-checker.git
cd infosys-competitor-checker
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
``` 

### 3. Install Dependencies
```bash
pip install -r requirements.txt
``` 

### 4. Configure Environment Variables
Create a .env file in the root directory and add your API keys:
```bash
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
``` 

## Running the Script
Make sure you're in the virtual environment:
```bash
python agent.py
``` 
