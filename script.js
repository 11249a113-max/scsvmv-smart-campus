
async function askQuestion(question) {
    const chatBox = document.getElementById("chat-box");

    const userMessage = document.createElement("div");
    userMessage.className = "message user";
    userMessage.textContent = question;
    chatBox.appendChild(userMessage);

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: question
            })
        });

        if (!response.ok) {
            throw new Error("Server error: " + response.status);
        }

        const data = await response.json();

        const botMessage = document.createElement("div");
        botMessage.className = "message bot";
        botMessage.textContent = data.reply;
        chatBox.appendChild(botMessage);

    } catch (error) {
        const errorMessage = document.createElement("div");
        errorMessage.className = "message bot";
        errorMessage.textContent =
            "Connection error: " + error.message;

        chatBox.appendChild(errorMessage);
        console.error("Chat error:", error);
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

document.getElementById("send-btn")
    .addEventListener("click", sendMessage);

document.getElementById("user-input")
    .addEventListener("keydown", function(event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });
