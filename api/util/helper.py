def convert_to_mins(time: int):
    hours = time // 60
    mins = time - hours*60
    return f"{hours} h {mins} min"
