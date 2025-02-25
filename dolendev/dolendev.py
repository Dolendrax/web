import reflex as rx
from dolendev.components.navbar import navbar
from dolendev.components.infoblock import infoblock
import dolendev.styles.styles as styles

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),

        rx.box(
            rx.center(
                rx.vstack(
                    infoblock(),
                ),
            ),
        ),

    )

app = rx.App()
app.add_page(index)
app._compile()