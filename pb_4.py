matrix = [
          ['A', 'B', 'C', 'D', 'E'],
          ['K', 'L', 'M', 'N', 'O'],
          ['F', 'G', 'H', 'I', 'J'],
          ['U', 'V', 'X', 'Y', 'Z'],
          ['P', 'Q', 'R', 'S', 'T']]

indici = ['A', 'B', 'C', 'D', 'E']
text_nou = ""
text = "COMPUTER SCIENCE"
print("Textul initial este: ", text)
text = list(text)
for i in range(len(text)):
    if text[i] != ' ':
        for j in range(5):
            for k in range(5):
                if text[i] == matrix[j][k] and text[i] != ' ':
                    text_nou += indici[j]+indici[k]
                    break
    else:
        text_nou += ' '
print("Textul dupa criptare este: ", text_nou)