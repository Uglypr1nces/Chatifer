function sendUserInput() {
  let user_input = document.getElementById("input-box").value.trim();
  let user_name = localStorage.getItem("user_name");
  if (!user_input) {
    alert("Please enter a message.");
    return;
  }

  document.getElementById("input-box").value = "";


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
    }
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

const eventSource = new EventSource("sse_messages/");

eventSource.onmessage = function (event) {
  if (event.data) {
    appendServerMessage(event.data);
  }
};

eventSource.onerror = function (error) {
  console.error("SSE connection error:", error);
};

document.addEventListener('keyup', (event) => {
  if (event.key == 'Enter') {
    sendUserInput();
  } else if(event.key == 'Escape'){
    window.location.href = "/home";
  }
});
