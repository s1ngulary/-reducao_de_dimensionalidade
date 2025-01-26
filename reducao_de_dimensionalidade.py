#Instalar a biblioteca pip install opencv-python matplotlib

import cv2
import numpy as np
import matplotlib.pyplot as plt


# Carregar a imagem colorida
# Substitua 'lena.png' pelo caminho correto para a imagem Lena
imagem_colorida = cv2.imread('lena.png')


# Converter a imagem de BGR (OpenCV padrão) para RGB (para visualização correta)
imagem_rgb = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2RGB)


# Converter para níveis de cinza
imagem_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)


# Aplicar binarização (thresholding)
# Threshold escolhido: 128 (meio termo entre 0 e 255)
thresh = 128
_, imagem_bin = cv2.threshold(imagem_cinza, thresh, 255, cv2.THRESH_BINARY)


# Exibir as imagens lado a lado
plt.figure(figsize=(12, 6))


# Imagem original colorida
plt.subplot(1, 3, 1)
plt.imshow(imagem_rgb)
plt.title("Colorida")
plt.axis('off')


# Imagem em níveis de cinza
plt.subplot(1, 3, 2)
plt.imshow(imagem_cinza, cmap='gray')
plt.title("Níveis de Cinza")
plt.axis('off')


# Imagem binarizada (preto e branco)
plt.subplot(1, 3, 3)
plt.imshow(imagem_bin, cmap='gray')
plt.title("Preto e Branco")
plt.axis('off')


plt.tight_layout()
plt.show()
