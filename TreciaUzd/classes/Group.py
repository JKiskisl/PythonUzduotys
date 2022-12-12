class Group:
  def __init__(self, groupname) -> None:
    self.groupname = groupname
    
  def __repr__(self) -> str:
    return f"{self.groupname}"
    