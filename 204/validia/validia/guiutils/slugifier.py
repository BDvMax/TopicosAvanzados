import re
import unicodedata

# Letras latinas que NFKD no descompone en base + marca combinante.
_TRANSLIT = str.maketrans({
    "ß": "ss", "ø": "o", "Ø": "O", "æ": "ae", "Æ": "AE", "œ": "oe", "Œ": "OE",
    "đ": "d", "Đ": "D", "ł": "l", "Ł": "L", "þ": "th", "Þ": "TH", "ð": "d", "Ð": "D",
})


def slug(text: str) -> str:
    """Convierte texto a un slug apto para URL.

    Quita acentos, transliterá letras latinas especiales (ß, ø, ł...), elimina
    símbolos, pasa a minúsculas y une palabras con guiones. Los alfabetos no
    latinos (cirílico, CJK, etc.) se eliminan.

    >>> slug("Canción Nueva!")
    'cancion-nueva'
    """
    text = text.translate(_TRANSLIT)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^a-zA-Z0-9\s-]", "", text).strip().lower()
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    return text.strip("-")
