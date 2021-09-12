from barcode import EAN13
from barcode.writer import ImageWriter

codigo_barra = EAN13('789134036549', writer=ImageWriter())
codigo_barra.save('codigo_barra')

codigo_produtos = {
    'Biscoito Recheado Itamaraty Cookie': '789134036954',
    'Biscoito recheado Gufs Morango': '789600503004',
    'Biscoito recheado Gufs Brigadeiro': '789600503005', 
} 

for produto in codigo_produtos:
    codigo_barra = EAN13(codigo_produtos[produto],writer=ImageWriter())
    codigo_barra.save(produto)

#até aqui gera imagem cim código de barras    