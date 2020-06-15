import pandas as pd
import configparser

cf = configparser.ConfigParser()
cf.read('config.ini', encoding="UTF-8")
xl = cf.get("xl_name1", 'xl')


# 获取数据类
class Ungroped():

    # 9999
    def nonomal(self):
        df = pd.read_excel(xl, keep_default_na=False)
        base_id = [df['BASE_ID'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '9999']
        sex = [df['SEX'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '9999']
        age = [df['AGE'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '9999']
        baby_age = [df['BABY_AGE'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '9999']
        in_days = [df['IN_DAYS'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '9999']
        hos_amount = [df['HOS_AMOUNT'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '9999']
        main_diag_code = [df['MAIN_DIAG_CODE'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '9999']
        main_diag_name = [df['MAIN_DIAG_NAME'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '9999']
        other_diags_code = [df['OTHER_DIAGS_CODE'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '9999']
        other_oper_code = [df['OTHER_OPER_CODE'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '9999']
        mdc_code = [df['MDC_CODE'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '9999']
        adrg_code = [df['ADRG_CODE'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '9999']
        drg_code = [df['DRG_CODE'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '9999']
        oper_code = [df['OPER_CODE'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '9999']
        error_log = [df['ERROR_LOG'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '9999']
        log = [df['LOG'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '9999']
        result = [base_id, sex, age, baby_age, in_days, hos_amount, main_diag_code, main_diag_name, other_diags_code,
                  other_oper_code, mdc_code, adrg_code, drg_code, oper_code, error_log, log]

        return result

    # 0000
    def non_diags(self):
        df = pd.read_excel(xl, keep_default_na=False)
        base_id = [df['BASE_ID'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '0000']
        sex = [df['SEX'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '0000']
        age = [df['AGE'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '0000']
        baby_age = [df['BABY_AGE'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '0000']
        in_days = [df['IN_DAYS'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '0000']
        hos_amount = [df['HOS_AMOUNT'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '0000']
        main_diag_code = [df['MAIN_DIAG_CODE'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '0000']
        main_diag_name = [df['MAIN_DIAG_NAME'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '0000']
        other_diags_code = [df['OTHER_DIAGS_CODE'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '0000']
        other_oper_code = [df['OTHER_OPER_CODE'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '0000']
        mdc_code = [df['MDC_CODE'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '0000']
        adrg_code = [df['ADRG_CODE'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '0000']
        drg_code = [df['DRG_CODE'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '0000']
        oper_code = [df['OPER_CODE'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '0000']
        error_log = [df['ERROR_LOG'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '0000']
        log = [df['LOG'][i] for i in range(len(df['BASE_ID'])) if df['DRG_CODE'][i] == '0000']
        result = [base_id, sex, age, baby_age, in_days, hos_amount, main_diag_code, main_diag_name, other_diags_code,
                  other_oper_code, mdc_code, adrg_code, drg_code, oper_code, error_log, log]

        return result

    # 无mdc
    def no_mdc(self):
        df = pd.read_excel(xl, keep_default_na=False)
        base_id = [df['BASE_ID'][i] for i in range(len(df['BASE_ID'])) if df['MDC_CODE'][i] == '']
        sex = [df['SEX'][i] for i in range(len(df['BASE_ID'])) if df['MDC_CODE'][i] == '']
        age = [df['AGE'][i] for i in range(len(df['BASE_ID'])) if df['MDC_CODE'][i] == '']
        baby_age = [df['BABY_AGE'][i] for i in range(len(df['BASE_ID'])) if df['MDC_CODE'][i] == '']
        in_days = [df['IN_DAYS'][i] for i in range(len(df['BASE_ID'])) if df['MDC_CODE'][i] == '']
        hos_amount = [df['HOS_AMOUNT'][i] for i in range(len(df['BASE_ID'])) if df['MDC_CODE'][i] == '']
        main_diag_code = [df['MAIN_DIAG_CODE'][i] for i in range(len(df['BASE_ID'])) if df['MDC_CODE'][i] == '']
        main_diag_name = [df['MAIN_DIAG_NAME'][i] for i in range(len(df['BASE_ID'])) if df['MDC_CODE'][i] == '']
        other_diags_code = [df['OTHER_DIAGS_CODE'][i] for i in range(len(df['BASE_ID'])) if df['MDC_CODE'][i] == '']
        other_oper_code = [df['OTHER_OPER_CODE'][i] for i in range(len(df['BASE_ID'])) if df['MDC_CODE'][i] == '']
        mdc_code = [df['MDC_CODE'][i] for i in range(len(df['BASE_ID'])) if df['MDC_CODE'][i] == '']
        adrg_code = [df['ADRG_CODE'][i] for i in range(len(df['BASE_ID'])) if df['MDC_CODE'][i] == '']
        drg_code = [df['DRG_CODE'][i] for i in range(len(df['BASE_ID'])) if df['MDC_CODE'][i] == '']
        oper_code = [df['OPER_CODE'][i] for i in range(len(df['BASE_ID'])) if df['MDC_CODE'][i] == '']
        error_log = [df['ERROR_LOG'][i] for i in range(len(df['BASE_ID'])) if df['MDC_CODE'][i] == '']
        log = [df['LOG'][i] for i in range(len(df['BASE_ID'])) if df['MDC_CODE'][i] == '']
        result = [base_id, sex, age, baby_age, in_days, hos_amount, main_diag_code, main_diag_name, other_diags_code,
                  other_oper_code, mdc_code, adrg_code, drg_code, oper_code, error_log, log]

        return result

    # 无adrg
    def no_adrg(self):
        df = pd.read_excel(xl, keep_default_na=False)
        base_id = [df['BASE_ID'][i] for i in range(len(df['BASE_ID'])) if
                   df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] == '']
        sex = [df['SEX'][i] for i in range(len(df['BASE_ID'])) if df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] == '']
        age = [df['AGE'][i] for i in range(len(df['BASE_ID'])) if df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] == '']
        baby_age = [df['BABY_AGE'][i] for i in range(len(df['BASE_ID'])) if
                    df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] == '']
        in_days = [df['IN_DAYS'][i] for i in range(len(df['BASE_ID'])) if
                   df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] == '']
        hos_amount = [df['HOS_AMOUNT'][i] for i in range(len(df['BASE_ID'])) if
                      df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] == '']
        main_diag_code = [df['MAIN_DIAG_CODE'][i] for i in range(len(df['BASE_ID'])) if
                          df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] == '']
        main_diag_name = [df['MAIN_DIAG_NAME'][i] for i in range(len(df['BASE_ID'])) if
                          df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] == '']
        other_diags_code = [df['OTHER_DIAGS_CODE'][i] for i in range(len(df['BASE_ID'])) if
                            df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] == '']
        other_oper_code = [df['OTHER_OPER_CODE'][i] for i in range(len(df['BASE_ID'])) if
                           df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] == '']
        mdc_code = [df['MDC_CODE'][i] for i in range(len(df['BASE_ID'])) if
                    df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] == '']
        adrg_code = [df['ADRG_CODE'][i] for i in range(len(df['BASE_ID'])) if
                     df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] == '']
        drg_code = [df['DRG_CODE'][i] for i in range(len(df['BASE_ID'])) if
                    df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] == '']
        oper_code = [df['OPER_CODE'][i] for i in range(len(df['BASE_ID'])) if
                     df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] == '']
        error_log = [df['ERROR_LOG'][i] for i in range(len(df['BASE_ID'])) if
                     df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] == '']
        log = [df['LOG'][i] for i in range(len(df['BASE_ID'])) if df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] == '']
        result = [base_id, sex, age, baby_age, in_days, hos_amount, main_diag_code, main_diag_name, other_diags_code,
                  other_oper_code, mdc_code, adrg_code, drg_code, oper_code, error_log, log]

        return result

    # 无drg
    def no_drg(self):
        df = pd.read_excel(xl, keep_default_na=False)
        base_id = [df['BASE_ID'][i] for i in range(len(df['BASE_ID'])) if
                   df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] != '' and df['DRG_CODE'][i] == '']
        sex = [df['SEX'][i] for i in range(len(df['BASE_ID'])) if
               df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] != '' and df['DRG_CODE'][i] == '']
        age = [df['AGE'][i] for i in range(len(df['BASE_ID'])) if
               df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] != '' and df['DRG_CODE'][i] == '']
        baby_age = [df['BABY_AGE'][i] for i in range(len(df['BASE_ID'])) if
                    df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] != '' and df['DRG_CODE'][i] == '']
        in_days = [df['IN_DAYS'][i] for i in range(len(df['BASE_ID'])) if
                   df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] != '' and df['DRG_CODE'][i] == '']
        hos_amount = [df['HOS_AMOUNT'][i] for i in range(len(df['BASE_ID'])) if
                      df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] != '' and df['DRG_CODE'][i] == '']
        main_diag_code = [df['MAIN_DIAG_CODE'][i] for i in range(len(df['BASE_ID'])) if
                          df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] != '' and df['DRG_CODE'][i] == '']
        main_diag_name = [df['MAIN_DIAG_NAME'][i] for i in range(len(df['BASE_ID'])) if
                          df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] != '' and df['DRG_CODE'][i] == '']
        other_diags_code = [df['OTHER_DIAGS_CODE'][i] for i in range(len(df['BASE_ID'])) if
                            df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] != '' and df['DRG_CODE'][i] == '']
        other_oper_code = [df['OTHER_OPER_CODE'][i] for i in range(len(df['BASE_ID'])) if
                           df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] != '' and df['DRG_CODE'][i] == '']
        mdc_code = [df['MDC_CODE'][i] for i in range(len(df['BASE_ID'])) if
                    df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] != '' and df['DRG_CODE'][i] == '']
        adrg_code = [df['ADRG_CODE'][i] for i in range(len(df['BASE_ID'])) if
                     df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] != '' and df['DRG_CODE'][i] == '']
        drg_code = [df['DRG_CODE'][i] for i in range(len(df['BASE_ID'])) if
                    df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] != '' and df['DRG_CODE'][i] == '']
        oper_code = [df['OPER_CODE'][i] for i in range(len(df['BASE_ID'])) if
                     df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] != '' and df['DRG_CODE'][i] == '']
        error_log = [df['ERROR_LOG'][i] for i in range(len(df['BASE_ID'])) if
                     df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] != '' and df['DRG_CODE'][i] == '']
        log = [df['LOG'][i] for i in range(len(df['BASE_ID'])) if
               df['MDC_CODE'][i] != '' and df['ADRG_CODE'][i] != '' and df['DRG_CODE'][i] == '']
        result = [base_id, sex, age, baby_age, in_days, hos_amount, main_diag_code, main_diag_name, other_diags_code,
                  other_oper_code, mdc_code, adrg_code, drg_code, oper_code, error_log, log]

        return result


if __name__ == '__main__':
    u = Ungroped()
    print(len(u.no_mdc()[0]))
