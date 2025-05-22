import qrcode

# Business card details
company_name = "Aurra Gold Company"
designation = "Sales Executive"
card_number = "AGC2025X001"
purchaser_name = "Ravi Kumar"

# Format the QR data
qr_data = f"""Company Name: {company_name}
Designation: {designation}
Card Number: {card_number}
Purchaser Name: {purchaser_name}"""

# Generate the QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)
qr.add_data(qr_data)
qr.make(fit=True)

# Create and save the image
img = qr.make_image(fill_color="black", back_color="white")
img.save("aurra_gold_qr.png")

print("QR code saved as 'aurra_gold_qr.png'")
