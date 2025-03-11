document.addEventListener("DOMContentLoaded", function () {
    let chatButtonVisible = false;
    let chatBoxVisible = false;
    let scrollTimeout;

    function createChatButton() {
        if (chatButtonVisible) return;
        chatButtonVisible = true;

        const chatButton = document.createElement("button");
        chatButton.innerText = "Консультант Chiara";
        chatButton.style.position = "fixed";
        chatButton.style.top = "1%";
        chatButton.style.left = "1%";
        chatButton.style.width = "auto";
        chatButton.style.height = "45.2px";
        chatButton.style.padding = "10px 20px";
        chatButton.style.background = "rgba(142, 125, 217, 0.5)";
        chatButton.style.color = "white";
        chatButton.style.border = "1px solid #ffffff7b";
        chatButton.style.borderRadius = "0.6rem";
        chatButton.style.cursor = "pointer";
        chatButton.style.zIndex = "1000";
        chatButton.style.fontFamily = "Caveat-Bold, cursive";
        chatButton.style.fontSize = "20px";
        chatButton.style.boxShadow = "0px 24px 10px -14px #6656ac";
        chatButton.style.transition = "top 0.5s ease-in-out, width 0.3s ease-in-out, opacity 0.5s ease-in-out, visibility 0.5s";
        chatButton.style.opacity = "0";
        chatButton.style.visibility = "hidden";
        document.body.appendChild(chatButton);

        setTimeout(() => {
            chatButton.style.opacity = "1";
            chatButton.style.visibility = "visible";
        }, 500);

        window.addEventListener("scroll", function () {
            if (window.scrollY === 0) {
                chatButton.style.top = "1%";
                chatButton.innerText = "Консультант Chiara";
                chatButton.style.width = "auto";
            } else {
                chatButton.style.top = "10%";
                chatButton.innerText = "Chiara";
                chatButton.style.width = "81.05px";
            }
        });

        const chatContainer = document.createElement("div");
        chatContainer.innerHTML = `
            <div id="chiara-chatbox" style="position: fixed; bottom: 100px; right: 20px; width: 300px; height: 400px; background: white; border: 1px solid #ccc; border-radius: 10px; overflow: hidden; display: none; flex-direction: column; box-shadow: 0 4px 8px rgba(0,0,0,0.2); font-family: 'Roboto-Italic', sans-serif; opacity: 0; transition: opacity 0.5s ease-in-out;">
                <div style="background: #8e7dd9; color: white; padding: 10px; text-align: center; font-weight: bold; display: flex; justify-content: space-between; align-items: center; font-family: 'Caveat-Bold', cursive; font-size: 20px;">
                    <span>Консультант Chiara</span>
                    <button id="chiara-close" style="background: none; border: none; color: white; font-size: 16px; cursor: pointer; font-family: 'Caveat-Bold', cursive;">✖</button>
                </div>
                <div id="chiara-messages" style="flex-grow: 1; padding: 10px; overflow-y: auto; font-family: 'Roboto-Italic', sans-serif;"></div>
                <div style="display: flex; align-items: center; padding: 5px; border-top: 1px solid #ccc;">
                    <input id="chiara-input" type="text" placeholder="Задай вопрос..." style="flex-grow: 1; border: none; padding: 10px; outline: none; font-family: 'Roboto-Italic', sans-serif;">
                    <button id="chiara-send" style="background: none; border: none; cursor: pointer; font-size: 20px; padding: 10px;">➤</button>
                </div>
            </div>
        `;
        document.body.appendChild(chatContainer);

        const chatBox = document.getElementById("chiara-chatbox");
        const input = document.getElementById("chiara-input");
        const messages = document.getElementById("chiara-messages");
        const closeButton = document.getElementById("chiara-close");
        const sendButton = document.getElementById("chiara-send");

        function sendMessage() {
            const message = input.value.trim();
            if (message) {
                messages.innerHTML += `<div style='margin: 5px 0; text-align: right; font-family: Roboto-Italic, sans-serif;'><b>Вы:</b> ${message}</div>`;
                input.value = "";
                input.focus();

                fetch("/api/chiara-chat/", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ message })
                })
                .then(response => response.json())
                .then(data => {
                    messages.innerHTML += `<div style='margin: 5px 0; text-align: left; font-family: Roboto-Italic, sans-serif;'><b>Chiara:</b> ${data.reply}</div>`;
                    messages.scrollTop = messages.scrollHeight;
                })
                .catch(err => console.error("Ошибка чата Chiara:", err));
            }
        }

        input.addEventListener("keydown", function (e) {
            if (e.key === "Enter") {
                e.preventDefault();
                sendMessage();
            }
        });

        sendButton.addEventListener("click", sendMessage);

        chatButton.addEventListener("click", function () {
            chatBox.style.display = "flex";
            setTimeout(() => chatBox.style.opacity = "1", 10);
            chatButton.style.display = "none";
            chatBoxVisible = true;
            messages.innerHTML += `<div style='margin: 5px 0; text-align: left; font-family: Roboto-Italic, sans-serif;'><b>Chiara:</b> Привет! Я Chiara, твой консультант. Ты можешь задать мне любой вопрос.</div>`;
        });

        closeButton.addEventListener("click", function () {
            chatBox.style.opacity = "0";
            setTimeout(() => {
                chatBox.style.display = "none";
                chatButton.style.display = "block";
                chatBoxVisible = false;
            }, 500);
        });
    }

    setTimeout(createChatButton, 5000);

    window.addEventListener("scroll", function () {
        if (!chatButtonVisible) {
            createChatButton();
        }
    });
});
