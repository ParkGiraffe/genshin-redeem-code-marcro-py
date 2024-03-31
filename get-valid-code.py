from datetime import datetime
import pandas as pd

def get_duration(x):
  data = x.split()[4:7]
  if (len(data) > 1 and len(data[1]) < 3):
    data[1] = ('0' + data[1])
  str = '-'.join(data).replace(',', '')
  if 'Notes' in str :
    remove_idx = str.find('Notes:')
    result = str[:remove_idx]
  else:
    result = str
  return result

def get_validation(x):
  str_duration = get_duration(x)
  if 'indefinite' in str_duration :
    return True
  elif str_duration == '' : 
    return False
  else :
    obj_duration = datetime.strptime(str_duration, '%B-%d-%Y')
    obj_now = datetime.now()
    result = obj_duration > obj_now
    return result

def get_valid_rows(df):
  return df[df['Valid'] == True]

def get_valid_codes(url):
  parsing_data = pd.read_html(url) # 리스트
  original_df = pd.DataFrame(parsing_data[0]) # 판다스 데이터프레임
  original_df['Valid']=original_df.Duration.map(get_validation)

  valid_df = get_valid_rows(original_df)
  return valid_df.drop(['Duration'], axis=1).drop(['Valid'], axis=1)


def get_json(pd_data):
  return pd_data.to_json('validRedeemCodes.json',orient='records')


valid_codes = get_valid_codes('https://genshin-impact.fandom.com/wiki/Promotional_Code')
json = get_json(valid_codes)