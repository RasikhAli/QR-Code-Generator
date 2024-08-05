from flask import Flask, render_template, request
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def generate_qr_code():
    qr_code = None

    if request.method == "POST":
        data = request.form["data"]

        # Generate QR code with custom colors
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Create the QR code image with custom colors
        qr_img = qr.make_image(fill_color="darkblue", back_color="white")

        # Save the QR code to a BytesIO object
        qr_io = BytesIO()
        qr_img.save(qr_io, format="PNG")
        qr_io.seek(0)

        # Encode the image as a base64 string
        qr_code = base64.b64encode(qr_io.read()).decode()

    return render_template("index.html", qr_code=qr_code)

if __name__ == "__main__":
    app.run(debug=True)
