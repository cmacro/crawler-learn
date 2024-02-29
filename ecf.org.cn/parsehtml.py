from lxml import html
import re

def parseListPage(html_text):
    tree = html.fromstring(html_text)

    # //*[@id="content_warp"]/div[3]/div[2]/li/a
    contants = tree.xpath('//*[@id="content_warp"]/div[3]/div[2]/li//a')
    # print(result)
    rows = []
    for raw in contants:
        name = raw.text_content().strip()
        if name == "": continue
        row = {'name': name,'url': raw.get('href')}
        match = re.search(r'\d+', row['url'])
        if match:
            row['id'] = match.group()
        rows.append(row)

    # page_count = 0
    total_pages_element = tree.xpath('//*[@id="ctl00_ContentPlaceHolder2_pageinfo"]/input/@value')[0]
    total_pages = int(total_pages_element.split("/")[-1].strip())

    return rows, total_pages

def getFirstValue(res):
    if len(res) > 0:
        return res[0]
    return ""

def parseDetailPage(html_text):
    # 参展商详细页面内容数据页面数据
    tree = html.fromstring(html_text)
    data = {}
    # 主数据
    data['name'] = getFirstValue(tree.xpath('//*[@id="ctl00_ContentPlaceHolder2_ctl01_ctl00_ctl00_Label1"]/text()'))
    data['en_name'] = getFirstValue(tree.xpath('//*[@id="ctl00_ContentPlaceHolder2_ctl01_ctl00_ctl00_Label2"]/text()'))
    data['address'] = getFirstValue(tree.xpath('//*[@id="ctl00_ContentPlaceHolder2_ctl01_ctl00_ctl00_Label3"]/text()'))
    data['en_address'] = getFirstValue(tree.xpath('//*[@id="ctl00_ContentPlaceHolder2_ctl01_ctl00_ctl00_Label4"]/text()'))

    # 扩展数据 公司信息 Company information
    script_text = getFirstValue(tree.xpath('//script[contains(text(), "F.load(function()")]/text()'))
    fields = ['exp_type','attrib','company_type','founded','website','tel','email','trading_group','area']
    offset = 7
    for field in fields:
        search_key = f"f{offset}_state=" + r'\{.*?"Text":\s*"(.*?)"\};'
        match = re.search(search_key, script_text, re.DOTALL)
        if match:
            data[field] = match.group(1)
        offset += 1
    return data


with open('data/浙江.html', 'r', encoding='utf-8') as f:
    html_text = f.read()
data,page_count = parseListPage(html_text)

print(page_count)

# with open('data/detail_4496.html', 'r', encoding='utf-8') as f:
#     html_text = f.read()
# data = parseDetailPage(html_text)
# print(data)
    