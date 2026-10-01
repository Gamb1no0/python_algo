import json


def group_anagrams(words):
    groups = {}

    for word in words:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)

    return list(groups.values())


if __name__ == "__main__":
    words = json.loads(input())
    print(json.dumps(group_anagrams(words), ensure_ascii=False))
