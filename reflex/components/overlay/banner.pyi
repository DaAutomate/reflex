"""Stub file for banner.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Union, overload, Optional
from reflex.components.component import Component
from reflex.components.overlay.modal import Modal
from reflex.components.layout.cond import Cond
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain

connection_error: Var
has_connection_error: Var
has_connection_error.type_

def default_connection_error() -> list[str | Var]: ...

class ConnectionBanner(Component):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "ConnectionBanner": ...  # type: ignore

class ConnectionModal(Component):
    @overload
    @classmethod
    def create(cls, *children, **props) -> "ConnectionModal": ...  # type: ignore
