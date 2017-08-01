

import shutil

import csv

import pandas as pd
# from pylon import datalines
def datalines(data, sample=None):
  '''返回一段文字中有效的行(非空行, 且不以注释符号开头)'''
  ret = []
  for l in data.splitlines():
    line = l.strip()
    if line and not line.startswith('#'):
      ret.append(line)
  if sample:
    return ret[:sample]
  else:
    return ret

import requests
session = requests.Session()





cancer_ids = '''
    # <select name="cancer" id="cancer" onchange="updateAges();updateSexes();">
    # 001 AllCancerSites
    071 Bladder
    076 Brain&ONS
    055 Breast(Female)
    400 Breast(Female_in_situ)
    057 Cervix
    # 516 Childhood_(Ages_under_15_AllSites)   # 选 Age > 65 则没有这项
    # 515 Childhood_(Ages_under_20_AllSites)   # 选 Age > 65 则没有这项
    020 Colon&Rectum
    017 Esophagus
    072 Kidney&RenalPelvis
    090 Leukemia
    035 Liver&BileDuct
    047 Lung&Bronchus
    053 Melanoma_of_the_Skin
    086 NonHodgkinLymphoma
    003 Oral_Cavity&Pharynx
    061 Ovary
    040 Pancreas
    # 066 Prostate   # 前列腺
    018 Stomach
    080 Thyroid
    058 Uterus(Corpus&Uterus_NOS)
'''




def download_state_cancer_csv(url, save_path):
  r = session.get(url, stream=True)
  if r.status_code == 200:
    with open(save_path, 'wb') as f:
      r.raw.decode_content = True
      shutil.copyfileobj(r.raw, f)
    print('save file {} done'.format(save_path))


def url_path_format(cancer_id, cancer_name):

  # stateFIPS=99: US by County
  # race=07: White Non-Hispanic
  # age=157: 65+

  # url_sample = 'https://statecancerprofiles.cancer.gov/incidencerates/index.php?stateFIPS=99&cancer=076&race=07&sex=2&age=157&type=incd&sortVariableName=rate&sortOrder=default#results'
  # csv_sample = 'https://statecancerprofiles.cancer.gov/incidencerates/index.php?stateFIPS=99&cancer=076&race=07&sex=2&age=157&type=incd&sortVariableName=rate&sortOrder=desc&output=1'
  csv_tmpl = 'https://statecancerprofiles.cancer.gov/incidencerates/index.php?stateFIPS=99&cancer={}&race=07&sex=2&age=157&type=incd&sortVariableName=rate&sortOrder=desc&output=1'
  csv_download_url = csv_tmpl.format(cancer_id)
  csv_local_path = 'white_non_hispanic_female_gt65_{}_{}_all_counties.csv'.format(cancer_id, cancer_name)
  return csv_download_url, csv_local_path



def exec_fetch_data():
  for line in datalines(cancer_ids):
    cancer_id, cancer_name = line.split(' ')
    print('downloading', cancer_id, cancer_name)
    csv_download_url, csv_local_path = url_path_format(cancer_id, cancer_name)
    download_state_cancer_csv(csv_download_url, csv_local_path)
    # break

# exec_fetch_data()




# from collections import namedtuple


def fix_state_cancer_csv(path):
  with open(path, encoding='cp1252') as f:
    content = f.read()
    # print([len(block) for block in content.split('\n\n')])
    content = max(content.split('\n\n'), key=lambda x: len(x))
    with open('fixed_'+path, 'w', encoding='utf-8') as output:
      output.write(content)


