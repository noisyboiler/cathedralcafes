import datetime

data = [{
    'city': 'Bath & Wells',
    'geometry': 'POINT (-2.6419115066528320 51.2123948795493362)',
    'date_visited': None,
    'slug': 'cathedral-church-of-saint-andrew',
    'name': 'Cathedral Church of Saint Andrew',
    'latitude': -2.6419115066528320,
    'longitude': 51.2123948795493362,
    }, {
    'city': 'Birmingham',
    'geometry': 'POINT (-86.8024900000000059 33.5206608000000017)',
    'date_visited': None,
    'slug': 'cathedral-church-of-saint-philip',
    'name': 'Cathedral Church of Saint Philip.',
    'latitude': -86.8024900000000059,
    'longitude': 33.5206608000000017,
    }, {
    'city': 'Blackburn',
    'geometry': 'POINT (-2.4847106000000001 53.7500998000000010)',
    'date_visited': None,
    'slug': 'cathedral-church-of-blackburn-saint-mary-the-virgin',
    'name': 'Cathedral Church of Blackburn Saint Mary the Virgin',
    'latitude': -2.4847106000000001,
    'longitude': 53.7500998000000010,
    }, {
    'city': 'Bradford',
    'geometry': 'POINT (-1.7524421999999999 53.7938529999999986)',
    'date_visited': None,
    'slug': 'cathedral-church-of-st-peter',
    'name': 'Cathedral Church of St Peter',
    'latitude': -1.7524421999999999,
    'longitude': 53.7938529999999986,
    }, {
    'city': 'Bristol',
    'geometry': 'POINT (-2.5919023000000001 51.4553129000000027)',
    'date_visited': None,
    'slug': 'the-cathedral-church-of-the-holy-and-undivided-trinity',
    'name': 'The Cathedral Church of the Holy and Undivided Trinity',
    'latitude': -2.5919023000000001,
    'longitude': 51.4553129000000027,
    }, {
    'city': 'Cantebury',
    'geometry': 'POINT (1.0805172999999999 51.2772689000000028)',
    'date_visited': None,
    'slug': 'cathedral-and-metropolitical-church-of-christ-at-canterbury',
    'name': 'Cathedral and Metropolitical Church of Christ at Canterbury.',
    'latitude': 1.0805172999999999,
    'longitude': 51.2772689000000028,
    }, {
    'city': 'Carlisle',
    'geometry': 'POINT (-2.9335681999999998 54.8951210999999972)',
    'date_visited': None,
    'slug': 'cathedral-church-of-the-holy-and-undivided-trinity',
    'name': 'Cathedral Church of the Holy and Undivided Trinity',
    'latitude': -2.9335681999999998,
    'longitude': 54.8951210999999972,
    }, {
    'city': 'Chester',
    'geometry': 'POINT (-2.8950071999999998 53.1914575999999997)',
    'date_visited': None,
    'slug': 'cathedral-church-of-christ-and-the-blessed-virgin-mary',
    'name': 'Cathedral Church of Christ and the Blessed Virgin Mary',
    'latitude': -2.8950071999999998,
    'longitude': 53.1914575999999997,
    }, {
    'city': 'Chelmsford',
    'geometry': 'POINT (0.4697078000000000 51.7358142000000001)',
    'date_visited': None,
    'slug': 'cathedral-church-of-st-mary-the-virgin-st-peter-and-st-cedd',
    'name': 'Cathedral Church of St Mary the Virgin St Peter and St Cedd',
    'latitude': 0.4697078000000000,
    'longitude': 51.7358142000000001,
    }, {
    'city': 'Coventry',
    'geometry': 'POINT (-1.5126610000000000 52.4058374999999970)',
    'date_visited': None,
    'slug': 'cathedral-church-of-st-michael',
    'name': 'Cathedral Church of St. Michael',
    'latitude': -1.5126610000000000,
    'longitude': 52.4058374999999970,
    }, {
    'city': 'Chichester',
    'geometry': 'POINT (-0.7801777000000000 50.8366393000000016)',
    'date_visited': '2012-10-20',
    'slug': 'cathedral-church-of-the-holy-trinity',
    'name': 'Cathedral Church of the Holy Trinity',
    'latitude': -0.7801777000000000,
    'longitude': 50.8366393000000016,
    'summary': """Chichester,"the most typical English Cathedral",was a well
    equipped cafe,has it\'s own treasury and accommodates one of our most
    famous composers.""",
    'blurb': """On the river Lavant,just beneath the South Downs
(and conveniently opposite a House of Frasier) we have an 11th century
church where a bishop sits rather comfortably. In this Sussex city with it's
Roman and Anglo-Saxon and Norman footnotes,we have a tidy little cathedral.

Structural embarrassments and natural disasters feature richly in The Cathedral
Church of the Holy Trinity history. It's a small cathedral that stands out
amongst all others in our CofE; the bell tower of this cathedral is separated
completely from the church itself!

Furthermore Philip Arthur Larkin was inspired to write a poem about a tomb
here. Some of Holst is here. It has a striking green copper roof! There is
only one other medieval cathedral visible from the sea. There are numerous
treasures (most notable to us the Roman mosaic) and the cafe is most competent
with excellent staff and a fantastic little garden. Plus this is a live music
venue that also hosts exhibitions. And at the base of the spire nest Peregrine
Falcons. Small church maybe, but continues to be important."""
    }, {
    'city': 'Derby',
    'geometry': 'POINT (-1.4756419999999999 52.9218992999999998)',
    'date_visited': None,
    'slug': 'cathedral-church-of-all-saints',
    'name': 'Cathedral Church of All Saints',
    'latitude': -1.4756419999999999,
    'longitude': 52.9218992999999998,
    }, {
    'city': 'Durham',
    'geometry': 'POINT (-1.5596051000000000 54.7786923000000030)',
    'date_visited': None,
    'slug': 'cathedral-church-of-christ-blessed-mary-the-virgin-and-st-\
    cuthbert-of-durham',
    'name': ' Cathedral Church of Christ Blessed Mary the Virgin and St \
    Cuthbert of Durham',
    'latitude': -1.5596051000000000,
    'longitude': 54.7786923000000030,
    }, {
    'city': 'Ely',
    'geometry': 'POINT (0.2597859000000000 52.3994489999999971)',
    'date_visited': None,
    'slug': 'cathedral-church-of-the-holy-and-undivided-trinity',
    'name': 'Cathedral Church of the Holy and Undivided Trinity',
    'latitude': 0.2597859000000000,
    'longitude': 52.3994489999999971,
    }, {
    'city': 'Exeter',
    'geometry': 'POINT (-3.5336170000000000 50.7218000000000018)',
    'date_visited': datetime.datetime(2012, 5, 12),
    'slug': 'cathedral-church-of-saint-pete',
    'name': 'Cathedral Church of Saint Pete',
    'latitude': -3.5336170000000000,
    'longitude': 50.7218000000000018,
    'summary': """Exeter cathedral has the cafe that other churches dream of!
Some surprising  treasures,stunning features,some bodies of note and a few
stories to tell.""",
    'blurb': """This was a day out that took all the Cathedral Cafe adventurers
a little by surprise. Apprehensive of the 8am train from London and the 3 hour
ride west,being greeted by glorious sunshine and a truly magnificent church on
a delightful village green immediately banished the journey to the back of our
minds.

Stand-out feature: The Cafe! With it's vaulted roof,stained glass windows,
immaculate garden, great food,great tea and great service. But don't spend your
entire visit drinking their tea. On a nice day ensure you leave time to soak up
the atmosphere and the hustle and bustle all around the church.

Must-Dos: Appreciate the twin towers,Hickery Dickery Dock,sledging flag.""",
    }, {
    'city': 'Gibraltar',
    'geometry': 'POINT (-5.3532522000000000 36.1449106000000029)',
    'date_visited': None,
    'slug': 'cathedral-of-the-holy-trinity-gibraltar',
    'name': 'Cathedral of the Holy Trinity Gibraltar',
    'latitude': -5.3532522000000000,
    'longitude': 36.1449106000000029,
    }, {
    'city': 'Gloucester',
    'geometry': 'POINT (-2.2486698999999999 51.8667425000000009)',
    'date_visited': None,
    'slug': 'cathedral-church-of-st-peter-and-the-holy-and-indivisible-\
    trinity',
    'name': 'Cathedral Church of St Peter and the Holy and Indivisible \
    Trinity',
    'latitude': -2.2486698999999999,
    'longitude': 51.8667425000000009,
    }, {
    'city': 'Guildford',
    'geometry': 'POINT (-0.5702912000000000 51.2364188000000027)',
    'date_visited': '2014-03-09',
    'slug': 'cathedral-church-of-the-holy-spirit',
    'name': 'Cathedral Church of the Holy Spirit',
    'latitude': -0.5702912000000000,
    'longitude': 51.2364188000000027,
    }, {
    'city': 'Hereford',
    'geometry': 'POINT (-2.7175467000000002 52.0559921999999986)',
    'date_visited': None,
    'slug': 'cathedral-church-of-blessed-virgin-mary-and-st-ethelbert',
    'name': 'Cathedral Church of Blessed Virgin Mary and St Ethelbert',
    'latitude': -2.7175467000000002,
    'longitude': 52.0559921999999986,
    }, {
    'city': 'Leicester',
    'geometry': 'POINT (-1.1295191000000000 52.6347704000000007)',
    'date_visited': None,
    'slug': 'cathedral-church-of-st-martin',
    'name': 'Cathedral Church of St. Martin',
    'latitude': -1.1295191000000000,
    'longitude': 52.6347704000000007,
    }, {
    'city': 'Lichfield',
    'geometry': 'POINT (-1.8223586000000001 52.6835558000000006)',
    'date_visited': None,
    'slug': 'cathedral-church-of-the-blessed-virgin-mary-and-st-chad',
    'name': 'Cathedral Church of the Blessed Virgin Mary and St Chad',
    'latitude': -1.8223586000000001,
    'longitude': 52.6835558000000006,
    }, {
    'city': 'Lincoln',
    'geometry': 'POINT (-0.4264058000000000 53.1811650000000000)',
    'date_visited': '2011-05-24',
    'slug': 'cathedral-church-of-the-blessed-virgin-mary',
    'name': 'Cathedral Church of the Blessed Virgin Mary',
    'latitude': -0.4264058000000000,
    'longitude': 53.1811650000000000,
    'summary': """Lincoln was a small,comfortable cafe,a feast of architecture,
holdiing treasure and stories... but was light on dead people.""",
    'blurb': """An architectural treat,to which we should thank Bishop Hugh, who
was quite a popular chap back in the late 1100's. By far the most important
figure-head Lincoln Cathedral has seen and he will be disappointed to be
automatically disqualified from the Dead Person category simply because of his
career choice. His zeal for the beauty of 'the house of God' led to decades of,
in cathedral terms,outrageous and sumptuous architecture.

Built on a hill to be closer to the clouds,with 1000 years of history, this
building stands out amongst Cathedrals.

Must-Dos: Roof tour,Magna Carta,Imp.""",
}, {
    'city': 'Liverpool',
    'geometry': 'POINT (-2.9778383000000002 53.4107765999999984)',
    'date_visited': None,
    'slug': 'cathedral-church-of-christ',
    'name': 'Cathedral Church of Christ',
    'latitude': -2.9778383000000002,
    'longitude': 53.4107765999999984,
    }, {
    'city': 'London',
    'geometry': 'POINT (-0.1262362000000000 51.5001523999999975)',
    'date_visited': None,
    'slug': 'cathedral-church-of-paul-the-apostle',
    'name': 'Cathedral Church of Paul the Apostle',
    'latitude': -0.1262362000000000,
    'longitude': 51.5001523999999975,
    }, {
    'city': 'Manchester',
    'geometry': 'POINT (-2.2343765000000002 53.4807125000000028)',
    'date_visited': None,
    'slug': 'the-cathedral-and-collegiate-church-of-st-mary-st-denys-\
    and-st-george-in-manchester',
    'name': 'The Cathedral and Collegiate Church of St Mary St Denys \
    and St George in Manchester',
    'latitude': -2.2343765000000002,
    'longitude': 53.4807125000000028,
    }, {
    'city': 'Newcastle',
    'geometry': 'POINT (-1.6129165000000001 54.9778403999999981)',
    'date_visited': None,
    'slug': 'the-cathedral-church-of-st-nicholas-newcastle-upon-tyne',
    'name': 'The Cathedral Church of St Nicholas Newcastle upon Tyne',
    'latitude': -1.6129165000000001,
    'longitude': 54.9778403999999981,
    }, {
    'city': 'Norwich',
    'geometry': 'POINT (1.2993494000000001 52.6281013999999985)',
    'date_visited': None,
    'slug': 'cathedral-church-of-the-holy-and-undivided-trinity',
    'name': 'Cathedral Church of the Holy and Undivided Trinity',
    'latitude': 1.2993494000000001,
    'longitude': 52.6281013999999985,
    'blurb': """In medieval Norwich this was not a popular church. Prior to
the Norman invasion, Norwich was a happy-go-lucky little Anglo-Saxon town
with happy people,many quaint little churches and a thriving marketplace -
Tombland. Herbert de Losinga's bullish Norman planning then set the cat amongst
the pigeons.

A relatively quick build,1096 - 1145,the church required the demolition of the
towns marketplace,two churches and a few houses. This was not long after 80 or
so houses and 25 hectares of land were lost to the build of the Norman's
castle. The church split the town in two,quite literally. On one side was the
French Borough of Norman immigrants and on the other,the good,honest,
hard-working Anglo-Saxon folk - understandably quite bitter!

Out of this hotbed of dissent a beautiful Norman cathedral was crafted. This
is England's most complete Norman cathedral. Bar the replacement of the wooden
roof and spire with material more tollerant to large-scale fire,this is the
church that the first monks prayed in. The unpopular priory continued to exist
for around 400 years,when they voluntarily left.

To put events into perspective,this priory was so unpopular Norwich became the
only English city to be excommunicated by the Pope following the riot of 1272.

The church is stunning. At completion it had the longest nave in England,
highest spire and largest cloisters. It does have the largest collection of
bosses in Christendom. And at the time of our visit,it's own maze. Tombland is
now a lovely cathedral precinct and the modern cafe stands our amongst it's
contemporaries.

Must dos: find original wall paintings,decipher some bosses,go to the cafe.""",
    }, {
    'city': 'Oxford',
    'geometry': 'POINT (-1.2558838000000001 51.7522791999999967)',
    'date_visited': None,
    'slug': 'cathedral-church-of-christ',
    'name': 'Cathedral Church of Christ',
    'latitude': -1.2558838000000001,
    'longitude': 51.7522791999999967,
    }, {
    'city': 'Peterborough',
    'geometry': 'POINT (-0.2437337000000000 52.5702460999999985)',
    'date_visited': None,
    'slug': 'cathedral-church-of-st-peter-st-paul-and-st-andrew',
    'name': 'Cathedral Church of St Peter St Paul and St Andrew',
    'latitude': -0.2437337000000000,
    'longitude': 52.5702460999999985,
    }, {
    'city': 'Portsmouth',
    'geometry': 'POINT (-1.0911626999999999 50.7989136999999999)',
    'date_visited': None,
    'slug': 'cathedral-church-of-st-thomas-of-canterbury',
    'name': 'Cathedral Church of St Thomas of Canterbury',
    'latitude': -1.0911626999999999,
    'longitude': 50.7989136999999999,
    }, {
    'city': 'Ripon & Leeds',
    'geometry': 'POINT (-1.5242118000000000 54.1387805000000029)',
    'date_visited': None,
    'slug': 'the-cathedral-church-of-st-peter-st-wilfrid',
    'name': ' The Cathedral Church of St. Peter & St. Wilfrid',
    'latitude': -1.5242118000000000,
    'longitude': 54.1387805000000029,
    }, {
    'city': 'Rochester',
    'geometry': 'POINT (0.5037320000000000 51.3897894999999991)',
    'date_visited': '2011-12-04',
    'slug': 'cathedral-church-of-christ-and-the-blessed-virgin-mary',
    'name': 'Cathedral Church of Christ and the Blessed Virgin Mary',
    'latitude': 0.5037320000000000,
    'longitude': 51.3897894999999991,
    'summary': """Rochester Cathedral is a fine Norman,has a famous
mouse,has a really old clock and has roots with one of our most famous
writers.""",
    'blurb': """England's second oldest Cathedral,in its smallest diocese,
this intimate church in central Rochester has over 1400 years of history
and was cheated out of one of England's greatest dead people.

King Ethelbert of Kent gave the go-ahead for construction in 604 and a
choir school from that day still sings. But the only physical evidence of
the Saxon church are the foundation stones; today's church mostly shows
what happened when the Normans pitched-up and Bishop Gundulf got building;
he created what is commonly cited as England's finest Norman church.

Must-Dos: Tea at the cafe,Kent Bell,Dickens.""",
    }, {
    'city': 'St Albans',
    'geometry': 'POINT (-0.3338920000000000 51.7515300000000025)',
    'date_visited': None,
    'slug': 'cathedral-and-abbey-church-of-st-alban',
    'name': 'Cathedral and Abbey Church of St Alban',
    'latitude': -0.3338920000000000,
    'longitude': 51.7515300000000025,
    }, {
    'city': 'St Edmundsbury & Ipswich',
    'geometry': 'POINT (1.1556721999999999 52.0593085000000002)',
    'date_visited': None,
    'slug': 'cathedral-church-of-st-james',
    'name': 'Cathedral Church of St James',
    'latitude': 1.1556721999999999,
    'longitude': 52.0593085000000002,
    }, {
    'city': 'Salisbury',
    'geometry': 'POINT (-1.7976262999999999 51.0673989000000006)',
    'date_visited': None,
    'slug': 'cathedral-of-saint-mary',
    'name': 'Cathedral of Saint Mary',
    'latitude': -1.7976262999999999,
    'longitude': 51.0673989000000006,
    }, {
    'city': 'Sheffield',
    'geometry': 'POINT (-1.4647953000000000 53.3830547999999965)',
    'date_visited': None,
    'slug': 'cathedral-church-of-st-peter-and-st-paul',
    'name': 'Cathedral Church of St Peter and St Paul',
    'latitude': -1.4647953000000000,
    'longitude': 53.3830547999999965,
    }, {
    'city': 'Isle Of Man',
    'geometry': 'POINT (-4.5480559999999999 54.2361069999999970)',
    'date_visited': None,
    'slug': 'cathedral-church-of-st-german',
    'name': 'Cathedral Church of St German',
    'latitude': -4.5480559999999999,
    'longitude': 54.2361069999999970,
    }, {
    'city': 'Southwark',
    'geometry': 'POINT (-0.0820877000000000 51.4834479000000016)',
    'date_visited': None,
    'slug': 'cathedral-and-collegiate-church-of-st-saviour-and-st-mary-overie',
    'name': 'Cathedral and Collegiate Church of St. Saviour and St. Mary \
    Overie',
    'latitude': -0.0820877000000000,
    'longitude': 51.4834479000000016,
    }, {
    'city': 'Southwell & Nottingham',
    'geometry': 'POINT (-1.1491718000000000 52.9551147000000029)',
    'date_visited': None,
    'slug': 'cathedral-and-parish-church-of-the-blessed-virgin-mary',
    'name': 'Cathedral and Parish Church of the Blessed Virgin Mary',
    'latitude': -1.1491718000000000,
    'longitude': 52.9551147000000029,
    }, {
    'city': 'Truro',
    'geometry': 'POINT (-5.0507023000000002 50.2629522000000009)',
    'date_visited': None,
    'slug': 'cathedral-church-of-the-blessed-virgin-mary',
    'name': 'Cathedral Church of the Blessed Virgin Mary',
    'latitude': -5.0507023000000002,
    'longitude': 50.2629522000000009,
    }, {
    'city': 'Wakefield',
    'geometry': 'POINT (-1.4990969999999999 53.6829650000000029)',
    'date_visited': None,
    'slug': 'cathedral-church-of-all-saints',
    'name': 'Cathedral Church of All Saints',
    'latitude': -1.4990969999999999,
    'longitude': 53.6829650000000029,
    }, {
    'city': 'Winchester',
    'geometry': 'POINT (-1.3165036999999999 51.0629403000000011)',
    'date_visited': None,
    'slug': 'cathedral-church-of-the-holy-trinity-and-of-st-peter-\
    and-st-paul-and-of-st-swithun',
    'name': 'Cathedral Church of the Holy Trinity and of St Peter \
    and St Paul and of St Swithun',
    'latitude': -1.3165036999999999,
    'longitude': 51.0629403000000011,
    }, {
    'city': 'Worcester',
    'geometry': 'POINT (-2.2235320000000001 52.1920347000000007)',
    'date_visited': None,
    'slug': 'cathedral-church-of-christ-and-the-blessed-virgin-mary',
    'name': 'Cathedral Church of Christ and the Blessed Virgin Mary',
    'latitude': -2.2235320000000001,
    'longitude': 52.1920347000000007,
    }, {
    'city': 'York',
    'geometry': 'POINT (-1.0822855000000000 53.9577018000000024)',
    'date_visited': None,
    'slug': 'cathedral-and-metropolitical-church-\of-st-peter',
    'name': 'Cathedral and Metropolitical Church of St Peter',
    'latitude': -1.0822855000000000,
    'longitude': 53.9577018000000024,
    },
]
