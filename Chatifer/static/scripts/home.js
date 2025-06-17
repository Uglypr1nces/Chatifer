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
    connectChat(server_ip,server_port)
  }
}

function connectChat(server_ip, server_port) {
  $.ajax({
    type: "POST",
    url: "connect/",
    data: {
      ip: server_ip,
      port: server_port
    },
    success: function (response) {
      alert("Connected to the server!")

      let saved_servers = document.getElementById("saved-servers");
      let saved_server = document.createElement("div");
      
      saved_server.innerHTML = `
      <h3>${server_ip}</h3>
      <h3>${server_ip}</h3>
      <button onclick="connectChat('${server_ip}', ${server_port})">Connect</button>
      `;

      saved_server.classList.add("saved-servers");
      saved_servers.appendChild(saved_server);

      window.location.href = "/chat/";
    },
    error: function () {
      alert("Couldnt connect to server.");
    },
  }); 
}