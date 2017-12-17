import pprint as p
from blockchain import Blockchain

bch = Blockchain()
bch.addNewBlock('First transaction')
bch.addNewBlock('Second transaction')
bch.addNewBlock('Third transaction')
bch.addNewBlock('First transaction')
bch.addNewBlock('Second transaction')
bch.addNewBlock('Second transaction')
bch.addNewBlock('Second transaction')
bch.addNewBlock('Second transaction')

p.pprint(bch.blocks)
