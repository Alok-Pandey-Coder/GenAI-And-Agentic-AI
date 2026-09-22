def brew_chai(flavor):
  if flavor not in ["masala", "Oolong", "ginger"]:
    raise ValueError("Unsupported flavor...")

brew_chai("mint")