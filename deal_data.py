from workstaion2.get_data import *
from workstaion2.get_tool_data import *
# 处理数据类
class DealData:
    # 9999

    # 住院时长超过60天
    def deal_nonomal1(self):
        u = Ungroped()
        nonomal = u.nonomal()
        base_id =[nonomal[0][i] for i in range(len(nonomal[0])) if nonomal[12][i] == '9999' and nonomal[4][i]>60]
        sex =[nonomal[1][i] for i in range(len(nonomal[0])) if nonomal[12][i] == '9999' and nonomal[4][i]>60]
        age =[nonomal[2][i] for i in range(len(nonomal[0])) if nonomal[12][i] == '9999' and nonomal[4][i]>60]
        baby_age =[nonomal[3][i] for i in range(len(nonomal[0])) if nonomal[12][i] == '9999' and nonomal[4][i]>60]
        in_days =[nonomal[4][i] for i in range(len(nonomal[0])) if nonomal[12][i] == '9999' and nonomal[4][i]>60]
        hos_amount =[nonomal[5][i] for i in range(len(nonomal[0])) if nonomal[12][i] == '9999' and nonomal[4][i]>60]
        main_diag_code =[nonomal[6][i] for i in range(len(nonomal[0])) if nonomal[12][i] == '9999' and nonomal[4][i]>60]
        main_diag_name =[nonomal[7][i] for i in range(len(nonomal[0])) if nonomal[12][i] == '9999' and nonomal[4][i]>60]
        other_diags_code =[nonomal[8][i] for i in range(len(nonomal[0])) if nonomal[12][i] == '9999' and nonomal[4][i]>60]
        other_oper_code =[nonomal[9][i] for i in range(len(nonomal[0])) if nonomal[12][i] == '9999' and nonomal[4][i]>60]
        mdc_code =[nonomal[10][i] for i in range(len(nonomal[0])) if nonomal[12][i] == '9999' and nonomal[4][i]>60]
        adrg_code =[nonomal[11][i] for i in range(len(nonomal[0])) if nonomal[12][i] == '9999' and nonomal[4][i]>60]
        drg_code =[nonomal[12][i] for i in range(len(nonomal[0])) if nonomal[12][i] == '9999' and nonomal[4][i]>60]
        oper_code =[nonomal[13][i] for i in range(len(nonomal[0])) if nonomal[12][i] == '9999' and nonomal[4][i]>60]
        error_log =[nonomal[14][i] for i in range(len(nonomal[0])) if nonomal[12][i] == '9999' and nonomal[4][i]>60]
        log =[nonomal[15][i] for i in range(len(nonomal[0])) if nonomal[12][i] == '9999' and nonomal[4][i]>60]
        result = [base_id,sex,age,baby_age,in_days,hos_amount,main_diag_code,main_diag_name,other_diags_code,other_oper_code,mdc_code,adrg_code,drg_code,oper_code,error_log,log]
        return result

    # 费用异常
    def deal_nonomal2(self):
        u = Ungroped()
        nonomal = u.nonomal()
        base_id =[nonomal[0][i] for i in range(len(nonomal[0])) if (nonomal[12][i] == '9999'and nonomal[4][i] !=0 and nonomal[5][i]/nonomal[4][i]<5) or (nonomal[12][i] == '9999'and nonomal[4][i] ==0)]
        sex =[nonomal[1][i] for i in range(len(nonomal[0])) if (nonomal[12][i] == '9999'and nonomal[4][i] !=0 and nonomal[5][i]/nonomal[4][i]<5) or (nonomal[12][i] == '9999'and nonomal[4][i] ==0)]
        age =[nonomal[2][i] for i in range(len(nonomal[0])) if (nonomal[12][i] == '9999'and nonomal[4][i] !=0 and nonomal[5][i]/nonomal[4][i]<5) or (nonomal[12][i] == '9999'and nonomal[4][i] ==0)]
        baby_age =[nonomal[3][i] for i in range(len(nonomal[0])) if (nonomal[12][i] == '9999'and nonomal[4][i] !=0 and nonomal[5][i]/nonomal[4][i]<5) or (nonomal[12][i] == '9999'and nonomal[4][i] ==0)]
        in_days =[nonomal[4][i] for i in range(len(nonomal[0])) if (nonomal[12][i] == '9999'and nonomal[4][i] !=0 and nonomal[5][i]/nonomal[4][i]<5) or (nonomal[12][i] == '9999'and nonomal[4][i] ==0)]
        hos_amount =[nonomal[5][i] for i in range(len(nonomal[0])) if (nonomal[12][i] == '9999'and nonomal[4][i] !=0 and nonomal[5][i]/nonomal[4][i]<5) or (nonomal[12][i] == '9999'and nonomal[4][i] ==0)]
        main_diag_code =[nonomal[6][i] for i in range(len(nonomal[0])) if (nonomal[12][i] == '9999'and nonomal[4][i] !=0 and nonomal[5][i]/nonomal[4][i]<5) or (nonomal[12][i] == '9999'and nonomal[4][i] ==0)]
        main_diag_name =[nonomal[7][i] for i in range(len(nonomal[0])) if (nonomal[12][i] == '9999'and nonomal[4][i] !=0 and nonomal[5][i]/nonomal[4][i]<5) or (nonomal[12][i] == '9999'and nonomal[4][i] ==0)]
        other_diags_code =[nonomal[8][i] for i in range(len(nonomal[0])) if (nonomal[12][i] == '9999'and nonomal[4][i] !=0 and nonomal[5][i]/nonomal[4][i]<5) or (nonomal[12][i] == '9999'and nonomal[4][i] ==0)]
        other_oper_code =[nonomal[9][i] for i in range(len(nonomal[0])) if (nonomal[12][i] == '9999'and nonomal[4][i] !=0 and nonomal[5][i]/nonomal[4][i]<5) or (nonomal[12][i] == '9999'and nonomal[4][i] ==0)]
        mdc_code =[nonomal[10][i] for i in range(len(nonomal[0])) if (nonomal[12][i] == '9999'and nonomal[4][i] !=0 and nonomal[5][i]/nonomal[4][i]<5) or (nonomal[12][i] == '9999'and nonomal[4][i] ==0)]
        adrg_code =[nonomal[11][i] for i in range(len(nonomal[0])) if (nonomal[12][i] == '9999'and nonomal[4][i] !=0 and nonomal[5][i]/nonomal[4][i]<5) or (nonomal[12][i] == '9999'and nonomal[4][i] ==0)]
        drg_code =[nonomal[12][i] for i in range(len(nonomal[0])) if (nonomal[12][i] == '9999'and nonomal[4][i] !=0 and nonomal[5][i]/nonomal[4][i]<5) or (nonomal[12][i] == '9999'and nonomal[4][i] ==0)]
        oper_code =[nonomal[13][i] for i in range(len(nonomal[0])) if (nonomal[12][i] == '9999'and nonomal[4][i] !=0 and nonomal[5][i]/nonomal[4][i]<5) or (nonomal[12][i] == '9999'and nonomal[4][i] ==0)]
        error_log =[nonomal[14][i] for i in range(len(nonomal[0])) if (nonomal[12][i] == '9999'and nonomal[4][i] !=0 and nonomal[5][i]/nonomal[4][i]<5) or (nonomal[12][i] == '9999'and nonomal[4][i] ==0)]
        log =[nonomal[15][i] for i in range(len(nonomal[0])) if (nonomal[12][i] == '9999'and nonomal[4][i] !=0 and nonomal[5][i]/nonomal[4][i]<5) or (nonomal[12][i] == '9999'and nonomal[4][i] ==0)]
        result = [base_id, sex, age, baby_age, in_days, hos_amount, main_diag_code, main_diag_name, other_diags_code,
                  other_oper_code, mdc_code, adrg_code, drg_code, oper_code, error_log, log]
        return result

    #  0000

    def code_match1(self):   # 0000先再国临2.0编码找到对应的诊断编码
        u = Ungroped()  # 未入组类
        t = ToolXl()  # 工具表类
        no_diags = u.non_diags()  # 0000
        icd_code = t.gl2_code()[0]  # 国临2.0诊断编码
        icd_name = t.gl2_code()[1]  # 国临2.0诊断名称
        base_id = [no_diags[0][i] for i in range(len(no_diags[7])) for j in range(len(icd_name)) if no_diags[7][i] == icd_name[j]]
        sex = [no_diags[1][i] for i in range(len(no_diags[7])) for j in range(len(icd_name)) if no_diags[7][i] == icd_name[j]]
        age = [no_diags[2][i] for i in range(len(no_diags[7])) for j in range(len(icd_name)) if no_diags[7][i] == icd_name[j]]
        baby_age = [no_diags[3][i] for i in range(len(no_diags[7])) for j in range(len(icd_name)) if no_diags[7][i] == icd_name[j]]
        in_days = [no_diags[4][i] for i in range(len(no_diags[7])) for j in range(len(icd_name)) if no_diags[7][i] == icd_name[j]]
        hos_amount = [no_diags[5][i] for i in range(len(no_diags[7])) for j in range(len(icd_name)) if no_diags[7][i] == icd_name[j]]
        main_diag_code = [icd_code[j] for i in range(len(no_diags[7])) for j in range(len(icd_name)) if no_diags[7][i] == icd_name[j]]
        main_diag_name = [no_diags[7][i] for i in range(len(no_diags[7])) for j in range(len(icd_name)) if no_diags[7][i] == icd_name[j]]
        other_diags_code = [no_diags[8][i] for i in range(len(no_diags[7])) for j in range(len(icd_name)) if no_diags[7][i] == icd_name[j]]
        other_oper_code = [no_diags[9][i] for i in range(len(no_diags[7])) for j in range(len(icd_name)) if no_diags[7][i] == icd_name[j]]
        mdc_code = [no_diags[10][i] for i in range(len(no_diags[7])) for j in range(len(icd_name)) if no_diags[7][i] == icd_name[j]]
        adrg_code = [no_diags[11][i] for i in range(len(no_diags[7])) for j in range(len(icd_name)) if no_diags[7][i] == icd_name[j]]
        drg_code = [no_diags[12][i] for i in range(len(no_diags[7])) for j in range(len(icd_name)) if no_diags[7][i] == icd_name[j]]
        oper_code = [no_diags[13][i] for i in range(len(no_diags[7])) for j in range(len(icd_name)) if no_diags[7][i] == icd_name[j]]
        error_log = [no_diags[14][i] for i in range(len(no_diags[7])) for j in range(len(icd_name)) if no_diags[7][i] == icd_name[j]]
        log = [no_diags[15][i] for i in range(len(no_diags[7])) for j in range(len(icd_name)) if no_diags[7][i] == icd_name[j]]

        result = [base_id,sex,age,baby_age,in_days,hos_amount,main_diag_code,main_diag_name,other_diags_code,other_oper_code,mdc_code,adrg_code,
                  drg_code,oper_code,error_log,log]
        return result

    # 0000得出的结果
    # 不是国临2.0编码
    def code_match2(self): # 不是国临2.0编码
        c = self.code_match1()
        u = Ungroped()
        no_diags = u.non_diags()# 0000
        base_id = [no_diags[0][i] for i in range(len(no_diags[0])) if no_diags[0][i] not in c[0]]
        sex =[no_diags[1][i] for i in range(len(no_diags[0])) if no_diags[0][i] not in c[0]]
        age =[no_diags[2][i] for i in range(len(no_diags[0])) if no_diags[0][i] not in c[0]]
        baby_age =[no_diags[3][i] for i in range(len(no_diags[0])) if no_diags[0][i] not in c[0]]
        in_days =[no_diags[4][i] for i in range(len(no_diags[0])) if no_diags[0][i] not in c[0]]
        hos_amount =[no_diags[5][i] for i in range(len(no_diags[0])) if no_diags[0][i] not in c[0]]
        main_diag_code =[no_diags[6][i] for i in range(len(no_diags[0])) if no_diags[0][i] not in c[0]]
        main_diag_name =[no_diags[7][i] for i in range(len(no_diags[0])) if no_diags[0][i] not in c[0]]
        other_diags_code =[no_diags[8][i] for i in range(len(no_diags[0])) if no_diags[0][i] not in c[0]]
        other_oper_code =[no_diags[9][i] for i in range(len(no_diags[0])) if no_diags[0][i] not in c[0]]
        mdc_code =[no_diags[10][i] for i in range(len(no_diags[0])) if no_diags[0][i] not in c[0]]
        adrg_code =[no_diags[11][i] for i in range(len(no_diags[0])) if no_diags[0][i] not in c[0]]
        drg_code =[no_diags[12][i] for i in range(len(no_diags[0])) if no_diags[0][i] not in c[0]]
        oper_code =[no_diags[13][i] for i in range(len(no_diags[0])) if no_diags[0][i] not in c[0]]
        error_log =[no_diags[14][i] for i in range(len(no_diags[0])) if no_diags[0][i] not in c[0]]
        log =[no_diags[15][i] for i in range(len(no_diags[0])) if no_diags[0][i] not in c[0]]
        result = [base_id, sex, age, baby_age, in_days, hos_amount, main_diag_code, main_diag_name, other_diags_code,
                  other_oper_code, mdc_code, adrg_code, drg_code, oper_code, error_log, log]
        return result
    #无映射
    def deal_map_matched1(self): # 将返回的能匹配到2.0编码的病例与映射进行匹配       # 无国临2.0 映射
        t = ToolXl()  # 工具表类
        c = self.code_match1()
        map = t.map() # 映射
        base_id = [c[0][i] for i in range(len(c[0])) if c[6][i] not in map]
        sex = [c[1][i] for i in range(len(c[0])) if c[6][i] not in map]
        age =[c[2][i] for i in range(len(c[0])) if c[6][i] not in map]
        baby_age =[c[3][i] for i in range(len(c[0])) if c[6][i] not in map]
        in_days =[c[4][i] for i in range(len(c[0])) if c[6][i] not in map]
        hos_amount =[c[5][i] for i in range(len(c[0])) if c[6][i] not in map]
        main_diag_code =[c[6][i] for i in range(len(c[0])) if c[6][i] not in map]
        main_diag_name =[c[7][i] for i in range(len(c[0])) if c[6][i] not in map]
        other_diags_code =[c[8][i] for i in range(len(c[0])) if c[6][i] not in map]
        other_oper_code =[c[9][i] for i in range(len(c[0])) if c[6][i] not in map]
        mdc_code =[c[10][i] for i in range(len(c[0])) if c[6][i] not in map]
        adrg_code =[c[11][i] for i in range(len(c[0])) if c[6][i] not in map]
        drg_code =[c[12][i] for i in range(len(c[0])) if c[6][i] not in map]
        oper_code =[c[13][i] for i in range(len(c[0])) if c[6][i] not in map]
        error_log =[c[14][i] for i in range(len(c[0])) if c[6][i] not in map]
        log =[c[15][i] for i in range(len(c[0])) if c[6][i] not in map]
        result = [base_id, sex, age, baby_age, in_days, hos_amount, main_diag_code, main_diag_name, other_diags_code,
                  other_oper_code, mdc_code, adrg_code, drg_code, oper_code, error_log, log]
        return  result
    # 有编码，有映射，原因待查
    def deal_map_matched2(self):  # 有编码和映射，原因待查
        c = self.code_match1()# 47个
        d = self.deal_map_matched1() # 46个

        base_id =[c[0][i] for i in range(len(c[0])) if c[0][i] not in d[0]]
        sex =[c[1][i] for i in range(len(c[0])) if c[0][i] not in d[0]]
        age =[c[2][i] for i in range(len(c[0])) if c[0][i] not in d[0]]
        baby_age =[c[3][i] for i in range(len(c[0])) if c[0][i] not in d[0]]
        in_days =[c[4][i] for i in range(len(c[0])) if c[0][i] not in d[0]]
        hos_amount =[c[5][i] for i in range(len(c[0])) if c[0][i] not in d[0]]
        main_diag_code =[c[6][i] for i in range(len(c[0])) if c[0][i] not in d[0]]
        main_diag_name =[c[7][i] for i in range(len(c[0])) if c[0][i] not in d[0]]
        other_diags_code =[c[8][i] for i in range(len(c[0])) if c[0][i] not in d[0]]
        other_oper_code =[c[9][i] for i in range(len(c[0])) if c[0][i] not in d[0]]
        mdc_code =[c[10][i] for i in range(len(c[0])) if c[0][i] not in d[0]]
        adrg_code =[c[11][i] for i in range(len(c[0])) if c[0][i] not in d[0]]
        drg_code =[c[12][i] for i in range(len(c[0])) if c[0][i] not in d[0]]
        oper_code =[c[13][i] for i in range(len(c[0])) if c[0][i] not in d[0]]
        error_log =[c[14][i] for i in range(len(c[0])) if c[0][i] not in d[0]]
        log =[c[15][i] for i in range(len(c[0])) if c[0][i] not in d[0]]
        result = [base_id,sex,age,baby_age,in_days,hos_amount,main_diag_code,main_diag_name,other_diags_code,other_oper_code,mdc_code,adrg_code,drg_code,oper_code,error_log,log]
        return result
        # 无mdc

    def deal_no_mdc(self):
        u = Ungroped()
        t = ToolXl()
        no_mdc = u.no_mdc()
        mdc_dic = t.dic_mdc_diag()
        adrg_dic = t.dic_adrg_diag()


        base_id = [no_mdc[0][i] for i in range(len(no_mdc[6]))  if no_mdc[6][i] not in mdc_dic[1] ]
        sex =[no_mdc[1][i] for i in range(len(no_mdc[6]))  if no_mdc[6][i] not in mdc_dic[1] ]
        age =[no_mdc[2][i] for i in range(len(no_mdc[6]))  if no_mdc[6][i] not in mdc_dic[1] ]
        baby_age =[no_mdc[3][i] for i in range(len(no_mdc[6]))  if no_mdc[6][i] not in mdc_dic[1] ]
        in_days =[no_mdc[4][i] for i in range(len(no_mdc[6]))  if no_mdc[6][i] not in mdc_dic[1] ]
        hos_amount =[no_mdc[5][i] for i in range(len(no_mdc[6]))  if no_mdc[6][i] not in mdc_dic[1] ]
        main_diag_code =[no_mdc[6][i] for i in range(len(no_mdc[6]))  if no_mdc[6][i] not in mdc_dic[1] ]
        main_diag_name =[no_mdc[7][i] for i in range(len(no_mdc[6]))  if no_mdc[6][i] not in mdc_dic[1] ]
        other_diags_code =[no_mdc[8][i] for i in range(len(no_mdc[6]))  if no_mdc[6][i] not in mdc_dic[1] ]
        other_oper_code =[no_mdc[9][i] for i in range(len(no_mdc[6]))  if no_mdc[6][i] not in mdc_dic[1] ]
        mdc_code =[no_mdc[10][i] for i in range(len(no_mdc[6]))  if no_mdc[6][i] not in mdc_dic[1] ]
        adrg_code =[no_mdc[11][i] for i in range(len(no_mdc[6]))  if no_mdc[6][i] not in mdc_dic[1] ]
        drg_code =[no_mdc[12][i] for i in range(len(no_mdc[6]))  if no_mdc[6][i] not in mdc_dic[1] ]
        oper_code =[no_mdc[13][i] for i in range(len(no_mdc[6]))  if no_mdc[6][i] not in mdc_dic[1] ]
        error_log =[no_mdc[14][i] for i in range(len(no_mdc[6]))  if no_mdc[6][i] not in mdc_dic[1] ]
        log =[no_mdc[15][i] for i in range(len(no_mdc[6]))  if no_mdc[6][i] not in mdc_dic[1] ]
        adrg_match = []

        for i in range(len(main_diag_code)):
            for j in range(len(adrg_dic[2])):
                if main_diag_code[i] == adrg_dic[2][j]:
                    adrg_match.append(adrg_dic[1][j])


        result = [base_id, sex, age, baby_age, in_days, hos_amount, main_diag_code, main_diag_name, other_diags_code,
              other_oper_code, mdc_code, adrg_code, drg_code, oper_code, error_log, log,adrg_match]
        return result





if __name__ == '__main__':
    d = DealData()
    print(d.deal_no_mdc()[16])






