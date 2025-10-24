import React, { useState } from 'react';
import axios from 'axios';
import DashboardNavbar from './DashboardNavbar';
import './css/Dashboard.css';

function StudentDashboard() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);

  const handleLogout = () => {
    localStorage.removeItem('studentToken');
    localStorage.removeItem('adminToken');
    window.location.href = '/';
  };

  const handleSend = async () => {
    if (!message.trim()) return;

    const userMessage = { role: "user", text: message };
    setChat([...chat, userMessage]);
    setMessage("");

    try {
      const res = await axios.post("http://localhost:5000/api/chatbot/chat", { message });
      console.log("AI Response:", res.data);
      const aiMessage = { role: "ai", text: res.data.reply };
      setChat((prev) => [...prev, aiMessage]);
    } catch (err) {
      console.error("Chatbot error:", err);
      setChat((prev) => [...prev, { role: "ai", text: "Error connecting to chatbot." }]);
      console.error(err);
    }
  };

  return (
    <div>
      <DashboardNavbar onLogout={handleLogout} />
      <div className="dashboard-container">
        <h2>Welcome, Student!</h2>
        <section>
          <h3>Upcoming Companies</h3>
          <ul>
            <li>Company A - 25th Oct</li>
            <li>Company B - 28th Oct</li>
            <li>Company C - 1st Nov</li>
          </ul>
        </section>
        <section>
          <h3>Skill Gap Analysis</h3>
          <p>You need to improve: React, Python, SQL</p>
        </section>
        <section>
          <h3>Resume Analysis</h3>
          <p>Your resume score: 75%</p>
        </section>

        {/* Chatbot Section */}
        <div className="chatbot-container">
          <h3>Placement Assistant Chatbot</h3>
          <div className="chat-window">
            {chat.map((msg, index) => (
              <div
                key={index}
                className={`chat-message ${msg.role === "user" ? "user" : "ai"}`}
              >
                {msg.text}
              </div>
            ))}
          </div>
          <div className="chat-input">
            <input
              type="text"
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && handleSend()}
              placeholder="Ask me about placements..."
            />
            <button onClick={handleSend}>Send</button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default StudentDashboard;
