// Get references to the DOM elements
const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

// Bot's simple response logic
const botResponses = {
    hello: "Hi there! How can I assist you today?",
    help: "I'm here to help! Try asking me anything.",
    bye: "Goodbye! Have a great day!",
};

// Add a message to the chat
function addMessage(text, sender) {
    const message = document.createElement('div');
    message.classList.add('message', sender);
    message.textContent = text;
    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to the latest message
}

// Handle user input
function handleUserMessage() {
    const userText = userInput.value.trim();
    if (userText === "") return;

    // Add user's message
    addMessage(userText, 'user');

    // Generate bot response
    const botText = botResponses[userText.toLowerCase()] || "I'm not sure how to respond to that.";
    setTimeout(() => addMessage(botText, 'bot'), 500);

    // Clear input
    userInput.value = '';
}

// Event listeners
sendBtn.addEventListener('click', handleUserMessage);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') handleUserMessage();
});
