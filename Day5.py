# Day 5 - Lists

games = ['League Of Legends', 'Mega Bonk', 'Bindng Of Isaac', '2XKO', 'Guilty Gear', 'Overwatch', 'Marvel Rivals']
print(games)
print(len(games))
firstGame = games[0]
middleGame = games[3]
lastGame = games[6]
print(firstGame + ', ' + middleGame + ', ' + lastGame)

mixedDataTypes = ['name', 44, 188, 'single', 'Antartica']
print(mixedDataTypes)

itCompanies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(itCompanies)
print(itCompanies[0] + ', ' + itCompanies[3] + ', ' + itCompanies[6])
itCompanies.pop(5)
print(itCompanies)
itCompanies.append('Bing')
itCompanies.insert(2, 'Firefox')
print(itCompanies)
# itCompanies.pop(3)
# msUpper = 'microsoft'.upper()
# itCompanies.insert(3, msUpper)
print(itCompanies)
doesExist = 'Facebook' in itCompanies
print(doesExist)

# itCompanies.sort()
# print(itCompanies)
# itCompanies.sort(reverse=True)
# print(itCompanies)
itNoMid = itCompanies[0:3] + itCompanies[5:7]
print(itNoMid)

itCompanies.remove('Facebook')
print(itCompanies)
itCompanies.pop(3)
itCompanies.pop(5)
print(itCompanies)

itCompanies.clear()
print(itCompanies)
del itCompanies

frontEnd = ['HTML', 'CSS', 'JS', 'React', 'Redux']
backEnd = ['Node', 'Express', 'MongoDB']

webTech = frontEnd + backEnd
print(webTech)
variableFullStack = webTech.copy()
variableFullStack.insert(5, 'Python')
variableFullStack.insert(6, 'SQL')
print(variableFullStack)

# Exercise Lvl 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print('Min & Max ages are 19 and 26')
print('Mean age is 24')
print('the range is: ', 26 - 19)
rangeAbs = abs(19-26)
print(rangeAbs)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

print(countries.index('Lesotho'))
firstCountries = countries[0:97]
secondCountries = countries[97:]
print(len(firstCountries))
print(len(secondCountries))

unpackTest = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
firstItem, secondItem, ThirdItem, *rest = unpackTest
print(firstItem)
print(secondItem)
print(ThirdItem)
print(rest)


