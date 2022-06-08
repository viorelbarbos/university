matrix = [
    ['A', 'B', 'C', 'D', 'E'],
    ['K', 'L', 'M', 'N', 'O'],
    ['F', 'G', 'H', 'I', 'J'],
    ['P', 'Q', 'R', 'S', 'T'],
    ['U', 'V', 'X', 'Y', 'Z']]
indici = ['A', 'B', 'C', 'D', 'E']
text_criptat = "ACEADCDDACDCCDDADEBECBDCAACACDAE"
text_decriptat = ""
i = 0
while i < len(text_criptat) - 1:
    a = indici.index(text_criptat[i])
    b = indici.index(text_criptat[i+1])
    text_decriptat += matrix[a][b]
    i += 2
print(text_decriptat)