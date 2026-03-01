document.addEventListener('DOMContentLoaded', () => {
    const bookElement = document.getElementById('book');

    // Calculate adaptive sizing based on window
    const ww = window.innerWidth;
    const wh = window.innerHeight;

    let isMobile = ww < 800;
    // We want a portrait book proportion normally, e.g. 400x600 per page.
    let baseWidth = isMobile ? ww * 0.95 : 400;
    let baseHeight = isMobile ? wh * 0.85 : 600;

    const pageFlip = new St.PageFlip(bookElement, {
        width: baseWidth,       // base page width
        height: baseHeight,     // base page height
        size: "stretch",        // stretch to fit bounds
        minWidth: 250,
        maxWidth: 600,
        minHeight: 350,
        maxHeight: 800,
        maxShadowOpacity: 0.5,  // flip shadow
        showCover: true,        // hard cover
        mobileScrollSupport: false,
        drawShadow: true,
        useMouseEvents: true,
        flippingTime: 700
    });

    // Load pages
    pageFlip.loadFromHTML(document.querySelectorAll('.page'));
});
