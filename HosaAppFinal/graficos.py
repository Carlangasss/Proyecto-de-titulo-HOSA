import flet as ft

class SampleRod(ft.BarChartRod):
    def __init__(self, y: float, hovered: bool = False):
        super().__init__()
        self.hovered = hovered
        self.y = y

    def _before_build_command(self):
        self.to_y = self.y + 1 if self.hovered else self.y
        self.color = ft.colors.YELLOW if self.hovered else ft.colors.WHITE
        self.border_side = (
            ft.BorderSide(width=1, color=ft.colors.GREEN_400)
            if self.hovered
            else ft.BorderSide(width=0, color=ft.colors.WHITE)
        )
        super()._before_build_command()

    

    def _build(self):
        self.tooltip = str(self.y)
        self.width = 30
        self.color = ft.colors.WHITE
        self.bg_to_y = 70
        self.bg_color = ft.colors.ORANGE

consumoLuz = 0.288 #kw/h
consumoLuz2 = 12 #W/h

def main(page: ft.Page):
    def on_chart_event(e: ft.BarChartEvent):
        for group_index, group in enumerate(chart.bar_groups):
            for rod_index, rod in enumerate(group.bar_rods):
                rod.hovered = e.group_index == group_index and e.rod_index == rod_index
        chart.update()

    chart = ft.BarChart(
        bar_groups=[
            ft.BarChartGroup(
                x=0,
                bar_rods=[SampleRod(consumoLuz2*3)],
            ),
            ft.BarChartGroup(
                x=1,
                bar_rods=[SampleRod(consumoLuz2*5)],
            ),
            ft.BarChartGroup(
                x=2,
                bar_rods=[SampleRod(consumoLuz2*5.4)],
            ),
            ft.BarChartGroup(
                x=3,
                bar_rods=[SampleRod(consumoLuz2*3.8)],
            ),
            ft.BarChartGroup(
                x=4,
                bar_rods=[SampleRod(consumoLuz2*4.3)],
            ),
            ft.BarChartGroup(
                x=5,
                bar_rods=[SampleRod(consumoLuz2*4.1)],
            ),
            ft.BarChartGroup(
                x=6,
                bar_rods=[SampleRod(consumoLuz2*3.7)],
            ),
        ],
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(value=0, label=ft.Text("L")),
                ft.ChartAxisLabel(value=1, label=ft.Text("M")),
                ft.ChartAxisLabel(value=2, label=ft.Text("W")),
                ft.ChartAxisLabel(value=3, label=ft.Text("J")),
                ft.ChartAxisLabel(value=4, label=ft.Text("V")),
                ft.ChartAxisLabel(value=5, label=ft.Text("S")),
                ft.ChartAxisLabel(value=6, label=ft.Text("D")),
            ],
        ),
        on_chart_event=on_chart_event,
        interactive=True,
    )

    a = ft.Container(
        chart, bgcolor=ft.colors.GREEN_200, padding=10, border_radius=5,  width=250, height=400, margin=30
    )

    b = ft.Container(height=40)
    c = ft.Container(height=40)

    page.add(b,
        a,
        c
    )

# ft.app(main)