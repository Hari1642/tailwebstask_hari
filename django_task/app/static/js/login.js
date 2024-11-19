document.addEventListener("DOMContentLoaded", function () {
            const passwordField = document.getElementById("password");
            const showPasswordIcon = document.querySelector(".show-password");

            showPasswordIcon.addEventListener("click", function () {
                if (passwordField.type === "password") {
                    passwordField.type = "text";
                } else {
                    passwordField.type = "password";
                }
            });
        });