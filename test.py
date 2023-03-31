import tkinter as tk

class Arbre:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='white')
        self.canvas.pack()
        self.nodes = []
        self.current_node = None
        self.draw_mode = False
        self.link_mode = False
        self.link_button = tk.Button(self.root, text="Lier", command=self.toggle_link_mode)

        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<Button-3>", self.toggle_draw_mode)

        self.root.mainloop()

    def on_click(self, event):
        if not self.link_mode:
            x, y = event.x, event.y
            node = self.canvas.create_oval(x-20, y-20, x+20, y+20, fill='red')
            self.nodes.append(node)
            num = len(self.nodes)
            self.canvas.create_text(x, y, text=str(num))
            self.canvas.tag_bind(node, '<Button-1>', self.select_node)

    def select_node(self, event):
        if self.draw_mode:
            node = event.widget.find_closest(event.x, event.y)[0]
            if self.current_node is None:
                self.current_node = node
            else:
                self.canvas.create_line(*self.canvas.coords(self.current_node), *self.canvas.coords(node))
                self.current_node = None

    def toggle_draw_mode(self, event):
        self.draw_mode = not self.draw_mode
        if self.draw_mode:
            self.canvas.config(cursor='cross')
            self.current_node = None
        else:
            self.canvas.config(cursor='')

    def toggle_link_mode(self):
        self.link_mode = not self.link_mode
        if self.link_mode:
            self.link_button.config(text="Annuler Lier")
            self.draw_mode = False
            self.canvas.config(cursor='')
        else:
            self.link_button.config(text="Lier")
            self.draw_mode = True
            self.canvas.config(cursor='cross')

    def clear_canvas(self):
        self.canvas.delete('all')
        self.nodes = []
        self.current_node = None
        self.draw_mode = False
        self.link_mode = False
        self.link_button.config(text="Lier")
        self.canvas.config(cursor='')
        
    def show_link_button(self):
        self.link_button.pack()

if __name__ == '__main__':
    arbre = Arbre()
    arbre.show_link_button()
