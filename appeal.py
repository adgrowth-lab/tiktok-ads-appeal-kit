#!/usr/bin/env python3
"""
TikTok Ads Suspension Appeal Field Kit & Evidence Generator (2026 Edition) 📨

Automates customized, high-authority appeal packets for suspended TikTok Ad Accounts
and disabled Business Centers. Generates ready-to-paste letters, evidence checklists,
and escalation SOPs across 5 major suspension triggers.

Official Partner Gateway: https://getstartedtiktok.partnerlinks.io/apmgdhnv6eng
Interactive Web Simulator: https://adgrowth-lab.github.io/
"""

import sys
import os
import json
import argparse
import datetime
from typing import Dict, Any, List

OFFICIAL_PORTAL = "https://getstartedtiktok.partnerlinks.io/apmgdhnv6eng"
WEB_CALCULATOR = "https://adgrowth-lab.github.io/"

APPEAL_CATALOG: Dict[str, Dict[str, Any]] = {
    "unusual-activity": {
        "name": "Unusual Account Activity & Security Verification Appeal",
        "description": "For accounts flagged by automated IP geolocation shifts, rapid ad group scaling, or multi-user logins.",
        "subject": "URGENT APPEAL: Account Suspension Due to Unusual Activity - [{{BRAND_NAME}}] (Account ID: {{ACCOUNT_ID}})",
        "documents": [
            "Official Certificate of Incorporation / Business License (Color PDF)",
            "Government-Issued Photo ID of Primary Account Administrator (Passport/Driver's License)",
            "Recent Utility Bill / Corporate Bank Statement displaying registered company address",
            "Documentation proving store ownership (Shopify admin screenshot / domain registration)"
        ],
        "template": """Dear TikTok Advertising Governance & Risk Assessment Team,

We are submitting this formal appeal regarding the suspension of our advertising account for alleged 'Unusual Account Activity':
• Account Legal Entity: {{BRAND_NAME}}
• TikTok Ad Account ID: {{ACCOUNT_ID}}
• Destination Website: {{WEBSITE_URL}}
• Support Case / Ticket ID: {{TICKET_ID}}
• Submission Date: {{DATE}}

1. EXECUTIVE SUMMARY & LEGITIMACY CONFIRMATION
Our advertising account was automatically flagged and suspended due to suspected unusual activity. We confirm that {{BRAND_NAME}} is a verified, legally registered enterprise operating compliant direct-to-consumer commerce. All recent campaign actions—including creative uploads and budget adjustments—were authorized by our internal media buying team.

The automated security flag was triggered by:
- Secure login from our verified media buyer team operating via authorized corporate IP addresses.
- Normal scaling operations preparing for seasonal sales volume.

2. SUBMITTED CORPORATE VERIFICATION EVIDENCE
To verify the authentic ownership of Account {{ACCOUNT_ID}}, we have attached the following official records:
• Attachment 1: Certificate of Good Standing / Corporate Entity Registration (State/Federal Registry)
• Attachment 2: Government-issued Photo Identification of Authorized Corporate Officer
• Attachment 3: Domain Ownership Verification (WHOIS / Registrar invoice for {{WEBSITE_URL}})
• Attachment 4: Bank Statement confirming physical business address

3. COMMITMENT TO POLICY ALIGNMENT
Our media buying team adheres to strict operational standards:
- All campaign creative materials strictly comply with TikTok Advertising Policies (Policies 3.0 through 6.0).
- We maintain direct-to-consumer inventory, provide real-time order tracking, and uphold customer satisfaction rates above 95%.
- We are committed to a sustained monthly advertising budget on TikTok and seek to establish an enduring, cooperative partnership.

4. REQUEST FOR HUMAN RE-EXAMINATION
Given our verified business documentation and the absence of any malicious or fraudulent intent, we respectfully request an expedited manual review by a senior risk specialist to restore our ad account to active standing.

Thank you for your prompt diligence and assistance.

Sincerely,
Media Buying & Compliance Director
{{BRAND_NAME}}
Official Email: contact@{{WEBSITE_URL}}"""
    },
    "payment": {
        "name": "Payment Discrepancy & Card Verification Appeal",
        "description": "For suspensions triggered by VCC binding, 3DS authentication failure, or billing name mismatch.",
        "subject": "PAYMENT VERIFICATION APPEAL: Card Discrepancy Reversal - [{{BRAND_NAME}}] (Account ID: {{ACCOUNT_ID}})",
        "documents": [
            "Official Bank Statement for the card on file (showing recent TikTok charges/holds)",
            "Photo/Screenshot of the card showing Cardholder Name and last 4 digits (middle digits redacted)",
            "Business registration linking Cardholder Name to Company Name",
            "Proof of billing address matching bank record"
        ],
        "template": """Dear TikTok Ads Billing & Anti-Fraud Operations Team,

We are submitting this official verification appeal regarding the payment suspension on our account:
• Account Name: {{BRAND_NAME}}
• Ad Account ID: {{ACCOUNT_ID}}
• Case / Ticket Reference: {{TICKET_ID}}
• Date of Submission: {{DATE}}

1. BACKGROUND & ROOT CAUSE EXPLANATION
Our account was flagged for a payment discrepancy or unverified payment method upon binding our commercial payment card. We understand TikTok's strict security protocols against automated payment fraud. 

This verification flag occurred due to:
- Using our corporate commercial debit card issued by our business banking partner.
- An initial AVS (Address Verification Service) formatting discrepancy between our bank statement address and the Ads Manager billing profile.

2. CARD OWNERSHIP & FINANCIAL PROOF
We confirm that the card added to Ads Account {{ACCOUNT_ID}} is 100% legally owned and authorized by {{BRAND_NAME}}. To substantiate this, we have provided comprehensive evidence:
[Attachment 1] Official Corporate Bank Statement (last 30 days) displaying:
  • Company Legal Name and Registered Address
  • Bank Name & Institution Header
  • Exact matching ending digits of the payment method
  • Recent test authorization / pending charges from TikTok Ads
[Attachment 2] Card Authorization Document confirming our authorized director is the legal holder.
[Attachment 3] Certificate of Good Standing / Corporate Entity Documentation.

3. RECTIFICATION ACTIONS TAKEN
We have verified that:
• The billing address in TikTok Ads Manager now perfectly mirrors the exact format on our bank statement.
• Sufficient liquid capital ($5,000+ USD equivalent) is maintained to cover all billing thresholds seamlessly.
• 3D-Secure mobile authentication is enabled and will be immediately approved for all transactions.

4. CONCLUSION & RESTORATION REQUEST
All financial documentation demonstrates legitimate corporate ownership with zero fraud risk. We kindly request that you verify the attached records, lift the payment hold, and reactivate Account {{ACCOUNT_ID}}.

Respectfully submitted,
Head of Finance & Operations
{{BRAND_NAME}}"""
    },
    "creative": {
        "name": "Creative Policy & Misleading Claims Rectification Appeal",
        "description": "For account suspensions resulting from ad rejections (Policies 5.1, 5.2, or 5.4).",
        "subject": "POLICY COMPLIANCE APPEAL: Creative Review & Account Reinstatement - [{{BRAND_NAME}}] (Account ID: {{ACCOUNT_ID}})",
        "documents": [
            "Full copy transcript of the flagged ad with line-by-line remediation",
            "Third-party laboratory testing / certifications / ingredients documentation",
            "Revised compliant video creative ready for replacement",
            "Store Terms of Service, Refund Policy, and Shipping Policy URLs"
        ],
        "template": """Dear TikTok Advertising Policy & Content Integrity Team,

We respectfully appeal the recent ad creative disapproval and resultant account suspension on:
• Business / Brand Name: {{BRAND_NAME}}
• Ad Account ID: {{ACCOUNT_ID}}
• Store URL: {{WEBSITE_URL}}
• Ticket ID: {{TICKET_ID}}
• Date: {{DATE}}

1. ACKNOWLEDGEMENT OF FLAGGED CONTENT
We have reviewed the notice citing Policy 5.1 (Misleading Claims / Exaggerations) regarding our recent ad group. We recognize that certain colloquial phrasing in our video hook could be interpreted by automated systems as an over-promissory or absolute claim.

We take TikTok's Community Guidelines and Ad Policies with utmost seriousness and acknowledge that our previous phrasing did not meet your high standards of creative transparency.

2. IMMEDIATE REMEDIATION & CORRECTIVE ACTIONS
We have taken immediate, comprehensive corrective measures:
• Completely deleted the flagged creative assets from all campaigns in Account {{ACCOUNT_ID}}.
• Conducted an exhaustive audit of our entire creative catalog using a strict compliance linter.
• Re-edited the creative assets to focus strictly on real customer experience and objective product utility without superlatives, before/after claims, or medical promises.
• Updated our destination landing page ({{WEBSITE_URL}}) to feature clear disclaimers, transparent refund policies (30-day money-back guarantee), and verified customer testimonials.

3. SUPPORTING PRODUCT CREDENTIALS
To verify our product claims are truthful and non-deceptive, we have attached:
[Attachment 1] Independent Quality Certifications / Lab Test Reports
[Attachment 2] Comprehensive Ingredient / Material Safety Data Sheet
[Attachment 3] Customer Support & Return Metrics proving >96% positive delivery rate

4. REQUEST FOR ACCOUNT REINSTATEMENT
As an established e-commerce brand investing significant resources into the TikTok ecosystem, our objective is to run compliant, high-converting campaigns that delight TikTok users. We respectfully request that you restore Account {{ACCOUNT_ID}} to active status so we may submit our fully compliant creative assets for review.

Sincerely,
Creative Operations & Legal Compliance Lead
{{BRAND_NAME}}"""
    },
    "business-center": {
        "name": "TikTok Business Center (BC) & Agency Account Ban Appeal",
        "description": "For suspensions impacting the entire Business Center or agency advertiser portfolio.",
        "subject": "EXECUTIVE APPEAL: Business Center Account Suspension Review - [{{BRAND_NAME}}] (BC ID: {{ACCOUNT_ID}})",
        "documents": [
            "Corporate agency contract / client authorization forms",
            "Master Business Center Admin ID verification",
            "Audited list of all linked Ad Accounts with risk status",
            "Corporate bank documentation and enterprise entity proof"
        ],
        "template": """Dear TikTok Global Agency & Enterprise Risk Management,

We are submitting an executive appeal regarding the suspension of our TikTok Business Center:
• Organization / Agency Name: {{BRAND_NAME}}
• Business Center ID: {{ACCOUNT_ID}}
• Registered Website: {{WEBSITE_URL}}
• Reference Case: {{TICKET_ID}}
• Date: {{DATE}}

1. EXECUTIVE SUMMARY & IMPACT
Our Business Center (BC ID: {{ACCOUNT_ID}}) was recently disabled. This action has halted legitimate commercial advertising across our client accounts and DTC brands, resulting in substantial financial disruption. 

Our compliance team has conducted an exhaustive portfolio review across all linked sub-accounts to isolate the root cause.

2. PORTFOLIO AUDIT FINDINGS
The automated flag appears to have originated from:
- A legacy sandbox test account that experienced an automated billing decline.
- Rapid client onboarding resulting in multiple sub-account activations over a compressed timeframe.

We confirm that all active brands operating under this Business Center are verified commercial entities with legitimate supply chains and valid payment instruments.

3. ENTERPRISE COMPLIANCE MEASURES
To ensure absolute platform harmony, we have implemented the following governance protocols:
• Unlinked and archived all inactive or test ad accounts.
• Implemented a strict pre-flight compliance checklist (zero tolerance for misleading claims or unauthorized placements).
• Consolidated billing exclusively to tier-1 commercial banking partners with pre-funded reserves.

[Attached Documentation]
- Official Enterprise Incorporation Documents
- Identification Records of Primary BC Administrators
- Client Representation Authorizations
- Financial Solvency & Good Standing Certification

4. RESOLUTION REQUEST
We value our commercial partnership with TikTok and request an expedited executive re-examination to reactivate Business Center {{ACCOUNT_ID}} and its constituent compliant ad accounts.

Sincerely,
Managing Partner & Head of Ad Operations
{{BRAND_NAME}}"""
    },
    "identity": {
        "name": "Advertiser Identity Verification (KYB/KYC) Appeal",
        "description": "For accounts failing business verification due to legal name, address, or tax doc discrepancies.",
        "subject": "KYB RE-VERIFICATION APPEAL: Business Entity Documentation - [{{BRAND_NAME}}] (Account ID: {{ACCOUNT_ID}})",
        "documents": [
            "Official Government Business Registration / Certificate of Incorporation",
            "IRS EIN Confirmation Letter (CP 575) or official Tax ID certificate",
            "Government Photo ID of Company Director (Passport or National ID)",
            "Utility bill / Bank statement confirming registered corporate address"
        ],
        "template": """Dear TikTok Advertiser Verification & Identity Compliance Team,

We are writing to appeal the rejection of our Advertiser Identity Verification (KYB) for:
• Legal Business Name: {{BRAND_NAME}}
• TikTok Ad Account ID: {{ACCOUNT_ID}}
• Official Domain: {{WEBSITE_URL}}
• Reference Ticket: {{TICKET_ID}}
• Date: {{DATE}}

1. DISCREPANCY RECONCILIATION
Our initial verification submission was declined, likely due to a minor character or abbreviation variance between our Doing-Business-As (DBA) brand name and our legal parent corporation name on government tax records.

We have aligned all account naming conventions in Ads Manager to match our government filing with 100% precision.

2. SUBMITTED GOVERNMENT EVIDENCE
We have enclosed official, unedited color scans of all required identity documentation:
[Document 1] Official Certificate of Incorporation / Government Business Registry Extract
[Document 2] Official Tax Authority Registration (EIN Confirmation Letter / VAT Certificate)
[Document 3] High-Resolution Color Passport / Driver's License of Company Director
[Document 4] Corporate Bank Statement showing current address within the last 60 days

3. DIRECT CONFIRMATION
• Legal Entity: {{BRAND_NAME}}
• Registered Address: As stated on Document 1 & Document 4
• Beneficial Ownership: Confirmed per Director ID on Document 3

We respectfully request that you review the attached primary government documents and approve our Advertiser Identity status.

Sincerely,
Authorized Corporate Officer
{{BRAND_NAME}}"""
    }
}


