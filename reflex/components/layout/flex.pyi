"""Stub file for flex.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Union, overload, List, Optional
from reflex.components.libs.chakra import ChakraComponent
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain

class Flex(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, align: Optional[Union[Var[str], str]] = None, basis: Optional[Union[Var[str], str]] = None, direction: Optional[Union[Var[Union[str, List[str]]], Union[str, List[str]]]] = None, grow: Optional[Union[Var[str], str]] = None, justify: Optional[Union[Var[str], str]] = None, wrap: Optional[Union[Var[Union[str, List[str]]], Union[str, List[str]]]] = None, shrink: Optional[Union[Var[str], str]] = None, **props) -> "Flex": ...  # type: ignore
