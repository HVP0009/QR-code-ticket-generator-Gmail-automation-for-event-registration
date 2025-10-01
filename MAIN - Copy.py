import pandas as pd
import yagmail
import re
import qrcode
import os

# --- Step 1: Generate QR Codes ---
def generate_qr_codes(registrants_file, output_folder):
    """Generate QR codes for registrants."""
    data = pd.read_csv(registrants_file)  # Read registrant details from a CSV file
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for index, row in data.iterrows():
        qr_data = f"Name: {row['NAME']}, Email: {row['EMAIL ID']}"
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")
        img.save(f"{output_folder}/{row['NAME']}.png")
    
    print(f"QR Codes generated and saved in '{output_folder}'.")
 # --- Step 2: Email QR Codes ---
def send_emails_with_qr(registrants_file, output_folder, sender_email, sender_password):
    """Email QR codes with an automated message to registrants."""
    yag = yagmail.SMTP(sender_email, sender_password)
    data = pd.read_csv(registrants_file)  # Load registrant details from the CSV
    print(data.head())
    
    for index, row in data.iterrows():
        email = row['EMAIL ID']
        name = row['NAME']
        qr_code_path = f"{output_folder}/{row['NAME']}.png"  # Path to the QR code file
        
       

  

    # Initialize email client
    yag = yagmail.SMTP(sender_email, sender_password)

    try:
        data = pd.read_csv(registrants_file)
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        for index, row in data.iterrows():
            email = row['EMAIL ID']
            name = row['NAME']
            qr_code_path = f"{output_folder}/{row['NAME']}.png"

            # Validate email
            if not pd.notnull(email) or not re.match(email_pattern, email):
                print(f"Invalid email for {name}: {email}. Skipping...")
                continue

            # Send email
            subject = "Registration Confirmation-- Nagpur Film Festival"
            body = f""" Hello {name},\n\nThank you for registering for the Nagpur Film Festival! We are excited to have you join us for this incredible event showcasing a variety of captivating films.
                     Event Details:
                    - Date: [Event Date]
                    - Time: [Start Time]
                    - Venue: [Venue Name/Location]
                    - Digital Pass: Attached below is your unique digital pass (QR code). Please present this pass at the entrance for seamless entry.
                    
                    Stay tuned for updates and event highlights. If you have any questions, feel free to reach out to us at [Support Email/Contact Number].
                    We look forward to seeing you at the festival!
                    Best regards,  
                    [Your Name/Team Name]  
                    [Film Festival Name]  
                    [Contact Details]"""
            try:
                yag.send(to=email, subject=subject, contents=body, attachments=qr_code_path)
                print(f"Email sent to {email}.")
            except Exception as e:
                print(f"Error sending email to {email}: {e}")
    finally:
        # Close the SMTP connection
        yag.close()
        print("SMTP connection closed.")




# --- Main Function ---
if __name__ == "__main__":
    registrants_file = "NFF1.csv"  # Path to the CSV file with registrant details
    qr_output_folder = "qr_codes"        # Folder to save QR codes
    attendance_file = "attendance.csv"  # CSV file to store attendance logs
    sender_email = "pushadapuharshitha@gmail.com"  # Your email
    sender_password = "jaxr ekte brbm cfly"       # Your email password

    # Step 1: Generate QR Codes
    generate_qr_codes(registrants_file, qr_output_folder)

     # Step 2: Email QR Codes (uncomment to enable)
    send_emails_with_qr(registrants_file, qr_output_folder, sender_email, sender_password)
