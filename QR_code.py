import qrcode as qr
#using the make function to make the format
img=qr.make("https://www.javatpoint.com/python-programs")
#using the save function to save the data 
img.save("javatpoint_qr.png")