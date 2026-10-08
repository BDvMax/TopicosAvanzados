import re
import tkinter as tk


class ValidatedEntry(tk.Entry):
    """``tk.Entry`` que valida su contenido con una regex (``fullmatch``) en vivo.

    Parámetros
    ----------
    master : widget padre.
    pattern : regex en texto. Si es ``None``, cualquier contenido es válido.
    ok_color, bad_color, neutral_color, focus_color : colores del borde.
    ok_bg, bad_bg, neutral_bg : colores de fondo según el estado.
    **kwargs : cualquier opción de ``tk.Entry``. Si se pasa ``textvariable``,
        se respeta y se usa para validar.
    """

    def __init__(self, master=None, pattern=None, *,
                 ok_color="#22c55e", bad_color="#ef4444",
                 neutral_color="#d1d5db", focus_color="#3b82f6",
                 ok_bg="#f0fdf4", bad_bg="#fef2f2", neutral_bg="white",
                 **kwargs):
        self.ok_color, self.bad_color = ok_color, bad_color
        self.neutral_color, self.focus_color = neutral_color, focus_color
        self.ok_bg, self.bad_bg, self.neutral_bg = ok_bg, bad_bg, neutral_bg

        self._var = kwargs.pop("textvariable", None) or tk.StringVar()
        kwargs.setdefault("font", ("Helvetica", 12))
        kwargs.setdefault("relief", "flat")
        kwargs.setdefault("bd", 0)
        kwargs.setdefault("highlightthickness", 2)
        kwargs.setdefault("highlightbackground", neutral_color)
        kwargs.setdefault("highlightcolor", focus_color)
        kwargs.setdefault("insertwidth", 2)
        super().__init__(master, textvariable=self._var, **kwargs)

        self._pattern = re.compile(pattern) if pattern else None
        self._valid = self._pattern is None
        self._trace_id = self._var.trace_add("write", self._on_change)
        self._on_change()  # estado inicial coherente con el contenido

    @property
    def valid(self):
        return self._valid

    def _on_change(self, *args):
        text = self._var.get()
        self._valid = self._pattern is None or bool(self._pattern.fullmatch(text))
        if not text:
            # Vacío: neutro, pero se conserva el azul de foco.
            self.configure(bg=self.neutral_bg,
                           highlightbackground=self.neutral_color,
                           highlightcolor=self.focus_color)
        elif self._valid:
            self.configure(bg=self.ok_bg, highlightbackground=self.ok_color,
                           highlightcolor=self.ok_color)
        else:
            self.configure(bg=self.bad_bg, highlightbackground=self.bad_color,
                           highlightcolor=self.bad_color)

    def destroy(self):
        try:
            self._var.trace_remove("write", self._trace_id)
        except tk.TclError:
            pass
        super().destroy()
