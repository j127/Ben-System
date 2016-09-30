"""A generator for the Ben System."""


systems = {}

systems['ben_pridmore'] = {
    # TODO: double-check accuracy
    first_letters: 's,t,n,m,r,l,g/j,k,f/th,b,p,h,sk/sn/sm,st/sp,sh/sl/sw,d,None,None,None'.split(','),
    middle_letters: 'oo,a,e,i,o,u,A,E,I,O,None,None,None,None,None,None,ow,or,ar'.split(','),
    final_letters: 's,t,n,m,r,l,g,k,f/th,b,None,None,None,None,None,None,j/sh/ch,p,d',split(','),
    decimals: [ '0',  '1', '2', '3', '4', '5', '6', '7', '8', '9', None, None, None, None, None, None, None, None, None],
    binaries: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', None, None, None],
    card_suits: 'ss,cd,ch,cs,dc,dh,ds,cc,hc,hd,hs,hh,sc,sd,sh,dd, None, None, None'.split(','),
    card_values: ['10', 'A', '2', '3', '4', '5', '6', '7', '8', '9', None, None, None, None, None, None, 'J', 'Q', 'K'],
}

systems['josh_cohen'] = {
    # TODO: fix this
    first_letters: 's,t,n,m,r,l,g/j,k,f/th,b,p,h,sk/sn/sm,st/sp,sh/sl/sw,d,None,None,None'.split(','),
    middle_letters: 'oo,a,e,i,o,u,A,E,I,O,None,None,None,None,None,None,ow,or,ar'.split(','),
    final_letters: 's,t,n,m,r,l,g,k,f/th,b,None,None,None,None,None,None,j/sh/ch,p,d',split(','),
    decimals: [ '0',  '1', '2', '3', '4', '5', '6', '7', '8', '9', None, None, None, None, None, None, None, None, None],
    binaries: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', None, None, None],
    card_suits: 'ss,cd,ch,cs,dc,dh,ds,cc,hc,hd,hs,hh,sc,sd,sh,dd, None, None, None'.split(','),
    card_values: ['10', 'A', '2', '3', '4', '5', '6', '7', '8', '9', None, None, None, None, None, None, 'J', 'Q', 'K'],
}


def suit_letters_to_entities(suit_pair):
    pass


def render_template(context):
    pass