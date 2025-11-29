import pytest
from ftheory.axioms import AxiomConsistency
class DummyLaw:
    def is_consistent(self):
        return True

def test_axiom_consistency():
    a = AxiomConsistency()
    assert a.check([DummyLaw(), DummyLaw()])
