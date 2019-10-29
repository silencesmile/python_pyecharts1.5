# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 3:21 PM
# @Author  : Python小学僧
# @File    : 上下布局.py
# @Software: PyCharm

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line,Scatter


def grid_vertical():
    bar = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="Grid-Bar"))
    )
    line = (
        Line()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .add_yaxis("商家B", Faker.values())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Grid-Line", pos_top="48%"),
            legend_opts=opts.LegendOpts(pos_top="48%"),
        )
    )

    grid = (
        Grid()
        .add(bar, grid_opts=opts.GridOpts(pos_bottom="60%"))
        .add(line, grid_opts=opts.GridOpts(pos_top="60%"))
    )
    return grid

grid = grid_vertical()
grid.render("./html_files/Grid-上下布局.html")