async function analyze() {
  const home = document.getElementById("home").value;
  const away = document.getElementById("away").value;

  const res = await fetch("/analyze", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({home, away})
  });

  const data = await res.json();
  document.getElementById("output").innerText =
    JSON.stringify(data, null, 2);
}
