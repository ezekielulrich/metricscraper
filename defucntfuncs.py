
def ends_with_university_domain(input_string):

    university_patterns = [
        r".*mit\.edu$",
        r".*umich\.edu$",
        r".*gatech\.edu$",
        r".*illinois\.edu$",
        r".*stanford\.edu$",
        r".*northwestern\.edu$"
    ]

    for pattern in university_patterns:
        if re.match(pattern, input_string):
            return True

    return False

def get_affiliation(input_string):
    if re.match(r".*mit\.edu$", input_string):
        return 'MIT'
    elif re.match(r".*umich\.edu$", input_string):
        return "UMichigan"
    elif re.match(r".*gatech\.edu$", input_string):
        return "Georgia Tech"
    elif re.match(r".*illinois\.edu$", input_string):
        return "UIUC"
    elif re.match(r".*stanford\.edu$", input_string):
        return "Stanford"
    elif re.match(r".*northwestern\.edu$", input_string):
        return "Northwestern"
    else:
        return "Other"