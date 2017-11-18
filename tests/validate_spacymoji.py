import spacy
from spacymoji import Emoji

nlp = spacy.load('en')
emoji = Emoji(nlp)
nlp.add_pipe(emoji, first=True)

doc = nlp(u"This is a test 😻 👍🏿")
assert doc._.has_emoji == True
assert doc[2:5]._.has_emoji == True
assert doc[0]._.is_emoji == False
assert doc[4]._.is_emoji == True
assert doc[5]._.emoji_desc == u'thumbs up dark skin tone'
assert len(doc._.emoji) == 2
assert doc._.emoji[1] == (u'👍🏿', 5, u'thumbs up dark skin tone')