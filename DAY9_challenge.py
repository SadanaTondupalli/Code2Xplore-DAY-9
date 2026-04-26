import copy

def generate_data():
    return [
        {
            "id": 1,
            "data": {"files": ["a.txt", "b.txt"], "usage": 500}
        },
        {
            "id": 2,
            "data": {"files": ["c.txt"], "usage": 300}
        }
    ]


def replicate_data(users):
    assigned = users              
    shallow = users[:]          
    deep = copy.deepcopy(users)   
    return assigned, shallow, deep


def modify_data(data):
    for user in data:
        # EVEN → Add file
        user["data"]["files"].append("new_file.txt")

        user["data"]["usage"] += 100


def check_integrity(original, shallow, deep):
    leakage_count = 0
    safe_count = 0
    overlap_count = 0

    for i in range(len(original)):
        orig_files = set(original[i]["data"]["files"])
        shallow_files = set(shallow[i]["data"]["files"])
        deep_files = set(deep[i]["data"]["files"])

        if orig_files != deep_files:
            leakage_count += 1

        if deep_files != shallow_files:
            safe_count += 1

        overlap_count += len(orig_files.intersection(shallow_files))

    return (leakage_count, safe_count, overlap_count)



def main():
    original = generate_data()

    print("BEFORE")
    print("Original:", original)

    assigned, shallow, deep = replicate_data(original)

    print("\nAssignment Copy:", assigned)

    modify_data(shallow)

    print("\nAFTER")
    print("Original (affected):", original)
    print("Shallow Copy:", shallow)
    print("Deep Copy (safe):", deep)

    report = check_integrity(original, shallow, deep)

    print("\nINTEGRITY REPORT")
    print("(leakage_count, safe_count, overlap_count) =", report)

main()