# -*- coding: utf-8 -*-
__author__ = 'pierregm'


from pymongo import MongoClient

from bson.json_util import (dumps, loads)


client = MongoClient()

db = client.strn_test_20150314

def loader(fname, cname):
    with open(fname, 'r') as f:
        txt = f.read()
    content = loads(txt)
    db.drop_collection(cname)
    collection = db[cname]
    collection.insert(content)
    print "Loading %i in collection '%s'" % (collection.count(), cname)
    return collection

if 0:
    people_collection = loader('people.json', 'people')
    bands_collection = loader('bands.json', 'bands')
    releases_collection = loader('releases.json', 'releases')

releases = [
{
    u'extra_artists': [{u'name': u'S\xe9bastien Trihan',
                        u'role': u'Artworks'}],
    u'labels': [{u'catno': 'STRN-35', u'name': 'La Souterraine'}],
    u'released': u'2015-01-07',
    u'title': u'Vol. 5',
    u'tracklist': [
        {u'artists': [{u'name': u'Sourdure'}],
         u'duration': u'03:30',
         u'position': 1,
         u'title': u'Bonsoir Belle Berg\xe8re'},
        {u'artists': [{u'name': u'Maud Octallinn'}],
         u'duration': u'01:49',
         u'position': 2,
         u'title': u'Super fi\xe8re sur mon bulldozer'},
        {u'artists': [{u'name': u'O'}],
         u'duration': u'05:00',
         u'position': 3,
         u'title': u'B\xe9bi'},
        {u'artists': [{u'name': u'T\xe9m\xe9 Tan'}],
         u'duration': u'01:53',
         u'position': 4,
         u'title': u'Motamo'},
        {u'artists': [{u'name': u'Silvain Vanot'}],
         u'duration': u'03:42',
         u'position': 5,
         u'title': u'Je suis le carnet de route'},
        {u'artists': [{u'name': u'Mehdi Zannad'}],
         u'duration': u'03:30',
         u'position': 6,
         u'title': u'Bagatelle'},
        {u'artists': [{u'name': u'Requin Chagrin'}],
         u'duration': u'02:57',
         u'position': 7,
         u'title': u'Ad\xe9la\xefde'},
        {u'artists': [{u'name': u'Marie Math\xe9matique'}],
         u'duration': u'02:25',
         u'position': 8,
         u'title': u'Sinon je serais autre chose'},
        {u'artists': [{u'name': u'France'}],
         u'duration': u'25:42',
         u'position': 9,
         u'title': u"Meltdown of Planet Earth (en public au Festival Humanist SK'14)"},
        {u'artists': [{u'name': u'Emmanuelle Parrenin'}],
         u'duration': u'03:57',
         u'position': 10,
         u'title': u'Innocence Light'}
      ]
},
{
    u"title": "mostLaPiNtape",
    u"label": [{u"catno": "STRN-36", u"name": u"la Souterraine"}],
    u"artist": u"Lapin",
    u"released": "2015-01-31",
    u"tracklist": [
        {u'duration': '03:15', u'position': 1, u'title': 'Cette fille'},
        {u'duration': '03:20',
         u'position': 2,
         u'title': "L'oeil dans le bleu du ciel"},
        {u'duration': '02:34', u'position': 3,
         u'title': 'Une paire de bras'},
        {u'duration': '04:15', u'position': 4, u'title': 'Coco'},
        {u'duration': '04:39', u'position': 5,
         u'title': 'Coeurs solitaires'},
        {u'duration': '03:12', u'position': 6,
         u'title': 'Le continent rose'},
        {u'duration': '04:44', u'position': 7,
         u'title': 'Ciel des nuits'},
        {u'duration': '03:43', u'position': 8, u'title': 'Petite fleur'},
        {u'duration': '03:14', u'position': 9, u'title': 'La nuit'},
        {u'duration': '04:48', u'position': 10,
         u'title': 'Les montagnes de sucre'}
    ]
},
{
    u"title": u"FLEGMATIC - Esprit de conquête, la mostla tape",
    u"labels": [{u"catno": "STRN-37", u"name": "la Souterraine"}],
    u"artist": u"Flegmatic",
    u"released": "2015-11-02",
    u"tracklist": [
        {u'duration': '05:28', u'position': 1, u'title': 'Rebecca',
         u"extra_artists": [
             {u"name": u"Michael Wookey",
              u"role": u"Production, Arrangements, Backing vocals"},
             {u"name": u"Marion Dinse",
              u"role": u"Backing vocals"}
         ]},
        {u'duration': '03:29', u'position': 2,
         u'title': 'B\xc3\xa9ziers',
         u"extra_artists": [
             {u"name": u"Ives Grimonperez",
              u"role": u"Production"},
             {u"name": u"Julien Bousquet",
              u"role": u"Bass, Guitar"},
             {u"name": u"Flavien Girard",
              u"role": u"Drums"},
             {u"name": u"Jean-Christophe Lacroix",
              u"role": u"Trumpet"},
             {u"name": u"Hélène Doudiès",
              u"role": u"Chorus"}
         ]},
        {u'duration': '05:48',
         u'position': 3,
         u'title': 'La nuit est une gorge chaude',
         u"extra_artists": [
             {u"name": u"Michael Wookey",
              u"role": u"Production, Arrangements, Backing vocals"},
             {u"name": u"Marion Dinse",
              u"name": u"Backing vocals"}
         ]
        },
        {u'duration': '03:51', u'position': 4, u'title': 'Peter Falk',
         u"extra_artists": [
             {u"name": u"Michael Wookey",
              u"role": u"Production, Arrangements, Backing vocals"},
             {u"name": u"Marion Dinse",
              u"name": u"Backing vocals"}
         ]},
        {u'duration': '03:44',
         u'position': 5,
         u'title': 'Anniversaire',
         u"extra_artists": [
             {u"name": u"Michael Wookey",
              u"role": u"Production, Arrangements, Backing vocals"},
             {u"name": u"Marion Dinse",
              u"name": u"Backing vocals"}
         ]},
        {u'duration': '03:26',
         u'position': 6,
         u'title': 'SOS',
         u"extra_artists": [
             {u"name": u"Michael Wookey",
              u"role": u"Production, Arrangements, Backing vocals"},
             {u"name": u"Marion Dinse",
              u"name": u"Backing vocals"}
         ]},
        {u'duration': '03:49',
         u'position': 7,
         u'title': "L'autoroute",
         u"extra_artists": [
             {u"name": u"Michael Wookey",
              u"role": u"Production, Arrangements, Backing vocals"},
             {u"name": u"Marion Dinse",
              u"name": u"Backing vocals"}
         ]},
        {u'duration': '03:29',
         u'position': 8,
         u'title': "L'Europe",
         u"extra_artists": [
             {u"name": u"Gilles Delès", u"role": u"Mixing"}]
        },
        {u'duration': '02:24',
         u'position': 9,
         u'title': 'Il est partout',
         u"extra_artists": [
             {u"name": u"Gilles Delès", u"role": u"Mixing"}]
        },
        {u'duration': '03:28', u'position': 10,
         u'title': 'Tu es venue me parler',
         u"extra_artists":[
            {u"name": u"Gilles Delès", u"role": u"Mixing"}
        ]}],
    u"notes":"""
Début 2012, je suis rentré chez moi, dans le Tarn, dans un état épouvantable. Je passais les mois qui suivirent, dans un état très stable de vide et de plénitude. Ni heureux, ni malheureux, j'expérimentais un genre de bouddhisme. Les journées étaient douces, lumineuses, rassurantes, égales et sans vent. Un changement de luminosité du jour pouvait me faire fondre en larmes. Incapable de me projeter dans l'avenir, j'essayais de me tenir à une distance raisonnable de toute forme d'engagement avec autrui.

Je touchais à une forme de bonheur parfait.

Et soudain ce fut évident : il ne me restait que quelques mois à vivre...
Je me suis mis à chanter des textes horribles d'une voix très douce, sur des petites mélodies, des petites bossa désinvoltes, à m'effondrer sur le piano en murmurant des chansons un peu connes, à écrire comme un type qui n'aurait plus aucun filtre (et plus de clopes au milieu de la nuit)... et mes obsessions pour les cartes topographiques, les viaducs autoroutiers, et l'auto-humiliation.

Bien que je n'ai jamais vraiment compris les partis-pris de l'anti-folk ou de l'anti-pop, je me suis dis que je faisais de l'anti-chanson. Puis, après bien des aventures, je suis allé chercher mon ami Michael Wookey, que j'accompagne au trombone avec les Hiddentracks depuis plus de trois ans, pour produire ce qui aurait dû être un EP de 6 titres dans son studio débordant d'orgues de collection et d'instruments qu'il trafique lui-même, EP auquel j'ai finalement ajouté Béziers enregistrée chez mon ami Ives en 2013, et une petite grappe de chansons enregistrées chez moi pour cette mostla-tape.

C'est un peu décousu, du coup. J'aime bien.

Thomas Boudineau AKA Flegmatic

Rebecca, Peter Falk, Anniversaire, S.O.S, La nuit est une gorge chaude, L'autoroute : produit par Michael Wookey, Octobre 2014.
Arrangements : Thomas Boudineau & Michael Wookey. Choeurs : Marion Dinse et Michael.

Béziers : produit par Ives Grimonprez, studio Apperte Recordings, Saint-Etienne, Avril 2013.
Avec Julien Bousquet, guitare et basse ; Flavien Girard, batterie ; Jean-Christophe Lacroix, trompette ; Hélène Doudiès, choeurs (montage choeurs : Gilles Delès).

L'Europe, Il est partout, Tu es venue me parler : enregistrées à la maison, à Albi, Décembre 2014. Mixées par Gilles Delès à Rethel, dans les Ardennes.
L'Europe et Tu es venue me parler auraient été un peu ternes sans la complicité de Ives Grimonprez dans l'écriture.

Masterisé par Gilles Delès, Janvier 2015.

photo de couverture © Phoebe Meyer // avant montage au scotch avec flegme

Plus d'infos : montanadiscount.tumblr.com/flegmatic

Merci Benjamin, Laurent, La Souterraine,
toute mon amitié pour Michael, Gilles, Ives, Mickaël, les Hiddentracks,
Marion, Hélène,
Phoebe, Laurent,
David, Marie, Laurent, Jasmina de Froggy's Delight
le Bleu Blanc Bar de Maison-Alfort,

Charlotte M.

Merci Richard Brautigan de m'avoir rendu le sourire... avant d'apprendre que tu t'étais flingué.
Le Flegmatic reviendra dans l'album En l'absence de ressources humaines.
"""
},
{
u"title": u"Degrad - MOSTLATAPE",
u"artist": u"Weli Noël",
u"released": "2015-02-28",
u"labels": [{u"catno": "STRN-37", u"name": u"la Souterraine"}],
u"tracklist": [{u'duration': '02:59',
                u'position': 1,
                u'title': 'Zoli zombi zoli fant\xc3\xb4me'},
               {u'duration': '03:27', u'position': 2,
                u'title': 'Comme une enveloppe'},
               {u'duration': '03:18', u'position': 3,
                u'title': 'La fluorescence'},
               {u'duration': '03:05', u'position': 4,
                u'title': 'Une maison'},
               {u'duration': '03:12', u'position': 5,
                u'title': 'La goyave'},
               {u'duration': '03:34',
                u'position': 6,
                u'title': 'La ros\xc3\xa9e si feuilles songes',
                u"extra_artists": [
                    {u"name": u"Alain Péters",
                     u"role": u"Composer"}
                ]},
               {u'duration': '03:49', u'position': 7,
                u'title': 'Cayenne',
                u"extra_artists": [
                    {u"name": u"Corentin Marot",
                     u"role": u"Soprano Sax"}
                ]},
               {u'duration': '03:47', u'position': 8,
                u'title': 'Fender benders'},
               {u'duration': '04:11',
                u'position': 9,
                u'title': 'Que font-ils en mon absence'},
               {u'duration': '01:23', u'position': 10,
                u'title': 'Le destin'}],
u"notes": """
Je me souviens d'un petit voyage sur l'Oyapock que j'ai fait avec W. depuis l’ouest de la Guyane. On allait chez lui. Il avait une maison en bois sur un terrain uniquement accessible par le fleuve. On allait arracher des mauvaises herbes et retourner un peu la terre pour semer. Et aussi, pour ma part, bouquiner dans le hamac. W. avait une barquette qu'il laissait flotter au dégrad de Saint-Georges, la bourgade principale de l'est. On a pris la barquette avec tout notre barda, dont ma guitare. La barquette était pourrie et l’eau s’infiltrait. Au milieu du fleuve, on a commencé d’écoper vivement, jusqu'à ce qu'on réalise l’imparable : on allait couler. J’ai regardé W. avec circonspection. Dans son regard, aucun signe de désespoir, mais au contraire, un amusement bonhomme. Alors j’ai ri. D’abord de voir W. s’enfoncer dans l’eau sans changer de position, assis sur sa planche, pagaie à la main et sourire en coin. J’ai ri aussi car je me trouvai d’un coup précieusement ridicule d’avoir compter rester sec. Enfin, j’étais heureux. Nos sacs de vêtements, le matériel de jardinage et ma guitare prenaient leur indépendance en une précaire flottaison. C'était bon de tout laisser faire. Puis de toute façon, sa ki pou'w la riviè pa ka chayé'y. La preuve en est qu’un piroguier brésilien nous a pris en cordée et que la grande rivière n’a pas emporté nos fardeaux dans ses flots.

Il faut aussi parler des animaux. Quelle stupeur charmante et un peu effrayante de voir les animaux de la forêt chez eux. On se sent vraiment vivre.

La folle nature, les siestes transpirantes, la liberté simple et la magie quotidienne sont les choses que j’aime mettre dans mes chansons.

J’ai enregistré un premier EP en 2009 (Une maison – Que font-ils en mon absence ?). Un single est sorti en 2010 (Fender benders en est la face b). Mon premier album voit le jour en ce début 2015. Dans cette Mostla tape figure une reprise de La rosée si feuilles songes d’Alain Péters, poète et musicien que j’admire.

Je chante et joue les guitares, les claviers et les percussions. Hélène Martin joue la contrebasse. Corentin Marot joue le saxophone soprano sur Cayenne. Les chansons ont été mixées et masterisées par Jaike Stambach, Vincent Mons et Rémi Salvador.
"""
},
{
u"title": u"LA mostla NÒVIA",
u"released": u"2015-03-11",
u"labels": [{u"catno": u"STRN-38", u"name": u"la Souterraine"}],
u"tracklist": [{u'artists': [{u'name': 'Jericho'}],
  u'duration': '09:59',
  u'position': 1,
  u'title': 'La Mantille / Dia me tu Catinel'},
 {u'artists': [{u'name': 'Toad'}],
  u'duration': '04:21',
  u'position': 2,
  u'title': 'Suite de bourr\xc3\xa9es: Païre maïre / I eron un i eron dos / Bourrée à Chabrier'},
 {u'artists': [{u'name': 'Faune'}],
  u'duration': '04:01',
  u'position': 3,
  u'title': 'Qui veut entendre une chanson'},
 {u'artists': [{u'name': 'La Cleda'}],
  u'duration': '08:59',
  u'position': 4,
  u'title': 'Lo vespre'},
 {u'artists': [{u'name': 'Le Verdouble'}],
  u'duration': '20:20',
  u'position': 5,
  u'title': 'Blanlhac le 22/04/14'},
 {u'artists': [{u'name': 'Violonneuses'}],
  u'duration': '11:18',
  u'position': 6,
  u'title': "Marches & bourr\xc3\xa9es:  : Marche de Noce d'Alfred Mouret / Nosferatu / Païre / N'ai tant / Bourrée coulée / Los chaumeilhos"},
 {u'artists': [{u'name': 'La Baracande'}],
  u'duration': '06:06',
  u'position': 7,
  u'title': 'Tout en me promenant'},
 {u'artists': [{u'name': u'Yann Gourdon',
                u'role': u'vielle à roue'},
               {u'name': u'Stéphane Mauchand',
                u'role': u'cornemuses 16p, 20p, 23p'}],
  u'duration': '04:31',
  u'position': 8,
  u'title': u'Scottishs: Tabadhadin / À table'},
 {u'artists': [{u'name': u'Jacques Puech',
                u'role': u'cabrette, chant'},
               {u'name': u'Yann Gourdon',
                u'role': u'vielle à roue'}],
  u'duration': '08:23',
  u'position': 9,
  u'title': 'La Can\xc3\xa7on'},
 {u'artists': [{u'name': u'Jacques Puech',
                u'role': u'cabrette'},
               {u'name': u'Yann Gourdon',
                u'role': u'vielle à roue'},
               {u'name': u'Basile Brémaud',
                u'role': u'violon'}],
  u'duration': '10:01',
  u'position': 10,
  u'title': u'Ont menarem'}],
u"notes":"""
LA NÒVIA est un collectif basé en Haute-Loire qui réunit des musiciens résidant sur un large territoire (Auvergne, Rhône-Alpes, Béarn, Limousin, Cévennes, Franche-Comté).
Ce collectif est un lieu de réflexion et d'expérimentation autour des musiques traditionnelles et/ou expérimentales. La pluralité de ces acteurs crée une dynamique et une cohérence esthétique forte.
"""
}
]

