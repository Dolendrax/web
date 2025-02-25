import reflex as rx
from dolendev.styles.styles import Size
from dolendev.styles.colors import Color


def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Dolendrax",
            heigh="40px",
            background_image="linear-gradient(90deg, #FFA500, #FFD700)",
            background_clip="text",
            font_weight="bold",
            font_size="1.5em",
            font_family="Caveat",
            ),


        bg=Color.CONTENT.value,
        position="sticky",
        padding_y=Size.DEFAULT.value,
        padding_x=Size.BIG.value,
        z_index="999",
        top="0",
        border_color="#FF0000",
    )