
def count_overlaping_sections(sections):
    section1=[int(a) for a in sections[0].split("-")]
    section2=[int(a) for a in sections[1].split("-")]

    if(section1[0] <= section2[0]):
        if( section2[1] <= section1[1] ):
            return 1

    if(section2[0] <= section1[0]):
        if( section1[1] <= section2[1] ):
            return 1
    return 0

def count_partial_overlaping_sections(sections):
    section1=[int(a) for a in sections[0].split("-")]
    section2=[int(a) for a in sections[1].split("-")]

    if( section1[1]< section2[0] or section2[1]< section1[0]):
        return 0
    return 1

if __name__ == "__main__":
    f = open("input", "r")
    # f = open("test", "r")
    result=0
    for line in f:
        sections=line.split(",")
        # result+=count_overlaping_sections(sections)
        result+=count_partial_overlaping_sections(sections)
    print(result)