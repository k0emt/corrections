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
    race = data_line[53: 53 + 30].strip()
    sex = data_line[83: 83 + 30].strip()
    birth_date = data_line[113: 113 + 8].strip()

    offense_county = data_line[150: 150 + 4].strip()
    sentence_county = data_line[154: 154 + 4].strip()
    ncic_code = data_line[158: 158 + 4].strip()
    missouri_charge = data_line[162: 162 + 8].strip()
    offense_description = data_line[170: 170 + 74].strip()

    sentence_LengthYears = int(data_line[271: 271 + 4].strip())
    sentence_LengthMonths = int(data_line[275: 275 + 2].strip())
    sentence_LengthDays = int(data_line[277: 277 + 2].strip())

    if offense_county == '':
        offense_county = sentence_county

    output_document = doc_id + "," + race + "," + sex + "," + birth_date + "," + county_map[offense_county] + "," + \
                      county_map[sentence_county] + "," + ncic_code + "," + missouri_charge + "," + \
                      offense_description.replace(",", "") + "," + \
                      str((sentence_LengthYears + (sentence_LengthMonths / 12.0) + (sentence_LengthDays / 365.0)))

    try:
        return_value = output_document

    except UnicodeDecodeError:
        return_value = ''
        print >> sys.stderr, output_document

    return return_value


def display_header():
    print("doc_id,race,sex,birth_date,county_offense,county_sentence," +
          "ncic_code,missouri_charge,offense_description,sentence_length_years")


fileToOpen = DOC_OFFENDERS_INPUT_FILE

try:
    dataFile = open(fileToOpen, 'r')

    try:
        display_header()
        for dataLine in dataFile:
            print(parse_data_line(dataLine))

    finally:
        dataFile.close()

except IOError:
    print ("*** AN ERROR OCCURRED ***")
    pass

# print ('processing complete')
