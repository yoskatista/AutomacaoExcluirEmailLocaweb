# AUTOMACAO P/ DELETAR EMAILS LOCAWEBMAIL
# (recomendado deixa a janela do código pequena e o locawebmail aberto atrás)

import pyautogui
#importando biblioteca

quantidade = int(input("Quantas vezes quer realizar tal tarefa? \nDica: Dividir quantidade total de emails por 50 que é a quantidade deletavel por pagina."))
#variavel int para puxar quantia necessária para excluir.


while quantidade > 0:
#Organizar a repetição exata de quantia necessária

    pyautogui.click(x=229,y=156)
    #clicar para selecionar
    pyautogui.sleep(0.5)
    #dar uma leve pausa para acompanhar o tempo de resposta
    pyautogui.click(x=496,y=155)
    #clicar para deletar
    pyautogui.sleep(3)
    #pausando 3 segundos para carregar os proximos emails
    quantidade = quantidade - 1
    # Realizado tudo, diminuir quantia necessária. chegando a 0 encerra.
