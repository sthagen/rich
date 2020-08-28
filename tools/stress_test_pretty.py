from rich.console import Console
from rich.panel import Panel
from rich.pretty import Pretty

DATA = {
    "foo": [1, 2, 3, (), {}, (1, 2, 3), {4, 5, 6, (7, 8, 9)}, "Hello, World"],
    "bar": [None, (False, True)] * 2,
}
console = Console()
for w in range(130):
    console.print(Panel(Pretty(DATA), width=w))
