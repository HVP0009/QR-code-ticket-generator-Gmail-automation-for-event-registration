

This Python utility reads a CSV of registrants, generates QR-code tickets for each registrant, and (optionally) emails the QR image to each participant using Gmail automation (yagmail).

Important security note: do not commit real credentials. Use a Gmail App Password (a 16‑character key from your Google Account) — not your normal Gmail password — for automated sending.

##Quick setup

*Create your Google Form and collect responses:

     In the Form, click Responses → open in Google Sheets.

     In Google Sheets: File → Download → Comma-separated values (.csv) to get a CSV of responses.

     Save that CSV and use its path as registrants_file in the script. The repository contains an example CSV for reference only — replace it with your own.

*Generate a Gmail App Password (recommended)

    Turn on 2‑Step Verification for your Google account (if not already).

    Go to Google Account → Security → App passwords.

    Create an app password for “Mail” on “Windows” (or “Other (custom)”); Google will show a 16‑character key.

    Use that 16‑character key in place of your Gmail password in the script or env variable.

*Replace the sample CSV

    The CSV included in this repo is for reference only (a sample export from a Google Form). Replace registrants_file = "NFF1.csv" with the path to your downloaded responses CSV.
