import codecs

with codecs.open('generated_pages.html', 'r', 'utf-8') as f:
    pages_html = f.read()

html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enciclopedia de las Hierbas Mágicas</title>
    <link rel="stylesheet" href="styles.css">
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Montserrat:wght@300;400;600&display=swap" rel="stylesheet">
</head>
<body>
    <div class="flip-book-container">
        <div id="book">
            <!-- Cover Page -->
            <div class="page cover-page" data-density="hard">
                <div class="page-content">
                    <img src="assets/magazine_cover_1772347328293.png" alt="Cover" class="cover-bg">
                    <div class="cover-text">
                        <h1>ENCICLOPEDIA DE LAS HIERBAS MÁGICAS</h1>
                        <h2>por Scott Cunningham</h2>
                    </div>
                </div>
            </div>
            
            <!-- Inside Cover -->
            <div class="page" data-density="hard">
                <div class="page-content center-content"></div>
            </div>

            <!-- Intro / Instructions -->
            <div class="page" data-density="soft">
                <div class="page-content center-content instructions">
                    <h2>Instrucciones</h2>
                    <p>Usa el ratón, haz clic o arrastra las esquinas de las páginas para leer el libro mágico.</p>
                </div>
            </div>
            
            <!-- Title Page inside -->
            <div class="page" data-density="soft">
                <div class="page-content center-content">
                    <h2 class="book-intro">Una guía esencial para la herbolaria mágica y esotérica.</h2>
                </div>
            </div>

            <!-- The Herbs Pages -->
            {pages_html}

            <!-- Inside Back Cover -->
            <div class="page" data-density="hard">
                <div class="page-content"></div>
            </div>

            <!-- Back Cover -->
            <div class="page back-cover" data-density="hard">
                <div class="page-content center-content">
                    <div class="cover-text" style="padding-top:0;">
                        <h1>El Fin</h1>
                        <p style="margin-top: 2rem;">&copy; 2026 Revista Digital Mágica</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- PageFlip.js -->
    <script src="https://cdn.jsdelivr.net/npm/page-flip/dist/js/page-flip.browser.js"></script>
    <script src="app.js"></script>
</body>
</html>
"""

with codecs.open('index.html', 'w', 'utf-8') as f:
    f.write(html)
