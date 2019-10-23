class Solution:
	def strangeGrid(self, h: int, w: int) -> list:
		lis=[[None]*w for i in range(h)]
		c='A'
		for j in range(w): # reservamos a j para columnas y a i para filas como siempre
			for i in range(h):
				# print(c,end=' ') # saldran en el orden deseado
				if j%2!=0:
					lis[h-i-1][j] = c
					c=chr(ord(c)+1) # ord convierte a c en un integer Unicode code point value 
				else:
					lis[i][j] = c
					c=chr(ord(c)+1) # chr es la inversa lo vuelve a como estaba pero ahora modificado
		return lis


s=Solution()
h = int(input())
w = int(input())
print(s.strangeGrid(h, w))