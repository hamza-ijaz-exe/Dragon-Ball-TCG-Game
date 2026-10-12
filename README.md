# Dragon Ball TCG Game

A personal Dragon Ball Trading Card Game web application.

## Tech Stack

- **Backend**: Python (Flask/FastAPI)
- **Frontend**: HTML/CSS/JS
- **Storage**: JSON files
- **Card Data**: Seeded from [tcgapi.dev](https://tcgapi.dev/)

## Project Structure

```
Dragon-Ball-TCG-Game/
├── .venv/              # Python virtual environment
├── data/               # JSON data files
│   ├── cards.json      # Seeded card data
│   └── users.json      # User data
├── src/                # Source code
│   └── app.py          # Main application entry point
├── .gitignore
└── README.md
```

## Setup

1. Create virtual environment:
   ```bash
   python -m venv .venv
   ```

2. Activate virtual environment:
   ```bash
   # Windows
   .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python src/app.py
   ```

## License

Personal project.
