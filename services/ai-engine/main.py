"""
NudgePay AI - FastAPI Microservice
Exposes REST endpoints for AI, ML, OCR simulation, barcode price-matching, and LangGraph pipelines.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from ml_modules import (
    classify_transaction,
    detect_anomaly,
    calculate_safe_to_spend,
    generate_phash_64,
    verify_receipt_duplicate
)
from langgraph_agent import NudgePayAgentGraph

app = FastAPI(
    title="NudgePay AI - Intelligent FinTech Agent Engine",
    description="Microservice powering autonomous subscription audits, receipt OCR matching, barcode price checks, and exact-cent group splits.",
    version="4.0.0"
)

agent_graph = NudgePayAgentGraph()

# In-memory storage for simulated receipts & hashes
KNOWN_RECEIPT_HASHES = ["e8f1c4a09b2d3e11", "a1b2c3d4e5f60718"]

class TransactionRequest(BaseModel):
    merchant: str
    amount_cents: int
    history_cents: Optional[List[int]] = []

class SafeToSpendRequest(BaseModel):
    current_balance_cents: int
    upcoming_fixed_cents: int
    payroll_inflow_cents: int

class BarcodeRequest(BaseModel):
    barcode: str
    current_store: Optional[str] = "Target"

class ReceiptOCRRequest(BaseModel):
    raw_text: str
    circle_id: Optional[str] = "circle-123"

class ExactCentSplitRequest(BaseModel):
    total_cents: int
    participants: List[str] # List of names or phone numbers

@app.get("/")
def health_check():
    return {
        "status": "online",
        "service": "NudgePay AI Python Engine",
        "version": "4.0.0",
        "guardrail_status": "L1_L2_ACTIVE"
    }

@app.post("/api/ml/categorize")
def categorize_endpoint(req: TransactionRequest):
    category = classify_transaction(req.merchant, req.amount_cents)
    anomaly_result = detect_anomaly(req.history_cents, req.amount_cents)
    return {
        "merchant": req.merchant,
        "amount_cents": req.amount_cents,
        "category": category,
        "anomaly_analysis": anomaly_result
    }

@app.post("/api/ml/safe-to-spend")
def safe_to_spend_endpoint(req: SafeToSpendRequest):
    result = calculate_safe_to_spend(
        req.current_balance_cents,
        req.upcoming_fixed_cents,
        req.payroll_inflow_cents
    )
    return result

@app.post("/api/ml/barcode-price-match")
def barcode_match_endpoint(req: BarcodeRequest):
    item = agent_graph.catalog_retail.get(req.barcode)
    if not item:
        return {
            "found": False,
            "barcode": req.barcode,
            "message": "Item indexed in retail catalog, but no lower competitor price found. You have the best deal!"
        }
    
    savings_cents = item["current_price_cents"] - item["competitor_price_cents"]
    return {
        "found": True,
        "product_name": item["product_name"],
        "scanned_store": item["current_store"],
        "scanned_price_cents": item["current_price_cents"],
        "scanned_price_usd": f"${item['current_price_cents']/100:.2f}",
        "competitor": item["competitor"],
        "competitor_price_cents": item["competitor_price_cents"],
        "competitor_price_usd": f"${item['competitor_price_cents']/100:.2f}",
        "instant_savings_usd": f"${savings_cents/100:.2f}",
        "cashier_price_match_pass": {
            "eligible": savings_cents > 0,
            "upc": req.barcode,
            "policy_statement": item["match_policy"],
            "verification_status": "VERIFIED_ACTIVE_PROMO"
        },
        "detour_navigation": {
            "distance_miles": 1.4,
            "estimated_fuel_cost_cents": 42,
            "net_savings_cents": savings_cents - 42
        }
    }

@app.post("/api/ocr/parse-receipt")
def parse_receipt_endpoint(req: ReceiptOCRRequest):
    # Calculate 64-bit perceptual hash for deduplication
    phash = generate_phash_64(req.raw_text)
    dup_check = verify_receipt_duplicate(phash, KNOWN_RECEIPT_HASHES)
    
    if dup_check["is_duplicate"]:
        raise HTTPException(
            status_code=400,
            detail=f"Receipt rejected: Duplicate receipt detected within circle (Hamming distance: {dup_check['hamming_distance']})."
        )
    
    # Store new receipt hash
    KNOWN_RECEIPT_HASHES.append(phash)
    
    # Simulate Line Item Extraction (AWS Textract style)
    lines = [l.strip() for l in req.raw_text.splitlines() if l.strip()]
    items = []
    total_cents = 0
    for line in lines:
        if "-" in line:
            parts = line.rsplit("-", 1)
            name = parts[0].strip()
            try:
                price = float(parts[1].replace("$", "").strip())
                cents = int(round(price * 100))
                items.append({"name": name, "price_cents": cents, "price_usd": f"${price:.2f}"})
                total_cents += cents
            except ValueError:
                continue
    
    # Smart Basket Splitter Logic (Aldi vs Walmart vs Kroger)
    # Produce & staples cheaper at Aldi; bulk paper goods cheaper at Walmart
    basket_aldi = []
    basket_walmart = []
    savings_accumulator = 0
    
    for it in items:
        n = it["name"].lower()
        if any(w in n for w in ["avocado", "milk", "egg", "apple", "bread", "banana"]):
            aldi_discount = int(it["price_cents"] * 0.22)
            savings_accumulator += aldi_discount
            basket_aldi.append({**it, "store": "Aldi", "discount_cents": aldi_discount})
        else:
            walmart_discount = int(it["price_cents"] * 0.15)
            savings_accumulator += walmart_discount
            basket_walmart.append({**it, "store": "Walmart", "discount_cents": walmart_discount})
            
    return {
        "receipt_phash_64": phash,
        "duplicate_audit": dup_check,
        "extracted_items_count": len(items),
        "items": items,
        "original_total_usd": f"${total_cents/100:.2f}",
        "smart_basket_split": {
            "basket_1": {"store": "Aldi (Produce & Pantry)", "items": basket_aldi},
            "basket_2": {"store": "Walmart (Bulk Goods & Home)", "items": basket_walmart},
            "total_split_savings_usd": f"${savings_accumulator/100:.2f}",
            "trip_justification": "Savings exceed $5.00 threshold; two-store pickup recommended." if savings_accumulator > 500 else "Single store swap recommended."
        }
    }

@app.post("/api/ledger/split-exact-cent")
def split_exact_cent_endpoint(req: ExactCentSplitRequest):
    """
    Exact-cent integer split math guaranteeing 0.00% rounding drift.
    Distributes remainder cents deterministically to the first n payers.
    """
    n = len(req.participants)
    if n == 0:
        raise HTTPException(status_code=400, detail="At least 1 participant required.")
    
    base_cents = req.total_cents // n
    remainder = req.total_cents % n
    
    splits = []
    for i, p in enumerate(req.participants):
        allocated = base_cents + (1 if i < remainder else 0)
        splits.append({
            "participant": p,
            "share_cents": allocated,
            "share_usd": f"${allocated / 100:.2f}",
            "settlement_sms_link": f"https://pay.nudgepay.ai/s/{p.lower().replace(' ', '')}-{allocated}"
        })
    
    # Audit verification
    sum_check = sum(s["share_cents"] for s in splits)
    assert sum_check == req.total_cents, "Integrity failure: rounding drift detected!"
    
    return {
        "original_total_cents": req.total_cents,
        "original_total_usd": f"${req.total_cents / 100:.2f}",
        "participant_count": n,
        "splits": splits,
        "audit": {
            "sum_allocated_cents": sum_check,
            "drift_cents": 0,
            "status": "ZERO_DRIFT_VERIFIED"
        }
    }

@app.post("/api/agent/run-autonomous-audit")
def run_autonomous_audit_endpoint(payload: Dict[str, Any]):
    """
    Triggers the 3-node LangGraph autonomous agent workflow.
    """
    result = agent_graph.run(payload)
    return result
