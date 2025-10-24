import React, { useState } from "react";
import axios from "axios";

function Chatbot() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);

  const sendMessage = async () => {
    if (!message.trim()) return;
    setChat([...chat, { sender: "user", text: message }]);

    try {
      const res = await axios.post("http://127.0.0.1:5000/api/chatbot/chat", { message });
      const reply = res.data.reply;
      setChat([...chat, { sender: "user", text: message }, { sender: "bot", text: reply }]);
      setMessage("");
    } catch (err) {
      setChat([...chat, { sender: "bot", text: "Error connecting to chatbot." }]);
    }
  };

  return (
    <div className="chatbot">
      <div className="chat-window">
        {chat.map((msg, i) => (
          <p key={i} className={msg.sender}>{msg.sender}: {msg.text}</p>
        ))}
      </div>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Ask me something..."
      />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

export default Chatbot;
