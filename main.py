import flet as ft

def main(page: ft.Page):
    page.title = "S.S. Market VIP"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#0b0f19"  # Premium dark market background
    page.padding = 15

    # App Bar (Pro Header)
    page.appbar = ft.AppBar(
        title=ft.Text("S.S. MARKET VIP", color=ft.colors.WHITE, weight=ft.FontWeight.BOLD, size=18),
        center_title=True,
        bgcolor="#111827",
        elevation=4,
    )

    # Dummy Data for Market / Items (Name, Mobile, Price, Change/Status)
    items_data = [
        {"name": "Gold VIP Rate", "mobile": "+91 9876543210", "price": "₹ 62,450", "change": "+150.00", "is_up": True},
        {"name": "Silver VIP Rate", "mobile": "+91 9123456789", "price": "₹ 74,200", "change": "-45.00", "is_up": False},
        {"name": "Platinum Pack", "mobile": "+91 9988776655", "price": "₹ 31,800", "change": "+12.50", "is_up": True},
        {"name": "Diamond Deal", "mobile": "+91 8877665544", "price": "₹ 95,100", "change": "+300.00", "is_up": True},
    ]

    list_view = ft.ListView(expand=1, spacing=10, padding=5)

    def create_card(data):
        return ft.Container(
            content=ft.Row(
                [
                    # Left: Name & Mobile Number (3-line feel / structured)
                    ft.Column(
                        [
                            ft.Text(data["name"], color=ft.colors.CYAN_ACCENT, weight=ft.FontWeight.BOLD, size=15),
                            ft.Text(f"Mob: {data['mobile']}", color=ft.colors.GREY_400, size=12),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=3,
                    ),
                    # Right: Price & Market Status
                    ft.Column(
                        [
                            ft.Text(data["price"], color=ft.colors.WHITE, weight=ft.FontWeight.BOLD, size=15),
                            ft.Text(
                                f"{data['change']}",
                                color=ft.colors.GREEN_ACCENT if data["is_up"] else ft.colors.RED_ACCENT,
                                size=12,
                                weight=ft.FontWeight.W_500,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.END,
                        spacing=3,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            bgcolor="#1f2937",
            padding=15,
            border_radius=10,
            border=ft.border.all(1, "#374151"),
        )

    for item in items_data:
        list_view.controls.append(create_card(item))

    # View History Button Action
    def open_history(e):
        page.dialog = ft.AlertDialog(
            title=ft.Text("Transaction History"),
            content=ft.Text("No recent history found. All trades/records will appear here."),
            actions=[ft.TextButton("Close", on_click=lambda _: close_dialog())],
        )
        page.dialog.open = True
        page.update()

    def close_dialog():
        page.dialog.open = False
        page.update()

    # Bottom View History Button (Amazon style clean look)
    history_btn = ft.ElevatedButton(
        text="View History",
        icon=ft.icons.HISTORY,
        color=ft.colors.WHITE,
        bgcolor="#2563eb",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            padding=ft.padding.symmetric(horizontal=20, vertical=15),
        ),
        on_click=open_history,
        width=300,
    )

    page.add(
        ft.Text("LIVE MARKET WATCH", color=ft.colors.GREY_500, size=12, weight=ft.FontWeight.BOLD),
        ft.Divider(height=10, color=ft.colors.TRANSPARENT),
        list_view,
        ft.Divider(height=10, color=ft.colors.TRANSPARENT),
        history_btn,
    )

ft.app(target=main)