def generate_appeal(
    appeal_type: str,
    brand: str = "My Brand",
    account_id: str = "ADV-XXXXXX",
    website: str = "example.com",
    ticket_id: str = "TT-CASE-XXXXXX",
    output_path: str = ""
) -> Dict[str, Any]:
    """Generate customized appeal letter and evidence checklist."""
    norm_type = appeal_type.lower().strip()
    if norm_type not in APPEAL_CATALOG:
        norm_type = "unusual-activity"

    item = APPEAL_CATALOG[norm_type]
    today_str = datetime.date.today().strftime("%B %d, %Y")

    subject = (
        item["subject"]
        .replace("{{BRAND_NAME}}", brand)
        .replace("{{ACCOUNT_ID}}", account_id)
    )

    body = (
        item["template"]
        .replace("{{BRAND_NAME}}", brand)
        .replace("{{ACCOUNT_ID}}", account_id)
        .replace("{{WEBSITE_URL}}", website)
        .replace("{{TICKET_ID}}", ticket_id)
        .replace("{{DATE}}", today_str)
    )

    saved_file = None
    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(f"SUBJECT: {subject}\n\n")
            f.write(body)
        saved_file = output_path

    return {
        "appeal_type": norm_type,
        "name": item["name"],
        "description": item["description"],
        "subject": subject,
        "body": body,
        "required_documents": item["documents"],
        "saved_file": saved_file,
        "escalation_strategy": [
            "1. Submit ticket via TikTok Business Help Center -> Account Suspension / Appeals.",
            "2. Attach all listed required documents as high-resolution PDFs (redacting middle 8 card digits).",
            "3. If unresolved within 24 hours, open a live chat via Business Center and reference your Ticket ID.",
            "4. Never create a new ad account with the same domain or payment card while an appeal is active."
        ],
        "official_portal": OFFICIAL_PORTAL,
        "web_calculator": WEB_CALCULATOR
    }


