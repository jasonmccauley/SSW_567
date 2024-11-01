import re
from inline import itest

class Var:
    def __init__(self, name):
        self.name = name

def get_assignment_map_from_checkpoint(tvars, init_c):
    for var in tvars:
        name = var.name
        m = re.match("^(.*):\\d+$", name)
        itest().given(name, "a:0").check_eq(m.group(1), "a")
        if m is not None:
            name = m.group(1)
        return name
    
if __name__ == "__main__":
    tvars = [Var("a:0")]
    init_c = None
    result = get_assignment_map_from_checkpoint(tvars, init_c)
    print(f"The result is: {result}")
    