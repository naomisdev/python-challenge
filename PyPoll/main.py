import csv

with open('Resources/election_data.csv') as csvFile:
    read_csv = csv.DictReader(csvFile)

    total = 0
    candidates = []
    votes = {}

    for row in read_csv:

        total += 1
        name = row['Candidate']

        if name not in candidates:
            candidates.append(name)
            votes[name] = 0
        votes[name] += 1

    output = (
        f'\n    Election Results\n'
        f'-------------------------\n'
        f'Total Votes: {total:,}\n'
        f'-------------------------\n'
    )

    winner_votes = 0
    for name in candidates:
        output += f'{name}: {votes[name]/total*100:.3f}% ({votes[name]:,})\n'

        if votes[name] > winner_votes:
            winner_votes = votes[name]
            winner = name
    output += f'-------------------------\nWinner: {winner}\n-------------------------\n'
    
print(output)
with open('Analysis/output.txt', 'w') as output_file:
    output_file.write(output)