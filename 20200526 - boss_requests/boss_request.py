import requests
from lxml import etree
import pymysql
import chardet,time,urllib
from urllib.parse import  quote,unquote
import xlwt

#1.获取单页html
def get_one_page(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    response=requests.get(url,headers=headers)
    response.encoding=chardet.detect(response.content)['encoding']
    return response.text
#2.解析html
def parse_one_page(html):
    #初始化
    result=etree.HTML(html)
    item={}
    item['t1']=result.xpath('//div[@class="el"]/p/span/a/text()') #职位名称
    item['t2']=result.xpath('//div[@class="el"]/span[@class="t2"]/a/text()') #公司名称
    item['t3']=result.xpath('//div[@class="el"]/span[@class="t3"]/text()') #工作地点
    t4=result.xpath('//div[@class="el"]/span[@class="t4"]')
    item['t4']=[]
    for i in t4:
        item['t4'].append(i.xpath('string(.)'))  #职位月薪
    item['t5']=result.xpath('//div[@class="el"]/span[@class="t5"]/text()') #发布时间
    item['href']=result.xpath('//div[@class="el"]/p/span/a/@href')  #详细链接

    #3.数据清洗,处理原始数据
    #(1)去掉职位名称前后空白
    for i in range(len(item['t1'])):
        item['t1'][i]=item['t1'][i].strip()

    #(2)薪资处理
    #定义列表，存储处理后的薪资数据
    zw_low=[] #最低月薪
    zw_height=[] #最高薪资
    #考虑薪资数据可能出现的情况做循环判断
    for xz in item['t4']:
        if xz !="":
            xz=xz.strip().split('-')
            if len(xz)>1:
                if xz[1][-1]=='月' and xz[1][-3]=='万':
                    zw_low.append(float(xz[0])*10000)
                    zw_height.append(float(xz[1][0:-3])*10000)
                elif xz[1][-1]=='年' and xz[1][-3]=='万':
                    zw_low.append(round((float(xz[0])*10000)/12,1))
                    zw_height.append(round((float(xz[1][0:-3])*10000)/12,1))
                elif xz[1][-1]=='月' and xz[1][-3]=='千':
                    zw_low.append(float(xz[0])*1000)
                    zw_height.append(float(xz[1][0:-3])*1000)
                else:
                    zw_low.append(0)
                    zw_height.append(0)
            else:
                if xz[0][-1] =='天' and xz[0][-3]=='元':
                    zw_low.append(xz[0][0:-3])
                    zw_height.append(xz[0][0:-3])
                else:
                    zw_low.append(0)
                    zw_height.append(0)
        else:
            zw_low.append(0)
            zw_height.append(0)
    item['xz_low']=zw_low
    item['xz_height']=zw_height

    #(3) 时间数据处理
    for i in range(len(item['t5'])):
        item['t5'][i]='2018-'+item['t5'][i]
    yield item
#4.存储至mysql
def write_to_mysql(content):
    #建立连接
    conn=pymysql.connect(host='127.0.0.1',user='root',passwd='root',db='test',charset='utf8')
    cursor=conn.cursor()
    for i in range(len(content['t1'])):
        zwmc=content['t1'][i]
        gsmc=content['t2'][i]
        gzdd=content['t3'][i]
        xz_low=content['xz_low'][i]
        xz_height=content['xz_height'][i]
        ptime=content['t5'][i]
        href=content['href'][i]
        print(zwmc,gsmc,gzdd,xz_low,xz_height,ptime,href)
        sql='insert into zhaoping values (null,%s,%s,%s,%s,%s,%s,%s)'
        parm=(zwmc,gsmc,gzdd,xz_low,xz_height,ptime,href)
        cursor.execute(sql,parm)
    conn.commit()
    cursor.close()
    conn.close()


'''
:https://search.51job.com/list/地点
(上海代号020000),000000,职能,行业,发布日期,月薪范围,职位,2,页数.html?
lang=c&postchannel=0000&workyear=工作年限&cotype=公司性质&degreefrom=学历要求&jobterm=工作类型&
companysize=公司规模&ord_field=0&dibiaoid=0&line=&welfare=薪资福利'''


#5.函数回调
def main(url=None):
    html=get_one_page(url)
    for i in parse_one_page(html):
        print(i)
        write_to_mysql(i)
        time.sleep(1)

def get_money_num():
    '''
        展示工资代码并让用户输入
    :return:
    '''
    money_list=[
        ["所有",'99'],
        ["2千以下",'01'],
        ["2-3千",'02'],
        ["3-4.5千",'03'],
        ["4.5-6千",'04'],
        ["6-8千",'05'],
        ["0.8-1万", '06'],
        ["1-1.5万",'07'],
        ["1.5-2万", '08'],
        ["2-3万", '09'],
        ["3-4万", '10'],
        ["4-5万", '11'],
        ["5万以上", '12'],
    ]
    for i in money_list:
        print("请输入：月薪范围：{}：请输入数字：{}".format(i[0],i[1]))

    your_select = input("请输入数字：")
    for i in money_list:
        if your_select in i:
            return_num = i[1]
            print(return_num)
            return return_num
    return False



def get_city_code():
    '''
    url = 'https://js.51jobcdn.com/in/resource/js/2019/search/common.7331dab4.js'
    rstr = requests.get(url).text
    start = rstr.find('window.area') +12
    #print(rstr[start])
    end = rstr.find('}',start)
    #print(rstr[end])
    rrstr = rstr[start:end+1]
    #print(rrstr)
    print(type(rrstr))
    city_dict = eval(rrstr)
    print(city_dict)
    '''
    city_dict = {'010000': '北京', '010100': '东城区', '010200': '西城区',
                 '010500': '朝阳区', '010600': '丰台区', '010700': '石景山区',
                 '010800': '海淀区', '010900': '门头沟区', '011000': '房山区',
                 '011100': '通州区', '011200': '顺义区', '011300': '昌平区',
                 '011400': '大兴区', '011500': '怀柔区', '011600': '平谷区',
                 '011700': '密云区', '011800': '延庆区', '020000': '上海',
                 '020100': '黄浦区', '020300': '徐汇区', '020400': '长宁区',
                 '020500': '静安区', '020600': '普陀区', '020800': '虹口区',
                 '020900': '杨浦区', '021000': '浦东新区', '021100': '闵行区',
                 '021200': '宝山区', '021300': '嘉定区', '021400': '金山区',
                 '021500': '松江区', '021600': '青浦区', '021800': '奉贤区',
                 '021900': '崇明区', '030000': '广东省', '030200': '广州',
                 '030201': '越秀区', '030202': '荔湾区', '030203': '海珠区',
                 '030204': '天河区', '030205': '白云区', '030206': '黄埔区',
                 '030207': '番禺区', '030208': '花都区', '030209': '南沙区',
                 '030211': '增城', '030212': '从化', '030300': '惠州',
                 '030400': '汕头', '030500': '珠海', '030501': '香洲区',
                 '030502': '斗门区', '030503': '金湾区', '030504': '横琴新区',
                 '030505': '高栏港经济区', '030506': '珠海高新区', '030507': '珠海保税区',
                 '030508': '万山海洋开发试验区', '030600': '佛山', '030601': '禅城区',
                 '030602': '顺德区', '030603': '南海区', '030604': '三水区',
                 '030605': '高明区', '030700': '中山', '030800': '东莞',
                 '030801': '莞城区', '030802': '南城区', '030803': '东城区',
                 '030804': '万江区', '030805': '石碣镇', '030806': '石龙镇',
                 '030807': '茶山镇', '030808': '石排镇', '030809': '企石镇',
                 '030810': '横沥镇', '030811': '桥头镇', '030812': '谢岗镇',
                 '030813': '东坑镇', '030814': '常平镇', '030815': '寮步镇',
                 '030816': '大朗镇', '030817': '麻涌镇', '030818': '中堂镇',
                 '030819': '高�墩�', '030820': '樟木头镇', '030821': '大岭山镇',
                 '030822': '望牛墩镇', '030823': '黄江镇', '030824': '洪梅镇',
                 '030825': '清溪镇', '030826': '沙田镇', '030827': '道�蛘�',
                 '030828': '塘厦镇', '030829': '虎门镇', '030830': '厚街镇',
                 '030831': '凤岗镇', '030832': '长安镇', '030833': '松山湖区',
                 '031400': '韶关', '031500': '江门', '031700': '湛江',
                 '031800': '肇庆', '031900': '清远', '032000': '潮州',
                 '032100': '河源', '032200': '揭阳', '032300': '茂名',
                 '032400': '汕尾', '032600': '梅州', '032700': '开平',
                 '032800': '阳江', '032900': '云浮', '040000': '深圳',
                 '040100': '福田区', '040200': '罗湖区', '040300': '南山区',
                 '040400': '盐田区', '040500': '宝安区', '040600': '龙岗区',
                 '040700': '光明新区', '040800': '坪山区', '040900': '大鹏新区',
                 '041000': '龙华新区', '050000': '天津', '050100': '和平区',
                 '050200': '河东区', '050300': '河西区', '050400': '南开区',
                 '050500': '河北区', '050600': '红桥区', '050700': '东丽区',
                 '050800': '西青区', '050900': '津南区', '051000': '北辰区',
                 '051100': '武清区', '051200': '宝坻区', '051300': '滨海新区',
                 '051400': '宁河区', '051500': '静海区', '051600': '蓟州区',
                 '060000': '重庆', '060100': '渝中区', '060200': '大渡口区',
                 '060300': '江北区', '060400': '沙坪坝区', '060600': '合川区',
                 '060700': '渝北区', '060800': '永川区', '060900': '巴南区',
                 '061000': '南川区', '061100': '九龙坡区', '061200': '万州区',
                 '061300': '涪陵区', '061400': '黔江区', '061500': '南岸区',
                 '061600': '北碚区', '061700': '长寿区', '061900': '江津区',
                 '062000': '綦江区', '062100': '潼南区', '062200': '铜梁区',
                 '062300': '大足区', '062400': '荣昌区', '062500': '璧山区',
                 '062600': '垫江县', '062700': '丰都县', '062800': '忠县',
                 '062900': '石柱县', '063000': '城口县', '063100': '彭水县',
                 '063200': '梁平区', '063300': '酉阳县', '063400': '开州区',
                 '063500': '秀山县', '063600': '巫溪县', '063700': '巫山县',
                 '063800': '奉节县', '063900': '武隆区', '064000': '云阳县',
                 '070000': '江苏省', '070200': '南京', '070201': '玄武区',
                 '070203': '秦淮区', '070204': '建邺区', '070205': '鼓楼区',
                 '070207': '浦口区', '070208': '六合区', '070209': '栖霞区',
                 '070210': '雨花台区', '070211': '江宁区', '070212': '溧水区',
                 '070213': '高淳区', '070300': '苏州', '070301': '姑苏区',
                 '070303': '吴中区', '070304': '相城区', '070305': '吴江区',
                 '070306': '工业园区', '070307': '高新区', '070400': '无锡',
                 '070401': '梁溪区', '070404': '滨湖区', '070405': '无锡新区',
                 '070406': '惠山区', '070407': '锡山区', '070408': '宜兴市',
                 '070409': '江阴市', '070500': '常州', '070501': '天宁区',
                 '070502': '钟楼区', '070504': '新北区', '070505': '武进区',
                 '070506': '金坛区', '070507': '溧阳市', '070600': '昆山',
                 '070700': '常熟', '070800': '扬州', '070900': '南通',
                 '071000': '镇江', '071100': '徐州', '071200': '连云港',
                 '071300': '盐城', '071400': '张家港', '071600': '太仓',
                 '071800': '泰州', '071900': '淮安', '072000': '宿迁',
                 '072100': '丹阳', '072300': '泰兴', '072500': '靖江',
                 '080000': '浙江省', '080200': '杭州', '080201': '拱墅区',
                 '080202': '上城区', '080203': '下城区', '080204': '江干区',
                 '080205': '西湖区', '080206': '滨江区', '080207': '余杭区',
                 '080208': '萧山区', '080209': '临安区', '080210': '富阳区',
                 '080211': '建德市', '080212': '桐庐县', '080213': '淳安县',
                 '080300': '宁波', '080301': '海曙区', '080303': '江北区',
                 '080304': '北仑区', '080305': '镇海区', '080306': '鄞州区',
                 '080307': '慈溪市', '080308': '余姚市', '080309': '奉化区',
                 '080310': '宁海县', '080311': '象山县', '080312': '高新区',
                 '080400': '温州', '080500': '绍兴', '080600': '金华',
                 '080700': '嘉兴', '080800': '台州', '080900': '湖州',
                 '081000': '丽水', '081100': '舟山', '081200': '衢州',
                 '081400': '义乌', '081600': '海宁', '090000': '四川省',
                 '090200': '成都', '090201': '青羊区', '090202': '锦江区',
                 '090203': '金牛区', '090204': '武侯区', '090205': '成华区',
                 '090206': '龙泉驿区', '090207': '青白江区', '090208': '新都区',
                 '090209': '温江区', '090210': '都江堰市', '090211': '彭州市',
                 '090212': '邛崃市', '090213': '崇州市', '090214': '金堂县',
                 '090215': '双流区', '090216': '郫都区', '090217': '大邑县',
                 '090218': '蒲江县', '090219': '新津县', '090220': '高新区',
                 '090221': '简阳市', '090300': '绵阳', '090400': '乐山',
                 '090500': '泸州', '090600': '德阳', '090700': '宜宾',
                 '090800': '自贡', '090900': '内江', '091000': '攀枝花',
                 '091100': '南充', '091200': '眉山', '091300': '广安',
                 '091400': '资阳', '091500': '遂宁', '091600': '广元',
                 '091700': '达州', '091800': '雅安', '091900': '西昌',
                 '092000': '巴中', '092100': '甘孜', '092200': '阿坝',
                 '092300': '凉山', 100000: '海南省', 100200: '海口',
                 100300: '三亚', 100400: '洋浦经济开发区', 100500: '文昌',
                 100600: '琼海', 100700: '万宁', 100800: '儋州',
                 100900: '东方', 101000: '五指山', 101100: '定安',
                 101200: '屯昌', 101300: '澄迈', 101400: '临高',
                 101500: '三沙', 101600: '琼中', 101700: '保亭',
                 101800: '白沙', 101900: '昌江', 102000: '乐东',
                 102100: '陵水', 110000: '福建省', 110200: '福州',
                 110201: '鼓楼区', 110202: '台江区', 110203: '仓山区',
                 110204: '马尾区', 110205: '晋安区', 110206: '闽侯县',
                 110207: '连江县', 110208: '罗源县', 110209: '闽清县',
                 110210: '永泰县', 110211: '平潭县', 110212: '福清市',
                 110213: '长乐市', 110300: '厦门', 110400: '泉州',
                 110500: '漳州', 110600: '莆田', 110700: '三明',
                 110800: '南平', 110900: '宁德', 111000: '龙岩',
                 120000: '山东省', 120200: '济南', 120201: '历下区',
                 120202: '市中区', 120203: '槐荫区', 120204: '天桥区',
                 120205: '历城区', 120206: '长清区', 120207: '平阴县',
                 120208: '济阳县', 120209: '商河县', 120210: '章丘区',
                 120211: '高新区', 120300: '青岛', 120301: '市南区',
                 120302: '市北区', 120303: '黄岛区', 120304: '崂山区',
                 120305: '城阳区', 120306: '李沧区', 120307: '胶州市',
                 120308: '即墨区', 120309: '平度市', 120310: '莱西市',
                 120311: '高新区', 120400: '烟台', 120500: '潍坊',
                 120600: '威海', 120700: '淄博', 120800: '临沂',
                 120900: '济宁', 121000: '东营', 121100: '泰安',
                 121200: '日照', 121300: '德州', 121400: '菏泽',
                 121500: '滨州', 121600: '枣庄', 121700: '聊城',
                 121800: '莱芜', 130000: '江西省', 130200: '南昌',
                 130201: '东湖区', 130202: '西湖区', 130203: '青云谱区',
                 130204: '湾里区', 130205: '青山湖区', 130206: '南昌县',
                 130207: '新建区', 130208: '安义县', 130209: '进贤县',
                 130210: '红谷滩新区', 130300: '九江', 130400: '景德镇',
                 130500: '萍乡', 130600: '新余', 130700: '鹰潭',
                 130800: '赣州', 130900: '吉安', 131000: '宜春',
                 131100: '抚州', 131200: '上饶', 140000: '广西',
                 140200: '南宁', 140300: '桂林', 140400: '柳州',
                 140500: '北海', 140600: '玉林', 140700: '梧州',
                 140800: '防城港', 140900: '钦州', 141000: '贵港',
                 141100: '百色', 141200: '河池', 141300: '来宾',
                 141400: '崇左', 141500: '贺州', 150000: '安徽省',
                 150200: '合肥', 150201: '瑶海区', 150202: '庐阳区',
                 150203: '蜀山区', 150204: '包河区', 150205: '经开区',
                 150206: '滨湖新区', 150207: '新站区', 150208: '高新区',
                 150209: '政务区', 150210: '北城新区', 150211: '巢湖市',
                 150212: '长丰县', 150213: '肥东县', 150214: '肥西县',
                 150215: '庐江县', 150300: '芜湖', 150400: '安庆',
                 150500: '马鞍山', 150600: '蚌埠', 150700: '阜阳',
                 150800: '铜陵', 150900: '滁州', 151000: '黄山',
                 151100: '淮南', 151200: '六安', 151400: '宣城',
                 151500: '池州', 151600: '宿州', 151700: '淮北',
                 151800: '亳州', 160000: '河北省', 160100: '雄安新区',
                 160200: '石家庄', 160300: '廊坊', 160400: '保定',
                 160500: '唐山', 160600: '秦皇岛', 160700: '邯郸',
                 160800: '沧州', 160900: '张家口', 161000: '承德',
                 161100: '邢台', 161200: '衡水', 161300: '燕郊开发区',
                 170000: '河南省', 170200: '郑州', 170201: '中原区',
                 170202: '二七区', 170203: '管城回族区', 170204: '金水区',
                 170205: '上街区', 170206: '惠济区', 170207: '中牟县',
                 170208: '巩义市', 170209: '荥阳市', 170210: '新密市',
                 170211: '新郑市', 170212: '登封市', 170213: '郑东新区',
                 170214: '高新区', 170215: '经开区', 170216: '郑州航空港区',
                 170300: '洛阳', 170400: '开封', 170500: '焦作', 170600: '南阳',
                 170700: '新乡', 170800: '周口', 170900: '安阳', 171000: '平顶山',
                 171100: '许昌', 171200: '信阳', 171300: '商丘', 171400: '驻马店',
                 171500: '漯河', 171600: '濮阳', 171700: '鹤壁', 171800: '三门峡',
                 171900: '济源', 172000: '邓州', 180000: '湖北省', 180200: '武汉',
                 180201: '江岸区', 180202: '江汉区', 180203: '�~口区', 180204: '汉阳区',
                 180205: '武昌区', 180206: '青山区', 180207: '洪山区', 180208: '东西湖区',
                 180209: '汉南区', 180210: '蔡甸区', 180211: '江夏区', 180212: '黄陂区',
                 180213: '新洲区', 180214: '武汉经济开发区', 180215: '东湖新技术产业开发区',
                 180300: '宜昌', 180400: '黄石', 180500: '襄阳', 180600: '十堰', 180700: '荆州',
                 180800: '荆门', 180900: '孝感', 181000: '鄂州', 181100: '黄冈', 181200: '随州',
                 181300: '咸宁', 181400: '仙桃', 181500: '潜江', 181600: '天门', 181700: '神农架',
                 181800: '恩施', 190000: '湖南省', 190200: '长沙', 190201: '芙蓉区', 190202: '天心区',
                 190203: '岳麓区', 190204: '开福区', 190205: '雨花区', 190206: '望城区', 190207: '长沙县',
                 190208: '宁乡县', 190209: '浏阳市', 190300: '株洲', 190400: '湘潭', 190500: '衡阳',
                 190600: '岳阳', 190700: '常德', 190800: '益阳', 190900: '郴州', 191000: '邵阳',
                 191100: '怀化', 191200: '娄底', 191300: '永州', 191400: '张家界', 191500: '湘西',
                 200000: '陕西省', 200200: '西安', 200201: '莲湖区', 200202: '新城区', 200203: '碑林区',
                 200204: '灞桥区', 200205: '未央区', 200206: '雁塔区', 200207: '阎良区', 200208: '临潼区',
                 200209: '长安区', 200210: '蓝田县', 200211: '周至县', 200212: '��邑区', 200213: '高陵区',
                 200214: '高新技术产业开发区', 200215: '经济技术开发区', 200216: '曲江文化新区',
                 200217: '�哄鄙�态区', 200218: '国家民用航天产业基地', 200219: '西咸新区',
                 200220: '西安阎良航空基地', 200221: '西安国际港务区', 200300: '咸阳', 200400: '宝鸡',
                 200500: '铜川', 200600: '延安', 200700: '渭南', 200800: '榆林', 200900: '汉中',
                 201000: '安康', 201100: '商洛', 201200: '杨凌', 210000: '山西省', 210200: '太原',
                 210300: '运城', 210400: '大同', 210500: '临汾', 210600: '长治', 210700: '晋城',
                 210800: '阳泉', 210900: '朔州', 211000: '晋中', 211100: '忻州', 211200: '吕梁',
                 220000: '黑龙江省', 220200: '哈尔滨', 220201: '道里区', 220202: '南岗区',
                 220203: '道外区', 220204: '平房区', 220205: '松北区', 220206: '香坊区',
                 220207: '呼兰区', 220208: '阿城区', 220209: '依兰县', 220210: '方正县',
                 220211: '宾县', 220212: '巴彦县', 220213: '木兰县', 220214: '通河县',
                 220215: '延寿县', 220216: '双城区', 220217: '尚志市', 220218: '五常市',
                 220300: '伊春', 220400: '绥化', 220500: '大庆', 220600: '齐齐哈尔',
                 220700: '牡丹江', 220800: '佳木斯', 220900: '鸡西', 221000: '鹤岗',
                 221100: '双鸭山', 221200: '黑河', 221300: '七台河', 221400: '大兴安岭',
                 230000: '辽宁省', 230200: '沈阳', 230201: '大东区', 230202: '浑南区',
                 230203: '康平县', 230204: '和平区', 230205: '皇姑区', 230206: '沈北新区',
                 230207: '沈河区', 230208: '苏家屯区', 230209: '铁西区', 230210: '于洪区',
                 230211: '法库县', 230212: '辽中区', 230213: '新民市', 230300: '大连',
                 230301: '西岗区', 230302: '中山区', 230303: '沙河口区', 230304: '甘井子区',
                 230305: '旅顺口区', 230306: '金州区', 230307: '瓦房店市', 230308: '普兰店区',
                 230309: '庄河市', 230310: '长海县', 230312: '高新园区', 230313: '长兴岛',
                 230314: '大连保税区', 230400: '鞍山', 230500: '营口', 230600: '抚顺',
                 230700: '锦州', 230800: '丹东', 230900: '葫芦岛', 231000: '本溪',
                 231100: '辽阳', 231200: '铁岭', 231300: '盘锦', 231400: '朝阳',
                 231500: '阜新', 240000: '吉林省', 240200: '长春', 240201: '朝阳区',
                 240202: '南关区', 240203: '宽城区', 240204: '二道区', 240205: '绿园区',
                 240206: '双阳区', 240207: '经济技术开发区', 240208: '高新技术产业开发区',
                 240209: '净月经济开发区', 240210: '汽车产业开发区', 240211: '榆树市',
                 240212: '九台区', 240213: '德惠市', 240214: '农安县', 240300: '吉林',
                 240400: '辽源', 240500: '通化', 240600: '四平', 240700: '松原',
                 240800: '延吉', 240900: '白山', 241000: '白城', 241100: '延边', 250000: '云南省', 250200: '昆明', 250201: '五华区', 250202: '盘龙区', 250203: '官渡区', 250204: '西山区', 250205: '东川区', 250206: '呈贡区', 250207: '晋宁区', 250208: '富民县', 250209: '宜良县', 250210: '石林彝族自治县', 250211: '嵩明县',
                 250212: '禄劝县', 250213: '寻甸县', 250214: '安宁市', 250300: '曲靖', 250400: '玉溪', 250500: '大理',
                 250600: '丽江', 251000: '红河州', 251100: '普洱', 251200: '保山',
                 251300: '昭通', 251400: '文山', 251500: '西双版纳', 251600: '德宏', 251700: '楚雄', 251800: '临沧', 251900: '怒江', 252000: '迪庆', 260000: '贵州省',
                 260200: '贵阳', 260300: '遵义', 260400: '六盘水', 260500: '安顺', 260600: '铜仁', 260700: '毕节', 260800: '黔西南', 260900: '黔东南', 261000: '黔南', 270000: '甘肃省', 270200: '兰州', 270300: '金昌', 270400: '嘉峪关', 270500: '酒泉', 270600: '天水', 270700: '武威', 270800: '白银', 270900: '张掖', 271000: '平凉',
                 271100: '定西', 271200: '陇南', 271300: '庆阳', 271400: '临夏', 271500: '甘南', 280000: '内蒙古',
                 280200: '呼和浩特', 280300: '赤峰', 280400: '包头', 280700: '通辽', 280800: '鄂尔多斯', 280900: '巴彦淖尔', 281000: '乌海', 281100: '呼伦贝尔', 281200: '乌兰察布', 281300: '兴安盟', 281400: '锡林郭勒盟', 281500: '阿拉善盟', 290000: '宁夏', 290200: '银川', 290300: '吴忠', 290400: '中卫', 290500: '石嘴山',
                 290600: '固原', 300000: '西藏', 300200: '拉萨', 300300: '日喀则', 300400: '林芝', 300500: '山南', 300600: '昌都', 300700: '那曲', 300800: '阿里', 310000: '新疆', 310200: '乌鲁木齐',
                 310300: '克拉玛依', 310400: '喀什地区', 310500: '伊犁', 310600: '阿克苏', 310700: '哈密', 310800: '石河子', 310900: '阿拉尔', 311000: '五家渠', 311100: '图木舒克',
                 311200: '昌吉', 311300: '阿勒泰', 311400: '吐鲁番', 311500: '塔城', 311600: '和田', 311700: '克孜勒苏柯尔克孜', 311800: '巴音郭楞', 311900: '博尔塔拉', 320000: '青海省', 320200: '西宁', 320300: '海东', 320400: '海西', 320500: '海北', 320600: '黄南', 320700: '海南', 320800: '果洛', 320900: '玉树',
                 330000: '香港', 340000: '澳门', 350000: '台湾', 360000: '国外', 361000: '亚洲', 361001: '日本', 361002: '韩国',
                 361003: '马来西亚', 361004: '新加坡', 361005: '泰国', 361006: '菲律宾', 361007: '印度尼西亚', 361008: '斯里兰卡', 361009: '印度', 361010: '缅甸', 361011: '越南', 361012: '朝鲜', 361013: '哈萨克斯坦', 361014: '乌兹别克斯坦', 361015: '伊朗', 361016: '伊拉克', 361017: '阿富汗', 361018: '巴基斯坦', 361019: '土耳其', 361020: '科威特', 361021: '沙特阿拉伯', 361022: '蒙古',
                 361023: '孟加拉国', 362000: '欧洲', 362001: '英国', 362002: '法国', 362003: '德国', 362004: '意大利', 362005: '西班牙', 362006: '葡萄牙', 362007: '爱尔兰', 362008: '波兰', 362009: '挪威',
                 362010: '瑞典', 362011: '芬兰', 362012: '奥地利', 362013: '乌克兰', 362014: '白俄罗斯', 362015: '保加利亚', 362016: '罗马尼亚', 362017: '匈牙利', 362018: '希腊', 362019: '俄罗斯', 362020: '瑞士', 362021: '丹麦', 362022: '比利时', 362023: '荷兰', 363000: '美洲', 363001: '美国', 363002: '加拿大', 363003: '墨西哥', 363004: '巴西', 363005: '阿根廷', 363006: '智利', 363007: '秘鲁',
                 363008: '哥伦比亚', 363009: '委内瑞拉', 363010: '玻利维亚', 364000: '非洲', 364001: '埃及', 364002: '南非', 364003: '苏丹', 364004: '阿尔及利亚', 364005: '埃塞俄比亚', 364006: '肯尼亚', 364007: '赞比亚', 364008: '坦桑尼亚', 364009: '马达加斯加', 364010: '莫桑比克', 364011: '安哥拉',
                 364012: '加纳', 364013: '摩洛哥', 364014: '尼日利亚',
                 365000: '大洋洲', 365001: '澳大利亚', 365002: '新西兰', 366000: '其他', '01': '珠三角'}
    return city_dict


def input_city_code():
    '''
        展示城市代码，并让用户输入
    :return:
    '''
    city_dict = get_city_code()
    is_city_code = None
    big = []
    while is_city_code == None:
        for k,v in city_dict.items():
            big.append(str(k))
        city_code = input("请输出相应的城市代码：")
        print(len(city_dict.keys()))
        if city_code in big:
            is_city_code = True
            return city_code


def inputkey_encode_encode():
    '''
        编码用户输入的关键字
    :return:
    '''
    input_key = input("请输入关键字：")
    temp_a = quote(input_key)
    return_res = quote(temp_a)
    print("已选择关键字：{}：中文编码后：{}".format(input_key,return_res))
    return return_res


def sql_to_excel(table=None, excel_path=None):
    '''
        sql_to_excel
    :param table:
    :param excel_path:
    :return:
    '''
    conn=pymysql.connect(host='127.0.0.1',user='root',passwd='root',db='test',charset='utf8')
    cursor=conn.cursor()
    ret = {"status": "false"}
    try:
        if excel_path == None and (str(excel_path).split("."))[-1] not in ["xls", "xlsx"]:
            print(ret)
            return ret
        if excel_path != None and table != None:
            print("if excel_path != None and table != None:", ret)
            sql = '''select * from {}'''.format(table)
            cursor.execute(sql, args=None)
            # 获取数据库中的表单
            results = cursor.fetchall()
            select_from_select_tables_list = results
            if select_from_select_tables_list != ():
                print("if select_from_select_tables_list != ():", ret)
                book = xlwt.Workbook(encoding='utf-8')
                table = book.add_sheet('1')
                # table.write(0, 0, "student_name")
                # table.write(0, 1, "student_id")
                # table.write(0, 2, 'student_email')
                # table.write(0, 3, 'student_gpa')
                for i in range(len(select_from_select_tables_list)):
                    try:
                        table.write(i, 0, select_from_select_tables_list[i][1])
                        table.write(i, 1, select_from_select_tables_list[i][2])
                        table.write(i, 2, select_from_select_tables_list[i][3])
                        table.write(i, 3, select_from_select_tables_list[i][4])
                        table.write(i, 4, select_from_select_tables_list[i][5])
                        table.write(i, 5, select_from_select_tables_list[i][6])
                        table.write(i, 6, select_from_select_tables_list[i][7])
                    except:
                        continue
            ret["status"] = "true"
            book.save(excel_path)
            sql = "Truncate Table zhaoping;"
            cursor.execute(sql)
            cursor.close()
            conn.close()
    except BaseException as e:
        print(e)
        return ret

    return ret


#6.回调主函数，完成分页
if __name__ == '__main__':
    city_code = input_city_code()
    print("已选择城市：{}".format(city_code))
    time.sleep(2)
    money_num = get_money_num()
    print("已选择工资范围：{}".format(money_num))
    time.sleep(2)
    input_key = inputkey_encode_encode()
    for i in range(1,3):
        url = 'https://search.51job.com/list/'+ str(city_code) +',000000,0000,00,9,' + str(money_num)+ ','+ str(input_key) +',2,' + str(i) + '.html'
        main(url)
    sql_to_excel(table="zhaoping",excel_path="save.xls")







