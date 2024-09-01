from refactor.design.structural import Base


class Observer(Base):
  """
  Watch changes of observable objects.
  
  :authors: Hieu Pham.
  :created: 00:13 Sun 1 Sep 2024.
  :updated: 11:40 Sun 1 Sep 2024.
  """

  def __call__(self, *args: any, **kwds: any) -> any:
    event, dispatcher, payload = kwds.get('event'), kwds.get('dispatcher'), kwds.get('payload')
    if isinstance(event, str):
      self.on_event(event, dispatcher, payload)

  def on_event(self, event: str, dispatcher: any, payload: any = None):
    self.logger.debug(f'{str(self)} received event: {event} from: {str(dispatcher)} with payload: {str(payload)}')



class Observable(Base):
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
  
  def emit(self, event: str, payload: any = None):
    if event in self._observers:
      for listener in self._observers[event]:
        listener(event=event, dispatcher=self, payload=payload)
    return self
