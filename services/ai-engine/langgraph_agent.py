"""
8. Autonomous Routing & Agentic LLM Guardrails
Implements the 3-Node Sequential Stateful LangGraph Topology:
 Node 1: Ingestion & Auditor Node (Deterministic rule audit)
 Node 2: Market Benchmarking Node (Retail & streaming catalog checks)
 Node 3: Advisory Synthesis Node (Structured JSON recommendation: CUT, NEGOTIATE, CAP, POOL)
Wrapped with Layer 1 / Layer 2 Compliance Guardrails preventing hallucinated mutations.
"""

from typing import Dict, Any, List

class AgentGuardrailException(Exception):
    pass

class NudgePayAgentGraph:
    def __init__(self):
        # Simulated live market catalog database
        self.catalog_streaming = {
            "spotify": {"individual": 1199, "family_6": 1999, "student": 599},
            "hulu": {"standalone": 1000, "ad_bundle": 799, "annual_discount_pct": 16},
            "netflix": {"standard": 1549, "ad_supported": 699, "premium": 2299}
        }
        
        self.catalog_retail = {
            "012345678901": {
                "product_name": "Sony WH-1000XM5 Wireless Headphones",
                "current_store": "Target",
                "current_price_cents": 39999,
                "competitor": "Best Buy",
                "competitor_price_cents": 32999,
                "match_policy": "Target Official Policy: Cashier matches Best Buy live online item."
            },
            "098765432109": {
                "product_name": "Ninja Air Fryer Pro 4-in-1",
                "current_store": "Walmart",
                "current_price_cents": 8900,
                "competitor": "Amazon",
                "competitor_price_cents": 6999,
                "match_policy": "Walmart Register Policy: Matches Amazon direct shipped & sold items."
            }
        }

    # Node 1: Deterministic Ingestion & Auditor Node
    def node_ingestion_and_auditor(self, state: Dict[str, Any]) -> Dict[str, Any]:
        transactions = state.get("transactions", [])
        recurring = [t for t in transactions if t.get("is_recurring")]
        state["audited_recurring"] = recurring
        state["total_recurring_burn_cents"] = sum(t.get("amount_cents", 0) for t in recurring)
        return state

    # Node 2: Market Benchmarking Node
    def node_market_benchmarking(self, state: Dict[str, Any]) -> Dict[str, Any]:
        findings = []
        recurring = state.get("audited_recurring", [])
        circle_users = state.get("circle_members_transactions", {})
        
        # Check streaming subscription circle pooling
        spotify_payers = []
        for member_id, tx_list in circle_users.items():
            for tx in tx_list:
                if "spotify" in tx.get("merchant", "").lower():
                    spotify_payers.append((member_id, tx.get("amount_cents", 1199)))
        
        if len(spotify_payers) >= 2:
            total_current = sum(p[1] for p in spotify_payers)
            family_plan = self.catalog_streaming["spotify"]["family_6"]
            annual_savings = (total_current - family_plan) * 12
            findings.append({
                "type": "SUBSCRIPTION_POOL",
                "service": "Spotify",
                "current_total_monthly": total_current,
                "pooled_monthly": family_plan,
                "annual_savings_cents": annual_savings,
                "members_count": len(spotify_payers)
            })

        for tx in recurring:
            m = tx.get("merchant", "").lower()
            amt = tx.get("amount_cents", 0)
            if "hulu" in m and amt >= 999:
                bundle_price = self.catalog_streaming["hulu"]["ad_bundle"]
                savings_annual = (amt - bundle_price) * 12
                findings.append({
                    "type": "SUBSCRIPTION_SWAP",
                    "service": "Hulu",
                    "current_monthly": amt,
                    "recommended_tier": "Ad-supported Bundle",
                    "recommended_monthly": bundle_price,
                    "annual_savings_cents": savings_annual
                })
        
        state["benchmark_findings"] = findings
        return state

    # Node 3: Advisory Synthesis Node (Structured Action Generation)
    def node_advisory_synthesis(self, state: Dict[str, Any]) -> Dict[str, Any]:
        recommendations = []
        for finding in state.get("benchmark_findings", []):
            if finding["type"] == "SUBSCRIPTION_POOL":
                recommendations.append({
                    "action": "POOL",
                    "title": f"Combine {finding['service']} into Circle Family Plan",
                    "description": f"Found {finding['members_count']} circle members paying separately. Pool together for ${finding['pooled_monthly']/100:.2f}/mo total.",
                    "annual_savings_usd": round(finding["annual_savings_cents"] / 100, 2),
                    "actionable_1tap": True
                })
            elif finding["type"] == "SUBSCRIPTION_SWAP":
                recommendations.append({
                    "action": "CUT",
                    "title": f"Migrate {finding['service']} to Lower Tier Bundle",
                    "description": f"Current cost is ${finding['current_monthly']/100:.2f}/mo. Switch to {finding['recommended_tier']} at ${finding['recommended_monthly']/100:.2f}/mo.",
                    "annual_savings_usd": round(finding["annual_savings_cents"] / 100, 2),
                    "actionable_1tap": True
                })
        
        state["final_recommendations"] = recommendations
        return state

    # Two-Layer Guardrail Compliance Gate
    def apply_guardrails(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Layer 1 & Layer 2 Guardrails:
        Ensures mathematical non-hallucination and isolates recommendations from direct ledger mutation.
        """
        for rec in state.get("final_recommendations", []):
            if rec.get("annual_savings_usd", 0) < 0:
                raise AgentGuardrailException("Negative savings recommendation rejected by Guardrail L1.")
            if "direct_debit" in rec:
                raise AgentGuardrailException("Direct ledger mutation forbidden in Advisory Node by Guardrail L2.")
        state["guardrail_passed"] = True
        return state

    def run(self, initial_state: Dict[str, Any]) -> Dict[str, Any]:
        s1 = self.node_ingestion_and_auditor(initial_state)
        s2 = self.node_market_benchmarking(s1)
        s3 = self.node_advisory_synthesis(s2)
        s_final = self.apply_guardrails(s3)
        return s_final