if 0:
    """
    #import discogs_client
    #d = discogs_client.Client('Souterraine/0.1')
    #access_token='vapFUwiXcNCXJwIxvGMasBfNDEXjtvNwzJokwNjI'
    """

people = [
    {u"realname": u"Tanguy Haesevoets",
     u"name": u"Tanguy Haesevoets",
     u"aliases":[u"Témé Tan"]}
]


raw_bands = [{'current_members': [], 'name': 'Sourdure'},
 {'current_members': [{u'name': u'Maud Octallinn', u'role': ''}],
  'name': u'Maud Octallinn'},
 {'current_members': [{u'name': u'Olivier Marguerit', u'role': ''},
   {u'name': u'J\xe9r\xf4me Laperruque', u'role': ''}],
  'name': 'O'},
 {'current_members': [{u'name': u'Tanguy Haesevoets', u'role': ''}],
  u'discogs_id': 3894930,
  'name': u'T\xe9m\xe9 Tan'},
 {'current_members': [{u'name': u'Silvain Vanot', u'role': ''}],
  u'discogs_id': 272579,
  'name': u'Silvain Vanot'},
 {'current_members': [{u'name': u'Mehdi Zannad', u'role': ''},
   {u'name': u'Ricky Hollywood', u'role': ''},
   {u'name': u'Olivier Marguerit', u'role': ''}],
  'discogs_id': 859588,
  'name': u'Mehdi Zannad'},
 {u'current_members': [], u'name': u'Requin Chagrin'},
 {'current_members': [], u'name': u'Marie Math\xe9matique'},
 {u'current_members': [{u'name': u'Emmanuelle Parrenin', u'role': ''}],
  u'discogs_id': 859588,
  u'name': u'Emmanuelle Parrenin'},
 {'current_members': [], u'name': u'Lapin'},
 {u'current_members': [{u'name': u'Thomas Boudineau', u'role': ''}],
  u'name': u'Flegmatic'},
 {u'current_members': [{u'name': u'Weli No\xebl', u'role': ''},
   {u'name': u'H\xe9l\xe8ne Martin', u'role': ''}],
  u'discogs_id': 1352252,
  u'name': u'Weli No\xebl'},
 {u'current_members': [{u'name': u'Cl\xe9ment Gauthier', u'role': ''},
   {u'name': u'Jacques Puech', u'role': ''},
   {u'name': u'Antoine Cognet', u'role': ''},
   {u'name': u'Yann Gourdon', u'role': ''}],
  u'name': u'J\xe9richo'},
 {u'current_members': [{u'name': u'Pierre-Vincent Fortunier', u'role': ''},
   {u'name': u'Yann Gourdon', u'role': ''},
   {u'name': u'Guilhem Lacroux', u'role': ''}],
  u'discogs_id': 3784829,
  u'name': 'Toad'},
 {u'current_members': [{u'name': u'Jacques Puech', u'role': ''},
   {u'name': u'Guilhem Lacroux', u'role': ''}],
  u'discogs_id': 3338836,
  u'name': u'Faune'},
 {u'current_members': [{u'name': u'Basile Br\xe9maud', u'role': ''},
   {u'name': u'Mat\xe8u Baudoin', u'role': ''},
   {u'name': u'Yann Gourdon', u'role': ''},
   {u'name': u'Nicolas Rouzier', u'role': ''}],
  u'name': u'La Ci\xe8da'},
 {u'current_members': [{u'name': u'Yann \xc9tienne', u'role': ''},
   {u'name': u'Yann Gourdon', u'role': ''}],
  u'name': u'Le Verdouble'},
 {u'current_members': [{u'name': u'Perrine Bourel',
    u'role': u'violon, violon grave, chant'},
   {u'name': u'Mana Serrano', u'role': u'violon, violon grave, chant'}],
  u'name': u'Violonneuses'},
 {u'current_members': [{u'name': u'Basile Br\xe9maud', u'role': 'chant'},
   {u'name': u'Pierre-Vincent Fortunier',
    u'role': u'cornemuse b\xe9chonnet 11 pouces, violon'},
   {u'name': u'Yann Gourdon',
    'role': 'vielle \xc3\xa0 roue, bo\xc3\xaete \xc3\xa0 bourdons'},
   {u'name': 'Guilhem Lacroux', u'role': 'guitare, lap steel'}],
  u'name': u'la Baracande'}]

