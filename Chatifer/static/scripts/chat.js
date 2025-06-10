
function sendUserInput() {
  let user_input = document.getElementById("input-box").value.trim();

  if (!user_input) {
    alert("Please enter a message.");
    return;
  }

  $.ajax({
    type: "POST",
    url: "send_message/",
    data: {
      user_message: user_input,
    },
    success: function (data) {
      console.log(data);

      let chat_box = document.getElementById("chat-box");
      let user_message = document.createElement("div");
      
      userMessage.classList.add("message", "user-message");
      userMessage.innerText = user_input;

      botMessage.classList.add("message", "bot-message");
      botMessage.innerText = data;

      chatBox.appendChild(userMessage);
      chatBox.appendChild(botMessage);

      document.getElementById("input-box").value = ""; // Clear input box
      waiting_animation.style.visibility = "hidden"; // Hide loading animation
    },
    error: function (xhr, status, error) {
      console.error("Error:", error);
      alert("Failed to send message. Please try again.");
      waiting_animation.style.visibility = "hidden"; // Hide loading animation
    },
  });
}

document.addEventListener('keyup', (event) => {
  if (event.key == 'Enter') {
    sendUserInput();
  }
  else if(event.key == 'Escape'){
    window.location.href = "/home";
  }
});