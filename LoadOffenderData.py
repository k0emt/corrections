# ReadFile.py
import json
import sys

# update this with the path and filename that points to where you extracted the file
DOC_OFFENDERS_INPUT_FILE = "fak930_first_200.txt"

county_map = {'ADAI': 'Adair',
              'ANDR': 'Andrew',
              'ATCH': 'Atchison',
              'AUDR': 'Audrain',
              'BARR': 'Barry',
              'BART': 'Barton',
              'BATE': 'Bates',
              'BENT': 'Benton',
              'BOLL': 'Bollinger',
              'BOON': 'Boone',
              'BUCH': 'Buchanan',
              'BUTL': 'Butler',
              'CALD': 'Caldwell',
              'CALL': 'Callaway',
              'CAMD': 'Camden',
              'CAPE': 'Cape Girardeau County',
              'CARR': 'Carroll',
              'CART': 'Carter',
              'CASS': 'Cass',
              'CEDA': 'Cedar',
              'CHAR': 'Chariton',
              'CHRI': 'Christian',
              'CLAR': 'Clark',
              'CLAY': 'Clay',
              'CLIN': 'Clinton',
              'COLE': 'Cole',
              'COOP': 'Cooper',
              'CRAW': 'Crawford',
              'DADE': 'Dade',
              'DALL': 'Dallas',
              'DAVI': 'Daviess',
              'DEKA': 'DeKalb',
              'DENT': 'Dent',
              'DOUG': 'Douglas',
              'DUNK': 'Dunklin',
              'FRAN': 'Franklin',
              'GASC': 'Gasconade',
              'GENT': 'Gensitey',
              'GREE': 'Greene',
              'GRUN': 'Grundy',
              'HARR': 'Harrison',
              'HENR': 'Henry',
              'HICK': 'Hickory',
              'HOLT': 'Holt',
              'HOWA': 'Howard',
              'HOWE': 'Howell',
              'IRON': 'Iron',
              'JACK': 'Jackson',
              'JASP': 'Jasper',
              'JEFF': 'Jefferson',
              'JOHN': 'Johnson',
              'KNOX': 'Knox',
              'LACL': 'Laclede',
              'LAFA': 'Lafayette',
              'LAWR': 'Lawrence',
              'LEWI': 'Lewis',
              'LINC': 'Lincoln',
              'LINN': 'Linn',
              'LIVI': 'Livingston',
              'MACO': 'Macon',
              'MADI': 'Madison',
              'MARE': 'Maries',
              'MARI': 'Marion',
              'MCDO': 'McDonald',
              'MERC': 'Mercer',
              'MILL': 'Miller',
              'MISS': 'Mississippi',
              'MONI': 'Moniteau',
              'MONR': 'Monroe',
              'MONT': 'Montgomery',
              'MORG': 'Morgan',
              'NEWM': 'New Madrid',
              'NEWT': 'Newton',
              'NODA': 'Nodaway',
              'OREG': 'Oregon',
              'OSAG': 'Osage',
              'OTST': 'Out-State',
              'OZAR': 'Ozark',
              'PEMI': 'Pemiscot',
              'PERR': 'Perry',
              'PETT': 'Pettis',
              'PHEL': 'Phelps',
              'PIKE': 'Pike',
              'PLAT': 'Platte',
              'POLK': 'Polk',
              'PULA': 'Pulaski',
              'PUTN': 'Putnam',
              'RALL': 'Ralls',
              'RAND': 'Randolph',
              'RAY': 'Ray',
              'REYN': 'Reynolds',
              'RIPL': 'Ripley',
              'SALI': 'Saline',
              'SCHU': 'Schuyler',
              'SCOL': 'Scotland',
              'SCOT': 'Scott',
              'SHAN': 'Shannon',
              'SHEL': 'Shelby',
              'STCH': 'St. Charles',
              'STCL': 'St. Clair',
              'STFR': 'St. Francois',
              'STEG': 'Ste. Genevieve',
              'STLC': 'St. Louis City',
              'STLO': 'St. Louis County',
              'STOD': 'Stoddard',
              'STON': 'Stone',
              'SULL': 'Sullivan',
              'TANE': 'Taney',
              'TEXA': 'Texas',
              'VERN': 'Vernon',
              'WARR': 'Warren',
              'WASH': 'Washington',
              'WAYN': 'Wayne',
              'WEBS': 'Webster',
              'WORT': 'Worth',
              'WRIG': 'Wright'
              }

