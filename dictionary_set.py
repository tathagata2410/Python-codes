marks={
  "Harry":100,
  "Shubham":56,
  "Roha":23
}
print(marks)
print(marks,type(marks))

print(marks["Harry"])

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Harry":69,"Tunai":79})
print(marks)
print(marks.get("Tunai"))
print(marks["Tunai"])