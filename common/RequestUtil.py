from urllib.parse import urlencode

import  requests
from yaml_util import read_config_file,write_extract_file
import jsonpath

class RequestUtil:
    # 获得session回传对象
    session = requests.session()

    def __int__(self,env='test'):
        #获取初始路径
        if env == 'test' or env =='test_base_url' or env =='test_url' or env == None:
            env = 'test_base_url'
        self.base_url = read_config_file('Env',env)


    def send_request(self,method,url,**kwargs):
        url = self.base_url + url
        # 处理请求数据

        res = RequestUtil.session.request(method= method,url=url,**kwargs)
        return res

    def json_form(self,json_data):
        params = {'form': urlencode(json_data)}
        return params

    # 规范yaml文件格式
    def analysis_yaml(self,caseInfo):
        # 判断一级关键字是否存在
        caseInfo_keys = dict(caseInfo).keys()
        if 'name' in caseInfo_keys and 'base_url' in caseInfo_keys and 'request' in caseInfo_keys and 'validate' in caseInfo_keys:
            # 判断request下的关键字是否存在：
            request_keys = dict(caseInfo['request']).keys()
            if 'method' in request_keys and 'url' in request_keys:
                method = caseInfo['request']['method']
                url = caseInfo['request']['url']
                header = None
                # 参数(params,data,json)，请求头，文件上传这些都不能约束
                if jsonpath.jsonpath(caseInfo,'$..headers'):
                    headers = caseInfo['request']['headers']
                files = None
                if jsonpath.jsonpath(caseInfo,'$..files'):
                    files  = caseInfo['request']['files']
                res = self.send_request(method=method,url=url,headers=headers,files=files,**caseInfo['reuqest'])
                return_data = res.json
                return_text = res.text
                # 提示接口关联变量
                if 'extract' in caseInfo_keys:
                    for key,value in dict(caseInfo['extract']).items():
                        # 正则表达式提取
                        if '(.+?)' in value or '(.+?)' in value:
                            ze_value = res.search(value,return_text)
                            if ze_value:
                                extract_data = {key:ze_value.group(1)}
                                write_extract_file(extract_data)
                        else:   # json提取
                            extract_data = {key:return_data[value]}
                            write_extract_file(extract_data)
            else:
                print("request下属关键字不存在")
        else:
            print("关键字不存在")



if __name__ == '__main__':
    resUtil = RequestUtil()
    data = {
        "nameKeyWord": "6974164582983",
        "types":"",
        "purchaseType":"",
        "brandNames":"",
        "keyBenefitId":"",
        "sellPointId":"",
        "principalId":"",
        "beginTime": "2023-11-20",
        "endTime":"2023-11-20",
        "belong":"",
        "saleAttribute":"",
        "salesVolumeCompare":"",
        "dateTypeEnum": "SENT",
        "productStatus":""
    }
    params = resUtil.json_form(json_data=data)
    print(params)