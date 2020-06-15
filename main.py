from workstaion2.deal_data import *
from workstaion2.get_data import *
import time

start = time.time()
t = ToolXl()
d = DealData()
u = Ungroped()

nonomal1 = d.deal_nonomal1()  # 住院时长超过60天
nonomal2 = d.deal_nonomal2()  # 费用异常
no_diags1 = d.deal_map_matched1()  # 无映射
no_diags2 = d.deal_map_matched2()  # 有编码有映射原因待查
no_diags3 = d.code_match2()  # 不是国临2.0编码
no_mdc = d.deal_no_mdc()  # 无mdc编码
no_adrg = u.no_adrg()  # 无adrg编码
no_drg = u.no_drg()  # 无drg编码

base_id_all = []
sex_all = []
age_all = []
baby_age_all = []
in_days_all = []
hos_amount_all = []
main_diag_code_all = []
main_diag_name_all = []
other_diags_code_all = []
other_oper_code_all = []
mdc_code_all = []
adrg_code_all = []
drg_code_all = []
oper_code_all = []
error_log_all = []
log_all = []
note_all = []
for i in range(len(nonomal1[0])):
    base_id_all.append(nonomal1[0][i])
    sex_all.append(nonomal1[1][i])
    age_all.append(nonomal1[2][i])
    baby_age_all.append(nonomal1[3][i])
    in_days_all.append(nonomal1[4][i])
    hos_amount_all.append(nonomal1[5][i])
    main_diag_code_all.append(nonomal1[6][i])
    main_diag_name_all.append(nonomal1[7][i])
    other_diags_code_all.append(nonomal1[8][i])
    other_oper_code_all.append(nonomal1[9][i])
    mdc_code_all.append(nonomal1[10][i])
    adrg_code_all.append(nonomal1[11][i])
    drg_code_all.append(nonomal1[12][i])
    oper_code_all.append(nonomal1[13][i])
    error_log_all.append(nonomal1[14][i])
    log_all.append(nonomal1[15][i])
    note_all.append('住院时长超过60天')
for i in range(len(nonomal2[0])):
    base_id_all.append(nonomal2[0][i])
    sex_all.append(nonomal2[1][i])
    age_all.append(nonomal2[2][i])
    baby_age_all.append(nonomal2[3][i])
    in_days_all.append(nonomal2[4][i])
    hos_amount_all.append(nonomal2[5][i])
    main_diag_code_all.append(nonomal2[6][i])
    main_diag_name_all.append(nonomal2[7][i])
    other_diags_code_all.append(nonomal2[8][i])
    other_oper_code_all.append(nonomal2[9][i])
    mdc_code_all.append(nonomal2[10][i])
    adrg_code_all.append(nonomal2[11][i])
    drg_code_all.append(nonomal2[12][i])
    oper_code_all.append(nonomal2[13][i])
    error_log_all.append(nonomal2[14][i])
    log_all.append(nonomal2[15][i])
    note_all.append('费用异常：住院费用/住院天数<5')
for i in range(len(no_diags1[0])):
    base_id_all.append(no_diags1[0][i])
    sex_all.append(no_diags1[1][i])
    age_all.append(no_diags1[2][i])
    baby_age_all.append(no_diags1[3][i])
    in_days_all.append(no_diags1[4][i])
    hos_amount_all.append(no_diags1[5][i])
    main_diag_code_all.append(' ')
    main_diag_name_all.append(no_diags1[7][i])
    other_diags_code_all.append(no_diags1[8][i])
    other_oper_code_all.append(no_diags1[9][i])
    mdc_code_all.append(no_diags1[10][i])
    adrg_code_all.append(no_diags1[11][i])
    drg_code_all.append(no_diags1[12][i])
    oper_code_all.append(no_diags1[13][i])
    error_log_all.append(no_diags1[14][i])
    log_all.append(no_diags1[15][i])
    note_all.append('无原始诊断编码到CHS分组方案编码映射')
for i in range(len(no_diags2[0])):
    base_id_all.append(no_diags2[0][i])
    sex_all.append(no_diags2[1][i])
    age_all.append(no_diags2[2][i])
    baby_age_all.append(no_diags2[3][i])
    in_days_all.append(no_diags2[4][i])
    hos_amount_all.append(no_diags2[5][i])
    main_diag_code_all.append(no_diags2[6][i])
    main_diag_name_all.append('')
    other_diags_code_all.append(no_diags2[8][i])
    other_oper_code_all.append(no_diags2[9][i])
    mdc_code_all.append(no_diags2[10][i])
    adrg_code_all.append(no_diags2[11][i])
    drg_code_all.append(no_diags2[12][i])
    oper_code_all.append(no_diags2[13][i])
    error_log_all.append(no_diags2[14][i])
    log_all.append(no_diags2[15][i])
    note_all.append('原始诊断编码不是国临2.0编码')
