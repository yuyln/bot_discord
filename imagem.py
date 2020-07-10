from simple_image_download import simple_image_download as simp
def link_imagem(input, quantidade):
    response = simp.simple_image_download
    return response().download(input, quantidade)
procurar = ['asuna', 'churrasco', 'giorno giovanna', 'harry styles', 'jonathan joestar', 'joseph joestar', 'josuke', 'jotaro', 'mayumi lol', 'megumin', 'mikasa ackerman', 'sayuri mattar', 'zero two']
for item in procurar:
    link_imagem(item, 100)


"""
lista = list(link_imagem('jonathan joestar', 10))
print(lista)
links = open('links_me.txt', 'w')
links.write(','.join(lista))

links.close()
"""