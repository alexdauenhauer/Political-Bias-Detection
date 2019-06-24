# import cPickle
import pickle

if __name__ == '__main__':
    # [lib, con, neutral] = cPickle.load(open('ibcData.pkl', 'rb'))
    filepath = r'/home/alex/Documents/MIDS/w266/final_project/fullIBC/full_ibc/ibcData.pkl'
    with open(filepath, 'rb') as f:
        # [lib, con, neutral] = cPickle.load(open('ibcData.pkl', 'rb'))
        [lib, con, neutral] = pickle.load(f)

    # how to access sentence text
    print('Liberal examples (out of ', len(lib), ' sentences): ')
    for tree in lib[0:5]:
        print(tree.get_words())

    print('\nConservative examples (out of ', len(con), ' sentences): ')
    for tree in con[0:5]:
        print(tree.get_words())

    print('\nNeutral examples (out of ', len(neutral), ' sentences): ')
    for tree in neutral[0:5]:
        print(tree.get_words())

    # how to access phrase labels for a particular tree
    ex_tree = lib[0]

    print('\nPhrase labels for one tree: ')

    # see treeUtil.py for the tree class definition
    for node in ex_tree:

        # remember, only certain nodes have labels (see paper for details)
        if hasattr(node, 'label'):
            print(node.label, ': ', node.get_words())
