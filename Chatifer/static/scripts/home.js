function checkInfo() {
  const server_ip = document.getElementById("server-ip").value;
  const server_port = document.getElementById("server-port").value;

  console.log(server_ip, server_port);

  if (server_ip.length < 3) {
    alert("address needs to be more than 2 characters");
    return false;
  } else if (server_port.length < 4) {
    alert("port needs to be more than 3 characters");
    return false;
  } else {
    return true;
  }
}

function connectChat() {
  const server_ip = document.getElementById("server-ip").value;
  const server_port = document.getElementById("server-port").value;

  if (checkInfo()) {
    $.ajax({
      type: "POST",
      url: "connect/",
      data: {
        ip: server_ip,
        port: server_port
      },
      success: function (response) {
        alert("Connected to the server!")
        sessionStorage.setItem("server_ip", server_ip);
        sessionStorage.setItem("server_port", server_port);
        window.location.href = "/chat/";
      },
      error: function () {
        alert("Couldnt connect to server.");
      },
    });
  }
}