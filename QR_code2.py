import qrcode  
# creating a QRCode object  
obj_qr = qrcode.QRCode(  
    version = 1,  #This parameter is an integer from 1 to 40 that controls the size of the QR Code (the smallest, version 1, is a 21×21 matrix).
    error_correction = qrcode.constants.ERROR_CORRECT_H,  
    box_size = 10,  
    border = 4,  
)  
# using the add_data() function  
obj_qr.add_data("https://learn.skillnation.in/lessons/day-4-modules-7/")  
# using the make() function  
obj_qr.make(fit = True)  
# using the make_image() function  
qr_img = obj_qr.make_image(fill_color = "orange",
                           back_color = "black")  
# saving the QR code image  
qr_img.save("qr-img1.png")  


