// NudgePay AI Interactive Single-Page App Logic & Mock Agent Orchestrator

function switchTab(tabId) {
  document.querySelectorAll('.tab-pane').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
  
  const targetPane = document.getElementById(`tab-${tabId}`);
  if (targetPane) targetPane.classList.add('active');

  const titles = {
    dashboard: ["Executive FinTech Dashboard", "Autonomous interventionist money-saving orchestration"],
    feature1: ["Subscription Swapper & Circle Pooling", "Auto-detection, family tier pooling, and silent price hike mitigation"],
    feature2: ["Paper Receipt OCR & Smart Basket Splitter", "Item-level OCR extraction, 64-bit pHash fraud prevention, and split carts"],
    feature3: ["In-Store Barcode Scanner & Cashier Pass", "Sub-850ms competitor pricing check, cashier match pass, and detour navigation"],
    feature4: ["Social Bill Splitting & In-App Wallet", "Zero-registration light identity SMS links and exact-cent deterministic math"],
    roadmap: ["Expandable AI Roadmap & Innovations", "Spare change round-ups and automated telecom retention scripts"]
  };

  if (titles[tabId]) {
    document.getElementById('page-title').innerText = titles[tabId][0];
    document.getElementById('page-subtitle').innerText = titles[tabId][1];
  }
}

// 1. Run LangGraph Autonomous Agent Workflow
function runLangGraphAgent() {
  const consoleEl = document.getElementById('agent-console');
  consoleEl.innerHTML = `<span style="color:#f59e0b;">[Starting Agent Execution]: Invoking 3-Node Topology...</span><br>`;
  
  setTimeout(() => {
    consoleEl.innerHTML += `[Node 1: Deterministic Auditor] Aggregated 4 recurring charges ($147.97/mo). Auditing leak points...<br>`;
  }, 400);

  setTimeout(() => {
    consoleEl.innerHTML += `[Node 2: Market Benchmarking] Querying indexed retail catalogs & streaming APIs... Verified Spotify 6-seat Family plan ($19.99/mo).<br>`;
  }, 800);

  setTimeout(() => {
    consoleEl.innerHTML += `[Node 3: Advisory Synthesis] Generated structured actions: POOL (Spotify: $191.76/yr circle savings) and CUT (Hulu: $24.12/yr savings).<br>`;
    consoleEl.innerHTML += `<span style="color:#10b981;">[Compliance Gate Passed]: Layer 1 (Math exact-cent verify) & Layer 2 (Ledger write isolation) OK.</span>`;
  }, 1200);
}

// 2. 1-Tap Execution of Subscription Migrations
function execute1TapSwap(service) {
  alert(`[NudgePay Autonomous Swapper]: Successfully executed 1-Tap transition for ${service}! Updated monthly direct debit and notified circle members.`);
}

// 3. Receipt OCR & Smart Basket Splitter Simulation
function simulateReceiptOCR() {
  const rawText = document.getElementById('receipt-text-input').value;
  const container = document.getElementById('ocr-results-container');
  
  container.innerHTML = `<div style="padding:1rem; color:#38bdf8;">Processing with simulated AWS Textract OCR & computing 64-bit DCT pHash...</div>`;
  
  setTimeout(() => {
    container.innerHTML = `
      <div class="pooling-box">
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <span class="pill pill-info">OCR P95 Latency: 1.1s</span>
          <span style="font-family:'JetBrains Mono'; font-size:0.75rem; color:#94a3b8;">pHash: 4a9f2b8c0d1e573a</span>
        </div>
        <h4>Smart Basket Split Recommendation</h4>
        <p style="font-size:0.85rem; color:#94a3b8;">Rather than shopping at a single supermarket, splitting into two local carts saves <strong>$21.40</strong> next week:</p>
        
        <div style="background:rgba(0,0,0,0.3); padding:0.8rem; border-radius:6px; font-size:0.82rem;">
          <strong style="color:#10b981;">Cart 1: Aldi (Produce & Pantry Staples)</strong><br>
          • Hass Avocados, Whole Milk, Eggs, Apples, Fresh Chicken<br>
          <span style="color:#94a3b8;">Est. Cost: $21.50 (Saves $8.40 vs Walmart produce)</span>
        </div>

        <div style="background:rgba(0,0,0,0.3); padding:0.8rem; border-radius:6px; font-size:0.82rem; margin-top:0.5rem;">
          <strong style="color:#3b82f6;">Cart 2: Walmart (Bulk Goods & Home Consumables)</strong><br>
          • Bounty Paper Towels 12pk, Tide Pods 42ct, Dawn Soap<br>
          <span style="color:#94a3b8;">Est. Cost: $34.20 (Saves $13.00 vs supermarket pricing)</span>
        </div>

        <div class="savings-alert">
          ✅ <strong>Trip Justification:</strong> Net savings ($21.40) exceeds estimated fuel ($1.20). 1-click pickup carts prepared.
        </div>
        <button class="btn btn-primary" onclick="alert('Order carts sent to Aldi & Walmart pickup APIs!')">
          ⚡ 1-Click Approve Split Pickup Carts
        </button>
      </div>
    `;
  }, 600);
}

