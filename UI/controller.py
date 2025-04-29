import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_crea_grafo(self, e):
        dist = self._view.txt_distanza_minima.value
        if dist is None or dist == "":
            self._view.create_alert("Inserire la distanza")
            return


        lista_archi = []
        self._model.buildGraph(dist)
        lista_archi = self._model._grafo.edges
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato!"))
        self._view.txt_result.controls.append(ft.Text(f"il numero di vertici del grafo : {self._model.getNumNodi}"))
        self._view.txt_result.controls.append(ft.Text(f"il numero di archi del grafo : {self._model.getNumArchi}"))
        for arco in lista_archi:
            self._view.txt_result.controls.append(ft.Text(str(lista_archi)))
        self._view.update_page()

