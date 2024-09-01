from typing import Any
from refactor.design import Object


class Observer(Object):
  """
  Watch changes of observable objects.
  
  :authors: Hieu Pham.
  :created: 00:13 Sun 1 Sep 2024.
  :updated: 11:40 Sun 1 Sep 2024.
  """

  def on_event_dispatched(self, event: str, dispatcher: Any, payload: Any = None) -> Any:
    self.logger.debug(f'{str(self)} received event: {event} from: {str(dispatcher)} with payload: {str(payload)}')



class Observable(Object):
  """
  Allows some objects to notify other objects about changes in their state.
  
  :authors: Hieu Pham.
  :created: 00:13 Sun 1 Sep 2024.
  :updated: 11:40 Sun 1 Sep 2024.
  """

  @property
  def events(self):
    return self._observers.keys()

  def __init__(self, observers: dict[str, list[Observer]] = None) -> None:
    super().__init__()
    self._observers = dict[str, list[Observer]]() if observers is None else observers

  def observe(self, events: str | list[str], observer: Observer):
    if isinstance(events, str):
      if events not in self._observers:
        self._observers[events] = list()
      if observer not in self._observers[events]:
        self._observers[events].append(observer)
      return self
    elif isinstance(events, list):
      for event in events:
        self.observe(event, observer)
      return self
    raise TypeError()
  
  def unobserve(self, events: str | list[str] | None, observer: Observer):
    if isinstance(events, str):
      if events in self._observers:
        self._observers[events].remove(observer)
      return self
    elif isinstance(events, list):
      for event in events:
        self.unobserve(event, observer)
      return self
    raise TypeError()
  
  def emit(self, event: str, payload: Any = None):
    if event in self._observers:
      for listener in self._observers[event]:
        listener.on_event_dispatched(event=event, dispatcher=self, payload=payload)
    return self