// 4. Duplicate Fraud Guard Test
function testDuplicateFraud() {
  const container = document.getElementById('ocr-results-container');
  container.innerHTML = `
    <div style="background:rgba(244,63,94,0.15); border:1px solid #f43f5e; padding:1.25rem; border-radius:8px; color:#fff;">
      <h4 style="color:#f43f5e;">🛑 Duplicate Receipt Rejected (Anti-Fraud Guard)</h4>
      <p style="font-size:0.85rem; margin-top:0.5rem;">
        64-Bit Perceptual Hash match detected with an earlier upload in circle "Sunset Roommates".
      </p>
      <div style="font-family:'JetBrains Mono'; font-size:0.75rem; margin-top:0.5rem; background:rgba(0,0,0,0.4); padding:0.5rem; border-radius:4px;">
        Fingerprint: e8f1c4a09b2d3e11<br>
        Hamming Distance: 1 (≤ 3 within 90-day threshold)<br>
        Status: FRAUD_PREVENTION_TRIGGERED
      </div>
    </div>
  `;
}

// 5. Barcode Scanner & Cashier Pass
function lookupBarcode() {
  const code = document.getElementById('barcode-select').value;
  const container = document.getElementById('barcode-result-container');
  
  container.innerHTML = `<div style="padding:1rem; color:#38bdf8;">Querying indexed retail catalog APIs (SLA <850ms)...</div>`;
  
  setTimeout(() => {
    if (code === "012345678901") {
      container.innerHTML = `
        <div class="cashier-pass-card">
          <div class="pass-header">
            <div>
              <span style="font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; color:#a7f3d0;">Verified Cashier Pass</span>
              <h3>Target Cashier Price Match</h3>
            </div>
            <span class="pill pill-warning" style="background:#f59e0b; color:#000;">Save $70.00</span>
          </div>
          <p style="font-size:0.85rem;"><strong>Item:</strong> Sony WH-1000XM5 Wireless Headphones</p>
          <div style="display:flex; justify-content:space-between; margin-top:0.5rem; font-size:0.85rem;">
            <span>Target Shelf Price: <strong>$399.99</strong></span>
            <span>Best Buy Competitor: <strong style="color:#6ee7b7;">$329.99</strong></span>
          </div>
          
          <div class="pass-barcode">||| | |||| || ||| |||| | |||</div>
          <div style="text-align:center; font-size:0.72rem; color:#d1fae5; font-family:'JetBrains Mono';">UPC: 012345678901 | SKU: BB-994102</div>
          
          <div style="background:rgba(0,0,0,0.3); padding:0.75rem; border-radius:6px; font-size:0.78rem; margin-top:0.75rem;">
            <strong>Target Price Match Guarantee Policy:</strong> We match Best Buy on identical, in-stock items at checkout. Cashier discount override code #44.
          </div>
        </div>
      `;
    } else {
      container.innerHTML = `
        <div class="cashier-pass-card" style="background:linear-gradient(135deg, #1e3a8a 0%, #172554 100%); border-color:#3b82f6;">
          <div class="pass-header">
            <div>
              <span style="font-size:0.75rem; text-transform:uppercase; letter-spacing:1px; color:#93c5fd;">Verified Cashier Pass</span>
              <h3>Walmart Price Match Pass</h3>
            </div>
            <span class="pill" style="background:#10b981; color:#000;">Save $19.01</span>
          </div>
          <p style="font-size:0.85rem;"><strong>Item:</strong> Ninja Air Fryer Pro 4-in-1</p>
          <div style="display:flex; justify-content:space-between; margin-top:0.5rem; font-size:0.85rem;">
            <span>Walmart Shelf Price: <strong>$89.00</strong></span>
            <span>Amazon Direct: <strong style="color:#93c5fd;">$69.99</strong></span>
          </div>
          
          <div class="pass-barcode">|||| | || ||||| || | |||| ||</div>
          <div style="text-align:center; font-size:0.72rem; color:#bfdbfe; font-family:'JetBrains Mono';">UPC: 098765432109</div>
        </div>
      `;
    }
  }, 450);
}