def exec_fix_all_csv():
  csv_paths = '''
    white_non_hispanic_female_gt65_003_Oral_Cavity&Pharynx_all_counties.csv
    white_non_hispanic_female_gt65_017_Esophagus_all_counties.csv
    white_non_hispanic_female_gt65_018_Stomach_all_counties.csv
    white_non_hispanic_female_gt65_020_Colon&Rectum_all_counties.csv
    white_non_hispanic_female_gt65_035_Liver&BileDuct_all_counties.csv
    white_non_hispanic_female_gt65_040_Pancreas_all_counties.csv
    white_non_hispanic_female_gt65_047_Lung&Bronchus_all_counties.csv
    white_non_hispanic_female_gt65_053_Melanoma_of_the_Skin_all_counties.csv
    white_non_hispanic_female_gt65_055_Breast(Female)_all_counties.csv
    white_non_hispanic_female_gt65_057_Cervix_all_counties.csv
    white_non_hispanic_female_gt65_058_Uterus(Corpus&Uterus_NOS)_all_counties.csv
    white_non_hispanic_female_gt65_061_Ovary_all_counties.csv
    white_non_hispanic_female_gt65_071_Bladder_all_counties.csv
    white_non_hispanic_female_gt65_072_Kidney&RenalPelvis_all_counties.csv
    white_non_hispanic_female_gt65_076_Brain&ONS_all_counties.csv
    white_non_hispanic_female_gt65_080_Thyroid_all_counties.csv
    white_non_hispanic_female_gt65_086_NonHodgkinLymphoma_all_counties.csv
    white_non_hispanic_female_gt65_090_Leukemia_all_counties.csv
    white_non_hispanic_female_gt65_400_Breast(Female_in_situ)_all_counties.csv
  '''
  for path in datalines(csv_paths):
    fix_state_cancer_csv(path)








def clean_csv(path, cancer_site):
  df = pd.read_csv(path)
  df = df[1:]  # drop first row "US (SEER+NPCR) §"
  df['State_and_County'] = df['County'].map(lambda x: x.split('(')[0] if '(' in x else x)
  df.insert(0, 'State', df['State_and_County'].map(lambda x: x.split(', ')[1] if x != 'District of Columbia' else 'District of Columbia'))
  df.insert(0, 'Cancer_Site', cancer_site)
  df['County'] = df['State_and_County'].map(lambda x: x.split(', ')[0] if x != 'District of Columbia' else 'District of Columbia')
  df = df[df['Average Annual Count'].apply(lambda x: x.isdigit() and int(x) >= 5)]
  return df


def exec_merge_csv():
  fixed_csv_paths = '''
    fixed_white_non_hispanic_female_gt65_003_Oral_Cavity&Pharynx_all_counties.csv
    fixed_white_non_hispanic_female_gt65_017_Esophagus_all_counties.csv
    fixed_white_non_hispanic_female_gt65_018_Stomach_all_counties.csv
    fixed_white_non_hispanic_female_gt65_020_Colon&Rectum_all_counties.csv
    fixed_white_non_hispanic_female_gt65_035_Liver&BileDuct_all_counties.csv
    fixed_white_non_hispanic_female_gt65_040_Pancreas_all_counties.csv
    fixed_white_non_hispanic_female_gt65_047_Lung&Bronchus_all_counties.csv
    fixed_white_non_hispanic_female_gt65_053_Melanoma_of_the_Skin_all_counties.csv
    fixed_white_non_hispanic_female_gt65_055_Breast(Female)_all_counties.csv
    fixed_white_non_hispanic_female_gt65_057_Cervix_all_counties.csv
    fixed_white_non_hispanic_female_gt65_058_Uterus(Corpus&Uterus_NOS)_all_counties.csv
    fixed_white_non_hispanic_female_gt65_061_Ovary_all_counties.csv
    fixed_white_non_hispanic_female_gt65_071_Bladder_all_counties.csv
    fixed_white_non_hispanic_female_gt65_072_Kidney&RenalPelvis_all_counties.csv
    fixed_white_non_hispanic_female_gt65_076_Brain&ONS_all_counties.csv
    fixed_white_non_hispanic_female_gt65_080_Thyroid_all_counties.csv
    fixed_white_non_hispanic_female_gt65_086_NonHodgkinLymphoma_all_counties.csv
    fixed_white_non_hispanic_female_gt65_090_Leukemia_all_counties.csv
    fixed_white_non_hispanic_female_gt65_400_Breast(Female_in_situ)_all_counties.csv
  '''
  dfs = []
  for path in datalines(fixed_csv_paths):
    cancer_site = path.replace('fixed_white_non_hispanic_female_gt65', '')
    cancer_site = cancer_site.replace('_all_counties.csv', '')
    cancer_site = cancer_site[5:]
    print(cancer_site)
    df = clean_csv(path, cancer_site)
    dfs.append(df)


  result = pd.concat(dfs)
  result = result[list(dfs[0].keys())]
  result.to_csv('result2.csv')

