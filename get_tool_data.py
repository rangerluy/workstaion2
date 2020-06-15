import pandas as pd
import configparser

cf = configparser.ConfigParser()
cf.read('config.ini', encoding='UTF-8')
xl2 = cf.get('xl_name2', 'xl')
xl3 = cf.get('xl_name3', 'xl')
xl4 = cf.get('xl_name4', 'xl')
xl5 = cf.get('xl_name5', 'xl')
xl6 = cf.get('xl_name6', 'xl')


# 用于比较未入组数据用的工具表
class ToolXl:
    # CHS_DRGS_DIC_MDC.xlsx
    def dic_mdc_diag(self):
        df = pd.read_excel(xl4, keep_default_na=False)
        mdc_code = [i for i in df['MDC_CODE']]
        diag_code = [i for i in df['DIAG_CODE']]
        result = [mdc_code, diag_code]
        return result

    #  国临2.0诊断编码
    def gl2_code(self):
        df = pd.read_excel(xl2, keep_default_na=False)
        diag_code = [i for i in df['ICD_CODE']]
        diag_name = [i for i in df['ICD_NAME']]
        result = [diag_code, diag_name]
        return result

    # 国临2.0到CHS的映射
    def map(self):
        df = pd.read_excel(xl3, keep_default_na=False)
        diag_code = [i for i in df['GL2_CODE']]
        return diag_code

    # CHS_DRGS_DIC_ADRG_DIAG
    def dic_adrg_diag(self):
        df = pd.read_excel(xl5, keep_default_na=False)
        mdc_code = [i for i in df['MDC']]
        adrg_code = [i for i in df['ADRG_CODE']]
        diag_code = [i for i in df['DIAG_CODE']]
        result = [mdc_code, adrg_code, diag_code]
        return result

    # CHS_DRGS_DIC_ADRG_OPER.xlsx

    def dic_adrg_oper(self):
        df = pd.read_excel(xl6, keep_default_na=False)
        mdc_code = [i for i in df['MDC']]
        adrg_code = [i for i in df['ADRG_CODE']]
        oper_code = [i for i in df['OPER_CODE1']]
        result = [mdc_code, adrg_code, oper_code]
        return result


if __name__ == '__main__':
    t = ToolXl()
    CHS_DIC_MDC = t.dic_mdc_diag()

    CHS_DIC_ADRG_DIAG = t.dic_adrg_diag()
    print(CHS_DIC_ADRG_DIAG[2])
