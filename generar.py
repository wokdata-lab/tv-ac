import random

BASE_URL = "https://antenacentro.com/tv"

categorias = {
    "ids": 10,
    "noticias": 180,
    "publicidad": 15,
    "documentales": 300
}

clips = {
    "ids": ["ids/id1/index.m3u8"],
    "publicidad": ["publicidad/pub1/index.m3u8"],
    "noticias": ["noticias/not1/index.m3u8"],
    "documentales": ["documentales/doc1/index.m3u8"]
}

m3u = "#EXTM3U\n#EXT-X-VERSION:3\n#EXT-X-TARGETDURATION:10\n\n"

ultimo = None

for i in range(30):
    cat = random.choice(list(categorias.keys()))
    if cat == ultimo:
        continue
    ultimo = cat

    clip = random.choice(clips[cat])
    m3u += f"#EXTINF:{categorias[cat]},\n"
    m3u += f"{BASE_URL}/{clip}\n"

with open("canal.m3u8", "w") as f:
    f.write(m3u)
