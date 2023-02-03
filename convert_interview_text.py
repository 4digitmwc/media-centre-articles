def convert_interview_text(text):
    new_lines = []
    for line in text.split("\n\n"):
        if line[0] == "#":
            new_lines.append(line)
            continue
        player, dialog = line.split(": ")
        new_line = f"**{player}**: {dialog}"
        new_lines.append(new_line)
    return "\n\n".join(new_lines)

with open('interviews/week3.md', 'r', encoding='utf-8') as f:
    data = f.read()
    with open('interviews/week3_edited.md', 'w+', encoding='utf-8') as f2:
        f2.write(convert_interview_text(data))
