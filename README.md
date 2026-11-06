# NudgePay AI — Proof of Concept (POC) Application

> **Autonomous FinTech Agent & Smart Payment Orchestration Platform**  
> Built strictly according to the *NudgePay AI Master Platform & Engineering Specification (v4.0 Master)*.

---

## 🚀 Key Modules Implemented in this POC

1. **Volume I Consumer Features**:
   - **Feature 1: AI Subscription Swapper & Circle Pooling**: Automatic detection of recurring streaming/utility expenses, promotional catalog matching, and multi-user circle pooling (e.g. 3 standalone Spotify subs into 1 Family Plan saving $64+/yr).
   - **Feature 2: Paper Receipt Grocery Manager & Smart Basket Splitter**: Simulated OCR parser extracting line items, comparing live local store catalogs (Walmart vs Aldi vs Kroger), and calculating multi-store split baskets with trip justification metrics.
   - **Feature 3: In-Store Barcode Scanner & Cashier Price-Match Pass**: UPC lookup returning competitor prices (<850ms SLA), interactive Cashier Pass with SKU/policy verification, and fuel-adjusted store detour map calculator.
   - **Feature 4: Social Bill Splitting & Digital Wallet (Exact-Cent Math)**: Zero-registration light identity SMS links, deterministic exact-cent allocation (zero remainder drift), and wallet ledger balances.
   - **Roadmap Previews**: Spare Change Micro-Savings Round-Up Simulator and Telecom Bill Retention Negotiation Script Generator.

2. **Volume II Engineering & System Architecture**:
   - **FastAPI / Python AI & ML Engine**:
     - XGBoost-style feature extractor & classification heuristic (`GROCERIES`, `SUBSCRIPTION`, `ONLINE_SHOPPING`, `GENERAL`).
     - Isolation Forest 3-sigma anomaly detector for introductory price hikes.
     - SARIMA/Prophet-inspired Safe-to-Spend 30-day liquidity burn projector.
     - 64-bit Perceptual Hash (pHash) DCT receipt deduplication & fraud guard with Hamming distance threshold.
     - LangGraph-style 3-node stateful workflow: Deterministic Auditor -> Market Benchmarking -> Advisory Synthesis with Layer 1/Layer 2 compliance gates.
   - **Node.js / Express / TypeScript-ready Backend Service**:
     - Complete Prisma ORM schema DDL with exact-cent integer math, `NUMERIC(12, 2)`, double-entry ledger audits, and relationships.
     - RESTful APIs covering Webhooks, Transactions, Receipts, Circles, and Wallets.
   - **Interactive Frontend / Demo UI (Web & Mobile Simulator)**:
     - Full interactive single-page dashboard with working live demos for all 4 core features, receipt uploader simulation, barcode scanner simulator, bill split calculator, and AI agent log inspector.

---

## 📂 Monorepo Topology

```text
nudgepay-ai-poc/
├── docker-compose.yml
├── README.md
├── packages/
│   └── database/
│       ├── schema.prisma             # Full Prisma Schema DDL & ledger models
│       └── seed.ts                   # Seed dataset (users, circles, transactions)
├── services/
│   ├── api-gateway/                  # Node.js / Express Backend
│   │   ├── package.json
│   │   ├── server.js                 # API routes & exact-cent split engine
│   │   └── Dockerfile
│   └── ai-engine/                    # Python FastAPI AI / ML Microservice
│       ├── requirements.txt
│       ├── main.py                   # FastAPI app with endpoints
│       ├── ml_modules.py             # Categorizer, Anomaly, Liquidity & pHash
│       ├── langgraph_agent.py        # 3-Node Agentic State Graph & Guardrails
│       └── Dockerfile
└── web-client/
    ├── index.html                    # Interactive Single-Page App Demo
    ├── style.css                     # FinTech Dark/Emerald Modern UI
    └── app.js                        # Dynamic frontend controller & mock API hooks
```

---

## 🛠️ Quickstart Instructions

### Option 1: Run with Docker Compose (Recommended)
```bash
docker-compose up --build
```
- Open `http://localhost:8000` to access the interactive web app & live demo.
- API Gateway running on `http://localhost:3000`.
- Python AI Microservice running on `http://localhost:8001` (OpenAPI Docs at `http://localhost:8001/docs`).

### Option 2: Standalone Local Run
1. **Python AI Engine**:
   ```bash
   cd services/ai-engine
   pip install -r requirements.txt
   uvicorn main:app --port 8001 --reload
   ```
2. **API Gateway**:
   ```bash
   cd services/api-gateway
   npm install
   npm start
   ```
3. **Frontend**:
   Open `web-client/index.html` directly in any web browser.
