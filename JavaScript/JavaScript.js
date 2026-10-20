// JavaScript code to reveal a button after 5 seconds
setTimeout(() => {
    const button = document.getElementById('myButton');
    if (button) {
        button.style.display = 'inline-block';
    }
}, 5000);
