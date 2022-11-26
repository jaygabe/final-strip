from typing import Optional, NoReturn
import pandas as pd
from datetime import datetime
from .models import USAFencingInfo


# convert yes/no into true/false
def yes_no_2_tf(yes_no: str) -> Optional[bool]:
    if yes_no in ['yes', 'Yes', 'YES']:
        return True
    elif yes_no in ['no', 'No', 'NO']:
        return False
    return None

# convert date format
def convert_date(orig_date: str) -> Optional[datetime]:
    if orig_date !='':
        return datetime.strptime(orig_date, '%m/%d/%Y').strftime('%Y-%m-%d')
    return None

# convert comp and non-comp to boolean
def convert_comp(comp_stat: str) -> Optional[bool]:
    if comp_stat == 'Competitive':
        return True
    elif comp_stat == 'Non-Competitive':
        return False
    return None

# Format data for SQL DB requirements
def extract_clean_data() -> pd.DataFrame:
    df=pd.read_csv('C:/Users/JustinD/py_projects/django/Fencing/finalstrip/journal/members04012022.csv',sep=',', keep_default_na=False).head(10)
    
    df['Birthdate verified'] = df['Birthdate verified'].apply(yes_no_2_tf)
    df['Club 1 ID#'] = df['Club 1 ID#'].map(lambda x: x if  x != '' else None)
    df['Club 2 ID#'] = df['Club 2 ID#'].map(lambda x: x if  x != '' else None)
    df['School ID#'] = df['School ID#'].map(lambda x: x if  x != '' else None)
    df['CheckEd'] = df['CheckEd'].apply(yes_no_2_tf)
    df['Competitive'] = df['Competitive'].apply(convert_comp)
    df['Expiration'] = df['Expiration'].apply(convert_date)
    df['US Citizen'] = df['US Citizen'].apply(yes_no_2_tf)
    df['Permanent Resident'] = df['Permanent Resident'].apply(yes_no_2_tf)
    df['Background Check Expires'] = df['Background Check Expires'].apply(convert_date)
    df['SafeSport Expires'] = df['SafeSport Expires'].apply(convert_date)
    df['Non-Comp Eligible'] = df['Non-Comp Eligible'].apply(yes_no_2_tf)
    df['Referee USA Year Foil'] = df['Referee USA Year Foil'].map(lambda x: x if  x != '' else None)
    df['Referee USA Year Epee'] = df['Referee USA Year Epee'].map(lambda x: x if  x != '' else None)
    df['Referee USA Year Saber'] = df['Referee USA Year Saber'].map(lambda x: x if  x != '' else None)
    df['Referee FIE Year Foil'] = df['Referee FIE Year Foil'].map(lambda x: x if  x != '' else None)
    df['Referee FIE Year Epee'] = df['Referee FIE Year Epee'].map(lambda x: x if  x != '' else None)
    df['Referee FIE Year Saber'] = df['Referee FIE Year Saber'].map(lambda x: x if  x != '' else None)

    return  df

# load data into django model
def load_membership_data() -> NoReturn:
    
    tmp_data = extract_clean_data()
    membership_info =[]
    for _, row in tmp_data.iterrows():
        membership_info.append(         
            USAFencingInfo(
                member_id = row['Member #'],
                last_name = row['Last Name'],
                first_name = row['First Name'],
                middle_name = row['Middle Name'],
                suffix = row['Suffix'],
                nickname = row['Nickname'],
                gender = row['Gender'],
                birthdate = row['Birthdate'],
                birthdate_verified = row['Birthdate verified'],
                division= row['Division'],
                club1 = row['Club 1 Name'],
                club1_abv = row['Club 1 Abbreviation'],
                club1_id = row['Club 1 ID#'],
                club2 = row['Club 2 Name'],
                club2_abv = row['Club 2 Abbreviation'],
                club2_id = row['Club 2 ID#'],
                school = row['School Name'],
                school_abv = row['School Abbreviation'],
                school_id = row['School ID#'],
                member_type = row['Member Type'],
                checked = row['CheckEd'],
                competitive = row['Competitive'],
                expiration = row['Expiration'],
                sabre = row['Saber'],
                epee = row['Epee'],
                foil = row['Foil'],
                us_citizen = row['US Citizen'],
                permanent = row['Permanent Resident'],
                country = row['Representing Country'],
                region = row['Region #'],
                background_expires = row['Background Check Expires'],
                safesport_expires = row['SafeSport Expires'],
                non_competitive = row['Non-Comp Eligible'],
                highest_ref_rating = row['Referee Highest USA Rating Earned'],
                us_ref_foil = row['Referee USA Rating Foil'],
                us_ref_foil_year = row['Referee USA Year Foil'],
                us_ref_epee = row['Referee USA Rating Epee'],
                us_ref_epee_year = row['Referee USA Year Epee'],
                us_ref_sabre = row['Referee USA Rating Saber'],
                us_ref_sabre_year = row['Referee USA Year Saber'],
                fie_ref_foil = row['Referee FIE Rating Foil'],
                fie_ref_foil_year = row['Referee FIE Year Foil'],
                fie_ref_epee = row['Referee FIE Rating Epee'],
                fie_ref_epee_year = row['Referee FIE Year Epee'],
                fie_ref_sabre = row['Referee FIE Rating Saber'],
                fie_ref_sabre_year = row['Referee FIE Year Saber'],
            )
        )
    USAFencingInfo.objects.all().delete()
    USAFencingInfo.objects.bulk_create(membership_info)
    