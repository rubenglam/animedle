import requests
from bs4 import BeautifulSoup
import json

# URL base de la wiki
BASE_URL = "https://myheroacademia.fandom.com"

# URL de la lista de personajes
CHARACTER_LIST_URL = f"{BASE_URL}/wiki/Category:Characters"

# Función para extraer información de un personaje
def get_character_details(character_url):
    response = requests.get(character_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Datos básicos
    character_data = {
        "url_imagen": None,
        "nombre": None,
        "genero": None,
        "don": None,
        "edad": None,
        "color_de_pelo": None,
        "trabajo": None,
        "arco_de_primera_aparicion": None
    }

    # Imagen del personaje
    img_tag = soup.find("a", {"class": "image"})
    if img_tag and img_tag.img:
        character_data["url_imagen"] = img_tag.img.get("src")
    
    # Nombre
    name_tag = soup.find("h1", {"class": "page-header__title"})
    if name_tag:
        character_data["nombre"] = name_tag.text.strip()
    
    # Información del personaje (busca en tablas o secciones específicas)
    info_box = soup.find("aside", {"class": "portable-infobox"})
    if info_box:
        for row in info_box.find_all("div", {"class": "pi-item"}):
            label = row.find("h3")
            value = row.find("div", {"class": "pi-data-value"})
            if label and value:
                key = label.text.strip().lower()
                if "quirk" in key or "don" in key:
                    character_data["don"] = value.text.strip()
                elif "gender" in key or "género" in key:
                    character_data["genero"] = value.text.strip()
                elif "age" in key or "edad" in key:
                    character_data["edad"] = value.text.strip()
                elif "hair color" in key or "color de pelo" in key:
                    character_data["color_de_pelo"] = value.text.strip()
                elif "occupation" in key or "trabajo" in key:
                    character_data["trabajo"] = value.text.strip()
    
    return character_data

# Función para extraer personajes desde la lista
def get_character_list():
    response = requests.get(CHARACTER_LIST_URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    characters = []
    
    # Encuentra enlaces a personajes
    character_links = soup.select("div.category-page__members a")
    for link in character_links:
        character_name = link.text.strip()
        character_url = f"{BASE_URL}{link['href']}"
        print(f"Extracting {character_name}...")
        try:
            character_data = get_character_details(character_url)
            characters.append(character_data)
        except Exception as e:
            print(f"Failed to extract {character_name}: {e}")
    
    return characters

# Ejecutar y guardar los datos en un archivo JSON
if __name__ == "__main__":
    print("Extracting characters...")
    character_data = get_character_list()
    with open("boku_no_hero_characters.json", "w", encoding="utf-8") as json_file:
        json.dump(character_data, json_file, ensure_ascii=False, indent=4)
    print("Character data saved to boku_no_hero_characters.json")