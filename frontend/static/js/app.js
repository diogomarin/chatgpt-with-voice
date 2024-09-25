async function sendMessage() {
    const inputElement = document.getElementById('user-input');
    const userInput = inputElement.value;

    if (userInput.trim() !== "") {
        const response = await fetch('http://127.0.0.1:8000/send-message/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_input: userInput })
        });
        const data = await response.json();
        updateChatWindow("user", userInput);
        updateChatWindow("assistant", data.response);
        inputElement.value = '';
    }
}

function updateChatWindow(role, message) {
    const chatWindow = document.getElementById('chat-window');
    const messageElement = document.createElement('div');
    messageElement.className = role;
    messageElement.innerText = message;
    chatWindow.appendChild(messageElement);
}
