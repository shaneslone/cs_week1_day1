def csSchoolYearsAndGroups(years, groups):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rtn_string = ""
    for i in range(years):
        for j in range(groups):
            rtn_string = rtn_string + f"{i + 1}{alphabet[j]}, "
    return rtn_string[:len(rtn_string)-2]
