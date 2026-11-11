#!/usr/bin/env python3
"""Genera index.html (es) y en/index.html (en), sitemap.xml y 404.html."""
from pathlib import Path

BASE = "https://dev.monsalve.com.co"
RAIZ = Path(__file__).parent
CORREO = "yosolosoy@monsalve.com.co"
PALABRA = "YOSOLOSOY"

APPS = [
    dict(id="lince", nombre="Lince", color="#0D0D0D", tinta="#F4F4F6", acento="#E8590C",
         play="https://play.google.com/store/apps/details?id=co.com.monsalve.lince",
         sitio={"es": "https://lincereader.com/es/", "en": "https://lincereader.com/"},
         linea={"es": "Lectura rápida, una palabra a la vez.", "en": "Speed reading, one word at a time."},
         estado={"es": "Disponible en Google Play", "en": "Available on Google Play"},
         datos={"es": ["Sin anuncios", "EPUB, PDF y artículos web", "6 temas de lectura"],
                "en": ["No ads", "EPUB, PDF and web articles", "6 reading themes"]}),
    dict(id="kinstride", nombre="Kinstride", color="#E2A31B", tinta="#0D0D0D", acento="#0D0D0D",
         play=None,
         sitio={"es": "https://getkinstride.com/es/", "en": "https://getkinstride.com/"},
         linea={"es": "Un RPG de fantasía que se juega caminando.", "en": "A fantasy RPG you play by walking."},
         estado={"es": "En prueba cerrada", "en": "Closed testing"},
         datos={"es": ["Sin anuncios", "Tus caminatas reales cruzan el mapa", "657 campamentos, cada uno con su historia"],
                "en": ["No ads", "Your real walks cross the map", "657 camps, each with its own story"]}),
    dict(id="flowmat", nombre="FlowMat", color="#F0917A", tinta="#0D0D0D", acento="#0D0D0D",
         play=None,
         sitio={"es": "https://flowmatapp.com/", "en": "https://flowmatapp.com/en/"},
         linea={"es": "Planifica la clase de pilates de cada alumno.", "en": "Plan each student's pilates class."},
         estado={"es": "En prueba cerrada", "en": "Closed testing"},
         datos={"es": ["500 ejercicios", "Según edad, nivel y condiciones médicas", "Mapa del cuerpo de cada clase"],
                "en": ["500 exercises", "By age, level and medical conditions", "Body map for every class"]}),
]

T = {
    "es": dict(
        lang="es", titulo="YosolosoY: apps independientes para Android",
        desc="Yo solo soy: una sola persona que diseña, programa y publica Lince, Kinstride y FlowMat, tres apps para Android.",
        etq="Estudio de una sola persona", frase="Yo solo soy.", traduce="",
        explica="Se lee igual al derecho y al revés. Así trabajo: una sola persona, del diseño al código y a la tienda.",
        revés="Leerlo al revés", revés_ok="Igual",
        apps="Tres apps", sitio="Ver el sitio", play="Google Play", contacto="Escríbeme",
        pie="Hecho en Chile.", otro="English", otro_url=f"{BASE}/en/", url=f"{BASE}/", idioma="Idioma",
        pantallas="Capturas de"),
    "en": dict(
        lang="en", titulo="YosolosoY: independent Android apps",
        desc="Yo solo soy, \"I am only me\": one person designing, coding and publishing Lince, Kinstride and FlowMat, three Android apps.",
        etq="A one-person studio", frase="Yo solo soy.", traduce=' <span class="trad">(I am only me)</span>',
        explica="Spanish for \"I am only me\". It reads the same forwards and backwards, and so does the work: one person, from design to code to the store.",
        revés="Read it backwards", revés_ok="Same",
        apps="Three apps", sitio="Visit the site", play="Google Play", contacto="Write to me",
        pie="Made in Chile.", otro="Español", otro_url=f"{BASE}/", url=f"{BASE}/en/", idioma="Language",
        pantallas="Screenshots of"),
}


def arcos():
    """Arcos anidados entre letras gemelas (viewBox: 9 columnas de ancho)."""
    out = []
    for k in range(4):
        x1, x2 = k + .5, 8 - k + .5
        r = (x2 - x1) / 2
        ry = r * .36
        out.append(f'<path class="arco" data-k="{k}" d="M{x1} 1.5 A{r} {ry:.3f} 0 0 1 {x2} 1.5" pathLength="1"/>')
    return "\n".join(out)


def letras():
    """YosolosoY: la «l» del centro es una raya, igual por los dos lados; la mitad derecha es el reflejo de la izquierda."""
    return "".join(
        f'<span class="l{" c" if i == 4 else ""}" data-i="{i}" tabindex="0">'
        f'<i class="g{" m" if i > 4 else ""}">{ch}</i></span>'
        for i, ch in enumerate("YosolosoY"))


