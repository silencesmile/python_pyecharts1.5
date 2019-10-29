# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 2:06 PM
# @Author  : Python小学僧
# @File    : map_code.py
# @Software: PyCharm

from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType

# 省会及直辖市
# data = [['广东', 64], ['北京', 47], ['上海', 28], ['江西', 145], ['湖南', 145], ['浙江', 57], ['江苏', 124], ["自定义点", 150]]

# 各个城市
data = [
    ("海门", 9),("鄂尔多斯", 12),("招远", 12),("舟山", 12),("齐齐哈尔", 74),("盐城", 15),
    ("赤峰", 56),("青岛", 18),("乳山", 18),("金昌", 69),("泉州", 21),("莱西", 21),
    ("日照", 21),("胶南", 22),("南通", 83),("拉萨", 24),("云浮", 24),("梅州", 25)]

# 方法一 设置地图参数
def geo_base():
    c = (
        Geo()
        .add_schema(maptype="china")
        # 加入自定义的点，格式为
        # .add_coordinate("自定义点", 80.39770014211535, 39.90779994986951)
        .add("geo", data)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="Geo-基本示例"),
        )
    )
    return c

c = geo_base()
c.render(path="./html_files/中国地图.html")

# 方法二 设置地图参数
def base_info():
    print(data)
    geo = Geo()
    geo.add_schema(maptype="china")  # 加入自定义的点，格式为
    # geo.add_coordinate("自定义点", 80.39770014211535,39.90779994986951)
    # 地图形式 type_=ChartType.HEATMAP
    geo.add("geo", data, type_=ChartType.EFFECT_SCATTER)
    # is_show：是否显示经纬度
    geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="Geo-基本示例"))

    return geo

c = base_info()
c.render(path="./html_files/中国地图.html")

