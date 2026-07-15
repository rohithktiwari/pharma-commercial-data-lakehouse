# Data Dictionary

## Sales

| Column | Description |
|---------|-------------|
| Sale_ID | Unique sales transaction identifier |
| Product_ID | Product identifier |
| HCP_ID | Healthcare professional identifier |
| Territory_ID | Sales territory |
| Hospital_ID | Hospital identifier |
| Sale_Date | Transaction date |
| Sales_Amount | Sales value |

---

## Products

| Column | Description |
|---------|-------------|
| Product_ID | Product identifier |
| Product_Name | Product name |
| Brand | Brand name |
| Category | Product category |

---

## Prescriptions

| Column | Description |
|---------|-------------|
| Prescription_ID | Prescription identifier |
| HCP_ID | Healthcare professional |
| Product_ID | Product prescribed |
| Prescription_Date | Date of prescription |

---

## Claims

| Column | Description |
|---------|-------------|
| Claim_ID | Insurance claim identifier |
| Product_ID | Product identifier |
| Claim_Amount | Claim value |
| Status | Claim status |

---

## HCP

Healthcare professional master data.

---

## Territory

Sales territory master information.

---

## Hospital

Hospital master information.

---

## Sales Representatives

Sales representative information used for territory mapping.
