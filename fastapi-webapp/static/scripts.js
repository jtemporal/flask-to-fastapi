// script.js
document.querySelector('#clickMeButton').addEventListener('click', (function() {
    let clickCount = 0;
    return function() {
        clickCount += 1;
        this.textContent = `👠👠 (${clickCount})`;
        if (clickCount === 3) {
            window.location.href = '/home';
        }
    };
})());