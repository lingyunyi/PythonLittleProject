import requests
import json, time, datetime,re


def get_gk_score():
    form_header = {
        "Host": "gzwb.zk789.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://gzwb.zk789.cn/Main.aspx",
        "Connection": "keep-alive",
        "Cookie": "security_session_verify=64e7b9e63e4ff88225c30415bb49a4ab; ASP.NET_SessionId=e3wq2jxveqev0wjfpzssr5zr; Hm_lvt_050f8955113b36425b90c785f931a78c=1614855498; Hm_lpvt_050f8955113b36425b90c785f931a78c=1614855685; PAGEVIEWSTATISTICS03=2021/3/4 18:58:28",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "max-age=0",
    }
    url = 'https://gzwb.zk789.cn/Signup/SignupStatistics.aspx'
    response = requests.get(url, headers=form_header, timeout=30)
    print(response.text)
    time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(time.time()))
    return

print(int(time.time()))

# get_gk_score()


a = '''<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><title>
	四川省2021年普通高等学校高职教育单独招生报名系统
</title><link href="/Resources/Contents/Themes/Base/Front/Styles/content.css" type="text/css" rel="stylesheet" />
    <script src="/Resources/Libs/Jquery/1.8.3/jquery.js" type="text/javascript"></script>
    <script>
        var _hmt = _hmt || [];
        (function () {
            var hm = document.createElement("script");
            hm.src = "https://hm.baidu.com/hm.js?050f8955113b36425b90c785f931a78c";
            var s = document.getElementsByTagName("script")[0];
            s.parentNode.insertBefore(hm, s);
        })();
    </script>
</head>
<body style="background-color: #CBDFEC; width:780px; margin:0px auto;" >
    <table width="780" border="0" cellpadding="0" cellspacing="0" style="background-color: #DDE6EF;">
        <tr>
            <td colspan="2">
                <img src="/Resources/Contents/Themes/Base/Front/Images/top.gif" id="xttop" alt="" width="780" height="94" usemap="#Map" style="border-top-style: none; border-right-style: none; border-left-style: none;
                    border-bottom-style: none;" /></td>
        </tr>
        <tr>
            <td colspan="2" align="left">
                <table width="770" border="0" cellpadding="0" cellspacing="0">
                    <tr>
                        <td align="left" style="width: 770px; height: 30px; background-image: url(/Resources/Contents/Themes/Base/Front/Images/navigate2.gif);">
                            <div id="navigate2" style="padding-left: 20px; font-size: 17px; color: White; font-weight: 900;">
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td align="left" style="width: 770px; height: 25px; background-image: url(/Resources/Contents/Themes/Base/Front/Images/subnavigate2.gif);">
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td>
                <table width="770" border="0" cellpadding="0" cellspacing="0">
                    <tr>
                        <td align="center" style="width: 770px; height: 30px; background-color: White;">
                            <div id="navigate" style="width: 300px; height: 21px; font-size: 17px; font-weight: 900;background-image: url(/Resources/Contents/Themes/Base/Front/Images/title_bg.gif); padding-top: 9px;" >
                                类 别 选 择
                            </div>
                        </td>
                    </tr>
                    <tr>
                        <td style="background-color: #FFFFFF">
                            <form method="post" action="./SignupStatistics.aspx" id="FormStuMasterPage">
<div class="aspNetHidden">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="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" />
</div>

<div class="aspNetHidden">

	<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="724E7910" />
	<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="l+eMmCoRFvd/+KJP1HVPc6s88KRi29XsKs6KBFqkZ+90VF+KGmeFe/OilenPbrJGKmISiLSWPAPgDGKkqazg+onEdGrMIxmoFf4aZRtJ4YEj90XzLcXvpSg1j18MWDPe" />
</div>
                                <div>
                                    
    <h1>院校报考人数统计</h1>
    <div>
	<table cellspacing="0" cellpadding="3" rules="rows" id="ContentPlaceHolder1_gvData" style="background-color:#E7E7FF;border-color:#E7E7FF;border-width:1px;border-style:None;font-size:13px;width:100%;border-collapse:collapse;">
		<tr style="color:#F7F7F7;background-color:#4A3C8C;font-weight:bold;height:25px;">
			<th scope="col">院校代号</th><th scope="col">院校名称</th><th scope="col">普高类计划数</th><th scope="col">中职类计划数</th><th scope="col">普高类已报名人数</th><th scope="col">中职类已报名人数</th>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    1161
                </td><td>北京社会管理职业学院</td><td>30</td><td>30</td><td>15</td><td>7</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    4351
                </td><td>长沙民政职业技术学院</td><td>126</td><td>114</td><td>19</td><td>17</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5054
                </td><td>重庆城市管理职业学院</td><td>550</td><td>150</td><td>79</td><td>51</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5140
                </td><td>川北幼儿师范高等专科学校</td><td>565</td><td>916</td><td>21</td><td>144</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5141
                </td><td>成都纺织高等专科学校</td><td>1455</td><td>1460</td><td>209</td><td>152</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5145
                </td><td>四川幼儿师范高等专科学校</td><td>1020</td><td>1100</td><td>188</td><td>86</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5146
                </td><td>四川中医药高等专科学校</td><td>740</td><td>1240</td><td>78</td><td>593</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5151
                </td><td>成都航空职业技术学院</td><td>1220</td><td>1255</td><td>181</td><td>118</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5152
                </td><td>四川交通职业技术学院</td><td>1480</td><td>1480</td><td>200</td><td>207</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5153
                </td><td>达州职业技术学院</td><td>1301</td><td>1394</td><td>111</td><td>244</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5154
                </td><td>四川机电职业技术学院</td><td>600</td><td>2800</td><td>33</td><td>273</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5155
                </td><td>四川工程职业技术学院</td><td>1155</td><td>1155</td><td>134</td><td>99</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5157
                </td><td>绵阳职业技术学院</td><td>800</td><td>1500</td><td>49</td><td>134</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5158
                </td><td>四川工商职业技术学院</td><td>1000</td><td>1200</td><td>90</td><td>92</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5159
                </td><td>四川建筑职业技术学院</td><td>1705</td><td>1705</td><td>262</td><td>114</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5160
                </td><td>四川国际标榜职业学院</td><td>1500</td><td>3500</td><td>182</td><td>152</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5161
                </td><td>成都农业科技职业学院</td><td>830</td><td>1590</td><td>108</td><td>135</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5162
                </td><td>宜宾职业技术学院</td><td>1000</td><td>2400</td><td>103</td><td>451</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5163
                </td><td>成都艺术职业大学</td><td>2155</td><td>3645</td><td>32</td><td>60</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5164
                </td><td>四川托普信息技术职业学院</td><td>3880</td><td>3882</td><td>159</td><td>291</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5165
                </td><td>四川职业技术学院</td><td>1290</td><td>1295</td><td>194</td><td>192</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5166
                </td><td>眉山职业技术学院</td><td>960</td><td>1810</td><td>107</td><td>274</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5167
                </td><td>泸州职业技术学院</td><td>950</td><td>2050</td><td>112</td><td>413</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5168
                </td><td>乐山职业技术学院</td><td>1145</td><td>1465</td><td>144</td><td>352</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5169
                </td><td>雅安职业技术学院</td><td>1550</td><td>1550</td><td>171</td><td>271</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5170
                </td><td>四川邮电职业技术学院</td><td>530</td><td>555</td><td>45</td><td>76</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5171
                </td><td>四川航天职业技术学院</td><td>1645</td><td>1955</td><td>148</td><td>379</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5172
                </td><td>四川化工职业技术学院</td><td>1020</td><td>1430</td><td>97</td><td>280</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5173
                </td><td>四川水利职业技术学院</td><td>1000</td><td>1000</td><td>86</td><td>76</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5174
                </td><td>南充职业技术学院</td><td>1325</td><td>1775</td><td>153</td><td>301</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5175
                </td><td>成都职业技术学院</td><td>810</td><td>1555</td><td>118</td><td>379</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5176
                </td><td>内江职业技术学院</td><td>1024</td><td>1526</td><td>53</td><td>117</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5177
                </td><td>成都东软学院</td><td>300</td><td>300</td><td>14</td><td>3</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5178
                </td><td>四川司法警官职业学院</td><td>175</td><td>175</td><td>50</td><td>22</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5179
                </td><td>四川工业科技学院</td><td>2000</td><td>3000</td><td>59</td><td>17</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5180
                </td><td>四川信息职业技术学院</td><td>660</td><td>1540</td><td>36</td><td>115</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5181
                </td><td>广安职业技术学院</td><td>1780</td><td>1795</td><td>186</td><td>339</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5182
                </td><td>四川商务职业学院</td><td>1000</td><td>1000</td><td>60</td><td>77</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5183
                </td><td>四川铁道职业学院</td><td>520</td><td>520</td><td>84</td><td>34</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5184
                </td><td>四川财经职业学院</td><td>820</td><td>820</td><td>126</td><td>81</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5185
                </td><td>四川文化产业职业学院</td><td>908</td><td>909</td><td>118</td><td>135</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5186
                </td><td>四川科技职业学院</td><td>3000</td><td>6800</td><td>373</td><td>311</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5187
                </td><td>四川艺术职业学院</td><td>567</td><td>835</td><td>78</td><td>105</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5188
                </td><td>四川文化传媒职业学院</td><td>2000</td><td>5000</td><td>204</td><td>586</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5189
                </td><td>四川华新现代职业学院</td><td>2000</td><td>4000</td><td>88</td><td>76</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5190
                </td><td>四川城市职业学院</td><td>4500</td><td>5300</td><td>238</td><td>218</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5191
                </td><td>四川现代职业学院</td><td>2270</td><td>3310</td><td>80</td><td>71</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5192
                </td><td>四川长江职业学院</td><td>3495</td><td>3755</td><td>149</td><td>232</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5193
                </td><td>民办四川天一学院</td><td>3007</td><td>5993</td><td>138</td><td>272</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5194
                </td><td>四川卫生康复职业学院</td><td>780</td><td>960</td><td>111</td><td>342</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5195
                </td><td>四川三河职业学院</td><td>1518</td><td>3542</td><td>61</td><td>162</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5196
                </td><td>四川电影电视学院</td><td>935</td><td>935</td><td>6</td><td>11</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5197
                </td><td>南充电影工业职业学院</td><td>790</td><td>810</td><td>2</td><td>5</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5198
                </td><td>四川汽车职业技术学院</td><td>1668</td><td>3500</td><td>89</td><td>105</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5199
                </td><td>四川护理职业学院</td><td>880</td><td>880</td><td>198</td><td>357</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5651
                </td><td>巴中职业技术学院</td><td>1900</td><td>4080</td><td>63</td><td>163</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5652
                </td><td>四川希望汽车职业学院</td><td>2305</td><td>4365</td><td>29</td><td>484</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5653
                </td><td>四川电子机械职业技术学院</td><td>2800</td><td>3200</td><td>167</td><td>122</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5655
                </td><td>川南幼儿师范高等专科学校</td><td>656</td><td>676</td><td>114</td><td>87</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5656
                </td><td>四川文轩职业学院</td><td>5160</td><td>6336</td><td>416</td><td>693</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5657
                </td><td>成都工业职业技术学院</td><td>971</td><td>1941</td><td>141</td><td>284</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5658
                </td><td>四川西南航空职业学院</td><td>1502</td><td>5800</td><td>19</td><td>12</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5659
                </td><td>四川应用技术职业学院</td><td>1370</td><td>1630</td><td>27</td><td>9</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5660
                </td><td>成都工贸职业技术学院</td><td>611</td><td>929</td><td>49</td><td>370</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5702
                </td><td>四川大学锦江学院</td><td>300</td><td>360</td><td>9</td><td>4</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5705
                </td><td>电子科技大学成都学院</td><td>412</td><td>413</td><td>15</td><td>4</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5706
                </td><td>西南交通大学希望学院</td><td>1880</td><td>1880</td><td>95</td><td>243</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5710
                </td><td>西南财经大学天府学院</td><td>1000</td><td>1000</td><td>20</td><td>12</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5713
                </td><td>西南科技大学城市学院</td><td>827</td><td>1009</td><td>16</td><td>17</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5719
                </td><td>四川传媒学院</td><td>270</td><td>280</td><td>17</td><td>10</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5724
                </td><td>成都银杏酒店管理学院</td><td>990</td><td>1010</td><td>7</td><td>0</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5747
                </td><td>成都文理学院</td><td>725</td><td>730</td><td>27</td><td>36</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5776
                </td><td>四川外国语大学成都学院</td><td>700</td><td>700</td><td>15</td><td>13</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5779
                </td><td>德阳农业科技职业学院</td><td>880</td><td>1820</td><td>41</td><td>24</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5780
                </td><td>四川文化艺术学院</td><td>1275</td><td>1625</td><td>13</td><td>4</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5781
                </td><td>天府新区通用航空职业学院</td><td>1600</td><td>2200</td><td>109</td><td>235</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5782
                </td><td>江阳城建职业学院</td><td>2043</td><td>2900</td><td>521</td><td>313</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5783
                </td><td>天府新区航空旅游职业学院</td><td>700</td><td>3100</td><td>4</td><td>68</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5784
                </td><td>德阳科贸职业学院</td><td>1950</td><td>2550</td><td>211</td><td>156</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5785
                </td><td>天府新区信息职业学院</td><td>1460</td><td>1790</td><td>160</td><td>216</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5786
                </td><td>眉山药科职业学院</td><td>2000</td><td>2100</td><td>86</td><td>110</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5787
                </td><td>德阳城市轨道交通职业学院</td><td>1880</td><td>1880</td><td>58</td><td>22</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5788
                </td><td>阿坝职业学院</td><td>219</td><td>221</td><td>5</td><td>7</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5789
                </td><td>西昌民族幼儿师范高等专科学校</td><td>690</td><td>830</td><td>64</td><td>46</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5790
                </td><td>四川体育职业学院</td><td>90</td><td>90</td><td>37</td><td>4</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5791
                </td><td>达州中医药职业学院</td><td>758</td><td>760</td><td>39</td><td>145</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5792
                </td><td>内江卫生与健康职业学院</td><td>0</td><td>1000</td><td>0</td><td>246</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5793
                </td><td>南充科技职业学院</td><td>925</td><td>1000</td><td>29</td><td>31</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5794
                </td><td>攀枝花攀西职业学院</td><td>480</td><td>770</td><td>0</td><td>1</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5795
                </td><td>资阳口腔职业学院</td><td>1101</td><td>1101</td><td>23</td><td>23</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5796
                </td><td>资阳环境科技职业学院</td><td>2150</td><td>2200</td><td>122</td><td>67</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5797
                </td><td>广元中核职业技术学院</td><td>350</td><td>700</td><td>10</td><td>58</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    5799
                </td><td>南充文化旅游职业学院</td><td>875</td><td>875</td><td>13</td><td>67</td>
		</tr><tr style="color:#4A3C8C;background-color:#F7F7F7;height:25px;">
			<td>
                    5803
                </td><td>绵阳飞行职业学院</td><td>570</td><td>630</td><td>1</td><td>0</td>
		</tr><tr style="color:#4A3C8C;background-color:#E7E7FF;height:25px;">
			<td>
                    
                </td><td>合计</td><td>118309</td><td>172642</td><td>9021</td><td>14612</td>
		</tr>
	</table>
</div>
    <br />
    <div style="padding-bottom:15px;">
        <input type="submit" name="ctl00$ContentPlaceHolder1$btnReturn" value="返回" id="ContentPlaceHolder1_btnReturn" style="height:22px;width:65px;" />
    </div>
    

                                </div>
                            </form>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
        <tr>
            <td style="height: 25px; background-image: url(/Resources/Contents/Themes/Base/Front/Images/down1.gif);" colspan="2">
            </td>
        </tr>
    </table>
    <map id="Map">
        <area alt="" shape="rect" coords="606,75,780,106" href="http://www.zk789.net" target="_blank" />
    </map>
    <div class="center">
        <table width="780" border="0" cellpadding="0" cellspacing="0">
            <tr>
                <td style="background-color: #99CCFF; width: 780px;">
                    <table width="780" border="0" cellspacing="0" cellpadding="0">
                        <tr>
                            <td align="center" height="80" style="font-size: 30px; font-weight: bolder; background-color: #B9CADE;
                                color: #5D7AA2;">
                                <div id="downyxjs">
                                </div>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
            <tr>
                <td style="background-image: url(/Resources/Contents/Themes/Base/Front/Images/down2.gif); height: 100px; width: 780px; text-align: center; font-family:'宋体';"
                    colspan="2">
                    <table width="780px" border="0" cellpadding="0" cellspacing="0">
                        <tr>
                            <td style="width:260px; color:#fff; padding-top:5px; padding-bottom:2px;">
                                <img src="/Resources/Contents/Themes/Base/Front/Images/Icons/icon-zk789wx.jpg" width="80" height="80" />
                                <br />微信公众号
                            </td>
                            <td style="text-align:left; width:520px; color:#fff; ">
                                <p style="margin:0px;">®2015-2021&nbsp;四川省教育考试院版权所有&nbsp;Ver:2.3 </p>
                                <p style="padding-left:10px; padding-top:5px;margin:0px;">技术服务：<a href="http://www.zk789.net" target="_blank" style="color:#fff">招生考试信息网</a>（<a href="http://www.zk789.net" target="_blank" style="color:#fff">www.zk789.net</a>）</p>
                                <p style="padding-left:60px; padding-top:5px;margin:0px;">版本日期 Date:2021.03.04</p>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </div>
    <div id="SYSTEM_YEAR" style="display: none;">2021</div>
    <div id="SYSTEM_IP" style="display: none;">117.182.133.110</div>
    <script language="javascript" type="text/javascript">
        setAdShow();
        function setAdShow() {
            switch (window.location.pathname.toLowerCase().substr(window.location.pathname.toLowerCase().lastIndexOf("/"))) {
                case "/default.aspx":
                    $("#navigate").html("类 别 选 择");
                    break;
                case "/information.aspx":
                    $("#navigate").html("信 息 提 示");
                    break;
                case "/showhelp.aspx":
                    $("#navigate").html("报 名 流 程");
                    break;
                case "/editsignup.aspx":
                    $("#navigate").html("填写院校志愿");
                    break;
                case "/registersignup.aspx":
                    $("#navigate").html("填写注册信息");
                    break;
                case "/showsignup.aspx":
                    $("#navigate").html("查看报名信息");
                case "/signupstatistics.aspx":
                    $("#navigate").html("报 考 统 计");
                    break;
            }
            $("#downyxjs").html("<img src='/Resources/Contents/Themes/Base/Front/Images/ad_2.gif' width='780' height='80' />");
            document.oncontextmenu = function (event) {
                event.preventDefault();
            };
            document.onkeydown = document.onkeyup = document.onkeypress = function (event) {
                var e = event || window.event || arguments.callee.caller.arguments[0];

                if (e && e.keyCode == 123) {
                    e.returnValue = false;
                    return (false);
                }
            }
        }
    </script>
    
    <script language="javascript" src="/Resources/Contents/Themes/Base/Front/Scripts/show.js" type="text/javascript" defer="defer"></script>
    <script language="javascript" src="/Resources/Contents/Themes/Base/Front/Scripts/show2.js" type="text/javascript" defer="defer"></script>
</body>
</html>'''


score_tuple = re.findall("</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td>",a,re.S)
score_list = sorted(score_tuple, key=lambda x : int(x[4]), reverse=True)
[print(i) for i in b]
