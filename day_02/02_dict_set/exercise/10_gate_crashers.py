invited = {"Ana", "Ben", "Carlo", "Dani"}
attended = {"Ben", "Carlo", "Ely"}



# TODO: Who are all the involved members?
involved_members = invited.union(attended)
print("Involved Members:", involved_members)

# TODO: Who was absent?
absent = invited.difference(attended)
print("Absent:", absent)

# TODO: Who gatecrashed?
gate_crashers = attended.difference(invited)
print("Not enrolled but attended:", gate_crashers)

# TODO: Who was invited and attended
print("Attended properly:")
