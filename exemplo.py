import tkinter as tk
from tkinter import ttk

class CronometroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        # Variáveis de tempo
        self.tempo = 0
        self.rodando = False

        # Interface do cronômetro
        self.label_tempo = ttk.Label(root, text="00:00:00", font=("Helvetica", 36))
        self.label_tempo.pack(pady=20)

        # Botões
        self.botao_iniciar = ttk.Button(root, text="Iniciar", command=self.iniciar)
        self.botao_iniciar.pack(side=tk.LEFT, padx=10)

        self.botao_pausar = ttk.Button(root, text="Pausar", command=self.pausar)
        self.botao_pausar.pack(side=tk.LEFT, padx=10)

        self.botao_zerar = ttk.Button(root, text="Zerar", command=self.zerar)
        self.botao_zerar.pack(side=tk.LEFT, padx=10)

    def atualizar_tempo(self):
        if self.rodando:
            self.tempo += 1
            horas = self.tempo // 3600
            minutos = (self.tempo % 3600) // 60
            segundos = self.tempo % 60
            self.label_tempo.config(text=f"{horas:02}:{minutos:02}:{segundos:02}")
            self.root.after(1000, self.atualizar_tempo)

    def iniciar(self):
        if not self.rodando:
            self.rodando = True
            self.atualizar_tempo()

    def pausar(self):
        self.rodando = False

    def zerar(self):
        self.rodando = False
        self.tempo = 0
        self.label_tempo.config(text="00:00:00")

# Configuração principal da janela
if __name__ == "__main__":
    root = tk.Tk()
    app = CronometroApp(root)
    root.mainloop()
