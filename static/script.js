let copyright = document.querySelector('.copyright_text');

function showCopyright() {
    let currentYear = new Date().getFullYear();
    copyright.innerHTML = `&copy; ${currentYear} Hasin. All rights reserved.`;
}


showCopyright();

// setInterval(() => {
//     showCopyright();
// }, 1000);
