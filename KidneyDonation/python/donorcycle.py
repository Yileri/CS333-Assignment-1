
def isInCycle(match_scores,donor_friends,query):
    # create an array for recipient nodes and adjacent nodes as arrays of each node
    node_count = len(match_scores[0])
    nodes = [set() for x in range(node_count)]

    donor_count = len(match_scores)

    # check if there is score 60 and above
    for row in range(donor_count):
        for col in range(node_count):
            if match_scores[row][col] >= 60:
                donor_id = row
                recipient_id = donor_friends[donor_id]
                nodes[recipient_id].add(col)
    print(nodes)
    return False

def take_input():
    n = int(input())
    m = int(input())
    donor_friends = input().split(',')
    for i in range(len(donor_friends)):
        donor_friends[i] = int(donor_friends[i])
    match_scores = []
    for i in range(m):
        match_row = input().split(',')
        for j in range(len(match_row)):
            match_row[j] = int(match_row[j])
        match_scores.append(match_row)
    query = int(input())
    print(isInCycle(match_scores,donor_friends,query))

take_input()
