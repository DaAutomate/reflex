"""Serializers used to convert Var types to JSON strings."""

from __future__ import annotations

import inspect
from typing import Any, Callable, Type

# Mapping from type to a serializer.
# The serializer should convert the type to a JSON string.
Serializer = Callable[[Type], str]
SERIALIZERS: dict[Type, Serializer] = {}


def serializer(fn: Serializer) -> Serializer:
    """Decorator to add a serializer for a given type.
    
    Args:
        fn: The function to decorate.

    returns:
        The decorated function.
    """
    # Get the global serializers.
    global SERIALIZERS

    # Inspect the function to get the type of the argument.
    argspec = inspect.getfullargspec(fn)
    args = argspec.args

    # Make sure the function takes a single argument.
    if len(args) != 1:
        raise ValueError("Serializer must take a single argument.")

    # Get the type of the argument.
    type_ = argspec.annotations[args[0]]

    # Make sure the type is not already registered.
    registered_fn = SERIALIZERS.get(type_)
    if registered_fn is not None and registered_fn != fn:
        raise ValueError(f"Serializer for type {type_} is already registered as {registered_fn}.")

    # Register the serializer.
    SERIALIZERS[type_] = fn

    # Return the function.
    return fn

def serialize(value: Any) -> str | None:
    """Serialize the value to a JSON string.
    
    Args:
        value: The value to serialize.

    Returns:
        The serialized value, or None if a serializer is not found.
    """
    global SERIALIZERS

    # Get the serializer for the type.
    serializer = SERIALIZERS.get(type(value))

    # If there is no serializer, return None.
    if serializer is None:
        return None
    
    # Serialize the value.
    return serializer(value)


def has_serializer(type_: Type) -> bool:
    """Check if there is a serializer for the type.
    
    Args:
        type_: The type to check.

    Returns:
        Whether there is a serializer for the type.
    """
    global SERIALIZERS

    return type_ in SERIALIZERS