if 0:
    bands = []
    for b in raw_bands:
        members = []
        current_members = b.get('current_members', [])
        for m in current_members:
            try:
                name = m.get('name')
            except AttributeError:
                members.append({u'name': m, u'role':''})
            else:
                members.append(m)
        b['current_members'] = members
        bands.append(b)


class PersonNotFound(BaseException):
    pass
class TooManyPeopleFound(BaseException):
    pass

class BandNotFound(BaseException):
    pass
class TooManyBandFound(BaseException):
    pass


def find_person_id(name):
    person = db.people.find({'$or': [{'name': name},
                                     {'realname': name}]})
    nb = person.count()
    if nb == 0:
        raise PersonNotFound(name)
    if nb > 1:
        raise TooManyPeopleFound(name)
    return person[0]['_id']






if 0:
    notes="""
    Jericho - La Mantille 09:59
    Toad - Suite de bourrées 04:21
    Faune - Qui veut entendre une chanson 04:01
    La Cleda - Lo vespre 08:59
    Le Verdouble - 22/04/14 20:20
    Violonneuses - Marches & bourrées 11:18
    La Baracande - Tout en me promenant 06:06
    Duo Gourdon/Mauchand - Scottishs 04:31
    Duo Puech/Gourdon - La Cançon 08:23
    Trio Puech/Gourdon/Brémaud - Ont menarem 10:01
    """

    tracklist = []
    for (i, line) in enumerate(notes.split('\n')):
        if not line:
            continue
        (artist, title) = line.split("-")
        artist = artist.strip()
        title = title.strip()
        tracklist.append({
            u"position": i,
            u"title": title[:-6],
            u"duration": title[-5:],
            u"artists":[
                {u"name": artist}
            ]
        })
