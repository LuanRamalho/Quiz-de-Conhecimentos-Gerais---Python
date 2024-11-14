import tkinter as tk

# Perguntas e respostas sequenciais
questions = [
    {"question": "Qual é a capital da França?", "options": ["Paris", "Londres", "Roma", "Madri"], "answer": 0},
    {"question": "Qual é a fórmula química da água?", "options": ["H2O", "CO2", "NaCl", "O2"], "answer": 0},
    {"question": "Quem descobriu o Brasil?", "options": ["Pedro Álvares Cabral", "Cristóvão Colombo", "Vasco da Gama", "Ferdinando Magalhães"], "answer": 0},
    {"question": "Qual é a raiz quadrada de 144?", "options": ["10", "11", "12", "13"], "answer": 2},
    {"question": "Quem pintou a Mona Lisa?", "options": ["Leonardo da Vinci", "Michelangelo", "Pablo Picasso", "Vincent van Gogh"], "answer": 0},
    {"question": "Qual é o idioma oficial do Brasil?", "options": ["Espanhol", "Português", "Inglês", "Francês"], "answer": 1},
    {"question": "Qual é o maior planeta do sistema solar?", "options": ["Marte", "Terra", "Júpiter", "Saturno"], "answer": 2},
    {"question": "Qual é o maior país do mundo em extensão territorial?", "options": ["Brasil", "China", "Canadá", "Rússia"], "answer": 3},
    {"question": "Qual é o maior rio do mundo em extensão?", "options": ["Rio Amazonas", "Rio Mississipi", "Rio Nilo", "Rio Tigre"], "answer": 2},
    {"question": "Qual é o maior continente do mundo em extensão territorial?", "options": ["África", "Europa", "América", "Ásia"], "answer": 3},
    {"question": "Qual é a capital do Brasil?", "options": ["Rio de Janeiro", "Brasília", "Salvador", "Curitiba"], "answer": 1},
    {"question": "Quem descobriu a América?", "options": ["Américo Vespúcio", "Cristóvão Colombo", "Dom Pedro I", "Dom João VI"], "answer": 1},
    {"question": "Quanto é 3 elevado a 3?", "options": ["2", "9", "27", "81"], "answer": 2},
    {"question": "Quem é o dono da Microsoft?", "options": ["Steve Jobs", "Elon Musk", "Bill Gates", "Mark Zuckerberg"], "answer": 2},
    {"question": "Qual é o componente responsável pelo processamento de dados do computador?", "options": ["HD", "Processador", "Memória RAM", "Placa de Vídeo"], "answer": 1},
    {"question": "Qual é a principal memória do computador?", "options": ["Memória RAM", "HD", "Processador", "Pen Drive"], "answer": 0},
    {"question": "Qual é o símbolo químico do ouro?", "options": ["Au", "Ag", "Fe", "Pb"], "answer": 0},
    {"question": "Quem foi o primeiro presidente dos Estados Unidos?", "options": ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams"], "answer": 1},
    {"question": "Qual é o país mais populoso do mundo?", "options": ["Índia", "Estados Unidos", "China", "Rússia"], "answer": 0},
    {"question": "Qual é o maior oceano do mundo?", "options": ["Atlântico", "Índico", "Pacífico", "Ártico"], "answer": 2},
    {"question": "Quem inventou a lâmpada elétrica?", "options": ["Nikola Tesla", "Thomas Edison", "Albert Einstein", "Alexander Graham Bell"], "answer": 1},
    {"question": "Qual é a principal fonte de energia do Sol?", "options": ["Fissão nuclear", "Fusão nuclear", "Energia elétrica", "Combustão"], "answer": 1},
    {"question": "Qual é o time de futebol com mais títulos da Copa do Mundo?", "options": ["Argentina", "Brasil", "Alemanha", "Itália"], "answer": 1},
    {"question": "Em que continente fica o Egito?", "options": ["África", "Ásia", "Europa", "América"], "answer": 0},
    {"question": "Qual é o nome do maior deserto do mundo?", "options": ["Sahara", "Deserto de Gobi", "Kalahari", "Antártico"], "answer": 3},
    {"question": "Quem escreveu 'Dom Casmurro'?", "options": ["Machado de Assis", "Jorge Amado", "Clarice Lispector", "Carlos Drummond de Andrade"], "answer": 0},
]

# Variáveis globais para pontuação e controle de perguntas
score = 0
current_question_index = 0

# Função para exibir a próxima pergunta
def show_question():
    global current_question_index
    if current_question_index < len(questions):
        question = questions[current_question_index]
        question_label.config(text=question["question"])
        for i, option in enumerate(question["options"]):
            buttons[i].config(text=option, bg="#FFDDC1", state="normal")
    else:
        game_over()

# Função para verificar a resposta do usuário
def check_answer(index):
    global score, current_question_index
    question = questions[current_question_index]
    correct_answer = question["answer"]
    if index == correct_answer:
        buttons[index].config(bg="#4CAF50")  # Destaque verde para correta
        score += 10
        score_label.config(text=f"Pontuação: {score}")
    else:
        buttons[index].config(bg="#F44336")  # Destaque vermelho para incorreta
        buttons[correct_answer].config(bg="#4CAF50")  # Destaque verde para correta
        for button in buttons:
            button.config(state="disabled")
        root.after(1500, game_over)
        return

    current_question_index += 1
    root.after(1000, show_question)  # Avança para a próxima pergunta após 1 segundo

# Função de término do jogo
def game_over():
    question_label.config(text="Fim de Jogo!")
    for button in buttons:
        button.config(state="disabled")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Quiz de Conhecimentos Gerais")
root.geometry("600x500")
root.config(bg="#333333")

# Pontuação e título do quiz
title_label = tk.Label(root, text="Quiz de Conhecimentos Gerais", font=("Arial", 20, "bold"), bg="#333333", fg="#FFFFFF")
title_label.pack(pady=10)
score_label = tk.Label(root, text=f"Pontuação: {score}", font=("Arial", 14), bg="#333333", fg="#FFD700")
score_label.pack(pady=10)

# Pergunta
question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=400, bg="#333333", fg="#FFFFFF")
question_label.pack(pady=20)

# Botões para as alternativas
buttons = []
for i in range(4):
    btn = tk.Button(root, text="", font=("Arial", 14), width=30, height=2, bg="#FFDDC1", fg="#333333", activebackground="#FFD700", command=lambda i=i: check_answer(i))
    btn.pack(pady=5)
    buttons.append(btn)

# Exibe a primeira pergunta
show_question()

# Inicia o loop da interface gráfica
root.mainloop()
