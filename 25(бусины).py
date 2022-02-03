def correct(seq, rules):
    if len(seq) != 4:
        return False
    for ch, rule in zip(seq, rules):
        if ch not in rule:
            return False
    return seq[-1] not in seq[:-1]

if __name__ == "__main__":
    for s in ("ИЛХФ", "ИХЛФ", "ФИХЛ", "ИФЛХ"):
        if correct(s, ("ФИ", "ИЛ", "ХЛ", "ХФ")):
            print(f"{s} is correct")
        else:
            print(f"{s} is not correct")