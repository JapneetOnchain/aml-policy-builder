"""
AML Policy Framework Builder for Indian VDA SPs
Streamlit interface — v0.2
"""

import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from composer import compose_policy


st.set_page_config(
    page_title="AML Policy Framework Builder | Indian VDA SPs",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# Minimal CSS - only widen layout and style the header
st.markdown("""
<style>
.main .block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
.header-bar {
    background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
    padding: 2rem 2.5rem;
    border-radius: 16px;
    margin-bottom: 1.5rem;
    color: white;
    box-shadow: 0 8px 24px rgba(37, 99, 235, 0.15);
}
.header-bar h1 {
    color: white !important;
    font-size: 2.2rem;
    font-weight: 800;
    margin: 0;
    letter-spacing: -0.02em;
}
.header-bar .tagline {
    color: rgba(255,255,255,0.95);
    font-size: 1.05rem;
    margin-top: 0.5rem;
    font-weight: 500;
}
.header-bar .meta {
    color: rgba(255,255,255,0.8);
    font-size: 0.85rem;
    margin-top: 0.75rem;
}
.version-pill {
    display: inline-block;
    background: rgba(255,255,255,0.25);
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    margin-left: 0.5rem;
    vertical-align: middle;
}
</style>
""", unsafe_allow_html=True)


# ============ HEADER ============

st.markdown("""
<div class="header-bar">
    <h1>AML/CFT/CPF Policy Framework Builder <span class="version-pill">v0.2</span></h1>
    <div class="tagline">For Indian Virtual Digital Asset Service Providers (VDA SPs)</div>
    <div class="meta">Anchored to FIU-IND AML & CFT Guidelines (January 8, 2026) · PMLA 2002 · PML Rules 2005</div>
</div>
""", unsafe_allow_html=True)


# ============ INTRO ============

st.info(
    "An open-source structured framework for drafting AML/CFT/CPF policies for Indian VDA SPs. "
    "Answer 19 firm-profile questions to generate a calibrated **starting draft** policy "
    "(approximately 60-80 pages) tailored to your firm. The policy is anchored paragraph-by-paragraph "
    "to the latest FIU-IND Guidelines, PMLA, and PML Rules."
)

with st.expander("⚠️ Important Disclaimers — Please Read Before Using"):
    st.markdown("""
**What this tool is:**
- An open-source structured framework that generates a **starting draft** AML/CFT/CPF policy
- Anchored paragraph-by-paragraph to the January 8, 2026 FIU-IND Guidelines, PMLA, and PML Rules
- Calibrated to your firm profile based on 19 inputs you provide
- Designed for compliance teams and consultants who will customise, validate, and route through legal review

**What this tool is NOT:**
- **Not legal advice.** Use of this tool does not create any attorney-client relationship.
- **Not a finished policy.** The output must be reviewed, customised, and approved by qualified counsel before adoption.
- **Not a substitute for operational implementation.** Having a policy document is necessary but not sufficient for regulatory compliance.

**Before adopting any output:**
1. Customise every section to reflect your firm's specific circumstances
2. Validate every regulatory citation against the current text of applicable statutes and guidelines
3. Obtain qualified Indian legal review
4. Ensure operational implementation of every requirement is in place
5. Have the policy approved by your Board of Directors or Board sub-committee

**About the author:**
Built by Japneet Singh, a financial crime compliance professional with five years of AML experience across EY, KPMG, American Express, and NAB. Currently transitioning into crypto compliance. Open-source and welcoming contributions, corrections, and peer review.
    """)


# ============ FORM ============

st.markdown("## 📋 Firm Profile")
st.markdown(
    "Answer the questions below across 10 sections. The generator calibrates "
    "the policy to your specific firm profile based on your responses."
)

with st.form("firm_profile_form"):

    st.subheader("1. Firm Identity")
    col1, col2 = st.columns(2)
    with col1:
        firm_name = st.text_input("Firm Name (legal entity) *", placeholder="e.g., Acme Crypto Exchange Pvt Ltd")
    with col2:
        registered_state = st.selectbox("Registered State", options=[
            "Maharashtra", "Karnataka", "Delhi", "Tamil Nadu", "Telangana",
            "Gujarat", "Haryana", "Uttar Pradesh", "West Bengal",
            "Andhra Pradesh", "Kerala", "Rajasthan", "Punjab", "Madhya Pradesh", "Other"
        ])
    year_founded = st.number_input("Year Founded", min_value=2000, max_value=2026, value=2021)

    st.subheader("2. Scale of Operations")
    col1, col2 = st.columns(2)
    with col1:
        annual_transaction_volume = st.selectbox(
            "Annual Transaction Volume",
            options=["<₹100 cr", "₹100-500 cr", "₹500-2000 cr", ">₹2000 cr"],
        )
    with col2:
        active_user_count = st.selectbox(
            "Active User Count",
            options=["<1,000", "1,000-10,000", "10,000-50,000", "50,000-200,000", ">200,000"],
        )

    st.subheader("3. Customer Base")
    customer_base = st.radio(
        "Customer Base Composition",
        options=["Retail only", "Institutional only", "Both retail and institutional"],
    )

    st.subheader("4. Geographic Footprint")
    cross_border_element = st.radio(
        "Cross-Border Customer Profile",
        options=["Indian-only customers", "Indian customers + NRI", "Indian customers + foreign customers"],
    )

    st.subheader("5. Services Offered")
    services_offered = st.multiselect(
        "Services Offered",
        options=["Spot trading", "Custody", "OTC desk", "Staking", "Lending", "P2P trading", "Derivatives"],
        default=["Spot trading"],
    )
    business_model_specifics = st.multiselect(
        "Additional Business Model Specifics (optional)",
        options=["Spot trading", "Custody", "OTC desk", "Staking", "Lending", "P2P trading"],
        default=[],
    )

    st.subheader("6. Asset Coverage")
    asset_coverage = st.multiselect(
        "Asset Coverage",
        options=["BTC", "ETH", "major altcoins", "stablecoins", "long-tail tokens", "derivatives"],
        default=["BTC", "ETH", "stablecoins"],
    )

    st.subheader("7. Wallet Custody Model")
    custody_model = st.radio(
        "Primary Wallet Custody Model",
        options=[
            "Hot wallets only (in-house)",
            "Hot + cold wallets (in-house)",
            "Hot + cold wallets (third-party custodian)",
            "Customer self-custody only (non-custodial model)",
        ],
    )

    st.subheader("8. Governance & Compliance Staffing")
    col1, col2 = st.columns(2)
    with col1:
        compliance_staffing = st.radio(
            "Compliance Staffing",
            options=["Solo Principal Officer", "Small team 2-5", "Larger team 6+"],
        )
    with col2:
        board_composition = st.radio(
            "Board Composition",
            options=["Founder-led", "Independent directors", "Listed company governance"],
        )

    st.subheader("9. Regulatory & Compliance Maturity")
    str_history = st.radio(
        "STR Filing History",
        options=[
            "No STRs filed yet (nascent posture)",
            "Occasional STRs (1-10 per year)",
            "Regular STR filing (10+ per year)",
        ],
    )
    regulatory_engagement = st.radio(
        "FIU-IND Engagement History",
        options=[
            "Never engaged with FIU-IND",
            "Initial registration completed only",
            "Active correspondence or inspection in last 24 months",
        ],
    )
    banking_status = st.radio(
        "Banking Relationship Status",
        options=[
            "Fully banked (stable multi-bank relationships)",
            "Partially banked or unstable banking relationships",
            "Unbanked or pre-banking",
        ],
    )

    st.subheader("10. Technology & Group Structure")
    tech_stack = st.multiselect(
        "Compliance Technology Stack",
        options=["Sumsub", "Onfido", "Chainalysis", "TRM Labs", "Elliptic", "in-house", "none"],
        default=["none"],
    )
    col1, col2 = st.columns(2)
    with col1:
        group_structure = st.radio("Group Structure", options=["Standalone", "Part of group"])
    with col2:
        existing_policy_status = st.radio(
            "Existing Policy Status",
            options=[
                "None (initial drafting)",
                "Refresh needed (existing policy pre-2026 Guidelines)",
                "Established (refining existing policy)",
            ],
        )

    st.markdown("")
    submitted = st.form_submit_button("🚀  Generate Calibrated Policy", type="primary", use_container_width=True)


# ============ GENERATION ============

if submitted:
    if not firm_name.strip():
        st.error("⚠️ Please enter the firm name before generating.")
    else:
        policy_status_map = {
            "None (initial drafting)": "None",
            "Refresh needed (existing policy pre-2026 Guidelines)": "Refresh needed",
            "Established (refining existing policy)": "Established",
        }
        str_history_map = {
            "No STRs filed yet (nascent posture)": "Nascent",
            "Occasional STRs (1-10 per year)": "Occasional",
            "Regular STR filing (10+ per year)": "Regular",
        }
        regulatory_engagement_map = {
            "Never engaged with FIU-IND": "Never engaged",
            "Initial registration completed only": "Registration only",
            "Active correspondence or inspection in last 24 months": "Active engagement",
        }
        banking_status_map = {
            "Fully banked (stable multi-bank relationships)": "Fully banked",
            "Partially banked or unstable banking relationships": "Partially banked",
            "Unbanked or pre-banking": "Unbanked",
        }
        custody_model_map = {
            "Hot wallets only (in-house)": "Hot only",
            "Hot + cold wallets (in-house)": "Hot + cold in-house",
            "Hot + cold wallets (third-party custodian)": "Hot + cold third-party",
            "Customer self-custody only (non-custodial model)": "Non-custodial",
        }

        user_answers = {
            "firm_name": firm_name.strip(),
            "registered_state": registered_state,
            "year_founded": year_founded,
            "annual_transaction_volume": annual_transaction_volume,
            "customer_base": customer_base,
            "active_user_count": active_user_count,
            "asset_coverage": asset_coverage,
            "services_offered": services_offered,
            "cross_border_element": cross_border_element,
            "compliance_staffing": compliance_staffing,
            "board_composition": board_composition,
            "tech_stack": tech_stack,
            "group_structure": group_structure,
            "existing_policy_status": policy_status_map[existing_policy_status],
            "business_model_specifics": business_model_specifics,
            "custody_model": custody_model_map[custody_model],
            "str_history": str_history_map[str_history],
            "regulatory_engagement": regulatory_engagement_map[regulatory_engagement],
            "banking_status": banking_status_map[banking_status],
        }

        with st.spinner("⚙️ Generating customised policy across 18 modules..."):
            try:
                modules_dir = Path(__file__).parent.parent / "policy_modules"
                policy = compose_policy(user_answers, modules_dir=str(modules_dir))

                st.markdown("---")
                st.success("✅ Policy generated successfully")

                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Characters", f"{len(policy):,}")
                with col2:
                    st.metric("Words", f"{len(policy.split()):,}")
                with col3:
                    st.metric("Approx. pages", f"~{len(policy.split()) // 350}")

                st.download_button(
                    label="📥  Download Policy (Markdown)",
                    data=policy,
                    file_name=f"AML_Policy_{firm_name.replace(' ', '_')}.md",
                    mime="text/markdown",
                    type="primary",
                    use_container_width=True,
                )

                st.markdown("## 🎯 How This Policy Was Calibrated for Your Firm")
                st.info(
                    "Your 19 inputs drove specific customisations across the policy. "
                    "Click any item below to see what changed."
                )

                calibration_items = []

                if compliance_staffing == "Solo Principal Officer":
                    calibration_items.append(("👤  Compliance Staffing: Solo Principal Officer",
                        "Section 5.3 reflects single-officer structure with external specialist support guidance. Section 9.2 requires PO external training annually."))
                elif compliance_staffing == "Small team 2-5":
                    calibration_items.append(("👥  Compliance Staffing: Small team 2-5",
                        "Section 5.3 reflects team-based compliance structure with functional roles. Section 9.2 includes function-specific training twice annually."))
                elif compliance_staffing == "Larger team 6+":
                    calibration_items.append(("👥  Compliance Staffing: Larger team 6+",
                        "Section 5.3 reflects multi-function compliance organisation with specialised sub-functions. Section 9.2 includes function-specific training."))

                if board_composition == "Listed company governance":
                    calibration_items.append(("📊  Board Composition: Listed company governance",
                        "Section 5 integrates listed-entity governance framework with Audit Committee coordination and SEBI Listing Regulations references."))

                if annual_transaction_volume in ["<₹100 cr", "₹100-500 cr"]:
                    calibration_items.append((f"📈  Transaction Volume: {annual_transaction_volume}",
                        "Risk Assessment and Audit Scope calibrated for current scale with proportionate documentation and 8-dimension audit coverage."))
                elif annual_transaction_volume in ["₹500-2000 cr", ">₹2000 cr"]:
                    calibration_items.append((f"📈  Transaction Volume: {annual_transaction_volume}",
                        "Risk Assessment expanded with quantitative + qualitative analysis. Audit Scope expanded to 12 dimensions including vendor coordination."))

                if customer_base == "Retail only":
                    calibration_items.append(("👤  Customer Base: Retail only",
                        "Section 7.5 emphasises retail onboarding. Section 10 fully expanded. Section 11 (Legal Persons) restricted with Board approval requirement."))
                elif customer_base == "Institutional only":
                    calibration_items.append(("🏢  Customer Base: Institutional only",
                        "Section 7.6 emphasises institutional onboarding. Section 11 fully expanded. Section 10 framed for authorised signatories."))
                else:
                    calibration_items.append(("👥  Customer Base: Both retail and institutional",
                        "Sections 7.5 and 7.6 both included. Sections 10 and 11 both fully expanded. Section 8.2 includes both risk classification frameworks."))

                if cross_border_element == "Indian-only customers":
                    calibration_items.append(("🇮🇳  Cross-Border: Indian-only customers",
                        "Section 7.3 restricts foreign/NRI onboarding. Section 14.6.1 uses domestic-only sanctions framework."))
                elif cross_border_element == "Indian customers + NRI":
                    calibration_items.append(("🌏  Cross-Border: Indian + NRI customers",
                        "Section 11.2.3 includes cross-border EDD. Section 14.6.1 includes OFAC/EU/UK supplementary lists. Section 12.2.7 includes cross-border TM typologies."))
                else:
                    calibration_items.append(("🌍  Cross-Border: Indian + foreign customers",
                        "Full cross-border emphasis: enhanced EDD, international sanctions lists, counterparty DD with jurisdictional risk assessment."))

                if user_answers["custody_model"] == "Non-custodial":
                    calibration_items.append(("🔐  Wallet Custody: Customer self-custody only",
                        "Section 17.2.4 reframes unhosted wallet provisions for non-custodial model. Section 12.2.5 adjusted. Honesty clause preserves regulatory baseline."))
                elif user_answers["custody_model"] in ["Hot + cold in-house", "Hot + cold third-party"]:
                    calibration_items.append((f"🔐  Wallet Custody: {custody_model}",
                        "Section 12.2.5 includes custody-specific reconstruction language. Cold wallet operations addressed: reconciliation, segregation-of-duties, third-party custodian arrangements."))
                else:
                    calibration_items.append(("🔐  Wallet Custody: Hot wallets only",
                        "Section 12.2.5 transaction data storage framed for hot-wallet architecture with wallet-level transaction logs and key custody safeguards."))

                if user_answers["str_history"] == "Nascent":
                    calibration_items.append(("📝  STR History: No STRs filed yet (nascent)",
                        "Section 9.2.1 (NEW) foundational STR capacity-building. Section 15.1.7 (NEW) workflow capacity-building with pre-populated templates, external consultation pathway."))
                elif user_answers["str_history"] == "Regular":
                    calibration_items.append(("📝  STR History: Regular (10+ per year)",
                        "Section 9.2.1 (NEW) advanced STR training. Section 15.1.7 (NEW) workflow at scale: automation, tiered review, quality assurance sampling."))

                if user_answers["regulatory_engagement"] == "Active engagement":
                    calibration_items.append(("📋  FIU-IND Engagement: Active correspondence",
                        "Section 4.5 emphasises heightened inspection-readiness. Section 15.3.4 (NEW) pre-established Section 12A response framework. Section 8.3.5 remediation track-record framing."))
                elif user_answers["regulatory_engagement"] == "Never engaged":
                    calibration_items.append(("📋  FIU-IND Engagement: Never engaged",
                        "Section 15.3.4 (NEW) Section 12A framework establishment with capability assessment and mock response exercises."))

                if user_answers["banking_status"] == "Fully banked":
                    calibration_items.append(("🏦  Banking Status: Fully banked",
                        "Section 14.6.4 (NEW) banking counterparty screening for fiat-leg sanctions risk."))
                elif user_answers["banking_status"] == "Unbanked":
                    calibration_items.append(("🏦  Banking Status: Unbanked / pre-banking",
                        "Section 7.4 (NEW) operational disclosure regarding banking integration. Section 14.6.4 (NEW) sanctions screening for VDA-only flow model."))

                vendor_tools = [t for t in tech_stack if t in ["Sumsub", "Onfido", "Chainalysis", "TRM Labs", "Elliptic"]]
                if vendor_tools:
                    calibration_items.append((f"🛠️  Technology Stack: {', '.join(vendor_tools)}",
                        "Sections 10.3.3, 12.2.1, 14.6.5 include vendor-specific operational language: alert review workflows, configuration management, performance validation."))
                elif "in-house" in tech_stack or "none" in tech_stack:
                    calibration_items.append(("🛠️  Technology Stack: In-house / no vendors",
                        "Sections 10.3.3, 12.2.1, 14.6.5 include manual procedure language and forward-looking guidance on vendor adoption."))

                for label, description in calibration_items:
                    with st.expander(label):
                        st.markdown(description)

                st.markdown("## 📄 Policy Preview")
                st.markdown(
                    "Full policy ready for download above. For actual use, "
                    "download and review in your preferred editor (Word, Notion, VS Code, etc.)."
                )
                with st.expander("📖 View full policy inline (60-80 pages — click to expand)"):
                    st.markdown(policy)

            except Exception as e:
                st.error(f"❌ Error: {e}")


# ============ FOOTER ============

st.markdown("---")
st.markdown(
    "**Built by Japneet Singh** · "
    "[GitHub](https://github.com/JapneetOnchain) · "
    "Open-source · Welcoming contributions, corrections, and peer review<br>"
    "*Anchored to FIU-IND AML & CFT Guidelines (January 8, 2026) · PMLA 2002 · PML Rules 2005*",
    unsafe_allow_html=True
)