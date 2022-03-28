"""Aqara iot enums."""

from dataclasses import dataclass
from enum import IntEnum


class AuthType(IntEnum):
    """Aqara Cloud Auth Type."""
    # Aqara账号授权:0、项目授权:1、虚拟账号授权:2
    AQARA_SMART_HOME = 0
    PROJECT = 1
    VIRTUAL = 2



AQARA_OAUTH2_AUTHORIZE = "/v3.0/open/authorize"

# 获取访问令牌
AQARA_OAUTH2_ACCESS_TOKEN = "/v3.0/open/access_token"


class AqaraCloudOpenAPIEndpoint:
    """Aqara Cloud Open API Endpoint."""

    #"/v3.0/open/api"

    # 中国大陆
    CHINA = "https://open-cn.aqara.com"
    # CHINA = "https://developer-test.aqara.com"

    # 美国
    AMERICA = "https://open-usa.aqara.com"

    # 韩国
    COREA = "https://open-kr.aqara.com"

    # 俄罗斯
    RUSSIA = "https://open-ru.aqara.com"

    # 欧洲
    EUROPE = "https://open-ger.aqara.com"



# PATH_CHINA = "https://open-cn.aqara.com"

#
PATH_OPEN_API = "/v3.0/open/api"
PATH_AUTH     = "/v3.0/open/authorize"
PATH_ACCESS_TOKEN = "/v3.0/open/access_token"

DEFAULT_APP_ID = '933393548471640064440ec2'
DEFAULT_APP_KEY = '07cps5et7s812bjlxyylffrvjp3vowoe'
DEFAULT_KEY_ID = 'K.933393548853321728'




#develop 
# DEFAULT_APP_ID = '948907588893974528e53aac'
# DEFAULT_APP_KEY = 'gchwjfo48nd0da9d3nlne8iblxorbyzl'
# DEFAULT_KEY_ID = 'K.948907589003026432'


# DEFAULT_APP_ID = '941380790062239744112522'
# DEFAULT_APP_KEY = 'tqvq2ol7va9v8u2w518qxedqxvx0e46i'
# DEFAULT_KEY_ID = 'K.941380790108377088'




EMPTY_PATH = ''

@dataclass
class Country:
    """Describe a supported country."""

    name: str
    country_code: str
    endpoint: str = AqaraCloudOpenAPIEndpoint.EUROPE


