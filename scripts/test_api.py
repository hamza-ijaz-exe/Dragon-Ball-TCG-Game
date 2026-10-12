"""
Test script to discover Dragon Ball card fields from TCG API.
Reads API key from .env (never displays it).
"""
import os
import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError

# Load API key from .env without displaying it
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
api_key = None
with open(env_path, 'r') as f:
    for line in f:
        line = line.strip()
        if line.startswith('TCG_API_KEY'):
            api_key = line.split('=', 1)[1].strip().strip('"').strip("'")
            break

if not api_key:
    print("ERROR: TCGAPI_KEY not found in .env")
    exit(1)

print("API key loaded successfully (not displayed for security)\n")

# Step 1: Get all games
url = "https://api.tcgapi.dev/v1/games"
req = Request(url)
req.add_header("X-API-Key", api_key)
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) DragonBallTCG/1.0")

try:
    with urlopen(req) as resp:
        games_data = json.loads(resp.read().decode())
    
    # Filter for Dragon Ball games
    db_games = [g for g in games_data['data'] if 'dragon' in g.get('name', '').lower() or 'dragon' in g.get('slug', '').lower()]
    
    print("=== Dragon Ball Games ===")
    for g in db_games:
        print(f"  {g['name']} (slug: {g['slug']}, id: {g['id']}, cards: {g['card_count']}, sets: {g['set_count']})")
    
    print(f"\nTotal Dragon Ball games found: {len(db_games)}")
    
except HTTPError as e:
    print(f"Error: {e.code} - {e.reason}")
    print(e.read().decode())
    exit(1)

# Step 2: Get a sample card from first DB game to inspect custom_attributes
if db_games:
    game_slug = db_games[0]['slug']
    print(f"\n=== Sample Card from {db_games[0]['name']} ===")
    
    search_url = f"https://api.tcgapi.dev/v1/search?q=goku&game={game_slug}&per_page=1"
    req2 = Request(search_url)
    req2.add_header("X-API-Key", api_key)
    req2.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) DragonBallTCG/1.0")
    
    try:
        with urlopen(req2) as resp:
            search_data = json.loads(resp.read().decode())
        
        if search_data['data']:
            card = search_data['data'][0]
            print(f"\nCard: {card['name']}")
            print(f"Number: {card.get('number')}")
            print(f"Rarity: {card.get('rarity')}")
            print(f"Image URL: {card.get('image_url')}")
            print(f"\nCustom Attributes:")
            custom = card.get('custom_attributes', {})
            if custom:
                for key, value in custom.items():
                    print(f"  {key}: {value}")
            else:
                print("  (none)")
            
            print(f"\nAll top-level keys: {list(card.keys())}")
        else:
            print("No cards found in search")
            
    except HTTPError as e:
        print(f"Error: {e.code} - {e.reason}")
        print(e.read().decode())
