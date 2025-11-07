document.querySelector('form').addEventListener('submit', (e) => {
    const username = document.querySelector('input[name="username"]').value;
    const password = document.querySelector('input[name="password"]').value;

    if (!username || !password) {
        e.preventDefault(); // جلوی ارسال فرم را می‌گیرد
        alert('لطفاً تمام فیلدها را پر کنید');
    }
});