def print_appeal_report(res: Dict[str, Any]) -> None:
    """Print terminal appeal packet."""
    print("=" * 72)
    print(f"📨 TIKTOK ADS ACCOUNT SUSPENSION APPEAL PACKET: {res['name']}")
    print("=" * 72)
    print(f"Appeal Target:       {res['description']}")
    print(f"Recommended Subject: {res['subject']}")
    print("-" * 72)
    print("MANDATORY EVIDENCE ATTACHMENT CHECKLIST:")
    for doc in res["required_documents"]:
        print(f"  [📎] {doc}")
    print("-" * 72)
    print("FULL APPEAL LETTER (READY TO COPY / PASTE):")
    print()
    print(res["body"])
    print()
    print("-" * 72)
    if res.get("saved_file"):
        print(f"💾 File Saved Successfully to: {res['saved_file']}")
        print("-" * 72)
    print("ESCALATION STRATEGY:")
    for step in res["escalation_strategy"]:
        print(f"  {step}")
    print("-" * 72)
    print(f"CLEAN SLATE RELAUNCH GATEWAY (IF APPEAL FAILS): {OFFICIAL_PORTAL}")
    print(f"INTERACTIVE CALCULATOR:    {WEB_CALCULATOR}")
    print("=" * 72)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="TikTok Ads Suspension Appeal Field Kit & Evidence Generator (2026 Edition)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Available Appeal Types:
  unusual-activity  Suspension due to automated IP/location alerts or velocity
  payment           Card discrepancy, 3DS authentication fail, or VCC hold
  creative          Misleading claims, absolute superlatives, or policy flags
  business-center   Business Center (BC) or agency portfolio disablement
  identity          Advertiser identity verification (KYB/KYC) document rejection

