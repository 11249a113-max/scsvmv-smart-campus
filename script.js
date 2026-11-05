
async function askQuestion(question) {
    const chatBox = document.getElementById("chat-box");

    const userMessage = document.createElement("div");
    userMessage.className = "user-message";
    userMessage.textContent = question;
    chatBox.appendChild(userMessage);

    try {
        const response = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: question })
        });

        const data = await response.json();

        const botMessage = document.createElement("div");
        botMessage.className = "bot-message";
        botMessage.textContent = data.reply;
        chatBox.appendChild(botMessage);

    } catch (error) {
        alert("Cannot connect to Python backend. Please check app.py.");
    }

    chatBox.scrollTop = chatBox.scrollHeight;
}

function sendMessage() {
    const input = document.getElementById("user-input");
    const question = input.value.trim();

    if (question) {
        askQuestion(question);
        input.value = "";
    }
}

document.getElementById("send-btn").addEventListener("click", sendMessage);

document.getElementById("user-input").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});
