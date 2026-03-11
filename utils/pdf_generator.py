from reportlab.pdfgen import canvas

def generate_pdf(user,result,image_path,file_name):

    c = canvas.Canvas(file_name)

    c.drawString(200,800,"Insect Damage Detection Report")

    c.drawString(100,750,f"User: {user}")
    c.drawString(100,720,f"Result: {result}")

    c.drawImage(image_path,100,500,width=300,height=200)

    c.save()