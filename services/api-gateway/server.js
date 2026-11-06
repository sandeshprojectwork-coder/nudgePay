const express = require('express');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;
const AI_SERVICE_URL = process.env.AI_SERVICE_URL || 'http://localhost:8001';

app.use(cors());
app.use(express.json());

// In-memory mock database for fast POC demonstration
const db = {
  users: [
    { id: 'usr-1', name: 'Alex Rivera', phone: '+14155550192', walletCents: 4520 },
    { id: 'usr-2', name: 'Jordan Lee', phone: '+14155550143', walletCents: 1200 },
    { id: 'usr-3', name: 'Taylor Swift', phone: '+14155550188', walletCents: 8900 }
  ],
  circles: [
    { id: 'cir-1', name: 'Sunset Roommates', members: ['usr-1', 'usr-2', 'usr-3'] }
  ],
  transactions: [
    { id: 'tx-1', userId: 'usr-1', merchant: 'Hulu', amountCents: 1000, isRecurring: true, date: '2026-11-03' },
    { id: 'tx-2', userId: 'usr-1', merchant: 'Spotify Premium', amountCents: 1199, isRecurring: true, date: '2026-11-01' },
    { id: 'tx-3', userId: 'usr-2', merchant: 'Spotify Premium', amountCents: 1199, isRecurring: true, date: '2026-11-01' },
    { id: 'tx-4', userId: 'usr-3', merchant: 'Spotify Premium', amountCents: 1199, isRecurring: true, date: '2026-11-02' }
  ]
};

// Exact-Cent Allocation Helper
function distributeExactCents(totalCents, count) {
  const base = Math.floor(totalCents / count);
  const remainder = totalCents % count;
  const allocations = [];
  for (let i = 0; i < count; i++) {
    allocations.push(base + (i < remainder ? 1 : 0));
  }
  return allocations;
}

// Health route
app.get('/health', (req, res) => {
  res.json({
    service: 'NudgePay Node API Gateway',
    status: 'HEALTHY',
    version: '4.0.0',
    db_connected: true
  });
});

// Bill Split Endpoint (Light-Identity zero-registration)
app.post('/api/splits/create', (req, res) => {
  const { title, totalCents, participants } = req.body;
  if (!participants || participants.length === 0) {
    return res.status(400).json({ error: 'Participants array required' });
  }

  const shares = distributeExactCents(totalCents, participants.length);
  const splitDetails = participants.map((p, index) => ({
    name: p.name || `Payer ${index + 1}`,
    phone: p.phone,
    shareCents: shares[index],
    shareUsd: `$${(shares[index] / 100).toFixed(2)}`,
    smsLink: `https://pay.nudgepay.ai/pay/${Math.random().toString(36).substring(7)}`,
    status: 'SENT_VIA_SMS'
  }));

  res.json({
    splitId: `split-${Date.now()}`,
    title,
    totalCents,
    totalUsd: `$${(totalCents / 100).toFixed(2)}`,
    audit: {
      allocatedTotal: shares.reduce((a, b) => a + b, 0),
      driftCents: 0
    },
    splits: splitDetails
  });
});

// Wallet balance endpoint
app.get('/api/wallet/:userId', (req, res) => {
  const user = db.users.find(u => u.id === req.params.userId) || db.users[0];
  res.json({
    userId: user.id,
    name: user.name,
    balanceCents: user.walletCents,
    balanceUsd: `$${(user.walletCents / 100).toFixed(2)}`,
    stripeConnectStatus: 'EXPRESS_ACTIVE',
    instantPayoutEligible: true
  });
});

app.listen(PORT, () => {
  console.log(`NudgePay API Gateway running on port ${PORT}`);
});