def reflejo():
    return "".join(f'<span class="r"><i class="g{" m" if i > 4 else ""}">{ch}</i></span>'
                   for i, ch in enumerate("YosolosoY"))


def tarjeta(a, t, n):
    lg = t["lang"]
    botones = f'<a class="btn" href="{a["sitio"][lg]}">{t["sitio"]}</a>'
    if a["play"]:
        botones += f'<a class="btn ghost" href="{a["play"]}">{t["play"]}</a>'
    datos = "".join(f"<li>{d}</li>" for d in a["datos"][lg])
    fotos = "".join(
        f'<img src="/img/{a["id"]}-{lg}-{i}.webp" width="360" height="640" loading="lazy" alt="{t["pantallas"]} {a["nombre"]} {i}">'
        for i in (1, 2, 3))
    return f'''<section class="app" id="{a["id"]}" style="--fondo:{a["color"]};--tinta:{a["tinta"]};--acento:{a["acento"]}">
  <div class="app-in">
    <div class="espejo">
      <h2 class="nom">{a["nombre"]}</h2>
      <img class="icono" src="/img/{a["id"]}.png" width="112" height="112" alt="">
      <p class="nom reflejo" aria-hidden="true">{a["nombre"]}</p>
    </div>
    <p class="linea">{a["linea"][lg]}</p>
    <p class="estado">{a["estado"][lg]}</p>
    <ul class="datos">{datos}</ul>
    <div class="fotos">{fotos}</div>
    <div class="botones">{botones}</div>
  </div>
</section>'''


def pagina(lg, pie404=False):
    t = T[lg]
    ruta = "" if lg == "es" else "en/"
    tarjetas = "\n".join(tarjeta(a, t, i + 1) for i, a in enumerate(APPS))
    return f'''<!doctype html>
<html lang="{t["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t["titulo"]}</title>
<meta name="description" content="{t["desc"]}">
{'<meta name="robots" content="noindex">' if pie404 else f'<link rel="canonical" href="{t["url"]}">'}
<link rel="alternate" hreflang="es" href="{BASE}/">
<link rel="alternate" hreflang="en" href="{BASE}/en/">
<link rel="alternate" hreflang="x-default" href="{BASE}/">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/img/favicon-96.png" type="image/png" sizes="96x96">
<link rel="icon" href="/img/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:title" content="{t["titulo"]}">
<meta property="og:description" content="{t["desc"]}">
<meta property="og:url" content="{t["url"]}">
<meta property="og:image" content="{BASE}/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0D0D0D">
<link rel="preload" href="/fuentes/onest-800extrabold.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/estilo.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Organization","name":"YosolosoY","url":"{BASE}/","logo":"{BASE}/img/marca.png","email":"{CORREO}"}}</script>
</head>
<body>
<div class="cima">
<header class="cab">
  <a class="idioma" href="{t["otro_url"]}" hreflang="{"en" if lg == "es" else "es"}" aria-label="{t["idioma"]}">{t["otro"]}</a>
</header>
<main>
<section class="portada">
  <div class="palabra" id="palabra" role="img" aria-label="YosolosoY">
    <div class="letras" aria-hidden="true">{letras()}</div>
    <div class="letras refl" aria-hidden="true">{reflejo()}</div>
  </div>
  <div class="frase-fila">
    <h1>{t["frase"]}{t["traduce"]}</h1>
    <button class="revés" id="reves" type="button" aria-label="{t["revés"]}" title="{t["revés"]}">
      <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 8h15M15 4l4 4-4 4"/><path d="M20 16H5M9 12l-4 4 4 4"/></svg>
    </button>
  </div>
</section>
</div>
{tarjetas}
</main>
<footer class="pie">
  <a class="correo" href="mailto:{CORREO}" aria-label="{t["contacto"]}: {CORREO}">
    <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>
    {CORREO}
  </a>
</footer>
<script src="/yo.js" defer></script>
</body>
</html>
'''


def main():
    (RAIZ / "index.html").write_text(pagina("es"), encoding="utf-8")
    (RAIZ / "en").mkdir(exist_ok=True)
    (RAIZ / "en" / "index.html").write_text(pagina("en"), encoding="utf-8")
    (RAIZ / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        + "".join(
            f'<url><loc>{u}</loc>'
            f'<xhtml:link rel="alternate" hreflang="es" href="{BASE}/"/>'
            f'<xhtml:link rel="alternate" hreflang="en" href="{BASE}/en/"/></url>\n'
            for u in (f"{BASE}/", f"{BASE}/en/"))
        + "</urlset>\n", encoding="utf-8")
    (RAIZ / "404.html").write_text(
        pagina("es", pie404=True).replace("<h1>Yo solo soy.</h1>", "<h1>Esta página no existe.</h1>"),
        encoding="utf-8")


if __name__ == "__main__":
    main()