for i in range(len(no_diags3[0])):
    base_id_all.append(no_diags3[0][i])
    sex_all.append(no_diags3[1][i])
    age_all.append(no_diags3[2][i])
    baby_age_all.append(no_diags3[3][i])
    in_days_all.append(no_diags3[4][i])
    hos_amount_all.append(no_diags3[5][i])
    main_diag_code_all.append(no_diags3[6][i])
    main_diag_name_all.append(no_diags3[7][i])
    other_diags_code_all.append(no_diags3[8][i])
    other_oper_code_all.append(no_diags3[9][i])
    mdc_code_all.append(no_diags3[10][i])
    adrg_code_all.append(no_diags3[11][i])
    drg_code_all.append(no_diags3[12][i])
    oper_code_all.append(no_diags3[13][i])
    error_log_all.append(no_diags3[14][i])
    log_all.append(no_diags3[15][i])
    note_all.append('原始诊断编码不是国临2.0编码')
for i in range(len(no_mdc[0])):
    base_id_all.append(no_mdc[0][i])
    sex_all.append(no_mdc[1][i])
    age_all.append(no_mdc[2][i])
    baby_age_all.append(no_mdc[3][i])
    in_days_all.append(no_mdc[4][i])
    hos_amount_all.append(no_mdc[5][i])
    main_diag_code_all.append(no_mdc[6][i])
    main_diag_name_all.append(no_mdc[7][i])
    other_diags_code_all.append(no_mdc[8][i])
    other_oper_code_all.append(no_mdc[9][i])
    mdc_code_all.append(no_mdc[10][i])
    adrg_code_all.append(no_mdc[11][i])
    drg_code_all.append(no_mdc[12][i])
    oper_code_all.append(no_mdc[13][i])
    error_log_all.append(no_mdc[14][i])
    log_all.append(no_mdc[15][i])
    note_all.append('该病例的诊断编码无对应的MDC组,但能入到' + "--" + no_mdc[16][i] + "--" + 'ADRG组')
for i in range(len(no_adrg[0])):
    base_id_all.append(no_adrg[0][i])
    sex_all.append(no_adrg[1][i])
    age_all.append(no_adrg[2][i])
    baby_age_all.append(no_adrg[3][i])
    in_days_all.append(no_adrg[4][i])
    hos_amount_all.append(no_adrg[5][i])
    main_diag_code_all.append(no_adrg[6][i])
    main_diag_name_all.append(no_adrg[7][i])
    other_diags_code_all.append(no_adrg[8][i])
    other_oper_code_all.append(no_adrg[9][i])
    mdc_code_all.append(no_adrg[10][i])
    adrg_code_all.append(no_adrg[11][i])
    drg_code_all.append(no_adrg[12][i])
    oper_code_all.append(no_adrg[13][i])
    error_log_all.append(no_adrg[14][i])
    log_all.append(no_adrg[15][i])
    note_all.append('可以入到该病例的MDC组，但是其缺少入到相应ADRG组的手术编码(OTHER_OPER_CODE中)，所以无法入ADRG组')
for i in range(len(no_drg[0])):
    base_id_all.append(no_drg[0][i])
    sex_all.append(no_drg[1][i])
    age_all.append(no_drg[2][i])
    baby_age_all.append(no_drg[3][i])
    in_days_all.append(no_drg[4][i])
    hos_amount_all.append(no_drg[5][i])
    main_diag_code_all.append(no_drg[6][i])
    main_diag_name_all.append(no_drg[7][i])
    other_diags_code_all.append(no_drg[8][i])
    other_oper_code_all.append(no_drg[9][i])
    mdc_code_all.append(no_drg[10][i])
    adrg_code_all.append(no_drg[11][i])
    drg_code_all.append(no_drg[12][i])
    oper_code_all.append(no_drg[13][i])
    error_log_all.append(no_drg[14][i])
    log_all.append(no_drg[15][i])
    note_all.append('该病例入的ADRG组没有细化到DRG组')

dic = {}
dic['BASE_ID'] = base_id_all
dic['SEX'] = sex_all
dic['AGE'] = age_all
dic['BABY_AGE'] = baby_age_all
dic['IN_DAYS'] = in_days_all
dic['HOS_AMOUNT'] = hos_amount_all
dic['MAIN_DIAG_CODE'] = main_diag_code_all
dic['MAIN_DIAG_NAME'] = main_diag_name_all
dic['OTHER_DIAGS_CODE'] = other_diags_code_all
dic['OTHER_OPER_CODE'] = other_oper_code_all
dic['MDC_CODE'] = mdc_code_all
dic['ADRG_CODE'] = adrg_code_all
dic['DRG_CODE'] = drg_code_all
dic['OPER_CODE'] = oper_code_all
dic['ERROR_LOG'] = error_log_all
dic['LOG'] = log_all
dic['NOTE'] = note_all
df = pd.DataFrame(dic)
df.to_excel('xl/result1.xlsx')
end = time.time()
print(end - start)
