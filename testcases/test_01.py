import  pytest
import  common.yaml_util
from common import RequestUtil


class Test:

    @pytest.mark.parametrize('casaInfo',read_testcase_file('testcase/test_yaml.yml'))
    def test_01(self,casaInfo):
        print(casaInfo)
        RequestUtil().analysis_yaml(casaInfo)

        headers = {
            "Content-Type": "application/json"
        }
        url= "product/productStatistics/statistics"
        data = {
            "nameKeyWord": "6974164582983",
            "types": "",
            "purchaseType": "",
            "brandNames": "",
            "keyBenefitId": "",
            "sellPointId": "",
            "principalId": "",
            "beginTime": "2023-11-20",
            "endTime": "2023-11-20",
            "belong": "",
            "saleAttribute": "",
            "salesVolumeCompare": "",
            "dateTypeEnum": "SENT",
            "productStatus": ""
        }
        resUtil = RequestUtil()
        res = resUtil.send_request(method='POST',url=url,data=data)
