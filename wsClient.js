export function createWS() {
  return new WebSocket("ws://localhost:8000/ws/chat");
}
