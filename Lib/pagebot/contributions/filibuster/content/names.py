# -*- coding: UTF-8 -*-
#
"""
        history
        Names, first names, last names, foreign names.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
3.0.0    - split all the content into babycontents
evb        - note: only one dictionary named 'content' allowed per module
        this limitation is to speed up loading
4.0    - fixed a bug
3.0.2    -fixed names_japanese
3.0.3    - removed the german names from the names_last because it messes up certain things in pagebuster
evb
"""

__version__ = '4.0'



# ------------------------------------------------------
#    names
#
content = {
    'corporation_japanese': [
        u'<#name_japanese#><#p_corporateform#>',
        u'<#name_japanese#><#p_oldbiz_corporateform#>',
        u'<#name_japanese#>-<#name_japanese#><#p_corporateform#>',
        u'<#name_japanese#>-<#name_japanese#><#p_oldbiz_corporateform#>',
    ],
    'name': [
        u'<#names_first#> <#names_last#>',
        u'<#names_first#> <#names_last#>',
        u'<#names_first#> <#names_last#>',
        u'<#names_first#> <#names_last#>',
        u'<#names_first#> <#names_last#>',
        u'<#names_first#> <#names_initial_weighted#><#names_last#>',
        u'<#names_first#> <#names_initial_weighted#><#names_last#>',
        u'<#names_first#> <#names_last#>-<#names_last#>',
        u'<#names_first#> <#names_last#><#names_sx_weighted#>',
        u'<#names_initial_weighted#><#names_first#> <#names_last#>',
    ],
    'name_english': [
        'Gibbs', 'McLaren', 'Miller', 'Kwon', 'Little', 'Reage', 'Keaney', 'Muller', 'Chou',
        'Lamberti', 'Feldman', 'Michaelson', 'Cho', 'Davis', 'Hoffman', 'Marsh', 'Suh',
        'Fernandez', 'Fitzpatrick', 'Lin', 'Vanderbeck', 'Lee', 'Larssen','Vanderkeere',
        'Nobelman','Frime','Mustcado','Fnimble','Handersjen','Devries','Naaktgeboren',
        'McNaville','Stormby','Stromby','McMillen','Wrombley',u'Zóchi',u'Ångstrøm',
        'Jansen','Janson','Janssen','Hendrikson','Pwolley','Marinski','Rwandi',u'Pagréwski',
        u'Jønne',u'Vilår',
        'Kobayashi','Gallagher','Baker','Duvall','Vazquez','Murphy','Rutkowski','Vogel',
        'Meyerson','DiLorenzo','Schneider','Abbott','Marlowe','Kaye','Wynn','Davidoff',
        'Li','Smith','Lam','Martin','Brown','Roy','Tremblay','Lee','Gagnon','Wilson',
        'Clark','Johnson','White','Williams',u'Côté','Taylor','Campbell','Anderson',
        'Chan','Jones',u'Hernández','Visigoth',u'García',u'Martínez',u'González',
        u'López',u'Rodríguez',u'Pérez',u'Sánchez',u'Ramírez','Flores','Ruiz',
        'Dominguez','Fernandez',u'Muñoz','Gomez',u'Álvarez','Suarez','Torres','Cruz',
        'Martin','Reyes','Ortiz','Santos','Smith',u'Jiménez',
        'smith', 'mitchell', 'jones', 'kelly', 'williams', 'cook', 'taylor', 'carter', 'brown', 'richardson',
        'davies', 'bailey', 'evans', 'collins', 'wilson', 'bell', 'thomas', 'shaw', 'johnson', 'murphy', 'roberts',
        'miller', 'robinson', 'cox', 'thompson', 'richards', 'wright', 'khan', 'walker', 'marshall', 'white', 'anderson',
        'edwards', 'simpson', 'hughes', 'ellis', 'green', 'adams', 'hall', 'singh', 'lewis', 'begum', 'harris', 'wilkinson',
        'clarke', 'foster', 'patel', 'chapman', 'jackson', 'powell', 'wood', 'webb', 'turner', 'rogers', 'martin',
        'gray', 'cooper', 'mason', 'hill', 'ali', 'ward', 'hunt', 'morris', 'hussain', 'moore', 'campbell', 'clark',
        'matthews', 'lee', 'owen', 'king', 'palmer', 'baker', 'holmes', 'harrison', 'mills', 'morgan', 'barnes',
        'allen', 'knight', 'james', 'lloyd', 'scott', 'butler', 'phillips', 'russell', 'watson', 'barker', 'davis',
        'fisher', 'parker', 'stevens', 'price', 'jenkins', 'bennett', 'murray', 'young', 'dixon', 'griffiths', 'harvey',
    ],
    'name_french': [
        u'Jean',
        u'Jeanne',
        u'Philipe',
        u'Pierre',
        u'Jacques',
        u'François',
        u'Françoise',
    ],
    'name_female': [
        u'<#names_first_female#> <#names_last#>',
        u'<#names_first_female#> <#names_last#>',
        u'<#names_first_female#> <#names_last#>',
        u'<#names_first_female#> <#names_last#>',
        u'<#names_first_female#> <#names_last#>',
        u'<#names_first_female#> <#names_initial_weighted#><#names_last#>',
        u'<#names_first_female#> <#names_initial_weighted#><#names_last#>',
        u'<#names_first_female#> <#names_last#>-<#names_last#>',
        u'<#names_first_female#> <#names_last#><#names_sx_weighted#>',
        u'<#names_initial_weighted#><#names_first_male#> <#names_last#>',
    ],
    'name_german': [
        u'<#name_german_descent#><#name_german_base#><#name_german_limb#>',
        u'<#name_german_descent#><#name_german_base#><#name_german_heimat#>',
        u'<#name_german_descent#><#name_german_base#>',
    ],
    'name_german_base': [
        u'<#!^,name_german_px1#><#name_german_px2#><#name_german_px3#>',
        u'<#!^,name_german_noun#><#name_german_px3#><#name_german_heimat#><#name_german_px3#>',
        u'<#!^,name_german_noun#><#name_german_px3#>',
        u'<#!^,name_german_noun#><#name_german_px3#>',
        u'<#!^,name_german_noun#>',
    ],
    'name_german_descent': [
        'von ',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
    ],
    'name_german_heimat': [
        u'dorf',
        u'stadt',
        u'burg',
        u'bürg',
        u'stuhl',
        u'berg',
        u'tal',
        u'bach',
        u'teich',
        u'meer',
        u'see',
        u'hof',
        u'heim',
        u'land',
        u'mark',
        u'wald',
        u'mann',
        u'felt',
        u'acker',
    ],
    'name_german_limb': [
        u'hand',
        u'handt',
        u'kopf',
        u'bein',
        u'fuss',
        u'fuß',
        u'tropp',
        u'tropf',
        u'tröpf',
        u'strauss',
        u'mund',
        u'münd',
    ],
    'name_german_male': [
        u'<#name_german_title_male#><#name_german_base#>',
        u'<#name_german_title_male#><#name_german_base#>',
        u'<#name_german_title_male#><#name_german_base#>',
        u'<#names_first_absurdlyGerman#>-<#names_first_absurdlyGerman#> <#name_german_base#>',
        u'<#names_first_absurdlyGerman#> <#name_german_base#>',
        u'<#names_first_absurdlyGerman#> <#name_german_base#>',
        u'<#names_first_absurdlyGerman#> <#name_german_base#>-<#name_german_base#>',
        u'<#name_german_title_male#><#name_german_base#>-<#name_german_base#>',
        u'<#name_german_title_male#><#name_german_title_profession#><#name_german_base#>',
        u'<#name_german_title_male#><#name_german_title_profession#><#name_german_base#>',
        u'<#name_german_title_male#><#name_german_title_profession#><#name_german_base#>',
    ],
    'name_german_noun': [
        u'fisch',
        u'schrein',
        u'bäck',
        u'hack',
        u'metz',
        u'dort',
        u'doof',
        u'depp',
        u'arl',
        u'mann',
        u'eber',
        u'kuh',
        u'schaf',
        u'münch',
        u'müll',
        u'lietz',
        u'ditz',
        u'koch',
        u'bach',
        u'wagen',
        u'bauer',
        u'mauer',
        u'heim',
        u'tal',
        u'brand',
        u'aden',
        u'mack',
        u'mark',
        u'schuss',
        u'schrick',
        u'schwein',
        u'tier',
        u'hoh',
        u'hoch',
        u'tief',
        u'breier',
        u'birn',
        u'lager',
        u'schuh',
        u'stiefel',
        u'enkel',
        u'schu',
        u'schlie',
    ],
    'name_german_px1': [
        u'sch',
    ],
    'name_german_px2': [
        u'iff',
        u'off',
        u'uff',
        u'ripp',
        u'orl',
        u'ank',
        u'reck',
        u'isch',
        u'esch',
        u'osch',
        u'wank',
        u'ein',
        u'an',
        u'auf',
        u'euf',
    ],
    'name_german_px3': [
        'en',
        'er',
        'en',
        'er',
        'en',
        'er',
        'en',
        'er',
        'en',
        'er',
        'ler',
        'inger',
        'elen',
        'erler',
        'erle',
        'erli',
        'mann',
        'auer',
    ],
    'name_german_title_female': [
        'Frau ',
        '',
        '',
        '',
    ],
    'name_german_title_male': [
        'Herr ',
        '',
        '',
        '',
    ],
    'name_german_title_profession': [
        'Doktor ',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
    ],
    'name_japanese': [
        '<#name_japanese_px#><#name_japanese_sx#>',
        '<#name_japanese_px#><#name_japanese_sx#><#name_japanese_sx#>',
        '<#name_japanese_px#><#name_japanese_sx#><#name_japanese_sx#>',
        '<#name_japanese_px#><#name_japanese_sx#><#name_japanese_sx#><#name_japanese_sx#>',
    ],
    'name_japanese_px': [
        'Sun',
        'San',
        'Son',
        'Su',
        'So',
        'Sa',
        'Yo',
        'Ya',
        'Ka',
        'Ko',
        'Mi',
        'Ma',
        'Ta',
        'To',
        'Ti',
    ],
    'name_japanese_sx': [
        'yi',
        'yo',
        'ya',
        'yu',
        'yan',
        'ki',
        'ka',
        'ko',
        'kan',
        'bi',
        'ban',
        'so',
        'san',
        'ta',
        'to',
        'ti',
        'shi',
        'sha',
        'sho',
        'tsu',
        'tsi',
        'hi',
        'ha',
        'ho',
        'mi',
        'ma',
        'mo',
    ],
    'name_male': [
        u'<#names_first_male#> <#names_last#>',
        u'<#names_first_male#> <#names_last#>',
        u'<#names_first_male#> <#names_last#>',
        u'<#names_first_male#> <#names_last#>',
        u'<#names_first_male#> <#names_last#>',
        u'<#names_first_male#> <#names_initial_weighted#><#names_last#>',
        u'<#names_first_male#> <#names_initial_weighted#><#names_last#>',
        u'<#names_first_male#> <#names_last#>-<#names_last#>',
        u'<#names_first_male#> <#names_last#><#names_sx_weighted#>',
        u'<#names_initial_weighted#><#names_first_male#> <#names_last#>',
    ],
    'name_somewhiteguy': [
        u'<#names_first_patrician#> <#names_initial_weighted#><#names_last_patrician#>',
        u'<#names_first_patrician#> <#names_initial_weighted#><#names_last_patrician#><#names_sx_weighted#>',
        u'<#names_first_patrician#> <#names_last_patrician#> <#names_last_patrician#><#names_sx_weighted#>',
        u'<#names_last_patrician#> <#names_initial_weighted#><#names_last_patrician#><#names_sx_weighted#>',
        u'<#names_initial_weighted#><#names_last_patrician#> <#names_last_patrician#><#names_sx_weighted#>',
        u'<#names_initial_weighted#><#names_first_patrician#> <#names_last_patrician#><#names_sx_weighted#>',
    ],
    'names_first': [
        u'<#names_first_male#>',
        u'<#names_first_female#>',
    ],
    'names_first_absurdlyBritish': [
        'Nigel',
        'Simon',
        'Cecil',
        'Jeremy',
        'Alastair',
        'Chesterton',
        'Oscar',
        'Augustus',
        'Isambard',
        'Morris',
        'Kingsley',
        'Neville',
    ],
    'names_first_absurdlyGerman': [
        'Jochen',
        'Achim',
        'Karl',
        'Adolf',
        'Heinz',
        'Klaus',
        'Hans',
        'Helmut',
        'Erich',
        'Gunther',
        'Brunhilda',
        'Edeltraut',
    ],
    'names_first_female': [
        'Jennifer',
        'Claudia',
        'Amy',
        'Erin',
        'Siobhan',
        'Susan',
        'Patricia',
        'Mary',
        'Elizabeth',
        'Nan',
        'Rosemary',
        'Meghan',
        'Leigh',
        'Bethany',
        'Justine',
        'Isabel',
        'Kirsten',
        'Ingeborg',
        'Petra',
        'Josie',
        'May',
        'Phoebe',
        'Zoe',
        'Karla',
        'Helen',
        'Theresa',
        'Tina',
        'Ellen',
        'Dara',
        'Penny',
        'Eloise',
        'Courtney',
        'Carmen',
        'Anna',
        'Daphne',
        'Laura',
        'Karen',
        'Bridget',
        'Sandra',
        'Emily',
        'Madeleine',
        'Tricia',
        'Kate',
        'Liz',
        'Jen',
        'Andrea',
        'Connie',
        'Lynn',
        'Thisbe',
    ],
    'names_first_male': [
        'Bill',
        'David',
        'Sasha',
        'Charles',
        'Michael',
        'Ted',
        'Eugene',
        'Victor',
        'Tomasso',
        'Giovanni',
        'Kurt',
        'Marc',
        'Brad',
        'Philip',
        'Franco',
        'Paul',
        'Irwin',
        'Torben',
        'Erik',
        'Petr',
        'Maarten',
        'Jasper',
        'Michiel',
        'Isaac',
        'Patrick',
        'Alexander',
        'Martin',
        'Raoul',
        'Carl',
        'Clifford',
        'Nigel',
        'Ian',
        'Ross',
        'Walter',
        'Scott',
        'Marcus',
        'Craig',
        'Dieter',
        'George',
        'Warren',
        'Peter',
        'Rob',
        'Tyler',
        'Greg',
        'Arch',
        'Bob',
        'James',
        'Alan',
        'Jeremy',
        'Miles',
        'Graham',
        'Stuart',
    ],
    'names_first_patrician': [
        'Bill',
        'David',
        'Charles',
        'Michael',
        'Eugene',
        'Brad',
        'Philip',
        'Paul',
        'Patrick',
        'Alexander',
        'Martin',
        'Clifford',
        'Ross',
        'Walter',
        'Scott',
        'Craig',
        'George',
        'Warren',
        'Peter',
        'Robert',
        'Tyler',
        'Greg',
        'Bob',
        'James',
        'Alan',
        'Stewart',
        'Walter',
        'Ted',
        'Ronald',
        'Gerald',
        'Richard',
        'Dick',
        'Lyndon',
        'Dwight',
        'John',
        'Burton',
        'Eustus',
        'Hollings',
        'Morgan',
        'Earl',
        'Felix',
        'Anthony',
        'Daniel',
        'Everett',
        'Chad',
    ],
    'names_first_purewhitetrash': [
        'Cletus',
        'Dallas',
        'Shasta',
        'Billy Rae',
        'Booker',
        'Jimbo',
        'Dee Dee',
        'Tiffany',
        'Kimberly',
        'Brittany',
    ],
    'names_initial_weighted': [
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        'A. ',
        'B. ',
        'C. ',
        'D. ',
        'E. ',
        'F. ',
        'G. ',
        'H. ',
        'J. ',
        'L. ',
        'M. ',
        'N. ',
        'P. ',
        'R. ',
        'S. ',
        'T. ',
        'V. ',
        'W. ',
    ],
    'names_last': [
        u'<#^,name_english#>',
        u'<#^,name_english#>',
        u'<#^,name_english#>',
        u'<#^,name_english#>',
        u'<#^,name_english#>',
        u'<#^,name_english#>',
        u'<#^,name_french#>',
        u'<#^,name_japanese#>',
        u'<#^,name_german#>',
    ],
    'names_last_absurdlyBritish': [
        'Balliol',
        'St. James',
        'St. John-Smythe',
        'Warburton',
        'Welby',
        'Northmore',
        'Pugh',
        'Sinclair',
    ],
    'names_last_patrician': [
        'Davenport',
        'Archer',
        'Bourne',
        'Whitney',
        'White',
        'Sterling',
        'Calder',
        'Stern',
        'Markham',
        'Tate',
        'Caldecott',
        'Davies',
        'Fitzsimmons',
        'Vanderpool',
        'Morgan',
        'Fisher',
        'Carnegie',
        'Ryan',
        'Jennings',
        'Dunbar',
        'Emerson',
        'Bryant',
        'Stanley',
        'Sinclair',
        'Forbes',
        'Rowe',
        'Lawson',
        'Upton',
        'Palmer',
        'Adams',
        'Clark',
        'Knox',
        'Walters',
        'Carson',
        'Parham',
        'Mills',
        'Riley',
        'Bushnell',
        'Dupont',
        'Harrison',
        'Kennerley',
        'Johnson',
        'MacArthur',
        'Acheson',
        'Winslow',
        'Price',
        'Harper',
        'Sloane',
        'Polk',
        'Parker',
        'Franklin',
        'Blockland',
        'Johns',
        'Foster',
    ],
    'names_px_scientific': [
        'Prof. ',
        'Dr. ',
    ],
    'names_sx': [
        ', Jr.',
        ', Jr.',
        ', Jr.',
        ' III',
        ' III',
        ' IV',
    ],
    'names_sx_weighted': [
        '',
        '',
        '',
        '',
        '',
        u'<#names_sx#>',
    ],
        }

