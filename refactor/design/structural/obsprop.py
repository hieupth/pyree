from typing import Any
from refactor.design.behavioral import Observable, Observer


class ObsProp(Observable):
  """
  A property that can notify others about its value changes automatically via on_value_changed event. 
  Also its owner can notify changes via on_property_changed event automatically.
  
  :authors: Hieu Pham.
  :created: 00:28 Sun 1 Sep 2024.
  :updated: 14:19 Sun 1 Sep 2024.
  """

  @property
  def owner(self):
    return self._owner

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if self._value != value:
      payload = {'from': self._value, 'to': value}
      self._value = value
      self.emit(event='on_value_changed', payload=payload)
      if self.owner is not None:
        payload.update({'property': self})
        self.owner.emit(event='on_property_changed', payload=payload)

  def __init__(self, owner: Observable = None, value: Any = None, observers: dict[str, list[Observer]] = None) -> None:
    self._value = value
    self._owner = owner
    super().__init__(observers=observers)
