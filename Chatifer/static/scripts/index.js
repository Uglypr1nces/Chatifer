document.addEventListener("DOMContentLoaded", checkLogin);

function checkLogin() {
    const user_name = localStorage.getItem("user_name");
    alert(user_name);
    if (user_name) {
        console.log("user logged in");
        if (window.location.pathname === "/" || window.location.pathname === "") {
            window.location.href = window.location.origin + "/home/";
        }
    } else {
        window.location.href = "/login/";
    }
}

console.log("test ts");