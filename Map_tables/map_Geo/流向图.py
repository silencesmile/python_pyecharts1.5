# -*- coding: utf-8 -*-
# @Time    : 2019/10/28 4:41 PM
# @Author  : Python小学僧
# @File    : 流向图.py
# @Software: PyCharm

from pyecharts import options as opts
from pyecharts.charts import Geo, Page
from pyecharts.globals import ChartType, SymbolType

# 城市
city_info = [("成都",10),("合肥",20),("宁波",30),("武汉",40),("西安",50),("郑州",60),("大连",70),("济南",80)]
# 添加城市
add_city = [("北京", 100), ("上海", 100)]
# 城市流向
city_change = [("上海","成都"),("上海","合肥"),("上海","宁波"),("上海","武汉"),("上海","西安"),("北京","郑州"),("北京","大连"),("北京","济南")]

#定义地理图
geo = Geo()
#设置画布宽度
geo.width = "800px"
#设置画布高度
geo.height = "600px"
#全局设置项
# 参考字段分段is_piecewise
geo.set_global_opts(visualmap_opts = opts.VisualMapOpts(max_=100, is_piecewise=True),
                    title_opts=opts.TitleOpts(title="Geo-流向图"))
#添加主题，中国地图，填充及边界颜色设置
geo.add_schema(
            maptype="china",
            # border_color 省份之间的区分线  color：地图背景色
            itemstyle_opts=opts.ItemStyleOpts( border_color="#111", color="#454545"),
        )

#添加系列
geo.add(
            "原城市", city_info, type_=ChartType.EFFECT_SCATTER,             #散点图的一种形式
            label_opts=opts.LabelOpts(is_show = False),   #不显示数值则设置为False
           # color="red"
        )
geo.add(
            "添加城市",add_city,
            type_=ChartType.HEATMAP,       #散点的另一种形式
            label_opts=opts.LabelOpts(is_show=False)
        )
#设置流向
geo.add(
            "流向图", city_change, type_=ChartType.LINES,
            linestyle_opts=opts.LineStyleOpts(curve=0.3,color="#63B8FF"),   #基本线条的弯曲程度及颜色，英文及RGB都行
            effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW, symbol_size=6, color="#FF7F00")  # 流向线条的形式、颜色
        )

geo.render(path="./html_files/地图流向图.html")
