

import shutil

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


for line in datalines(cancer_ids):
  cancer_id, cancer_name = line.split(' ')
  print('downloading', cancer_id, cancer_name)
  csv_download_url, csv_local_path = url_path_format(cancer_id, cancer_name)
  download_state_cancer_csv(csv_download_url, csv_local_path)
  # break


