#folder 00
import pandas as pd
import numpy as np

# Bước 2: Tạo một từ điển dữ liệu
du_lieu = {
    'evolution': ['Ivysaur', 'Charmeleon', 'Wartortle', 'Metapod'],
    'hp': [45, 39, 44, 45],
    'name': ['Bulbasaur', 'Charmander', 'Squirtle', 'Caterpie'],
    'pokedex': ['yes', 'no', 'yes', 'no'],
    'type': ['grass', 'fire', 'water', 'bug']
}

# Bước 3: Gán nó cho một biến gọi là pokemon
pokemon = pd.DataFrame(du_lieu)

# Bước 4: Sắp xếp lại thứ tự các cột theo thứ tự name, type, hp, evolution, pokedex
pokemon = pokemon[['name', 'type', 'hp', 'evolution', 'pokedex']]

# Bước 5: Thêm một cột mới gọi là place, và chèn dữ liệu mà bạn muốn
pokemon['place'] = ['rừng', 'núi', 'biển', 'đồng cỏ']

# Bước 6: Trình bày loại của mỗi cột
print(pokemon.dtypes)

# BONUS: Tạo câu hỏi riêng và trả lời nó
# Câu hỏi: Có bao nhiêu Pokémon trong DataFrame này có hơn 40 HP?
so_luong_hp_cao = pokemon[pokemon['hp'] > 40].shape[0]
print(f"Số lượng Pokémon có hơn 40 HP: {so_luong_hp_cao}")
