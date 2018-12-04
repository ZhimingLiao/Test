#! -*-encoding:utf-8-*-

import os

class XMLFormat:

    @classmethod
    def __prettyXml(cls, element, indent, newline, level = 0):
        if element:  # 判断element是否有子元素
            if element.text == None or element.text.isspace():
                element.text = newline + indent * (level + 1)
            else:
                element.text = newline + indent * (level + 1) + element.text.strip() \
                               + newline + indent * (level + 1)
        temp = list(element)

        for subelement in temp:
            if temp.index(subelement) < (len(temp) - 1):
                subelement.tail = newline + indent * (level + 1)
            else:  # 如果是list的最后一个元素， 说明下一行是母元素的结束，缩进应该少一个
                subelement.tail = newline + indent * level
            XMLFormat.__prettyXml(subelement, indent, newline, level=level+1)

    @classmethod
    def BsXML(cls, StrXML, TempFileName='temp'):
        '''格式化XML字符串'''
        with open(TempFileName, 'w+', encoding='utf-8') as tfp:
            tfp.write(StrXML)
        tfp.close()
        from xml.etree import ElementTree
        try:
            tree = ElementTree.parse(TempFileName)
            root = tree.getroot()
            XMLFormat.__prettyXml(root, '\t', '\n')
            tree.write(TempFileName, 'utf-8')

        except:
             return StrXML+'非标准xml格式'

        with open(TempFileName, 'r+', encoding='utf-8') as fp:
            content = fp.read()
            fp.seek(0, 0)
            fp.write('<?xml version="1.0" encoding="GB2312"?>')
            fp.write('\n')
            fp.write(content)
        fp.close()
        with open(TempFileName, 'r', encoding='utf-8') as fp:
            content = fp.read()

        if os.path.exists(TempFileName):
            os.remove(TempFileName)
        return content


if __name__ == '__main__':
   a = '''<?xml version="1.0" encoding="utf-8"?><DocumentElement><AccessKey>493B312F3B383C34281C130B6ADE4D4E6D0CB8314E5F777C12983DB1F3FB9315902DA23A4847B336AB</AccessKey>  <MethodName>MZ_GetPayList</MethodName><DataTable><data_org_id>1</data_org_id><data_sys_id>1</data_sys_id>  <PatientID>000019212300</PatientID><StartDate>2018-11-23</StartDate>  <EndDate>2018-11-23</EndDate></DataTable></DocumentElement>'''
   print(XMLFormat.BsXML(a))