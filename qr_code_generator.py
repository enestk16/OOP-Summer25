import qrcode
url = 'https://warsaw-web-wanderer.lovable.app/'
qr = qrcode.make(url)
qr.save('enes_qr.png')
