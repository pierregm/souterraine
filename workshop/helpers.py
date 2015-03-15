__author__ = 'pierregm'


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

