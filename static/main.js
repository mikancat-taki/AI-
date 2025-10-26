document.getElementById("send").onclick = async () => {
  const msg = document.getElementById("msg").value;
  const res = await fetch("/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({message: msg})
  });
  const data = await res.json();
  const box = document.getElementById("chat-box");
  box.innerHTML += `<div><b>YOU:</b> ${msg}</div>`;
  box.innerHTML += `<div><b>AI:</b> ${data.reply}</div>`;
  document.getElementById("msg").value = "";
};