Official Partner Portal: https://getstartedtiktok.partnerlinks.io/apmgdhnv6eng
Interactive Web Hub:     https://adgrowth-lab.github.io/

Examples:
  # 1. Generate Payment Verification Appeal and save to file
  python3 appeal.py --type payment --brand "EcoNest Goods" --account-id "ADV-883921" --output appeal.txt

  # 2. Generate Creative Policy Appeal
  python3 appeal.py --type creative --brand "Aura Skincare" --account-id "ADV-124992" --website "auraskin.com"

  # 3. Output machine-readable JSON for automated ticketing
  python3 appeal.py --type unusual-activity --brand "Pulse Footwear" --account-id "ADV-554102" --json

  # 4. List all available templates
  python3 appeal.py --list
        """
    )
    parser.add_argument("--type", "-t", choices=list(APPEAL_CATALOG.keys()), default="unusual-activity", help="Select suspension trigger type")
    parser.add_argument("--brand", "-b", default="My Brand LLC", help="Your Legal Business or Brand Name")
    parser.add_argument("--account-id", "-a", default="ADV-XXXXXX", help="TikTok Ads Account ID or Business Center ID")
    parser.add_argument("--website", "-w", default="example.com", help="Official store domain URL")
    parser.add_argument("--ticket-id", default="TT-CASE-XXXXXX", help="Existing support ticket reference ID")
    parser.add_argument("--output", "-o", default="", help="Optional file path to save formatted appeal letter")
    parser.add_argument("--list", "-l", action="store_true", help="List all available appeal template descriptions")
    parser.add_argument("--json", action="store_true", help="Output machine-readable JSON")

    args = parser.parse_args()

    if args.list:
        print("=" * 72)
        print("📨 TIKTOK ADS SUSPENSION APPEAL CATALOG (2026)")
        print("=" * 72)
        for k, v in APPEAL_CATALOG.items():
            print(f"• {k:<18} : {v['name']}")
            print(f"  Target: {v['description']}")
            print()
        print(f"Clean-slate partner registration: {OFFICIAL_PORTAL}")
        print("=" * 72)
        return

    res = generate_appeal(
        appeal_type=args.type,
        brand=args.brand,
        account_id=args.account_id,
        website=args.website,
        ticket_id=args.ticket_id,
        output_path=args.output
    )

    if args.json:
        print(json.dumps(res, indent=2))
    else:
        print_appeal_report(res)


if __name__ == "__main__":
    main()
