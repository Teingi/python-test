# -*- coding:UTF-8 -*-

'''
#绘制柱状图展示商家销售情况
from pyecharts import Bar  
attr=["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]    
v1=[5,20,36,10,75,90]    
v2=[10,25,8,60,20,80]    
bar=Bar("各商家产品销售情况")    
bar.add("商家A",attr,v1,is_stack=True)    
bar.add("商家B",attr,v2,is_stack=True)    
#bar.render()

#饼状图
from pyecharts import Pie    
attr=["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","鞋子"]    
v1=[11,12,13,10,10,10]    
pie=Pie("各产品销售情况")    
pie.add("",attr,v1,is_label_show=True)    
pie.render()


#圆环图
from pyecharts import Pie    
attr=["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","鞋子"]    
v1=[11,12,13,10,10,10]    
pie=Pie("饼图—圆环图示例",title_pos="center")    
pie.add("",attr,v1,radius=[40,75],label_text_color=None,    
       is_label_show=True,legend_orient="vertical",    
       legend_pos="left")    
pie.render()


#仪表盘
from pyecharts import Gauge    
gauge=Gauge("业务指标完成率—仪表盘")    
gauge.add("业务指标","完成率",66.66)    
gauge.render()
'''

#漏斗图
from pyecharts import Funnel    
attr=["潜在","接触","意向","明确","投入","谈判","成交"]    
value=[140,120,100,80,60,40,20]    
funnel=Funnel("销售管理分析漏斗图")    
funnel.add("商品",attr,value,is_label_show=True,    
          label_pos="inside",label_text_color="#fff")    
funnel.render()    
