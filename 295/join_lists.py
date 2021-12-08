from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if len(lst_of_lst) == 0:
        joined_lst = None
    else:
        joined_lst = lst_of_lst[0]
    for lst in lst_of_lst[1:]:
        joined_lst = joined_lst + [sep] + lst
    return joined_lst