def parse_data_line(data_line):
    doc_id = data_line[0:8]
    last_name = data_line[8: 8 + 18].strip()
    first_name = data_line[26: 26 + 12].strip()
    middle_name = data_line[38: 38 + 12].strip()
    suffix = data_line[50: 50 + 3].strip()
    race = data_line[53: 53 + 30].strip()
    sex = data_line[83: 83 + 30].strip()
    birth_date = data_line[113: 113 + 8].strip()

    offender_assigned_place = data_line[121: 121 + 8].strip()
    doc_location_function_flag = data_line[129: 129 + 1].strip()
    CauseNo = data_line[130: 130 + 20].strip()
    offense_county = data_line[150: 150 + 4].strip()
    sentence_county = data_line[154: 154 + 4].strip()
    ncic_code = data_line[158: 158 + 4].strip()
    missouri_charge = data_line[162: 162 + 8].strip()
    offense_description = data_line[170: 170 + 74].strip()
    completed_flag = data_line[244: 244 + 1].strip()
    CcCsInd = data_line[245: 245 + 2].strip()

    sentence_date = data_line[247: 247 + 8].strip()
    sentence_MaximumReleaseDate = data_line[255: 255 + 8].strip()
    sentence_MinimumReleaseDate = data_line[263: 263 + 8].strip()
    sentence_LengthYears = int(data_line[271: 271 + 4].strip())
    sentence_LengthMonths = int(data_line[275: 275 + 2].strip())
    sentence_LengthDays = int(data_line[277: 277 + 2].strip())
    sentence_ProbationDate = data_line[279: 279 + 8].strip()

    probation_Type = data_line[287: 287 + 3].strip()
    probation_TermYears = int(data_line[290: 290 + 4].strip())
    probation_TermMonths = int(data_line[294: 294 + 2].strip())
    probation_TermDays = int(data_line[296: 296 + 2].strip())

    if offense_county == '':
        offense_county = sentence_county

    output_document = {
        'docId': doc_id,
        'lastName': last_name,
        'firstName': first_name,
        'middleName': middle_name,
        'suffix': suffix,
        'race': race,
        'gender': sex,
        'birthDate': birth_date,
        'offenderAssignedPlace': offender_assigned_place,
        'DocLocFuncFlag': doc_location_function_flag,
        'CauseNo': CauseNo,
        'OffenseCounty': county_map[offense_county],
        'SentenceCounty': county_map[sentence_county],
        'NcicCode': ncic_code,
        'MissouriCharge': missouri_charge,
        'OffenseDescription': offense_description,
        'completed': completed_flag,
        'CcCsInd': CcCsInd,
        'sentenceDate': sentence_date,
        'sentenceMaximumReleaseDate': sentence_MaximumReleaseDate,
        'sentenceMinimumReleaseDate': sentence_MinimumReleaseDate,
        'sentenceLengthYears': sentence_LengthYears,
        'sentenceLengthMonths': sentence_LengthMonths,
        'sentenceLengthDays': sentence_LengthDays,
        'sentenceProbationDate': sentence_ProbationDate,
        'probationType': probation_Type,
        'probationTermYears': probation_TermYears,
        'probationTermMonths': probation_TermMonths,
        'probationTermDays': probation_TermDays}

    try:
        return_value = json.dumps(output_document)
    except UnicodeDecodeError:
        return_value = ''
        print >> sys.stderr, output_document

    return return_value

fileToOpen = DOC_OFFENDERS_INPUT_FILE

try:
    dataFile = open(fileToOpen, 'r')
    try:
        for dataLine in dataFile:

            print parse_data_line(dataLine)

    finally:
        dataFile.close()

except IOError:
    print ("*** AN ERROR OCCURRED ***")
    pass

# print ('processing complete')
