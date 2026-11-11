# dev.monsalve.com.co
Página de desarrollador de YosolosoY: Lince, Kinstride y FlowMat. Sitio estático (es + en).
- `python3 generar.py` regenera `index.html`, `en/index.html`, `404.html` y `sitemap.xml`. Textos y estados de las apps están en `generar.py`.
- Cambiar el estado de Kinstride/FlowMat ("En prueba cerrada") y agregar su botón de Google Play cuando salgan a producción.
- Publicación: GitHub Pages (repo YosolosoY/dev-web), DNS en Cloudflare, CNAME `dev` → `yosolosoy.github.io` (solo DNS).

## Regla de mantenimiento
Cada cambio en Lince, Kinstride o FlowMat (o en el sitio de cada una) se revisa aquí: estado, botón de Google Play, datos (`datos` en `generar.py`) y capturas (`img/<app>-<es|en>-N.webp`). Luego `python3 generar.py`.
