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

document.addEventListener("DOMContentLoaded", function () {

    const deleteTrigger = document.getElementById('delete-trigger');
    
    if(deleteTrigger) {
        const deleteCourseModal = document.getElementById('course-delete-modal');
        deleteCourseModal.addEventListener('show.bs.modal', function (event) {
        const button = event.relatedTarget;
        const formAction = button.getAttribute('data-url');

        const deleteForm = document.getElementById('course-delete-form');
        deleteForm.action = formAction;
        });
    }
});