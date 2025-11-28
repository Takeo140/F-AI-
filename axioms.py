from dataclasses import dataclass

@dataclass
class AxiomUniversalityExtremal:
    """Axiom 1: any valid Action should support stationarity (δS = 0)."""
    def holds(self, action) -> bool:
        return hasattr(action, "is_stationary") and action.is_stationary()

@dataclass
class AxiomTopology:
    """Axiom 2: state space must expose topological properties."""
    def holds(self, space) -> bool:
        return hasattr(space, "is_topological") and space.is_topological()

@dataclass
class AxiomConsistency:
    """Axiom 3: collection of laws should be internally consistent."""
    def check(self, laws) -> bool:
        return all(getattr(l, "is_consistent", lambda: False)() for l in laws)

@dataclass
class AxiomLayerStructure:
    """Axiom 4: layered/multi-level structure is well-defined."""
    def validate(self, layers) -> bool:
        return all(getattr(layer, 'is_well_defined', lambda: False)() for layer in layers)