AQARA_COUNTRIES = [
    Country("Afghanistan", "93", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Albania", "355", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Algeria", "213", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("American Samoa", "1-684", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Andorra", "376", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Angola", "244", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Anguilla", "1-264", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Antarctica", "672", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Antigua and Barbuda", "1-268", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Argentina", "54", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Armenia", "374", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Aruba", "297", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Australia", "61", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Austria", "43", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Azerbaijan", "994", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Bahamas", "1-242", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Bahrain", "973", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Bangladesh", "880", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Barbados", "1-246", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Belarus", "375", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Belgium", "32", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Belize", "501", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Benin", "229", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Bermuda", "1-441", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Bhutan", "975", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Bolivia", "591", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Bosnia and Herzegovina", "387", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Botswana", "267", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Brazil", "55", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("British Indian Ocean Territory", "246", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("British Virgin Islands", "1-284", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Brunei", "673", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Bulgaria", "359", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Burkina Faso", "226", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Burundi", "257", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Cambodia", "855", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Cameroon", "237", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Canada", "1", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Capo Verde", "238", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Cayman Islands", "1-345", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Central African Republic", "236", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Chad", "235", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Chile", "56", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("China", "86", AqaraCloudOpenAPIEndpoint.CHINA),
    Country("Christmas Island", "61"),
    Country("Cocos Islands", "61"),
    Country("Colombia", "57", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Comoros", "269", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Cook Islands", "682", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Costa Rica", "506", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Croatia", "385", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Cuba", "53"),
    Country("Curacao", "599", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Cyprus", "357", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Czech Republic", "420", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country(
        "Democratic Republic of the Congo", "243", AqaraCloudOpenAPIEndpoint.EUROPE
    ),
    Country("Denmark", "45", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Djibouti", "253", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Dominica", "1-767", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Dominican Republic", "1-809", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("East Timor", "670", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Ecuador", "593", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Egypt", "20", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("El Salvador", "503", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Equatorial Guinea", "240", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Eritrea", "291", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Estonia", "372", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Ethiopia", "251", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Falkland Islands", "500", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Faroe Islands", "298", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Fiji", "679", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Finland", "358", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("France", "33", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("French Polynesia", "689", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Gabon", "241", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Gambia", "220", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Georgia", "995", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Germany", "49", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Ghana", "233", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Gibraltar", "350", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Greece", "30", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Greenland", "299", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Grenada", "1-473", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Guam", "1-671", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Guatemala", "502", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Guernsey", "44-1481"),
    Country("Guinea", "224"),
    Country("Guinea-Bissau", "245", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Guyana", "592", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Haiti", "509", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Honduras", "504", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Hong Kong", "852", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Hungary", "36", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Iceland", "354", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("India", "91"),
    Country("Indonesia", "62", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Iran", "98"),
    Country("Iraq", "964", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Ireland", "353", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Isle of Man", "44-1624"),
    Country("Israel", "972", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Italy", "39", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Ivory Coast", "225", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Jamaica", "1-876", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Japan", "81", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Jersey", "44-1534"),
    Country("Jordan", "962", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Kazakhstan", "7", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Kenya", "254", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Kiribati", "686", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Kosovo", "383"),
    Country("Kuwait", "965", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Kyrgyzstan", "996", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Laos", "856", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Latvia", "371", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Lebanon", "961", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Lesotho", "266", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Liberia", "231", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Libya", "218", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Liechtenstein", "423", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Lithuania", "370", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Luxembourg", "352", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Macao", "853", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Macedonia", "389", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Madagascar", "261", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Malawi", "265", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Malaysia", "60", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Maldives", "960", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Mali", "223", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Malta", "356", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Marshall Islands", "692", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Mauritania", "222", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Mauritius", "230", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Mayotte", "262", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Mexico", "52", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Micronesia", "691", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Moldova", "373", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Monaco", "377", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Mongolia", "976", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Montenegro", "382", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Montserrat", "1-664", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Morocco", "212", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Mozambique", "258", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Myanmar", "95", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Namibia", "264", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Nauru", "674", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Nepal", "977", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Netherlands", "31", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Netherlands Antilles", "599"),
    Country("New Caledonia", "687", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("New Zealand", "64", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Nicaragua", "505", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Niger", "227", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Nigeria", "234", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Niue", "683", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("North Korea", "850",AqaraCloudOpenAPIEndpoint.COREA),
    Country("Northern Mariana Islands", "1-670", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Norway", "47", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Oman", "968", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Pakistan", "92", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Palau", "680", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Palestine", "970", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Panama", "507", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Papua New Guinea", "675", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Paraguay", "595", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Peru", "51", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Philippines", "63", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Pitcairn", "64"),
    Country("Poland", "48", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Portugal", "351", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Puerto Rico", "1-787, 1-939", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Qatar", "974", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Republic of the Congo", "242", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Reunion", "262", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Romania", "40", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Russia", "7", AqaraCloudOpenAPIEndpoint.RUSSIA),
    Country("Rwanda", "250", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Saint Barthelemy", "590", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Saint Helena", "290"),
    Country("Saint Kitts and Nevis", "1-869", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Saint Lucia", "1-758", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Saint Martin", "590", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Saint Pierre and Miquelon", "508", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country(
        "Saint Vincent and the Grenadines", "1-784", AqaraCloudOpenAPIEndpoint.EUROPE
    ),
    Country("Samoa", "685", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("San Marino", "378", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Sao Tome and Principe", "239", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Saudi Arabia", "966", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Senegal", "221", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Serbia", "381", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Seychelles", "248", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Sierra Leone", "232", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Singapore", "65", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Sint Maarten", "1-721", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Slovakia", "421", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Slovenia", "386", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Solomon Islands", "677", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Somalia", "252", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("South Africa", "27", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("South Korea", "82", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("South Sudan", "211"),
    Country("Spain", "34", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Sri Lanka", "94", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Sudan", "249"),
    Country("Suriname", "597", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Svalbard and Jan Mayen", "4779", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Swaziland", "268", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Sweden", "46", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Switzerland", "41", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Syria", "963"),
    Country("Taiwan", "886", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Tajikistan", "992", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Tanzania", "255", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Thailand", "66", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Togo", "228", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Tokelau", "690", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Tonga", "676", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Trinidad and Tobago", "1-868", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Tunisia", "216", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Turkey", "90", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Turkmenistan", "993", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Turks and Caicos Islands", "1-649", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Tuvalu", "688", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("U.S. Virgin Islands", "1-340", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Uganda", "256", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Ukraine", "380", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("United Arab Emirates", "971", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("United Kingdom", "44", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("United States", "1", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Uruguay", "598", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Uzbekistan", "998", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Vanuatu", "678", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Vatican", "379", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Venezuela", "58", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Vietnam", "84", AqaraCloudOpenAPIEndpoint.AMERICA),
    Country("Wallis and Futuna", "681", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Western Sahara", "212", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Yemen", "967", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Zambia", "260", AqaraCloudOpenAPIEndpoint.EUROPE),
    Country("Zimbabwe", "263", AqaraCloudOpenAPIEndpoint.EUROPE),
]


