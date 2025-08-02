# Crypto Price SMS Notifier

This Python script allows you to **get the current price of any cryptocurrency** in a selected currency and **receive the price as an SMS** using **Twilio**.

---

## Features

- Fetches the latest cryptocurrency price using **CryptoCompare API**.
- Supports both **cryptocurrency symbols** (e.g., `BTC`, `ETH`) and **coin names** (e.g., `Bitcoin`, `Ethereum`).
- Sends an **SMS notification** with the current price using **Twilio**.
- Interactive **command-line interface** for user input.

---

## Requirements

Install the following Python libraries before running the script:

```bash
pip install twilio cryptocompare
```

---

## Setup

1. **Get a Twilio Account**  
   - Sign up at [Twilio](https://www.twilio.com/).  
   - Create a phone number with SMS capabilities.  
   - Obtain your **Account SID** and **Auth Token**.

2. **Update the Script**  
   Replace the placeholders in the script with your credentials:

   ```python
   account_sid = "INSERT_YOUR_ACCOUNT_SID"
   auth_token = "INSERT_YOUR_AUTH_TOKEN"
   ```

3. **Set the Sender and Receiver Numbers**  
   - Update the `from_` and `to` phone numbers in the script:  

     ```python
     from_='+1XXXXXXXXXX',  # Twilio number
     to='+91XXXXXXXXXX'     # Your verified number
     ```

---

## How to Run

1. Run the script:

   ```bash
   python crypto_sms_notifier.py
   ```

2. Choose your input method:
   - **S** → Enter the **crypto symbol** (e.g., `BTC`)  
   - **N** → Enter the **crypto name** (e.g., `Bitcoin`)  

3. Enter the **currency symbol** (e.g., `USD`, `INR`, `EUR`).  

4. You will receive an **SMS with the current price**.

---

## Example Usage

**Input:**
```
Symbol or Names. Respond with the phrase or first letter (S or N): S
enter symbol: BTC
enter currency symbol: USD
```

**SMS Received:**
```
Current price for BTC in USD is 43125.50
```

---

## Notes

- Your Twilio trial account can **only send SMS to verified numbers**.
- CryptoCompare provides free price lookups without an API key.
- Ensure you have a **working internet connection** for API calls.
