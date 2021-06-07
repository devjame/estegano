"""
1 - Codificar a mensagem
    + converter a mensagem em binário
    + pegar pixels da imagem
    + modificar cada LSB pixal da imagem com a mensagem

2 - Salvar a imagem codificada

3 - Descodificar

Desenvolvido por: Jackson Sousa, Leonaldo Faleiro e Jodson Rompão
"""

import cv2
import numpy as np


def to_bin(data):
	if isinstance(data, str):
		return ''.join([format(ord(letra), '08b') for letra in data])

	if isinstance(data, bytes) or isinstance(data, np.ndarray):
		return [format(byte, '08b') for byte in data]

	if isinstance(data, int) or isinstance(data, np.uint8):
		return format(data, "08b")
	else:
		raise TypeError("Type not supported.")


def ler_ficheiro(ficheiro):
	"""Ler ficheiro do tipo txt."""

	with open(ficheiro) as texto:
		return texto.read()


def gravar_texto(novo_ficheiro, texto):
	"""Guardar texto num ficheiro do tipo txt.

	:param
		novo_ficheiro: nome do ficheiro a guardar o texto
		texto: o texto a ser guardado no ficheiro
	:return: None
	"""
	with open(novo_ficheiro, 'w') as ficheio:
		ficheio.write(texto)


def encode(nome_imagem, mensagem):
	"""
	Pega numa mensagem e numa imagem e esconde a mensagem dentro dela.

	:param nome_imagem: imagem que é usada para esconder a mensagem
	:param mensagem: mensagem a ser enscondida na imagem
	:return: uma nova imagem com a mensagem escondida
	"""
	imagem = cv2.imread(nome_imagem)
	mensagem += '====='
	msg_bin = to_bin(mensagem)
	data_index = 0
	data_len = len(msg_bin)

	for row in imagem:
		for pixel in row:
			r, g, b = to_bin(pixel)
			# mudar o ultimo bit do vermelho
			if data_index < data_len:
				pixel[0] = int(r[:-1] + msg_bin[data_index], 2)  # [1] somar os bits e converer para inteiro
				data_index += 1

			# mudar o ultimo bit do verde
			if data_index < data_len:
				pixel[1] = int(g[:-1] + msg_bin[data_index], 2)  # [1]
				data_index += 1

			# mudar o ultimo bit do azul
			if data_index < data_len:
				pixel[2] = int(b[:-1] + msg_bin[data_index], 2)  # [1]
				data_index += 1

			# parar loop se i index é maior que o tamnaho da mensagem a guardar
			if data_index >= data_len:
				break
	return imagem


def decode(encode_imagem):
	"""
	Pega num imagem com a mensagem escondida e retira a menasgem escondida.
	:param encode_imagem: imagem com a mensagem escondida
	:return: (string) menagem descodificada
	"""
	image = cv2.imread(encode_imagem)
	mensagem_codificada = ""
	for row in image:
		for pixel in row:
			r, g, b = to_bin(pixel)
			mensagem_codificada += r[-1]
			mensagem_codificada += g[-1]
			mensagem_codificada += b[-1]

	# separar os bits em 1 byte (8 bits)
	all_bytes = [mensagem_codificada[i: i + 8] for i in range(0, len(mensagem_codificada), 8)]

	mensagem = ""

	for byte in all_bytes:
		mensagem += chr(int(byte, 2))

		if mensagem[-5:] == "=====":
			break

	return mensagem[:-5]


def menu():
	print(
		"""
		Escolha, qual operação queres efetuar.

		[1] Codificar mensagem na imagem.

		[2] Descodifcar a mensagem na imagem

		[3] Para terminar a operação. 
		"""
	)

	opcao = int(input("O que queres fazer? "))

	if opcao == 1:
		print("[*] Codificar mensagem...\n")
		imagem = input("Imagem para guardar a mensagem [png/jpg]: ")
		# mensagem = input("Mensagem para enconder na mensagem: ")
		mensagem = ler_ficheiro('data/auto-da-barca-2.txt')
		output_imagem = input("Nome da nova imagem a ser salvo [png/jpg]: ") or 'encoded_imagem.png'
		encoded_imgem = encode(imagem, mensagem)
		cv2.imwrite(output_imagem, encoded_imgem)
		print("\n[*] Mensagem Codificada.")

	elif opcao == 2:
		print("[*] Descodificar mensagem...\n")
		imagem = input("Imagem para retirar a mensagem codificada [png/jpg]: ")
		decoded_mensagem = decode(imagem)
		gravar_texto('data/mensagem-descodificada.txt', decoded_mensagem)
		print("\n[*] Mensagem codificada:", decoded_mensagem)
	else:
		print("Obrigado pela visita. Vejo-te mais logo. ;)")


if __name__ == '__main__':
	menu()
