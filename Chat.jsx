import React, { useEffect, useRef, useState } from "react";

export default function Chat() {
  const ws = useRef(null);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  useEffect(() => {
    ws.current = new WebSocket("ws://localhost:8000/ws/chat");

    ws.current.onmessage = (event) => {
      const data = JSON.parse(event.data);

      if (data.type === "chunk") {
        setMessages((prev) => {
          const last = prev[prev.length - 1];

          if (!last || last.role !== "assistant" || last.done) {
            return [...prev, { role: "assistant", text: data.text, done: false }];
          }

          last.text += data.text;
          return [...prev];
        });
      }

      if (data.type === "done") {
        setMessages((prev) =>
          prev.map((m) =>
            m.role === "assistant" && !m.done
              ? { ...m, done: true }
              : m
          )
        );
      }
    };

    return () => {
      ws.current.close();
    };
  }, []);

  const sendMessage = () => {
    if (!input.trim()) return;

    setMessages((prev) => [...prev, { role: "user", text: input }]);

    ws.current.send(JSON.stringify({ question: input }));
    setInput("");
  };

  return (
    <div style={{ width: "600px", padding: "20px" }}>
      <div
        style={{
          height: "400px",
          overflowY: "scroll",
          border: "1px solid #ccc",
          padding: "10px"
        }}
      >
        {messages.map((m, i) => (
          <div key={i} style={{ margin: "10px 0" }}>
            <b>{m.role === "user" ? "Você" : "Assistente"}:</b> {m.text}
          </div>
        ))}
      </div>

      <div style={{ marginTop: 10 }}>
        <input
          style={{ width: "70%" }}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Digite sua pergunta..."
        />
        <button onClick={sendMessage} style={{ marginLeft: 10 }}>
          Enviar
        </button>
      </div>
    </div>
  );
}
