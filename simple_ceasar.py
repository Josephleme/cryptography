'''A simple program for encrypting and decrypting uppercase, lowercase English alphabets and numbers
	but not changing any other character within a message or a secret
	'''

from datetime import datetime as dm

class CryptographySimple:

	SHIFT = int(dm.now().strftime('%I'))#gen a number(based on the the hour of the day in 12 hour clock system)
										 # to shift alphabets and numbers

	def __init__(self):
		self.upper_decoder = ''.join([chr(((k-self.SHIFT)+2)%26 + ord('A')) for k in range(26)])
		self.upper_encoder = ''.join([chr(((k+self.SHIFT)-2)%26 + ord('A')) for k in range(26)])
		self.lower_decoder = ''.join([chr((k-self.SHIFT)%26 + ord('a')) for k in range(26)])
		self.lower_encoder = ''.join([chr((k+self.SHIFT)%26 + ord('a'))for k in range(26)])
		self.num_decoder = {0:'6',1:'7',2:'8',3:'9',4:'0',5:'1',6:'2',7:'3',8:'4',9:'5'}
		self.num_encoder = {6:'0',7:'1',8:'2',9:'3',0:'4',1:'5',2:'6',3:'7',4:'8',5:'9'}


	def decrypt(self,secret):
		'''Returns a decrypted message'''
		text = list(secret)
		for k in range(len(text)):
			if text[k].isupper():
				i = ord(text[k]) - ord('A')
				text[k] = self.upper_decoder[i]
			elif text[k].islower():
				i = ord(text[k]) - ord('a')
				text[k] = self.lower_decoder[i]
			elif text[k].isnumeric():
				text[k] = self.num_decoder[int(text[k])]
		text.reverse()
		return ''.join(text)


	def encrypt(self,msg):
		'''Returns an encrypted message'''
		text = list(msg)
		for k in range(len(text)):
			if text[k].isupper():
				# use upper_message to decrypt
				i = ord(text[k]) - ord('A')
				text[k] = self.upper_encoder[i]
			elif text[k].islower():
				i = ord(text[k]) - ord('a')
				text[k] = self.lower_encoder[i]
			elif text[k].isnumeric():
				text[k] = self.num_encoder[int(text[k])]
		text.reverse()
		return ''.join(text)


if __name__ == '__main__':
	a_message = '''wow!. Kate and John just discovered a potential oil field some place in sahara. 
				Its estimated size is 65km by 40km.
				With proper arrangements and agreements, this could be of great help to neighboring countries
				and Africa at large.
	'''
	cipher = CryptographySimple()
	secret = cipher.encrypt(a_message)
	reply = '''we should conduct the local authorities and the neighboring countries' leaders and start extraction and
	refinement as soon as possible'''
	msg = cipher.encrypt(reply)
	
	print(f'''Johnny the informat sent \n\n{cipher.decrypt(secret)}\n
to his business partner Jamey, then Jamey replied \n\n{cipher.decrypt(msg)}\n''')


	

		
