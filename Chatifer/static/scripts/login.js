window.onload = setUser;

function setUser() {
    localStorage.setItem("user_name", "");
    console.log("Set username to empty string");
}

function validateEmail(email) {
    const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return regex.test(email);
}

function validateUser(form) {
    const first_name = form.elements["first_name"].value.trim();
    const last_name = form.elements["last_name"].value.trim();
    const email = form.elements["sign-up-email"].value.trim().toLowerCase();
    const password = form.elements["sign-up-password"].value.trim();
    const confirm_password = form.elements["confirm-password"].value.trim();

    if (first_name.length < 2) {
        alert("First name must be at least 2 characters.");
        return false;
    }
    if (last_name.length < 2) {
        alert("Last name must be at least 2 characters.");
        return false;
    }
    if (!validateEmail(email)) {
        alert("Invalid email address.");
        return false;
    }
    if (password.length < 8) {
        alert("Password must be at least 8 characters.");
        return false;
    }
    if (password !== confirm_password) {
        alert("Passwords do not match.");
        return false;
    }

    console.log("User is valid.");
    return true;
}

function signUp(event) {
    event.preventDefault();

    const form = document.getElementById("sign-up-form");

    if (!validateUser(form)) {
        alert("Sign up invalid...");
        form.elements["sign-up-password"].value = "";
        form.elements["confirm-password"].value = "";
    } else {
        const user_data = {
            first_name: form.elements["first_name"].value.trim(),
            last_name: form.elements["last_name"].value.trim(),
            email: form.elements["sign-up-email"].value.trim().toLowerCase(),
            password: form.elements["sign-up-password"].value.trim(),
        };

        $.ajax({
            type: "POST",
            url: "sign_up/",
            data: user_data,
            success: function (response) {
                console.log("Sign-up successful:", response);
                alert("Sign up successful, you can now log in");
                clearSignUp(); 
            },
            error: function () {
                alert("Failed to sign up. Please try again later.");
            },
        });
    }
}

function logIn() {
    const email = document.getElementById("log-in-email");
    const password = document.getElementById("log-in-password");

    if (!email.value.trim() || !password.value.trim()) {
        alert("Please fill in all fields.");
    } else {
        $.ajax({
            type: "POST",
            url: "log_in/",
            data: {
                email: email.value.trim().toLowerCase(),
                password: password.value.trim(),
            },
            success: function (data) {
                if (data === "Couldn't find user") {
                    alert("User wasn't found, please try again");
                } else {
                    alert("Greetings " + data);
                    localStorage.setItem("user_name", data);
                    window.location.href = "/home/";
                }
            },
            error: function () {
                alert("Failed to verify user.");
            },
        });
    }
}

function clearSignUp() {
    const form = document.getElementById("sign-up-form");

    form.elements["first_name"].value = "";
    form.elements["last_name"].value = "";
    form.elements["sign-up-email"].value = "";
    form.elements["sign-up-password"].value = "";
    form.elements["confirm-password"].value = "";
}
