import tkinter as tk
from guiutils.validated_entry import ValidatedEntry
from guiutils.slugifier import slug

BG = "#f3f4f6"
CARD = "#ffffff"
TEXT = "#111827"
MUTED = "#6b7280"
OK = "#16a34a"
BAD = "#dc2626"

def main():
    root = tk.Tk()
    root.title("Demo Reusables")
    root.configure(bg=BG)
    root.geometry("460x420")
    root.minsize(420, 400)

    tk.Label(root, text="Demo Reusables", bg=BG, fg=TEXT,
             font=("Helvetica", 18, "bold")).pack(pady=(20, 2))
    tk.Label(root, text="Componentes de Tkinter con validación", bg=BG, fg=MUTED,
             font=("Helvetica", 10)).pack(pady=(0, 14))


    def card(parent, title):
        frame = tk.Frame(parent, bg=CARD, highlightthickness=1,
                         highlightbackground="#e5e7eb")
        frame.pack(fill="x", padx=24, pady=8, ipadx=12, ipady=10)
        tk.Label(frame, text=title, bg=CARD, fg=TEXT,
                 font=("Helvetica", 11, "bold")).pack(anchor="w", padx=12, pady=(6, 4))
        return frame


    # --- Correo ---
    c1 = card(root, "Correo electrónico")
    email = ValidatedEntry(c1, pattern=r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$")
    email.pack(fill="x", padx=12, ipady=6)
    lbl_estado = tk.Label(c1, text="● Inválido", bg=CARD, fg=BAD,
                          font=("Helvetica", 10))
    lbl_estado.pack(anchor="w", padx=12, pady=(6, 0))


    def refresh_estado(*_):
        if email.valid:
            lbl_estado.config(text="● Válido", fg=OK)
        else:
            lbl_estado.config(text="● Inválido", fg=BAD)


    email.bind("<KeyRelease>", refresh_estado)

    # --- Slug ---
    c2 = card(root, "Texto a slug")
    entrada = ValidatedEntry(c2, pattern=r".+")
    entrada.pack(fill="x", padx=12, ipady=6)
    lbl_slug = tk.Label(c2, text="Slug: —", bg=CARD, fg=MUTED,
                        font=("Courier", 11))
    lbl_slug.pack(anchor="w", padx=12, pady=(6, 0))


    def on_change(*_):
        s = slug(entrada.get())
        lbl_slug.config(text=f"Slug: {s}" if s else "Slug: —",
                        fg=TEXT if s else MUTED)


    entrada.bind("<KeyRelease>", on_change)
    root.mainloop()


if __name__ == "__main__":
    main()
