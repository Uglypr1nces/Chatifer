function connectChat(){
    const server_ip = document.getElementById("server-ip");
    const server_port = document.getElementById("server-port");
    $.ajax({
      type: "POST",
      url: "sign_up/",
      data: user_data,
      success: function (response) {
        console.log("Sign-up successful:", response);
        alert("Sign up successful, you can now log in")
        
      },
      error: function () {
        alert("Failed to sign up. Please try again later.");
      },
    });
}