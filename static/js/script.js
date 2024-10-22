document.addEventListener("DOMContentLoaded", function() {
    const redirect = document.getElementById('redirect');
    if(redirect) {
        const success = redirect.getAttribute('data-success-url')
        const cancel = redirect.getAttribute('data-cancel-url')

        currentUrl = window.location.pathname;

        if(currentUrl.includes("success")) {
            setTimeout(function() {
                window.location.href = success;
            }, 3000);
        } else if(currentUrl.includes("cancel")) {
            setTimeout(function() {
                window.location.href = cancel;
            }, 3000);
        }
    }
});

document.addEventListener("DOMContentLoaded", function() {
    const hideError = document.getElementById('django-message')

    if(hideError) {
        setTimeout(function() {
            hideError.hidden = true
        }, 3000);
    }
});