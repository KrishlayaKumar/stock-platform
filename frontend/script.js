/* ---------- PARALLAX ---------- */
const parallaxBg = document.querySelector(".parallax-bg");
window.addEventListener("scroll", () => {
  if (parallaxBg) {
    parallaxBg.style.transform = `translateY(${window.scrollY * 0.3}px)`;
  }
});

/* ---------- SCROLL REVEAL ---------- */
const appSection = document.getElementById("app");

window.addEventListener("scroll", () => {
  const revealPoint = window.innerHeight * 0.5;

  if (window.scrollY > revealPoint) {
    appSection.classList.remove("hidden");
  }
});


/* ---------- ANALYZE ---------- */
let chart = null;

function analyzeStock() {
  const stock = document.getElementById("stockSelect").value;
  if (!stock) return alert("Please select a stock");

  document.getElementById("result").classList.add("hidden");
  document.getElementById("loader").classList.remove("hidden");

  fetch("/analyze", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ symbol: stock })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("loader").classList.add("hidden");

    const badge =
      data.recommendation === "BUY" ? "buy" :
      data.recommendation === "SELL" ? "sell" : "hold";

    document.getElementById("result").innerHTML = `
      <p><b>Stock:</b> ${data.stock}</p>
      <p><b>Direction:</b> ${data.direction}</p>
      <p><b>Confidence:</b> ${data.confidence}%</p>
      <p><b>Sentiment:</b> ${data.sentiment}</p>
      <p><b>Recommendation:</b>
        <span class="badge ${badge}">${data.recommendation}</span>
      </p>
    `;
    document.getElementById("result").classList.remove("hidden");

    renderChart(generateDummyOHLC());
  });
}

/* ---------- DUMMY CANDLE DATA ---------- */
function generateDummyOHLC() {
  let price = 100;
  return Array.from({ length: 20 }, (_, i) => {
    let open = price;
    let close = open + (Math.random() - 0.5) * 8;
    let high = Math.max(open, close) + Math.random() * 4;
    let low = Math.min(open, close) - Math.random() * 4;
    price = close;

    return { x: i, o: open, h: high, l: low, c: close };
  });
}

/* ---------- CHART ---------- */
function renderChart(data) {
  const ctx = document.getElementById("priceChart");
  ctx.classList.remove("hidden");

  if (chart) chart.destroy();

  chart = new Chart(ctx, {
    type: "candlestick",
    data: {
      datasets: [{
        label: "Price",
        data: data,
        color: {
          up: "#2ecc71",
          down: "#e74c3c",
          unchanged: "#aaa"
        }
      }]
    },
    options: {
      responsive: true
    }
  });
}

/* ---------- EYES ---------- */
document.addEventListener("mousemove", e => {
  document.querySelectorAll(".pupil").forEach(pupil => {
    const eye = pupil.parentElement.getBoundingClientRect();
    pupil.style.transform =
      `translate(${(e.clientX - eye.left - eye.width/2)/8}px,
                 ${(e.clientY - eye.top - eye.height/2)/8}px)`;
  });
});

/* ---------- INDIAN TIME ---------- */
function updateTime() {
  const time = new Date().toLocaleTimeString("en-IN", {
    timeZone: "Asia/Kolkata"
  });
  document.getElementById("time").innerText = `🇮🇳 ${time}`;
}
setInterval(updateTime, 1000);
updateTime();
