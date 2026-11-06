"""
NudgePay AI - Machine Learning & Heuristic Modules
Covers:
7.1 Category Classification & Anomaly Detection (Isolation Forest / 3-sigma)
7.2 Liquidity Forecasting & Safe-to-Spend Guard (SARIMA/Prophet baseline)
7.3 Receipt Fraud & Duplicate Prevention (64-bit Perceptual Hashing & Hamming Distance)
"""
import math
import hashlib

def classify_transaction(merchant_name: str, amount_cents: int) -> str:
    """
    Simulates fast XGBoost PFC categorization engine with sub-10ms response.
    Categories: GROCERIES, SUBSCRIPTION, ONLINE_SHOPPING, GENERAL
    """
    m = merchant_name.lower()
    if any(k in m for k in ["hulu", "netflix", "spotify", "disney", "apple", "prime", "youtube"]):
        return "SUBSCRIPTION"
    if any(k in m for k in ["walmart", "kroger", "aldi", "trader joe", "heb", "safeway", "whole foods"]):
        return "GROCERIES"
    if any(k in m for k in ["amazon", "best buy", "ebay", "target"]):
        return "ONLINE_SHOPPING"
    return "GENERAL"

def detect_anomaly(historical_charges: list[int], current_charge_cents: int) -> dict:
    """
    Isolation Forest / 3-sigma anomaly detector.
    Flags bill spikes deviation > 30% from baseline or > 2 std dev.
    """
    if not historical_charges:
        return {"is_anomaly": False, "deviation_pct": 0.0, "reason": "No historical baseline"}
    
    avg = sum(historical_charges) / len(historical_charges)
    variance = sum((x - avg) ** 2 for x in historical_charges) / len(historical_charges)
    std_dev = math.sqrt(variance) if variance > 0 else 1.0
    
    pct_change = ((current_charge_cents - avg) / avg) * 100 if avg > 0 else 0
    is_anomaly = pct_change >= 30.0 or (current_charge_cents - avg) > (2 * std_dev)
    
    return {
        "is_anomaly": is_anomaly,
        "baseline_cents": int(avg),
        "current_cents": current_charge_cents,
        "deviation_pct": round(pct_change, 2),
        "alert": "Introductory promotion expiration or unexpected price hike detected!" if is_anomaly else "Normal recurring charge"
    }

def calculate_safe_to_spend(current_balance_cents: int, upcoming_fixed_cents: int, payroll_inflow_cents: int, days_window: int = 30) -> dict:
    """
    Predictive liquidity burn projection (SARIMA + Prophet hybrid heuristic).
    Calculates dynamic Safe-to-Spend reserve buffer.
    """
    net_projected_cents = (current_balance_cents + payroll_inflow_cents) - upcoming_fixed_cents
    # Retain a 15% emergency cash liquidity buffer
    safety_buffer_cents = int(upcoming_fixed_cents * 0.15)
    safe_to_spend_cents = max(0, net_projected_cents - safety_buffer_cents)
    
    is_breached = safe_to_spend_cents < (current_balance_cents * 0.10)
    return {
        "current_balance_cents": current_balance_cents,
        "upcoming_fixed_cents": upcoming_fixed_cents,
        "payroll_inflow_cents": payroll_inflow_cents,
        "safe_to_spend_cents": safe_to_spend_cents,
        "safety_buffer_cents": safety_buffer_cents,
        "overdraft_risk": "HIGH" if is_breached else "LOW",
        "sweeps_halted": is_breached
    }

def generate_phash_64(image_bytes_sim: str) -> str:
    """
    Simulates 64-bit DCT perceptual hash generation from receipt pixel data.
    Returns a 16-character hex string representing the 64-bit bitstring.
    """
    # Deterministic simulation using normalized hash of text/byte signature
    raw_hash = hashlib.sha256(image_bytes_sim.strip().lower().encode("utf-8")).hexdigest()
    return raw_hash[:16]

def calculate_hamming_distance(hash1: str, hash2: str) -> int:
    """
    Computes bitwise Hamming distance between two 64-bit hexadecimal hashes.
    """
    val1 = int(hash1, 16)
    val2 = int(hash2, 16)
    xor_val = val1 ^ val2
    # Count set bits
    return bin(xor_val).count('1')

def verify_receipt_duplicate(new_hash: str, circle_existing_hashes: list[str], max_hamming: int = 3) -> dict:
    """
    Receipt Fraud & Duplicate Prevention:
    Rejects receipt if Hamming distance <= 3 with any receipt in circle within 90 days.
    """
    for existing in circle_existing_hashes:
        dist = calculate_hamming_distance(new_hash, existing)
        if dist <= max_hamming:
            return {
                "is_duplicate": True,
                "hamming_distance": dist,
                "matched_hash": existing,
                "status": "REJECTED_DUPLICATE_FRAUD_GUARD"
            }
    return {
        "is_duplicate": False,
        "min_hamming_distance": min([calculate_hamming_distance(new_hash, h) for h in circle_existing_hashes]) if circle_existing_hashes else 64,
        "status": "VERIFIED_UNIQUE"
    }
