import numpy as np
from sklearn.preprocessing import OneHotEncoder
import file_reader as reader

import odor_seperate
import decision_tree
import isolation_forest

from sklearn.impute import SimpleImputer


def main(data):
    # One hot encoding
    enc = OneHotEncoder(handle_unknown='ignore')
    missing_data = reader.missing()
    missing_data = np.concatenate([data, missing_data])
    index = 0
    #removing odorless samples:
    for mush in missing_data:
        if mush[5] == "-":
            #print(index)
            missing_data = np.delete(missing_data, index ,0)
        else:
            index += 1
    odorless_data, odors = odor_seperate.main(missing_data)
    transformed_data = enc.fit_transform(odorless_data)
    missing_odorless, o = odor_seperate.main(missing_data)
    missing_odorless = enc.transform(missing_odorless)

    # Imputer for missing data
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    missing_data = imp.fit_transform(transformed_data)



    # DECISION TREE

    print("\nDECISION TREE: GINI ")
    print(decision_tree.gini_fit(missing_data, odors))

    isolation_forest.fit_evaluate(transformed_data, odors, missing_odorless)


#data = reader.main()
#main(data)
