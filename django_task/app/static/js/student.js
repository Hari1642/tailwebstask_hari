document.addEventListener("DOMContentLoaded", function () {
    const editButtons = document.querySelectorAll(".edit-btn");
    const studentIdInput = document.getElementById("studentId");
    const nameInput = document.getElementById("name");
    const subjectInput = document.getElementById("subject");
    const marksInput = document.getElementById("marks");
    const editForm = document.getElementById("editForm");

    editButtons.forEach(button => {
        button.addEventListener("click", function () {
            const id = this.getAttribute("data-id");
            const name = this.getAttribute("data-name");
            const subject = this.getAttribute("data-subject");
            const marks = this.getAttribute("data-marks");

            studentIdInput.value = id;
            nameInput.value = name;
            subjectInput.value = subject;
            marksInput.value = marks;
            editForm.action = `/edit_student/${id}/`;
        });
    });
});
const editButtons = document.querySelectorAll('.edit-btn');
editButtons.forEach(button => {
    button.addEventListener('click', () => {
        const studentId = button.getAttribute('data-id');
        const studentName = button.getAttribute('data-name');
        const studentSubject = button.getAttribute('data-subject');
        const studentMarks = button.getAttribute('data-marks');

        document.getElementById('studentId').value = studentId;
        document.getElementById('Name').value = studentName;
        document.getElementById('Subject').value = studentSubject;
        document.getElementById('Marks').value = studentMarks;
    });
});
