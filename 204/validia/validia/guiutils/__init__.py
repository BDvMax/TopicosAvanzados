"""guiutils: componentes reutilizables de Tkinter (widget validado y slugifier)."""

from .slugifier import slug

__all__ = ["ValidatedEntry", "slug"]
__version__ = "0.1.0"


def __getattr__(name):
    # Importación diferida: slug() no depende de tkinter y debe poder
    # usarse (y probarse) en equipos sin Tk.
    if name == "ValidatedEntry":
        from .validated_entry import ValidatedEntry
        return ValidatedEntry
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
