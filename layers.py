class Layer:
    def __init__(self, name, structure):
        self.name = name
        self.structure = structure

    def is_well_defined(self):
        return hasattr(self.structure, 'validate') or hasattr(self.structure, 'describe')

class LayeredState:
    def __init__(self, layers):
        self.layers = list(layers)

    def project(self, layer_name):
        for l in self.layers:
            if l.name == layer_name:
                return l
        raise KeyError(f"Layer {layer_name} not found")
