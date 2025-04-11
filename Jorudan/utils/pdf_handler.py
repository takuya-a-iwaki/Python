from reportlab.pdfgen import canvas

def convert_image_to_pdf(image_path, pdf_path):
    c = canvas.Canvas(pdf_path)
    c.drawImage(image_path, 0, 0, 595, 842)  # A4サイズに合わせる
    c.save()