// 6. Deterministic Exact-Cent Bill Splitting
function calculateExactCentSplit() {
  const title = document.getElementById('split-title').value;
  const amount = parseFloat(document.getElementById('split-amount').value);
  const totalCents = Math.round(amount * 100);
  const rawParticipants = document.getElementById('split-participants').value.split('\n').filter(p => p.trim());
  
  const n = rawParticipants.length;
  if (n === 0) return alert('Add at least one participant.');

  const baseCents = Math.floor(totalCents / n);
  const remainder = totalCents % n;
  
  let html = `
    <div class="pooling-box">
      <div style="display:flex; justify-content:space-between;">
        <h4>${title}</h4>
        <span class="pill pill-info">Exact-Cent Verification: 0.00% Drift</span>
      </div>
      <p style="font-size:0.82rem; color:#94a3b8;">Total: $${(totalCents / 100).toFixed(2)} (${totalCents} cents) divided across ${n} people.</p>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Participant</th>
              <th>Deterministic Share</th>
              <th>Settlement SMS Link</th>
            </tr>
          </thead>
          <tbody>
  `;

  let sumCheck = 0;
  rawParticipants.forEach((p, i) => {
    const allocated = baseCents + (i < remainder ? 1 : 0);
    sumCheck += allocated;
    const name = p.split(',')[0].trim();
    html += `
      <tr>
        <td><strong>${name}</strong></td>
        <td style="font-family:'JetBrains Mono'; color:#10b981;">$${(allocated / 100).toFixed(2)}</td>
        <td>
          <a href="#" style="color:#38bdf8; font-size:0.75rem;" onclick="alert('Simulated SMS sent: Hi ${name}, please settle your $${(allocated/100).toFixed(2)} share via Apple Pay: https://pay.nudgepay.ai/s/${name.toLowerCase()}')">
            📲 Send 1-Tap SMS Link
          </a>
        </td>
      </tr>
    `;
  });

  html += `
          </tbody>
        </table>
      </div>
      <div class="savings-alert" style="font-family:'JetBrains Mono'; font-size:0.78rem;">
        Ledger Verification: Sum of shares = ${sumCheck}¢ / Total = ${totalCents}¢ (Drift: 0¢).
      </div>
    </div>
  `;

  document.getElementById('split-results-container').innerHTML = html;
}

// 7. Micro-Savings Round-Up Simulator
function simulateRoundUp() {
  const amt = parseFloat(document.getElementById('roundup-amount').value);
  const totalCents = Math.round(amt * 100);
  const remainder = totalCents % 100;
  const sweepCents = remainder === 0 ? 0 : (100 - remainder);
  
  document.getElementById('roundup-result').innerHTML = `
    <div style="background:rgba(16,185,129,0.1); border:1px solid #10b981; padding:0.8rem; border-radius:6px; font-size:0.85rem;">
      Purchase: <strong>$${amt.toFixed(2)}</strong> ➜ Rounded up to <strong>$${Math.ceil(amt)}.00</strong><br>
      💰 Micro-Savings Swept to Vault: <strong>$${(sweepCents/100).toFixed(2)}</strong> (${sweepCents}¢)
    </div>
  `;
}

// 8. Retention Script Generator
function generateRetentionScript() {
  const service = document.getElementById('telecom-service').value;
  document.getElementById('retention-result').innerHTML = `
    <div class="console-box" style="height:auto; margin-top:0.5rem; font-size:0.75rem;">
      <strong>[AI Negotiation Agent Retention Script for ${service}]</strong><br><br>
      "Hello, I am reviewing my monthly statement and noticed my introductory rate expired, jumping my bill by over 30%. Competitors in my area currently offer equivalent broadband at $45.00/month. Because I have been a prompt-paying customer for over 12 months, I would like to request that my account be placed on your current customer retention promotional rate of $50.00/month, or I will need to initiate cancellation today."<br><br>
      <em>Est. annual recurring savings if negotiated: $420.00/year.</em>
    </div>
  `;
}
