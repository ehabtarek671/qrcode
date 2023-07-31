def make_qrcode(version, box_size,border,data=str,fill_color=str,back_color=str,path=str,image_name=str,image_exetintion=str):
    import qrcode
    qr= qrcode.QRCode(
    version=version,error_correction=qrcode.ERROR_CORRECT_H,box_size=box_size,border=border
)
    qr.add_data(data)
    qr.make()
    img = qr.make_image(fill_color=fill_color,back_color=back_color)
    img.save(path+image_name+'.'+image_exetintion)