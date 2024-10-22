document.addEventListener("DOMContentLoaded", function () {

    const deleteTrigger = document.getElementsByClassName('delete-trigger');
    
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