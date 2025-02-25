import reflex as rx

def infoblock() -> rx.Component:
    return rx.card(
            rx.data_list.root(
                rx.data_list.item(
                    rx.data_list.label("Status"),
                    rx.data_list.value(
                        rx.badge(
                            "Student",
                            variant="soft",
                            radius="full",
                        )
                    ),
                    align="center",
                ),
                rx.data_list.item(
                    rx.data_list.label("Name"),
                    rx.data_list.value("Pedro Alarcón Fuentes"),
                    align="center",
                ),
                rx.data_list.item(
                    rx.data_list.label("Email"),
                    rx.data_list.value(
                        rx.link(
                            "dolendev@fmail.com",
                            href="dolendev@fmail.com",
                        ),
                    ),
                ),
                rx.data_list.item(
                    rx.data_list.label("University"),
                    rx.data_list.value(
                        rx.link(
                            "UPCT",
                            href="https://reflex.dev",
                        ),
                    ),
                ),
            ),
        )