function sendUserInput() {
  let user_input = document.getElementById("input-box").value.trim();
  let user_name = localStorage.getItem("user_name");
  if (!user_input) {
    alert("Please enter a message.");
    return;
  }

  let chatBox = document.getElementById("chat-box");
  let userMessageDiv = document.createElement("div");
  userMessageDiv.classList.add("message", "user-message");
  userMessageDiv.innerText = user_input;
  chatBox.appendChild(userMessageDiv);

  document.getElementById("input-box").value = "";
  chatBox.scrollTop = chatBox.scrollHeight;

  $.ajax({
    type: "POST",
    url: "send_message/",
    data: {
      user_name: user_name,
      user_message: user_input,
    },
    success: function (data) {
      console.log(data);
    },
    error: function (xhr, status, error) {
      console.error("Error:", error);
      alert("Failed to send message. Please try again.");
    },
  });
}

let lastMessage = null;

function pollMessages() {
  $.ajax({
    type: "GET",
    url: "get_latest_message/",
    success: function (data) {
      const msg = data.message;
      if (msg && msg !== lastMessage) {
        appendServerMessage(msg);
        lastMessage = msg;
      }
    },
    error: function (xhr, status, error) {
      console.error("Polling error:", error);
    },
  });
}

function appendServerMessage(message) {
  let chatBox = document.getElementById("chat-box");
  let serverMessageDiv = document.createElement("div");
  serverMessageDiv.classList.add("message", "server-message");
  serverMessageDiv.innerText = message;
  chatBox.appendChild(serverMessageDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}

setInterval(pollMessages, 1000);

document.addEventListener('keyup', (event) => {
  if (event.key == 'Enter') {
    sendUserInput();
  } else if(event.key == 'Escape'){
    window.location.href = "/home";
  }
});
