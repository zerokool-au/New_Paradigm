// rr-visualizer/logger.js
export function logContradiction(event) {
  const logEntry = {
    timestamp: new Date().toISOString(),
    type: "contradiction",
    source: event.source || "unknown",
    details: event.details || {},
  };

  console.log("🧠 RR Contradiction Event:", logEntry);

  // Optional: persist locally
  // localStorage.setItem("rr_last_contradiction", JSON.stringify(logEntry));
}
