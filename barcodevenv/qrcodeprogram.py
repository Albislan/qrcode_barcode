import qrcode

imagem_qrcode = qrcode.make('https://www.jw.org/pt/Novidades')
imagem_qrcode.save('qrcode_novidades_jw.png')

#como gerar qrcodes